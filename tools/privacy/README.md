# Privacy tools

Local scripts for redaction and retention of on-disk artifacts (trace JSON + Event Graph JSONL).

## Scrub artifacts in-place

```bash
python tools/privacy/scrub_artifacts.py --trace traces/<trace_id>.json --in-place
python tools/privacy/scrub_artifacts.py --event-graph event_graph/events.jsonl --in-place
```

## Prune by age

```bash
python tools/privacy/prune_artifacts.py --traces-dir traces --max-age-days 14
python tools/privacy/prune_artifacts.py --event-graph event_graph/events.jsonl --max-age-days 14
```

