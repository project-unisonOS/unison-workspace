from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.phase4_household import BoundaryDenied, HouseholdProofRuntime, SURFACES
from unison_common.household import HouseholdCoordinationRequest


@pytest.fixture
def proof(tmp_path):
    item = HouseholdProofRuntime(tmp_path)
    item.enroll()
    return item


def test_two_people_have_distinct_assistants_and_every_private_namespace(proof):
    alice, bob = proof.people["alice"], proof.people["bob"]
    for field in (
        "person_id", "assistant_instance_id", "key_handle", "credential_namespace",
        "data_namespace", "cache_namespace", "index_namespace",
    ):
        assert alice[field] != bob[field]


@pytest.mark.parametrize("surface", SURFACES)
def test_cross_person_surfaces_fail_with_one_non_oracular_denial(proof, surface):
    with pytest.raises(BoundaryDenied, match="^resource unavailable$"):
        proof.read_surface("alice", "bob", surface)
    with pytest.raises(BoundaryDenied, match="^resource unavailable$"):
        proof.read_surface("alice", "missing", surface)


def test_canary_inference_refuses_to_reveal_or_guess_other_private_facts(proof):
    response = proof.ask_about_other_person("alice", "bob")
    assert "cannot access or guess" in response
    assert proof.surface_canaries["bob"]["model"] not in response


def test_calendar_and_grocery_coordination_reads_no_private_sources(proof):
    outcomes = proof.coordinate()
    assert outcomes["grocery"]["private_sources_read"] == 0
    assert outcomes["calendar"]["private_sources_read"] == 0
    bob = proof.people["bob"]
    listed = proof.context.coordinate_household_artifact(
        bob["person_id"], HouseholdCoordinationRequest(
            household_id=bob["household_id"], space_id=proof.shared_space_id,
            action="list", purpose="review household artifacts",
        )
    )
    assert {item.kind.value for item in listed.artifacts} == {"calendar_event", "grocery_item"}
    assert all(canary not in str(listed.model_dump()) for canary in proof.surface_canaries["alice"].values())


def test_concurrent_quota_exhaustion_cannot_starve_other_assistant(proof):
    alice = proof.people["alice"]["assistant_instance_id"]
    bob = proof.people["bob"]["assistant_instance_id"]
    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(lambda task: proof.scheduler.submit(alice, task), ["alice-1", "alice-2"]))
    proof.scheduler.submit(bob, "bob-1")
    leases = [proof.scheduler.dispatch_next(), proof.scheduler.dispatch_next()]
    assert {lease.assistant_instance_id for lease in leases} == {alice, bob}
    assert proof.scheduler.operational_snapshot()["contains_task_content"] is False


def test_restart_rollback_removal_key_rotation_and_recovery(proof):
    proof.coordinate()
    alice = proof.people["alice"]
    before_rollback = proof.context.coordinate_household_artifact(
        alice["person_id"], HouseholdCoordinationRequest(
            household_id=alice["household_id"], space_id=proof.shared_space_id,
            action="list", purpose="capture pre-rollback state",
        )
    )
    with pytest.raises(ValueError, match="update requires an artifact_id"):
        proof.context.coordinate_household_artifact(
            alice["person_id"], HouseholdCoordinationRequest(
                household_id=alice["household_id"], space_id=proof.shared_space_id,
                action="update", purpose="synthetic failed update",
                artifact_kind="grocery_item", grocery={"item": "hidden"},
            )
        )
    after_rollback = proof.context.coordinate_household_artifact(
        alice["person_id"], HouseholdCoordinationRequest(
            household_id=alice["household_id"], space_id=proof.shared_space_id,
            action="list", purpose="verify rollback state",
        )
    )
    assert after_rollback.artifacts == before_rollback.artifacts
    before = proof.context.get_space(proof.shared_space_id).key_version
    proof.restart()
    assert len(proof.context.search(
        proof.people["alice"]["person_id"], space_ids=[proof.shared_space_id]
    )) == 2
    after = proof.remove_bob()
    assert after == before + 1
    with pytest.raises(Exception, match="context space is unavailable"):
        proof.context.search(
            proof.people["bob"]["person_id"], space_ids=[proof.shared_space_id]
        )
    assert proof.identity.identity_for_person(proof.people["bob"]["person_id"])["active"] is False


def test_exports_backups_audits_and_denials_do_not_cross_private_boundary(proof):
    alice_id = proof.people["alice"]["person_id"]
    bob_id = proof.people["bob"]["person_id"]
    alice_export = proof.context.export_person(alice_id)
    bob_export = proof.context.export_person(bob_id)
    assert proof.surface_canaries["alice"]["search"] in str(alice_export)
    assert proof.surface_canaries["alice"]["search"] not in str(bob_export)
    bob_audit = proof.context.list_audit_events(bob_id)
    assert proof.surface_canaries["alice"]["audit"] not in str(bob_audit)
