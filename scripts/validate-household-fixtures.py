#!/usr/bin/env python3
"""Validate that Phase 0 household fixtures are synthetic and boundary-ready."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "household" / "two-adults.v1.json"


def fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    if data.get("synthetic") is not True:
        fail("fixture must be explicitly synthetic")

    people = data.get("people") or []
    if len(people) != 2:
        fail("household proof fixture must contain exactly two adults")

    person_ids = {person.get("person_id") for person in people}
    assistant_ids = {person.get("assistant_instance_id") for person in people}
    spaces = {person.get("private_space_id") for person in people}
    canaries = {person.get("private_canary") for person in people}
    if any(len(values) != 2 for values in (person_ids, assistant_ids, spaces, canaries)):
        fail("person, assistant, private-space, and canary values must be unique")

    shared = data.get("shared_spaces") or []
    if len(shared) != 1 or set(shared[0].get("members") or []) != person_ids:
        fail("fixture must contain one explicit shared space with both members")

    serialized = json.dumps(data).lower()
    prohibited = ("@gmail.", "@outlook.", "@proton.", "real-person", "secret-key")
    if any(value in serialized for value in prohibited):
        fail("fixture appears to contain real or secret-like personal data")

    print("[PASS] Synthetic two-adult household fixture is structurally valid.")


if __name__ == "__main__":
    main()

