# Power-on Sequence (Manifest-driven)

## Current State Findings (workspace discovery)

### Orchestrator entrypoints + interaction loop
- Runtime entrypoint: `unison-orchestrator/src/server.py`
  - FastAPI app boot + route registration.
  - Publishes a capability manifest to context-graph on startup (`publish_capabilities_to_context()`).
- Input loop (planner → policy → tool → ROM → renderer):
  - `unison-orchestrator/src/orchestrator/api/input.py` exposes `POST /input` and calls `run_input_event(...)`.
  - `unison-orchestrator/src/orchestrator/interaction/input_runner.py` contains the thin vertical slice:
    - emits first feedback to renderer (`RendererEmitter.emit(... type="intent.recognized")`)
    - runs `RouterStage` + `PlannerStage` + `PolicyGate` + `ToolRegistry` + `RomBuilder`
    - writes a trace artifact via `unison_common.trace_artifacts.recorder.TraceRecorder`

### Renderer entrypoints + event transport
- Runtime entrypoint: `unison-experience-renderer/src/main.py`
  - Serves a web surface (`GET /`) and an SSE stream (`GET /events/stream`).
  - Receives envelopes via `POST /events` and stores them in an in-memory log/queue for SSE.
- Web UI composition:
  - `unison-experience-renderer/src/web/app.js` subscribes to `/events/stream`.
  - `unison-experience-renderer/src/web/composer.js` maps envelopes → scenes + modality plans.
  - `unison-experience-renderer/src/web/modality/visual.js` renders scenes.
  - `unison-experience-renderer/src/web/modality/audio.js` currently plays simple tones only.
- Orchestrator → renderer transport:
  - HTTP `POST {renderer}/events` (see `unison-orchestrator/src/orchestrator/interaction/input_runner.py:RendererEmitter`).

### Existing manifest capability (format, loader, usage)
- Schema: `unison-common/src/unison_common/schemas/multimodal_manifest.schema.json`
  - Required root field: `modalities` with arrays of `displays`, `speakers`, `microphones`, `cameras`.
  - The schema does not currently describe renderer assets or IO profile defaults (but it allows extra fields).
- Loader + validator:
  - `unison-common/src/unison_common/multimodal/manifest_client.py`
    - `CapabilityClient.refresh()` loads JSON from URL or local file path and validates against the bundled schema.
    - `CapabilityClient.from_env()` reads `MULTIMODAL_MANIFEST_URL` (default points at orchestrator `/capabilities`).
- Publisher:
  - `unison-orchestrator/src/server.py` initializes a `CapabilityClient` and publishes its manifest to context-graph (`POST /capabilities`).
- Consumers:
  - `unison-experience-renderer/src/main.py` uses `CapabilityClient` against orchestrator `/capabilities` to determine display readiness.

### IO subsystem (speech)
- Speech IO service:
  - `unison-io-speech/src/server.py` exposes:
    - `POST /speech/stt` (stub)
    - `POST /speech/tts` (stub)
    - `WS /stream` streaming façade with VAD + partial/final transcript messages.
  - Streaming behavior and message types:
    - `unison-io-speech/WEBSOCKET_API.md` (protocol overview)
    - `unison-io-speech/src/message_schema.py` (pydantic message models)
    - `unison-io-speech/src/websocket_handler.py` (session logic, VAD, partial/final transcript stubs, barge-in in-session)

### Tracing / telemetry
- OpenTelemetry instrumentation exists in multiple services (e.g., `unison-orchestrator/src/server.py`, `unison-io-speech/src/server.py`).
- File-friendly trace artifacts (JSON) already exist:
  - `unison-common/src/unison_common/trace_artifacts/recorder.py` (`TraceRecorder`)
  - Used today in `unison-orchestrator/src/orchestrator/interaction/input_runner.py`

## Power-on Contract (v1)

This work defines a “power on → boot renderer → initialize IO → ready/listening” contract driven by the existing multimodal manifest.

### Readiness semantics
- **Renderer ready**: renderer health checks and event ingestion path are reachable:
  - `GET {renderer}/ready` returns `{ready: true}`
  - `POST {renderer}/events` accepts a boot envelope (2xx)
- **Speech ready**: speech is enabled in manifest and at least one backend path is reachable (e.g., io-speech `GET /readyz`).
- **System ready**: renderer ready AND at least one input modality available (speech if enabled; otherwise text fallback via `POST /input`).

### Boot stages emitted to renderer
The orchestrator emits a predictable sequence of renderer envelopes:
- `poweron.BOOT_START`
- `poweron.MANIFEST_LOADED`
- `poweron.IO_DISCOVERED`
- `poweron.RENDERER_READY`
- `poweron.SPEECH_READY` or `poweron.SPEECH_UNAVAILABLE`
- `poweron.READY_LISTENING`

Each envelope includes: `trace_id`, `ts_unix_ms`, and a minimal UI payload (stage, logo URL, etc.).

## Manifest schema additions (minimal, optional fields)

The canonical required shape remains unchanged (`modalities`), and the following optional fields are added for v1 power-on and speech policy defaults:

```jsonc
{
  "version": "1.0.0",
  "modalities": { "displays": [], "microphones": [], "speakers": [] },

  "renderer": {
    "assets": {
      "logo": "/static/assets/unison-logo.svg",
      "startup_earcon": "/static/assets/earcon.wav"
    }
  },

  "io": {
    "speech": {
      "enabled": true,
      "endpoint": "http://io-speech:8084",
      "ws_endpoint": "ws://io-speech:8084/stream",
      "preferred_input_device": null,
      "preferred_output_device": null,
      "default_asr_profile": "fast",
      "default_tts_profile": "lightweight",
      "endpointing": { "hangover_ms": 700, "min_utterance_ms": 250, "max_utterance_ms": 10000 }
    }
  },

  "models": {
    "planner": { "provider": "inference", "name": "default" }
  }
}
```

Notes:
- All fields under `renderer`, `io`, and `models` are optional and defaultable.
- The orchestrator treats missing fields as “best-effort” and degrades gracefully (e.g., no earcon if missing).

## Devstack wiring (local)

- Manifest file: `unison-workspace/manifests/dev.multimodal.json`
- Devstack mounts + env:
  - `unison-workspace/unison-devstack/docker-compose.yml` sets `MULTIMODAL_MANIFEST_URL=file:///manifests/dev.multimodal.json`
  - `unison-workspace/unison-devstack/docker-compose.yml` mounts `../manifests:/manifests:ro`
- Renderer logo asset used by the manifest:
  - `unison-experience-renderer/src/web/assets/unison-logo.svg` (served as `/static/assets/unison-logo.svg`)
