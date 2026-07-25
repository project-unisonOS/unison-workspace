# Semantic experience SE4 through SE7 acceptance evidence

Status: **Software and simulated qualification scope complete; supported-release gates remain open**

Acceptance date: 2026-07-25

## Accepted software scope

- SE4 replaces binary renderer/voice routing with reproducible expression plans
  that select input and output independently from preferences, live health, risk,
  environment, privacy, latency, resources, and explicit choice.
- Quiet, shared-room, bystander, sensitive-content, offline, and failed-device
  rules are deterministic. Every exclusion and fallback has an audit explanation.
- SE5 retains semantic focus, references, pending actions, confirmation state,
  progress, recovery, and person identity while expressions change.
- One-time confirmations remain bound to the person and action across modality
  changes. They cannot be replayed.
- Semantic-diff gates compare required meaning, actions, and recovery.
- SE6 reconciles API, document, accessibility-tree, computer-use, and vision
  observations into SEM with provenance, confidence, ambiguity, and source
  priority. Structured observations precede vision observations.
- Untrusted content is data only. Injection text cannot grant authority, alter a
  recipient, remove confirmation, or override policy.
- Consequential targets use short-lived person/capability/state bindings and are
  revalidated immediately before execution.
- Stale or ambiguous targets stop with an understandable recovery path.

## Simulated qualification

The automated suite covers all six SE0 journeys, mixed input/output modes,
sensitive shared-room rules, offline planning, device fallback, modality
switches, one-time confirmations, semantic loss, provenance, table, chart,
image, form, error, confirmation, stale state, ambiguity, and prompt injection.

This is engineering evidence from synthetic fixtures. It is not physical-device
or lived-experience evidence.

## Accepted component commits

| Repository | Commit | Scope |
| --- | --- | --- |
| unison-common | 9463f917c7610594f57bae4847e3ddae48822486 | Expression-plan, session, equivalence, observation, target, risk, and provenance contracts |
| unison-orchestrator | 93ad889af5945000382a428a3a795c63567c76d4 | Deterministic planning, continuity, confirmation, equivalence, and interpretation |
| unison-experience-renderer | 76494b52026f8a6ee379bb29d1066dc6ad71394c | Modality-neutral renderer continuity and semantic-diff metadata |
| unison-capabilities | fc2c8a9fdce6bc3f141bc2939543f877dc5242bb | Authenticated, expiring, live-state target binding |

## Automated results

| Gate | Result |
| --- | --- |
| Strict semantic runtime contracts | 3 passed |
| Planner, continuity, equivalence, interpreter, and six-journey qualification | 22 passed |
| Capability target negative-security suite | 3 passed |
| Renderer composer and semantic-diff conformance | Passed |
| Expression planner host simulation | 1,000 plans under the 2-second CI budget |
| Component hosted CI, security, and container scans | Passed |

## Compatibility status

| Capability | Software status | Supported status |
| --- | --- | --- |
| Conversational and visual semantic expressions | Implemented and simulated | Awaiting participatory and appliance qualification |
| Braille semantic expression | Implemented and simulated | Awaiting representative displays and Braille-user validation |
| Expression planning and modality fallback | Implemented and simulated | Awaiting representative I/O and appliance profiles |
| Cross-modal continuity | Implemented and simulated | Awaiting multi-device restore and participant validation |
| Existing-experience interpretation | Implemented with synthetic sources | Awaiting camera, desktop, browser, document, and participant matrices |
| Sign, switch/AAC, haptic, and camera paths | Contract/design coverage only | Not supported |

## Open SE7 release gates

- SE-HW-01 through SE-HW-08 remain open.
- Participatory testing with people using the prioritized interaction modes has
  not occurred.
- Supported appliance latency, resource-contention, thermal, microphone,
  speaker, camera, Braille, switch/AAC, sign, and haptic matrices remain open.
- Public experience claims remain unchanged until those claims have direct
  compatibility and acceptance evidence.

SE7 software qualification is complete. SE7 supported-release qualification
remains deliberately open and prevents supported or accessibility-validated
claims.
