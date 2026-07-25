import json
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from unison_common import (
    ExpressionContext, ExpressionPlanRequest, ModalityCapability, SemanticExpression,
    SemanticObservation,
)
from orchestrator.interaction.semantic_runtime import (
    InteractionSessionStore, compare_expressions, interpret_observations, plan_expression,
)


ROOT = Path(__file__).resolve().parents[2]
CAPABILITIES = [
    ModalityCapability(modality="conversation", input_available=True, output_available=True),
    ModalityCapability(modality="visual", input_available=True, output_available=True),
    ModalityCapability(modality="braille", output_available=True),
]


def journeys():
    return json.loads((ROOT / "tests/fixtures/semantic-experience/se0-journeys.v1.json").read_text())["journeys"]


@pytest.mark.parametrize("journey", journeys(), ids=lambda value: value["journey_id"])
def test_all_baseline_journeys_switch_without_semantic_loss(journey):
    required = [f"required-{index}" for index, _ in enumerate(journey["required_meaning"])]
    actions = [action["action_id"] for action in journey["actions"]]
    conversation = SemanticExpression(
        experience_id=journey["journey_id"], modality="conversation", summary=journey["outcome"],
        required_node_ids=required, action_ids=actions, fallback=journey["recovery"],
    )
    visual = conversation.model_copy(update={"modality": "visual"})
    assert compare_expressions(conversation, visual).equivalent
    store = InteractionSessionStore()
    session = store.open(journey["journey_id"], "synthetic-person").model_copy(update={
        "semantic_focus": required[0], "pending_action_ids": actions, "recovery": journey["recovery"],
    })
    store.sessions[session.session_id] = session
    switched = store.switch(session.session_id, ["visual"])
    assert switched.semantic_focus == required[0]
    assert switched.pending_action_ids == actions


def test_expression_plans_cover_mixed_io_degraded_offline_and_sensitive_contexts():
    voice_visual = plan_expression(ExpressionPlanRequest(
        person_id="p", session_id="voice", requested_input="conversation", requested_outputs=["visual"], capabilities=CAPABILITIES,
    ))
    keyboard_conversation = plan_expression(ExpressionPlanRequest(
        person_id="p", session_id="keyboard", requested_input="visual", requested_outputs=["conversation"], capabilities=CAPABILITIES,
    ))
    sensitive = plan_expression(ExpressionPlanRequest(
        person_id="p", session_id="private", requested_outputs=["conversation", "visual"], capabilities=CAPABILITIES,
        environment=ExpressionContext(shared_room=True, sensitive_content=True),
    ))
    offline = plan_expression(ExpressionPlanRequest(
        person_id="p", session_id="offline", requested_outputs=["visual"], capabilities=CAPABILITIES,
        environment=ExpressionContext(offline=True),
    ))
    assert voice_visual.input_modality == "conversation" and voice_visual.output_modalities == ["visual"]
    assert keyboard_conversation.input_modality == "visual" and keyboard_conversation.output_modalities == ["conversation"]
    assert sensitive.output_modalities == ["braille"]
    assert any("offline" in detail for detail in offline.explanation)


@pytest.mark.parametrize("kind", ["table", "chart", "image", "form", "error", "confirmation"])
def test_existing_experience_meaning_is_conversational_and_provenance_bearing(kind):
    observation = SemanticObservation(
        observation_id=kind, source_type="document", source_id=f"fixture:{kind}", state_version="1",
        trust="trusted", confidence=.95,
        content={"nodes": [{"node_id": kind, "kind": "value", "label": kind.title(), "summary": f"Understandable {kind} meaning", "required": True}]},
    )
    sem = interpret_observations(trace_id=kind, session_id="s", person_id="p", observations=[observation])
    assert sem.nodes[0].summary == f"Understandable {kind} meaning"
    assert sem.nodes[0].provenance[0].source_id == f"fixture:{kind}"


def test_stale_ambiguous_and_adversarial_content_stops_before_action():
    now = datetime.now(timezone.utc)
    source = SemanticObservation(
        observation_id="unsafe", source_type="accessibility-tree", source_id="fixture:website",
        observed_at=now - timedelta(seconds=5), state_version="4", confidence=.8,
        ambiguities=["multiple recipients"], injection_signals=["ignore confirmation"],
        content={"stale": True, "actions": [{"action_id": "send", "label": "Send", "capability": "email.send", "consequence": "sends a message"}]},
    )
    sem = interpret_observations(trace_id="unsafe", session_id="s", person_id="p", observations=[source])
    assert not sem.actions
    assert "stale or ambiguous" in sem.outcome
    assert sem.privacy["untrusted_instructions_ignored"] == 1


def test_expression_planning_simulation_stays_within_host_budget():
    request = ExpressionPlanRequest(
        person_id="p", session_id="performance", requested_outputs=["visual"], capabilities=CAPABILITIES,
    )
    started = time.perf_counter()
    for _ in range(1000):
        plan_expression(request)
    assert time.perf_counter() - started < 2.0
