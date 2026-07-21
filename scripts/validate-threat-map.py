#!/usr/bin/env python3
"""Ensure every authoritative threat has planned boundary evidence."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THREAT_MODEL = ROOT / "docs" / "planning" / "UNISON_THREAT_MODEL.md"
TEST_MAP = ROOT / "tests" / "security" / "phase0-boundary-test-map.json"


def fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    documented = set(re.findall(r"\| (T-\d{2}) \|", THREAT_MODEL.read_text(encoding="utf-8")))
    data = json.loads(TEST_MAP.read_text(encoding="utf-8"))
    mapped = [item.get("id") for item in data.get("threats", [])]
    if data.get("schema_version") != 1:
        fail("threat map schema_version must be 1")
    if len(mapped) != len(set(mapped)):
        fail("threat map contains duplicate IDs")
    if documented != set(mapped):
        fail(f"threat coverage mismatch; missing={sorted(documented-set(mapped))}, extra={sorted(set(mapped)-documented)}")
    for item in data["threats"]:
        if not item.get("phase") or not item.get("evidence"):
            fail(f"incomplete threat mapping: {item.get('id')}")
    print(f"[PASS] {len(mapped)} threats have planned boundary evidence.")


if __name__ == "__main__":
    main()
