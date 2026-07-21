from __future__ import annotations

import importlib.util
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[2]
sys.path.insert(0, str(ROOT / "unison-common/src"))
sys.path.insert(0, str(ROOT / "unison-policy/src"))
sys.path.insert(0, str(ROOT / "unison-capability/src"))

from trust_service import TrustEvaluator, TrustRepository, request_hash
from governance import ReplayGuard, authorize_execution, validate_governance_manifest
from errors import CapabilityPolicyError
from unison_common.trust_governance import TrustRequest


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


disclosure = load("phase3_disclosure", ROOT / "unison-inference/src/disclosure.py")
migration = load("phase3_migration", ROOT / "unison-consent/src/migration.py")


def base(**updates):
    value = {"principal_id": "synthetic-p1", "assistant_id": "synthetic-a1", "purpose": "assist", "audience": ["self"], "space_id": "private:synthetic-p1", "assurance": "local-unlocked", "data_classes": ["personal"], "action": "read", "channel": "local"}
    value.update(updates); return value


def governed_manifest(**updates):
    governance = {"actions": ["draft"], "data_read": ["personal"], "data_write": [], "recipient_classes": [], "execution_location": "device", "risk": "low", "reversible": True, "cost_ceiling": "0", "confirmation": "draft-first", "accessibility": {"semantic": True}, "audit": {"owner_readable": True}, "retention": {"days": 7}, "egress": [], "filesystem": [], "devices": [], "timeout_seconds": 5, "resource_limits": {"cpu": "1", "memory": "128Mi"}, "signature": "sha256:synthetic", "revocation_id": "synthetic:1"}
    governance.update(updates)
    return {"governance_version": "unison.capability-governance.v1", "governance": governance}


def authority(**updates):
    value = {"decision_id": "d1", "outcome": "allow", "principal_id": "synthetic-p1", "assistant_id": "synthetic-a1", "action": "draft", "grant_id": "g1", "expires_at": (datetime.now(timezone.utc) + timedelta(minutes=1)).isoformat(), "nonce": "n1"}
    value.update(updates); return value


def test_policy_matrix_relationship_recipient_sensitivity_and_channel():
    cases = json.loads((ROOT / "tests/fixtures/phase3-policy-matrix.v1.json").read_text())["cases"]
    evaluator = TrustEvaluator(TrustRepository())
    for case in cases:
        expected = case.pop("expected"); case.pop("name")
        assert evaluator.evaluate(base(**case)).outcome.value == expected


@pytest.mark.parametrize(("field", "value"), [("purpose", "unknown"), ("audience", ["unknown"]), ("data_classes", ["unknown"]), ("assurance", "unknown"), ("channel", "unknown")])
def test_every_unknown_authority_dimension_denies(field, value):
    assert TrustEvaluator(TrustRepository()).evaluate(base(**{field: value})).outcome.value == "deny"


@pytest.mark.parametrize("source", ["email", "website", "document", "tool", "model-output"])
def test_adversarial_content_never_gains_authority(source):
    raw = base(action="send", audience=["work"], provenance=[source], untrusted_input=True)
    decision = TrustEvaluator(TrustRepository()).evaluate(raw)
    assert decision.outcome.value == "deny" and decision.reason_code == "untrusted-instruction"


def test_minimization_metric_and_remote_disclosure_canary():
    fields = ["title", "time", "attendees", "health_note", "credential", "location"]
    decision = TrustEvaluator(TrustRepository()).evaluate(base(requested_fields=fields))
    assert len(decision.disclosed_fields) / len(fields) <= 0.5
    remote = disclosure.enforce_disclosure("remote-provider", {"intent": "summarize", "prompt": "synthetic", "attachments": ["CANARY"], "secrets": {"token": "CANARY"}, "local_alternative_checked": True, "trust_decision": decision.to_dict()})
    assert "CANARY" not in json.dumps(remote)


def test_confirmation_expiry_cancellation_replay_and_exact_request_binding():
    repo = TrustRepository(); evaluator = TrustEvaluator(repo)
    raw = base(action="send", audience=["family"], recipient_ids=["synthetic-r1"])
    decision = evaluator.evaluate(raw); request = TrustRequest.from_mapping(raw)
    assert repo.resolve_confirmation(decision.confirmation_id, raw["principal_id"], request_hash(request), False) == "cancelled"
    assert repo.resolve_confirmation(decision.confirmation_id, raw["principal_id"], request_hash(request), True) == "replayed"
    second = evaluator.evaluate(raw)
    repo._db.execute("UPDATE confirmations SET expires_at=? WHERE id=?", ((datetime.now(timezone.utc) - timedelta(seconds=1)).isoformat(), second.confirmation_id)); repo._db.commit()
    assert repo.resolve_confirmation(second.confirmation_id, raw["principal_id"], request_hash(request), True) == "expired"


def test_capability_manifest_overreach_secret_timeout_replay_and_revocation():
    with pytest.raises(CapabilityPolicyError): validate_governance_manifest(governed_manifest(filesystem=["/**"]))
    with pytest.raises(CapabilityPolicyError): validate_governance_manifest(governed_manifest(timeout_seconds=301))
    with pytest.raises(CapabilityPolicyError): authorize_execution(governed_manifest(), authority(action="send"))
    with pytest.raises(CapabilityPolicyError): authorize_execution(governed_manifest(), authority(), revoked={"synthetic:1"})
    guard = ReplayGuard(); guard.consume("n1")
    with pytest.raises(CapabilityPolicyError): guard.consume("n1")


def test_secret_broker_and_legacy_migration_fail_closed():
    repo = TrustRepository(); cid = repo.store_credential("synthetic-p1", "mail", "CANARY-SECRET")
    assert repo.inject_credential(cid, "synthetic-p1", "mail", lambda value: len(value)) == len("CANARY-SECRET")
    assert "CANARY-SECRET" not in json.dumps(repo.audit_for("synthetic-p1"))
    assert migration.migrate_legacy_grant("legacy", {"subject": "synthetic-p1", "scopes": ["mail"]})["status"] == "disabled"
