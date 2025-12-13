#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Optional


def _dur_ms(start_ns: int, end_ns: int) -> float:
    return (end_ns - start_ns) / 1_000_000.0


def load_trace(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def find_first_event_ns(trace: Dict[str, Any], name: str) -> Optional[int]:
    for evt in trace.get("events", []):
        if evt.get("name") == name:
            attrs = evt.get("attrs") or {}
            # Prefer actual renderer feedback, not failures.
            if name == "renderer_emitted" and attrs.get("ok") is not True:
                continue
            ts = evt.get("ts_monotonic_ns")
            if isinstance(ts, int):
                return ts
    return None


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Print latency metrics from a trace artifact JSON.")
    parser.add_argument("trace_json", type=Path)
    args = parser.parse_args(argv)

    trace = load_trace(args.trace_json)
    created_ns = trace.get("created_monotonic_ns")
    if not isinstance(created_ns, int):
        raise SystemExit("invalid trace: missing created_monotonic_ns")

    first_feedback_ns = find_first_event_ns(trace, "renderer_emitted")
    total_end_ns = None
    for span in trace.get("spans", []):
        if span.get("name") == "rom_built":
            end_ns = span.get("end_monotonic_ns")
            if isinstance(end_ns, int):
                total_end_ns = max(total_end_ns or end_ns, end_ns)
        end_ns = span.get("end_monotonic_ns")
        if isinstance(end_ns, int):
            total_end_ns = max(total_end_ns or end_ns, end_ns)

    print(f"trace_id: {trace.get('trace_id')}")
    if first_feedback_ns is not None:
        print(f"time_to_first_feedback_ms: {_dur_ms(created_ns, first_feedback_ns):.2f}")
    else:
        print("time_to_first_feedback_ms: (none)")
    if total_end_ns is not None:
        print(f"total_ms: {_dur_ms(created_ns, total_end_ns):.2f}")
    else:
        print("total_ms: (none)")

    print("spans:")
    for span in trace.get("spans", []):
        name = span.get("name")
        start_ns = span.get("start_monotonic_ns")
        end_ns = span.get("end_monotonic_ns")
        if isinstance(name, str) and isinstance(start_ns, int) and isinstance(end_ns, int):
            print(f"- {name}: {_dur_ms(start_ns, end_ns):.2f} ms ({span.get('status')})")
        elif isinstance(name, str):
            print(f"- {name}: (incomplete)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
