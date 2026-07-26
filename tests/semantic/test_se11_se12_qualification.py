import copy
import json
from pathlib import Path

from model_lifecycle import ModelLifecycleManager, build_compatibility_matrix, state_fingerprint
from unison_common import GoldenSemanticJourney, ModelHardwareQualification, ModelHealthSignal


ROOT = Path(__file__).resolve().parents[2]


def golden_journeys():
    fixtures = json.loads((ROOT / "tests/fixtures/semantic-experience/se0-journeys.v1.json").read_text())["journeys"]
    return [
        GoldenSemanticJourney(
            journey_id=item["journey_id"], required_fact_ids=item["exact_content"],
            required_node_ids=item["required_meaning"],
            action_ids=[action["action_id"] for action in item["actions"]],
            provenance_source_ids=item["provenance"], recovery_required=True,
        )
        for item in fixtures
    ]


def output(journey, *, regressed=False):
    return {
        "fact_ids": [] if regressed else journey.required_fact_ids,
        "required_node_ids": journey.required_node_ids,
        "action_ids": journey.action_ids,
        "provenance_source_ids": journey.provenance_source_ids,
        "recovery": "Safe recovery", "modality_equivalent": not regressed,
        "disclosure_fields": [], "latency_ms": 120,
    }


def test_all_golden_journeys_pass_shadow_and_regression_rolls_back_without_state_change():
    journeys = golden_journeys()
    manager = ModelLifecycleManager(); manager.establish("semantic-construction", "stable@1")
    results = manager.shadow(task="semantic-construction", candidate_ref="candidate@2", journeys=journeys, runner=lambda _, journey: output(journey))
    assert all(result.passed for result in results)
    person_state = {
        "identity": "person", "memory": ["preference"], "permissions": ["calendar.read"],
        "pending_actions": ["propose-move"], "profile": {"outputs": ["conversation"]},
    }
    before = state_fingerprint(copy.deepcopy(person_state))
    manager.begin_canary(task="semantic-construction", candidate_ref="candidate@2", fraction=.05)
    deployment = manager.observe(task="semantic-construction", health=ModelHealthSignal(
        model_ref="candidate@2", sample_count=100, contract_success_rate=.95,
        semantic_success_rate=.90, fallback_rate=.10, error_rate=.05, p95_latency_ms=8000,
    ))
    assert deployment.active_model_ref == "stable@1"
    assert before == state_fingerprint(person_state)


def test_simulated_appliance_load_offline_update_and_rollback_matrix_is_truthful():
    record = ModelHardwareQualification(
        model_ref="candidate@2", runtime_ref="fixture@1", hardware_profile="simulated-appliance",
        evidence_kind="synthetic", processor="fixture", architecture="x86_64", ram_mb=8192,
        storage_mb=20000, latency_ms={"idle": 120, "four-concurrent": 220}, concurrent_workloads=4,
        offline_passed=True, update_passed=True, rollback_passed=True,
        semantic_quality_passed=True, safe_fallback_passed=True,
        limitations=["Physical energy, thermals, and representative hardware remain unmeasured"],
    )
    matrix = build_compatibility_matrix([record])
    assert not record.supported
    assert matrix.supported_model_refs == []
    assert "No model" in matrix.truthful_notice
