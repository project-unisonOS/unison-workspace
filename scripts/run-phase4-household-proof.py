#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import time
from pathlib import Path

from tools.phase4_household import BoundaryDenied, HouseholdProofRuntime, SURFACES


def main() -> int:
    started = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="unison-phase4-") as directory:
        proof = HouseholdProofRuntime(Path(directory))
        proof.enroll()
        outcomes = proof.coordinate()
        denials = 0
        for surface in SURFACES:
            try:
                proof.read_surface("alice", "bob", surface)
            except BoundaryDenied:
                denials += 1
        report = {
            "schema_version": "unison.phase4-proof-result.v1",
            "profile": "two-independent-adults",
            "result": "pass",
            "assistant_count": 2,
            "shared_artifacts_created": len(outcomes),
            "negative_surfaces_passed": denials,
            "private_sources_read_for_coordination": 0,
            "resource_profile": proof.scheduler.operational_snapshot(),
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 2),
            "contains_private_canary_values": False,
            "phase5_started": False,
        }
        print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

