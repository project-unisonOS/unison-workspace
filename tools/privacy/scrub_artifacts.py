from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any


def _load_redactor():
    """
    Import `redact_obj` from the workspace `unison-common` checkout.
    """
    here = Path(__file__).resolve()
    root = here.parents[2]
    sys.path.insert(0, str(root / "unison-common" / "src"))
    from unison_common.redaction import redact_obj  # type: ignore

    return redact_obj


def _atomic_write(path: Path, content: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


def scrub_trace_json(path: Path, *, in_place: bool, out: Path | None) -> Path:
    redact_obj = _load_redactor()
    data = json.loads(path.read_text(encoding="utf-8"))
    scrubbed = redact_obj(data)
    target = path if in_place else (out or path.with_suffix(".scrubbed.json"))
    _atomic_write(target, json.dumps(scrubbed, indent=2, sort_keys=False) + "\n")
    return target


def scrub_event_graph_jsonl(path: Path, *, in_place: bool, out: Path | None) -> Path:
    redact_obj = _load_redactor()
    target = path if in_place else (out or path.with_suffix(".scrubbed.jsonl"))
    tmp = target.with_suffix(target.suffix + ".tmp")
    with path.open("r", encoding="utf-8") as r, tmp.open("w", encoding="utf-8") as w:
        for line in r:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            w.write(json.dumps(redact_obj(obj), separators=(",", ":"), ensure_ascii=False) + "\n")
    tmp.replace(target)
    return target


def main() -> int:
    p = argparse.ArgumentParser(description="Scrub trace JSON and Event Graph JSONL artifacts.")
    p.add_argument("--trace", type=str, help="Path to a trace JSON artifact")
    p.add_argument("--event-graph", type=str, help="Path to an Event Graph JSONL file")
    p.add_argument("--in-place", action="store_true", help="Rewrite in-place (atomic)")
    p.add_argument("--out", type=str, help="Output path (ignored if --in-place)")
    args = p.parse_args()

    out = Path(args.out) if args.out else None
    if not args.trace and not args.event_graph:
        p.error("expected --trace and/or --event-graph")

    if args.trace:
        src = Path(args.trace)
        scrub_trace_json(src, in_place=args.in_place, out=out)
    if args.event_graph:
        src = Path(args.event_graph)
        scrub_event_graph_jsonl(src, in_place=args.in_place, out=out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

