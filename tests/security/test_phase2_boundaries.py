from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
from sqlalchemy import create_engine


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "unison-context" / "src"))
sys.path.insert(0, str(ROOT / "unison-common" / "src"))

from governed_repository import AmbiguousContext, ContextAccessDenied, GovernedContextRepository  # noqa: E402
from unison_common.governed_context import MemberRole, MemoryGovernance, MemoryKind  # noqa: E402


FIXTURE = json.loads((ROOT / "tests" / "fixtures" / "phase2-governed-context.v1.json").read_text(encoding="utf-8"))


def test_fixture_private_canaries_never_cross_any_context_surface(tmp_path):
    repo = GovernedContextRepository(create_engine(f"sqlite:///{tmp_path / 'boundary.db'}", future=True))
    spaces = {
        person["person_id"]: repo.ensure_private_space(person["person_id"], person["assistant_instance_id"])
        for person in FIXTURE["people"]
    }
    for person in FIXTURE["people"]:
        for surface, canary in person["canaries"].items():
            kind = {"memory": MemoryKind.ASSERTED_FACT, "summary": MemoryKind.SUMMARY, "index": MemoryKind.DERIVED_INDEX}[surface]
            repo.admit_memory(
                person["person_id"], space_id=spaces[person["person_id"]].space_id,
                kind=kind, content={"canary": canary}, provenance="phase2 fixture",
                governance=MemoryGovernance(allow_inference=True),
            )

    alice_canaries = tuple(FIXTURE["people"][0]["canaries"].values())
    bob_export = json.dumps(repo.export_person("bob"), sort_keys=True)
    for canary in alice_canaries:
        assert canary not in bob_export  # nosec B101
        assert repo.search("bob", query=canary) == []  # nosec B101
    with pytest.raises(ContextAccessDenied):
        repo.build_prompt_context(
            "bob", space_ids=[spaces["alice"].space_id],
            query="CANARY", purpose="answer",
        )


def test_explicit_share_relationship_ambiguity_and_revocation(tmp_path):
    repo = GovernedContextRepository(create_engine(f"sqlite:///{tmp_path / 'sharing.db'}", future=True))
    alice = repo.ensure_private_space("alice", "assistant-alice")
    repo.ensure_private_space("bob", "assistant-bob")
    shared = repo.create_space(
        "alice", household_id="household-proof", name="Household groceries",
        purpose="coordinate groceries",
    )
    repo.invite_member("alice", shared.space_id, "bob", MemberRole.EDITOR)
    repo.accept_invitation("bob", shared.space_id)
    private = repo.admit_memory(
        "alice", space_id=alice.space_id, kind=MemoryKind.GROCERY_ITEM,
        content={"item": "tea", "note": "private source"}, provenance="alice",
    )
    clone = repo.share_memory("alice", private.record_id, shared.space_id)
    assert clone.source_record_id == private.record_id  # nosec B101
    assert repo.get_memory("alice", private.record_id).space_id == alice.space_id  # nosec B101
    assert repo.search("bob", query="tea", space_ids=[shared.space_id])  # nosec B101

    for edge in FIXTURE["overlapping_relationships"]:
        repo.add_relationship(
            edge["owner_person_id"], subject_id=edge["subject_id"],
            label=edge["label"], provenance="fixture",
        )
    with pytest.raises(AmbiguousContext):
        repo.resolve_relationship("alice", "sam")
    assert repo.resolve_relationship("alice", "sam", "friend").label == "friend"  # nosec B101

    assert repo.remove_member("alice", shared.space_id, "bob") == 2  # nosec B101
    with pytest.raises(ContextAccessDenied):
        repo.search("bob", space_ids=[shared.space_id])
