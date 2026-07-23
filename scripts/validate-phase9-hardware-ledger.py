#!/usr/bin/env python3
"""Ensure physical Phase 9 acceptance remains explicit and evidence-backed."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "manifests/phase9-hardware-validation.v1.json"


def fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("hardware ledger schema_version must be 1")
    allowed = set(data["policy"]["allowed_statuses"])
    candidate = data["policy"].get("current_release_candidate")
    items = data.get("items", [])
    ids = [item.get("id") for item in items]
    if len(items) < 17 or len(ids) != len(set(ids)):
        fail("hardware ledger must contain all unique Phase 9 physical checks")
    for item in items:
        if not re.fullmatch(r"HW-\d{3}", str(item.get("id", ""))):
            fail(f"invalid hardware test id: {item.get('id')}")
        if item.get("status") not in allowed:
            fail(f"invalid status for {item['id']}")
        if not item.get("configurations") or not item.get("test"):
            fail(f"incomplete hardware test: {item['id']}")
        if item["status"] == "passed":
            evidence = item.get("evidence")
            if not candidate or not evidence or not (ROOT / evidence).is_file():
                fail(f"{item['id']} cannot pass without candidate-bound evidence")
    pending = sum(item["status"] in {"pending-hardware", "blocked"} for item in items)
    print(f"[PASS] Hardware ledger tracks {len(items)} checks; {pending} await physical evidence.")


if __name__ == "__main__":
    main()
