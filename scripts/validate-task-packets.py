#!/usr/bin/env python3
"""Validate every committed Unison agent task packet."""

import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
schema = json.loads((ROOT / "tasks/task-packet.schema.json").read_text(encoding="utf-8"))
packets = sorted((ROOT / "tasks").glob("*.task.json"))
if not packets:
    raise SystemExit("no task packets found")
for packet in packets:
    jsonschema.validate(json.loads(packet.read_text(encoding="utf-8")), schema)
    print(f"validated {packet.relative_to(ROOT)}")
