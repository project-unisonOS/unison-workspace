from __future__ import annotations

import argparse
import json
import time
from pathlib import Path


def _now_unix_ms() -> int:
    return int(time.time() * 1000)


def prune_traces_dir(traces_dir: Path, *, max_age_days: int) -> int:
    cutoff_ms = _now_unix_ms() - max_age_days * 24 * 60 * 60 * 1000
    removed = 0
    for p in traces_dir.glob("*.json"):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            created = int(data.get("created_unix_ms") or 0)
        except Exception:
            created = int(p.stat().st_mtime * 1000)
        if created and created < cutoff_ms:
            try:
                p.unlink()
                removed += 1
            except Exception:
                pass
    return removed


def prune_event_graph_jsonl(path: Path, *, max_age_days: int) -> int:
    cutoff_ms = _now_unix_ms() - max_age_days * 24 * 60 * 60 * 1000
    tmp = path.with_suffix(path.suffix + ".tmp")
    kept = 0
    with path.open("r", encoding="utf-8") as r, tmp.open("w", encoding="utf-8") as w:
        for line in r:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            ts = int(obj.get("ts_unix_ms") or 0)
            if ts and ts < cutoff_ms:
                continue
            w.write(json.dumps(obj, separators=(",", ":"), ensure_ascii=False) + "\n")
            kept += 1
    tmp.replace(path)
    return kept


def main() -> int:
    p = argparse.ArgumentParser(description="Prune trace artifacts and Event Graph JSONL by age.")
    p.add_argument("--max-age-days", type=int, default=14)
    p.add_argument("--traces-dir", type=str, help="Directory containing trace JSON artifacts")
    p.add_argument("--event-graph", type=str, help="Path to an Event Graph JSONL file")
    args = p.parse_args()

    if not args.traces_dir and not args.event_graph:
        p.error("expected --traces-dir and/or --event-graph")

    if args.traces_dir:
        removed = prune_traces_dir(Path(args.traces_dir), max_age_days=args.max_age_days)
        print(f"traces_removed={removed}")
    if args.event_graph:
        kept = prune_event_graph_jsonl(Path(args.event_graph), max_age_days=args.max_age_days)
        print(f"event_graph_kept={kept}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

