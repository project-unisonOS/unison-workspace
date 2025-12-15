# SpeechIO Adapter (v1)

## Goal

Provide a modular, swappable speech interface so orchestration + policy code does not depend on any specific ASR/TTS implementation (local engines, remote services, or multimodal models).

The orchestrator owns:
- orchestration, policy, and session lifecycle
- capability-based routing and profile defaults
- end-to-end tracing spans/events

IO modules own:
- capture/actuation (mic, speakers)
- engine-specific streaming and buffering

## Interface (v1)

Contract types live in:
- `unison-common/src/unison_common/contracts/v1/speechio.py`
- `unison-common/src/unison_common/speechio/v1.py` (runtime adapter Protocol)

### Capabilities

`SpeechCapabilities` advertises what the adapter can do:
- `streaming_partials`: supports partial hypothesis streaming
- `barge_in`: supports hard interrupt semantics
- `endpointing`: supports hangover/min/max behavior
- `engines`: best-effort engine inventory

### Profiles

- `AsrProfile`: `"fast"` | `"accurate"`
- `TtsProfile`: `"lightweight"` | `"natural"`

Profiles are *requests*; implementations route to the best available engine.
If only one engine exists, it is used for both profiles, but profile metadata must still be surfaced in:
- emitted `TranscriptEvent.profile`
- trace attributes (`asr_profile`, `tts_profile`, chosen engine name)

### Endpointing policy

`EndpointingPolicy`:
- `hangover_ms`: silence hangover before finalizing
- `min_utterance_ms`: ignore too-short utterances
- `max_utterance_ms`: force-finalize after max duration

If the underlying engine does not expose equivalent parameters, the adapter implements best-effort behavior in its streaming facade.

### Transcript events

`TranscriptEvent.type`:
- `vad_start` | `vad_end`
- `partial` | `final`
- `error`

The streaming facade requirement is satisfied if the adapter yields:
- a quick `vad_start`, then `partial` updates as recognition progresses
- a single `final` event on completion

### Barge-in contract (hard interrupt)

If the adapter is speaking and receives `vad_start`, it must:
1) immediately stop the current TTS (`stopSpeaking(reason="barge_in")`)
2) emit a trace event `tts.interrupt.barge_in`

This rule is enforced inside the SpeechIO adapter (not left to orchestrator timing).

### Methods

Required minimum methods:
- `initialize(config) -> Promise[void]`
- `getCapabilities() -> SpeechCapabilities`
- `getStatus() -> SpeechStatus`
- `startCapture({ asr_profile, endpointing, locale?, streaming_facade? }) -> AsyncIterable[TranscriptEvent]`
- `stopCapture()`
- `speak(text, options) -> SpeakResult`
- `stopSpeaking(reason?)`

Optional but preferred:
- `setActiveProfiles({ asr_profile, tts_profile })`

## Capability-based routing (v1 behavior)

Routing is internal to the SpeechIO implementation:
- ASR:
  - `"fast"` prefers low-latency engines when available
  - `"accurate"` prefers higher-quality engines when available
- TTS:
  - `"lightweight"` prefers low-latency / lower compute
  - `"natural"` prefers higher quality (may be higher latency)

The chosen engine is recorded in trace attributes and surfaced back in events/results.

