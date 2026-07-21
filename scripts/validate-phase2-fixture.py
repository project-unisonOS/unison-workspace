#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "phase2-governed-context.v1.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> None:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    require(data["schema_version"] == 1, "unsupported fixture schema")
    people = data["people"]
    require(len(people) == 2, "fixture must contain exactly two people")
    require(len({person["person_id"] for person in people}) == 2, "person IDs must be unique")
    require(
        len({person["assistant_instance_id"] for person in people}) == 2,
        "assistant instance IDs must be unique",
    )
    require(
        len({person["private_space_id"] for person in people}) == 2,
        "private space IDs must be unique",
    )
    canaries = [value for person in people for value in person["canaries"].values()]
    require(len(canaries) == len(set(canaries)), "canaries must be unique")
    require(all("CANARY" in value for value in canaries), "canaries must be conspicuous")
    labels = {
        edge["label"] for edge in data["overlapping_relationships"]
        if edge["owner_person_id"] == "alice" and edge["subject_id"] == "sam"
    }
    require(labels == {"friend", "business"}, "overlapping relationship contexts are missing")
    shared = data["shared_spaces"][0]
    require(bool(shared["purpose"]), "shared spaces require a purpose")
    require(
        {member["person_id"] for member in shared["members"]} == {"alice", "bob"},
        "shared space membership must contain both fixture people",
    )
    require(
        {item["kind"] for item in data["shared_artifacts"]} == {"calendar_event", "grocery_item"},
        "fixture must contain calendar and grocery artifacts",
    )
    print("[PASS] Phase 2 overlapping-relationship and governed-space fixture is valid.")


if __name__ == "__main__":
    main()
