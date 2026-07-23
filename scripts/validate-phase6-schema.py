#!/usr/bin/env python3
"""Validate canonical/package backup schema parity and representative data."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "unison-common" / "schemas" / "provider-blind-backup.v1.schema.json"
PACKAGED = ROOT / "unison-common" / "src" / "unison_common" / "schemas" / "provider-blind-backup.v1.schema.json"


def main() -> int:
    canonical = json.loads(CANONICAL.read_text(encoding="utf-8"))
    packaged = json.loads(PACKAGED.read_text(encoding="utf-8"))
    if canonical != packaged:
        raise SystemExit("canonical and packaged Phase 6 schemas differ")
    Draft202012Validator.check_schema(canonical)
    print("[PASS] Provider-blind backup v1 canonical/package schema parity passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
