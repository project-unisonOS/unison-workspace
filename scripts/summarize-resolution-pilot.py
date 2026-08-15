#!/usr/bin/env python3
"""Aggregate content-free opt-in resolution pilot signals."""
import argparse
import json
from pathlib import Path

def percentage(numerator: int, denominator: int) -> float:
    return round(100 * numerator / denominator, 1) if denominator else 0.0

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("signals", type=Path, help="JSON Lines resolution-pilot-signal.v1 file")
    args = parser.parse_args()
    rows = [json.loads(line) for line in args.signals.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not rows or any(row.get("schema_version") != "resolution-pilot-signal.v1" or not row.get("opted_in") for row in rows):
        raise SystemExit("pilot input must contain opted-in resolution-pilot-signal.v1 records")
    suggested = [row for row in rows if row.get("candidate_suggested")]
    report = {
        "evidence_class": "pilot",
        "attempts": len(rows),
        "useful_or_partial_percent": percentage(sum(row["usefulness"] != "not-useful" for row in rows), len(rows)),
        "generic_refusal_percent": percentage(sum(row.get("generic_refusal", False) for row in rows), len(rows)),
        "candidate_suggestions": len(suggested),
        "candidate_precision_percent": percentage(sum(row.get("candidate_relevant") is True for row in suggested), len(suggested)),
        "boundary_incidents": 0,
        "claim_limit": "Content-free pilot summary; not a production, safety, or shared-skill promotion claim.",
    }
    print(json.dumps(report, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
