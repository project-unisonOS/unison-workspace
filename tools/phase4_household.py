"""Synthetic two-assistant household proof harness.

This composes the production identity, governed-context, and scheduler modules.
It never uses real credentials or household data.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path
from typing import Any

from sqlalchemy import create_engine


ROOT = Path(__file__).resolve().parents[1]
for source in (
    ROOT / "unison-common" / "src",
    ROOT / "unison-auth" / "src",
    ROOT / "unison-context" / "src",
    ROOT / "unison-orchestrator" / "src",
):
    if str(source) not in sys.path:
        sys.path.insert(0, str(source))

from governed_repository import GovernedContextRepository  # noqa: E402
from identity_store import IdentityStore  # noqa: E402
from orchestrator.household_resources import HouseholdResourceScheduler  # noqa: E402
from unison_common.governed_context import MemberRole, MemoryGovernance, MemoryKind  # noqa: E402
from unison_common.household import (  # noqa: E402
    AssistantResourceQuota,
    HouseholdCoordinationRequest,
)


SURFACES = (
    "api", "storage", "search", "cache", "embedding", "prompt", "model",
    "trace", "log", "audit", "credential", "backup", "error-oracle",
)


class BoundaryDenied(RuntimeError):
    pass


def _digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class HouseholdProofRuntime:
    def __init__(self, root: Path):
        self.root = root
        self.identity = IdentityStore(str(root / "identity.db"))
        self.context_url = f"sqlite:///{root / 'context.db'}"
        self.context = GovernedContextRepository(create_engine(self.context_url, future=True))
        self.scheduler = HouseholdResourceScheduler(total_concurrent_tasks=2)
        self.people: dict[str, dict[str, Any]] = {}
        self.private_spaces: dict[str, str] = {}
        self.surface_canaries: dict[str, dict[str, str]] = {}
        self.shared_space_id: str | None = None

    def enroll(self) -> None:
        alice = self.identity.bootstrap_first_person(
            confirmed=True, login_handle="alice-proof", display_name="Alice Example",
            household_name="Synthetic Household", password_hash="synthetic-hash-alice",
        )
        token, _ = self.identity.create_invitation(
            invited_by_person_id=alice["person_id"], household_id=alice["household_id"]
        )
        bob = self.identity.accept_invitation(
            invitation_token=token, login_handle="bob-proof", display_name="Bob Example",
            password_hash="synthetic-hash-bob",
        )
        self.people = {"alice": alice, "bob": bob}
        for name, identity in self.people.items():
            space = self.context.ensure_private_space(
                identity["person_id"], identity["assistant_instance_id"]
            )
            self.private_spaces[name] = space.space_id
            self.scheduler.register(AssistantResourceQuota(
                assistant_instance_id=identity["assistant_instance_id"],
                max_concurrent_tasks=1, max_queued_tasks=4, cpu_units=1, memory_mb=512,
            ))
            self.surface_canaries[name] = {
                surface: _digest(f"PHASE4-{name}-{surface}-PRIVATE") for surface in SURFACES
            }
            self.context.admit_memory(
                identity["person_id"], space_id=space.space_id,
                kind=MemoryKind.ASSERTED_FACT,
                content={"canary_hash": self.surface_canaries[name]["search"]},
                provenance="phase4-synthetic-fixture",
                governance=MemoryGovernance(allow_inference=True, allow_backup=True),
            )
            self.context.set_charter(
                identity["person_id"],
                [f"Serve {name}'s objectives", "Never optimize for third-party engagement"],
                "phase4-synthetic-fixture",
            )
            self.context.create_goal(
                identity["person_id"], space_id=space.space_id,
                title=f"Private {name} goal", origin="phase4-synthetic-fixture",
            )

        shared = self.context.create_space(
            alice["person_id"], household_id=alice["household_id"],
            name="Synthetic household coordination", purpose="calendar and groceries",
        )
        self.context.invite_member(
            alice["person_id"], shared.space_id, bob["person_id"], MemberRole.EDITOR
        )
        self.context.accept_invitation(bob["person_id"], shared.space_id)
        self.shared_space_id = shared.space_id

    def coordinate(self) -> dict[str, Any]:
        alice, bob = self.people["alice"], self.people["bob"]
        grocery = self.context.coordinate_household_artifact(
            alice["person_id"],
            HouseholdCoordinationRequest(
                household_id=alice["household_id"], space_id=str(self.shared_space_id),
                action="create", purpose="breakfast groceries", artifact_kind="grocery_item",
                grocery={"item": "oats", "quantity": "1 bag"},
            ),
        )
        calendar = self.context.coordinate_household_artifact(
            bob["person_id"],
            HouseholdCoordinationRequest(
                household_id=bob["household_id"], space_id=str(self.shared_space_id),
                action="create", purpose="household dinner", artifact_kind="calendar_event",
                calendar={
                    "title": "Household dinner",
                    "starts_at": "2030-01-02T18:00:00Z",
                    "ends_at": "2030-01-02T19:00:00Z",
                },
            ),
        )
        return {
            "grocery": grocery.model_dump(mode="json"),
            "calendar": calendar.model_dump(mode="json"),
        }

    def read_surface(self, actor: str, owner: str, surface: str) -> str:
        if surface not in SURFACES or actor not in self.people or owner not in self.people:
            raise BoundaryDenied("resource unavailable")
        if actor != owner:
            raise BoundaryDenied("resource unavailable")
        return self.surface_canaries[owner][surface]

    def ask_about_other_person(self, actor: str, owner: str) -> str:
        try:
            self.read_surface(actor, owner, "model")
        except BoundaryDenied:
            return "I cannot access or guess another person's private information."
        return "Private information is available only to its owner."

    def restart(self) -> None:
        self.context = GovernedContextRepository(create_engine(self.context_url, future=True))
        self.scheduler.restart()

    def remove_bob(self) -> int:
        alice, bob = self.people["alice"], self.people["bob"]
        key_version = self.context.remove_member(
            alice["person_id"], str(self.shared_space_id), bob["person_id"]
        )
        self.identity.remove_household_member(
            removed_by_person_id=alice["person_id"], household_id=alice["household_id"],
            person_id=bob["person_id"],
        )
        return key_version
