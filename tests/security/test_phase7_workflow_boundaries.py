from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
for import_root in (
    ROOT,
    ROOT / "unison-common" / "src",
    ROOT / "unison-orchestrator" / "src",
):
    if str(import_root) not in sys.path:
        sys.path.insert(0, str(import_root))

from orchestrator.phase7 import GovernedWorkflowEngine
from tools.phase7_workflow_demo import _request, run_demo
from unison_common.workflows import WorkflowKind


def test_seven_journeys_return_time_with_zero_boundary_incidents():
    result = run_demo()
    assert result["journeys_completed"] == 7
    assert result["estimated_minutes_returned"] >= 60
    assert result["administrative_tasks_completed"] == 7
    assert result["commitments_completed"] == 7
    assert result["boundary_incidents"] == 0


def test_private_shared_and_wrong_recipient_boundaries_regress():
    engine = GovernedWorkflowEngine()
    with pytest.raises(PermissionError):
        engine.plan(
            _request(WorkflowKind.EMAIL_TRIAGE_DRAFT, key="wrong-space").model_copy(
                update={"context_space_ids": ("private-bob",)}
            )
        )
    with pytest.raises(PermissionError):
        engine.plan(
            _request(WorkflowKind.EMAIL_TRIAGE_DRAFT, key="wrong-recipient").model_copy(
                update={"recipient_ids": ("contact-unapproved",)}
            )
        )
    assert not engine.providers["mail"].calls


def test_adversarial_provider_content_is_not_promoted_to_authority():
    engine = GovernedWorkflowEngine()
    plan = engine.plan(_request(WorkflowKind.DOCUMENT_WEB_RESEARCH, key="tainted"))
    outcome = engine.execute(plan.plan_id)
    assert outcome.metrics.boundary_incidents == 0
    payload = engine.providers["research"].calls[0]["payload"]
    assert "instructions" not in payload
    assert "sponsored" not in payload


def test_commercial_ranking_signals_fail_closed():
    engine = GovernedWorkflowEngine()
    for signal in ("advertising", "engagement", "sponsored", "provider_lock_in"):
        with pytest.raises(ValueError):
            engine.plan(
                _request(WorkflowKind.TRAVEL_PLANNING, key=signal).model_copy(
                    update={"ranking_signals": {signal: 1.0}}
                )
            )


def test_fake_provider_recordings_are_synthetic_and_personal_data_free():
    fixture = json.loads(
        (ROOT / "fixtures" / "phase7" / "fake-provider-records.json").read_text()
    )
    serialized = json.dumps(fixture).lower()
    assert fixture["records"]
    assert fixture["contains_personal_data"] is False
    assert "@gmail.com" not in serialized
    assert "@outlook.com" not in serialized
    assert "access_token" not in serialized
    assert "refresh_token" not in serialized
