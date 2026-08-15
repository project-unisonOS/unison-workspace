#!/usr/bin/env python3
"""Validate the content-free pilot summarizer with synthetic records."""
import json
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
completed = subprocess.run(
    [sys.executable, str(root / "scripts/summarize-resolution-pilot.py"),
     str(root / "tests/fixtures/resolution-pilot-signals.synthetic.jsonl")],
    check=True, capture_output=True, text=True,
)
report = json.loads(completed.stdout)
assert report["attempts"] == 2
assert report["candidate_suggestions"] == 1
assert report["candidate_precision_percent"] == 100.0
assert report["generic_refusal_percent"] == 0.0
print("validated synthetic content-free resolution pilot summary")

forbidden = subprocess.run(
    [sys.executable, str(root / "scripts/summarize-resolution-pilot.py"),
     str(root / "tests/fixtures/resolution-pilot-signals.forbidden.synthetic.jsonl")],
    capture_output=True, text=True,
)
assert forbidden.returncode != 0
assert "prohibited fields: prompt" in forbidden.stderr
print("validated rejection of private pilot content")
