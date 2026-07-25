# Semantic experience SE0 inventory and baseline

Status: **Complete software inventory; hardware and participatory validation deferred**  
Last updated: 2026-07-25

## Contract and path inventory

| Area | Current path | SE0 finding | Migration disposition |
| --- | --- | --- | --- |
| Response | `unison-common` ROM text/cards | Presentation-centered and generic metadata | SEM v1 is authoritative; ROM remains a compatibility view |
| Orchestration | `RomBuilder` and renderer envelopes | Tool result becomes text | Build typed SEM before compatibility ROM |
| Visual renderer | browser composer and scene graph | Visual scene is always applied | Native visual composer consumes SEM |
| Conversation | voice loop, ASR/TTS, renderer audio | Speaks a best-effort text summary | Native conversational composer consumes SEM; transport remains separate |
| Captions | speech partial/final renderer events | Coherent speech transcription exists | Retain as alternate expression and input feedback |
| Braille | device, translator, focus-feed planning | Some output mirrors visual focus text | Native Braille composer navigates semantic identifiers |
| Sign | sign gateway/avatar design | Text/caption fallbacks dominate | Future native composer uses composer conformance contract |
| Vision | capture/describe and multimodal inference | Can interpret images but lacks SEM observation contract | SE6 interpreter work |
| Haptic | renderer adapter stub | Cue-only and off by default | Future native composer uses semantic cue plan |
| Switch/AAC | planned adapter family | No canonical expression contract | Future native composer uses composer conformance contract |
| Browser/VDI | computer-use action paths | Control and screen state are implementation-facing | SE6 interprets external experiences into SEM |
| Preferences | renderer flags and general person profile | Display/speech settings are fragmented | Interaction Profile v1 is governed private context |
| Policy/disclosure | trust-governance and inference gates | Deterministic boundaries exist | Bind unchanged to SEM actions and expression plans |
| Audit | trace, event graph, governed audit | Model/renderer events exist | Add semantic experience and profile provenance identifiers |

## Visual-first and input-coupled dependencies

The migration backlog includes:

- output directives that select `voice` from voice input and `renderer` from text input;
- the browser renderer applying a visual scene before optional audio/haptic output;
- the power-on voice loop speaking a best-effort ROM summary;
- Braille focus feeds derived from renderer selection text;
- tests that use `screen_reader_support` as the final adaptation;
- response contracts that encode text/cards without required semantic meaning;
- visual density onboarding without a unified interaction profile.

These paths remain compatibility behavior until their owning SE slice replaces
and tests them. None is represented as the target experience.

## Synthetic journey baseline

The canonical fixture is
`tests/fixtures/semantic-experience/se0-journeys.v1.json`. It contains six
non-personal journeys:

1. calendar conflict and rescheduling;
2. table and trend comparison;
3. bill review and payment proposal;
4. privacy-sensitive sharing confirmation;
5. website form completion;
6. modality/device loss and recovery.

Each journey identifies required meaning, exact content, actions, risk,
provenance, confirmation, and recovery without visual-control vocabulary.

## Baseline measures

| Measure | Pre-SE baseline | SE0-SE3 software target |
| --- | --- | --- |
| Required meaning represented structurally | No | Every fixture validates as SEM |
| Stable semantic references | No | Unique node/action identifiers |
| Conversation progressive detail | Best-effort summary | Detail, relative reference, interruption, resumption |
| Visual/conversation source parity | Shared text only | Same SEM and required identifiers |
| Braille independence from visual focus | No | Semantic navigation in simulation |
| Invalid action/reference handling | Inconsistent | Fail closed with explicit fallback |
| Interaction preference governance | Fragmented profile flags | Private lifecycle with proposal, approval, correction, reset, export, deletion |
| Hardware/lived-experience proof | Absent | Remains explicitly deferred |

Latency baselines remain environment-dependent and are captured in later
qualification. SE0-SE3 acceptance concerns software semantics and simulation,
not supported hardware or lived experience.


