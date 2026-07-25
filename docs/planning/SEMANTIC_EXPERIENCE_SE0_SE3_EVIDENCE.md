# Semantic experience SE0 through SE3 acceptance evidence

Status: **Software scope complete; hardware and participatory validation deferred**  
Acceptance date: 2026-07-25

## Accepted scope

- SE0 records active response and modality paths, visual-first migration debt,
  six synthetic journeys, and measurable software baselines.
- SE1 adds strict Semantic Experience Model v1, semantic expression, and
  interaction profile contracts with canonical packaged JSON schemas.
- Orchestration constructs SEM from capability outcomes before producing a
  temporary ROM compatibility view.
- SE2 stores interaction profiles as private person-owned state with proposal,
  approval, correction, temporary override, reset, export, deletion, history,
  and non-oracular cross-person denial.
- SE3 provides independent conversational and visual composers over one SEM.
- Conversation supports progressive detail, stable references, interruption,
  resumption, correction, cancellation, and recovery.
- Braille composition navigates semantic identifiers without a visual focus feed.
- Invalid SEM and action bindings fail with explicit fallback behavior.

## Component candidates

| Repository | Commit | Scope |
| --- | --- | --- |
| unison-common | cf6f75c6c6f0956e9d590b9296d9d08a15a43578 | SEM, expression, and interaction-profile contracts |
| unison-context | beb5707fc204a05903822288821b786ed75ffafc | Governed interaction-profile lifecycle, authenticated route binding, and standalone CI dependency pin |
| unison-orchestrator | 283b986f50652dafdbe2bdcbef4b33b9f1ff4e3b | Semantic outcome construction, ROM adapter, and standalone CI dependency pin |
| unison-experience-renderer | 9ac534b18155dfab4d3a8c5e6d5a8b0a9956b853 | Native conversational and visual composers |
| unison-io-braille | 9c1749b60164c657c6b1b8dc74297010b2db8b6a | Native semantic Braille composer |

## Local evidence

| Suite | Result |
| --- | --- |
| unison-common complete unit suite | 312 passed, 1 skipped |
| Governed interaction profile plus repository suite | 13 passed |
| Orchestrator semantic builder | 2 passed |
| Existing renderer-emission regression | Passed independently |
| Renderer semantic composer conformance | Passed |
| Renderer Phase 8 and UI regressions | 3 passed |
| unison-io-braille complete suite | 19 passed |
| Workspace SE0 fixture and schema drift tests | Passed in integration candidate |

An existing orchestrator renderer client-cache interaction can make its
renderer-emission test fail when it follows another test that replaces the same
process-global HTTP client. Both suites pass independently. This is retained as
test-isolation debt and does not alter runtime semantic behavior.

## Acceptance mapping

- Six SE0 fixtures represent required meaning, exact content, provenance, action
  risk, confirmation, and recovery without visual-control vocabulary.
- SEM rejects unknown fields, duplicate identifiers, and dangling relationships.
- SEM preserves policy, privacy, action, provenance, required, and exact fields.
- Conversation and visual composition return the same required node and action
  identifiers from one SEM.
- Braille simulation navigates the same semantic identifiers independently.
- Inferred adaptations remain proposed until the person approves them.
- Cross-person interaction profile reads return one non-oracular denial.
- Temporary overrides expire and restore durable preferences.

## Deferred validation

The complete SE-HW-01 through SE-HW-08 ledger remains open. SE3 software
completion does not claim microphone or speaker quality, real Braille device
compatibility, switch/AAC support, sign quality, haptic distinguishability, or
participant validation. SE7 owns those promotion gates.

## Gate decision

The defined SE0 through SE3 software deliverables and automated acceptance
criteria are complete. SE4 through SE12 remain planned and unimplemented.
Public GitHub Pages claims remain unchanged until qualification.
