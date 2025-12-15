#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, Optional


@dataclass(frozen=True)
class EventStamp:
    name: str
    ts_ns: int
    attrs: Dict[str, Any]


def _load_trace(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _pick_latest_trace(path: Path) -> Path:
    if path.is_file():
        return path
    if not path.is_dir():
        raise FileNotFoundError(str(path))
    candidates = sorted((p for p in path.glob("*.json") if p.is_file()), key=lambda p: p.stat().st_mtime, reverse=True)
    if not candidates:
        raise FileNotFoundError(f"no *.json traces in {path}")
    return candidates[0]


def _event_index(trace: Dict[str, Any]) -> Dict[str, EventStamp]:
    out: Dict[str, EventStamp] = {}
    for e in trace.get("events") or []:
        if not isinstance(e, dict):
            continue
        name = e.get("name")
        ts = e.get("ts_monotonic_ns")
        if not isinstance(name, str) or not isinstance(ts, int):
            continue
        out[name] = EventStamp(name=name, ts_ns=ts, attrs=e.get("attrs") if isinstance(e.get("attrs"), dict) else {})
    return out


def _fmt_ms(ns: int) -> str:
    return f"{ns / 1_000_000.0:,.2f}ms"


def _delta_ms(a: Optional[EventStamp], b: Optional[EventStamp]) -> Optional[str]:
    if not a or not b:
        return None
    return _fmt_ms(b.ts_ns - a.ts_ns)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: tools/trace/report_latency.py <trace.json|traces_dir>")
        return 2

    target = _pick_latest_trace(Path(argv[1]))
    trace = _load_trace(target)
    idx = _event_index(trace)

    t0 = idx.get("poweron.boot_start")
    vad = idx.get("speech.vad_start")
    first_partial = idx.get("speech.first_partial_transcript")
    first_feedback = idx.get("renderer.emitted_first_feedback")
    final_tx = idx.get("speech.final_transcript")
    tts_first = idx.get("tts.first_audio")
    done = idx.get("tts.end") or idx.get("completed")

    print(f"trace: {target}")
    print(f"trace_id: {trace.get('trace_id')}")

    if t0:
        print(f"time_to_first_partial_from_poweron: {_delta_ms(t0, first_partial) or 'n/a'}")
        print(f"time_to_first_feedback_from_poweron: {_delta_ms(t0, first_feedback) or 'n/a'}")
        print(f"time_to_first_audio_from_poweron: {_delta_ms(t0, tts_first) or 'n/a'}")
        print(f"total_from_poweron: {_delta_ms(t0, done) or 'n/a'}")

    if vad:
        print(f"time_to_first_partial_from_vad: {_delta_ms(vad, first_partial) or 'n/a'}")
        print(f"time_to_first_feedback_from_vad: {_delta_ms(vad, first_feedback) or 'n/a'}")
        print(f"time_to_final_transcript_from_vad: {_delta_ms(vad, final_tx) or 'n/a'}")
        print(f"time_to_first_audio_from_vad: {_delta_ms(vad, tts_first) or 'n/a'}")

    spans = trace.get("spans") or []
    span_rows: list[tuple[str, float]] = []
    for s in spans:
        if not isinstance(s, dict):
            continue
        name = s.get("name")
        dur = s.get("duration_ms")
        if isinstance(name, str) and isinstance(dur, (int, float)):
            span_rows.append((name, float(dur)))

    if span_rows:
        print("\nspans:")
        for name, dur in sorted(span_rows, key=lambda r: r[1], reverse=True)[:30]:
            print(f"- {name}: {dur:,.2f}ms")

    # Print a minimal timeline (ordered by timestamp).
    events: list[EventStamp] = sorted(idx.values(), key=lambda e: e.ts_ns)
    if events:
        print("\nkey_events:")
        keep = {
            "poweron.boot_start",
            "poweron.manifest_loaded",
            "poweron.io_discovered",
            "poweron.renderer_ready",
            "speech.initialize_start",
            "speech.initialize_end",
            "speech.capture_start",
            "speech.vad_start",
            "speech.first_partial_transcript",
            "speech.final_transcript",
            "planner.start",
            "planner.end",
            "tool.start",
            "tool.end",
            "rom.built",
            "renderer.emitted_first_feedback",
            "tts.start",
            "tts.interrupt.barge_in",
            "tts.first_audio",
            "tts.end",
        }
        base = events[0].ts_ns
        for e in events:
            if e.name not in keep:
                continue
            print(f"- +{_fmt_ms(e.ts_ns - base)} {e.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

