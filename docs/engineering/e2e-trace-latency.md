# E2E Trace Latency (Power-on → First Response Audio)

## What this measures

This trace is a single JSON artifact written to `traces/` that captures:
- power-on boot stages
- speech capture timeline (VAD → partials → final transcript)
- planner/tool/ROM latency
- first renderer feedback and first response audio (best-effort)

Trace artifacts use monotonic timestamps (`*_monotonic_ns`) when available so durations are stable even if wall-clock time changes.

## Trace spans/events emitted (minimum set)

Events (via `TraceRecorder.emit_event`):
- `poweron.boot_start`
- `poweron.manifest_loaded`
- `poweron.io_discovered`
- `poweron.renderer_ready`
- `speech.initialize_start` / `speech.initialize_end`
- `speech.capture_start`
- `speech.vad_start`
- `speech.first_partial_transcript`
- `speech.final_transcript`
- `planner.start` / `planner.end`
- `tool.start` / `tool.end`
- `rom.built`
- `renderer.emitted_first_feedback`
- `tts.start`
- `tts.interrupt.barge_in` (when triggered)
- `tts.first_audio` (best-effort)
- `tts.end`

Recommended event attributes:
- `asr_profile`, `tts_profile`
- `engine` (chosen engine)
- endpointing params (`hangover_ms`, `min_utterance_ms`, `max_utterance_ms`)

## Trace output location

Traces are written to:
- `traces/<run_id>.json`

The directory is configurable with `UNISON_TRACE_DIR` (defaults to `traces`).

## Generate a latency report

Use the report tool:
- `python3 tools/trace/report_latency.py traces/<run_id>.json`

Output includes:
- time-to-first-partial
- time-to-first-feedback (renderer)
- time-to-first-audio
- total time
- per-event deltas and per-span durations (when available)

## Notes / limitations

- `tts.first_audio` is best-effort in dev mode unless the output device provides an explicit playback callback; when unavailable, the system records the timestamp when the renderer is instructed to begin playback.

