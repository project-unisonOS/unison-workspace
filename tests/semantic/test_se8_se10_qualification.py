import hashlib

import pytest

from governed_models import ModelManifestSigner, ModelRegistry, route_operation, validate_semantic_proposal
from orchestrator.interaction.semantic_runtime import compare_expressions
from unison_common import (
    ModelManifest, ModelSemanticProposal, ModelTaskRequirement, SemanticExpression,
)


ARTIFACT = b"qualified synthetic model"
TASKS = ["interpretation", "extraction", "vision", "semantic-construction", "synthesis", "conversation"]


def qualified_registry():
    signer = ModelManifestSigner({"qualification": b"q" * 32})
    model = ModelManifest(
        model_id="synthetic-local", version="1", artifact_digest="sha256:" + hashlib.sha256(ARTIFACT).hexdigest(),
        source="synthetic-fixture", provenance=["se8-se10-suite"], runtime="fixture", runtime_version="1",
        tasks=TASKS, modalities=["text", "image"], languages=["en"], context_tokens=8192,
        structured_output=True, hardware={"architectures": ["x86_64"], "min_ram_mb": 1024},
        execution_location="device", provider="local", license="test-only", license_approved=True,
        privacy={"retention": "none", "required_disclosure_fields": []},
        measured_quality={task: .9 for task in TASKS}, measured_latency_ms={task: 100 for task in TASKS},
        approved_risk=["low", "medium", "high", "critical"], supported=True,
    )
    registry = ModelRegistry(signer); registry.register(signer.sign(model, "qualification"))
    registry.inventory_installed({"synthetic-local@1": ARTIFACT})
    return registry


@pytest.mark.parametrize("task", TASKS)
def test_every_approved_task_routes_as_an_independent_bounded_operation(task):
    decision = route_operation(
        operation_id=f"operation:{task}",
        requirement=ModelTaskRequirement(task=task, modality="image" if task == "vision" else "text", max_cost=0),
        registry=qualified_registry(), policy={"cost_ceiling": 0},
        hardware={"architecture": "x86_64", "ram_mb": 4096}, offline=True,
    )
    assert decision.selected_model_id == "synthetic-local"
    assert decision.operation_id == f"operation:{task}"


def test_validated_semantic_contribution_is_equivalent_in_every_qualified_expression():
    proposal = ModelSemanticProposal(
        operation_id="bill", model_id="synthetic-local", model_version="1",
        source_state_versions={"bill": "7"}, fact_claims={"amount": 20}, recipients=["utility"],
        recovery="Keep the bill unpaid",
        nodes=[{"node_id": "amount", "kind": "value", "label": "Amount", "value": 20, "required": True, "exact": True, "provenance": [{"source_id": "bill", "source_type": "document"}]}],
        provenance=[{"source_id": "bill", "source_type": "document"}],
    )
    accepted = validate_semantic_proposal(
        proposal=proposal,
        requirement=ModelTaskRequirement(task="semantic-construction", risk="high", required_fact_ids=["amount"], deterministic_fallback_required=True),
        deterministic_facts={"amount": 20}, current_source_versions={"bill": "7"},
        allowed_recipients={"utility"}, deterministic_action_ids=set(),
    )
    assert accepted["language_path"] == "deterministic"
    expressions = [
        SemanticExpression(experience_id="bill", modality=modality, summary="Amount is 20", required_node_ids=["amount"], provenance_source_ids=["bill"], fallback=accepted["recovery"])
        for modality in ("conversation", "visual", "braille")
    ]
    assert compare_expressions(expressions[0], expressions[1]).equivalent
    assert compare_expressions(expressions[0], expressions[2]).equivalent
