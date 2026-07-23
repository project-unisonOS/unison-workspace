# Phase 8 expansion 8.1 acceptance evidence

Status: **Engineering candidate**
Evidence date: 2026-07-23
Phase 8 program: **In progress**

## Bounded claim

Expansion 8.1 covers semantic modality negotiation; local streaming speech,
barge-in, captions, and non-voice fallback; adaptive keyboard/screen-reader
visual controls with high contrast, reduced motion, and simplified-language
preferences; privacy/cost/risk/offline model routing; and Ed25519-signed,
permission-diffed, compatibility-checked, revocable capability packages.

It does not promote Braille, sign, switch/AAC, or haptic adapters beyond
experimental status. Those require representative disabled-user research,
assistive-hardware evidence, maintenance ownership, and incident exercises.
BCI, robotics, spatial control, and autonomous financial actions remain deferred.

## Threat and maintenance review

| Expansion | Assurance and privacy | Failure/recovery | Maintenance |
| --- | --- | --- | --- |
| Local speech/captions | Speech is intent input, never identity or protected-action authority; raw audio is local and bounded | Explicit/voice interruption, caption/keyboard fallback, visible error | `unison-io-speech`; local ASR/VAD matrix and incident contact required per release |
| Adaptive surface | Preferences are person-scoped; semantic actions do not depend on color, motion, speech, or visual presence | Caption/text fallback retains confirm, cancel, retry, recover, dismiss | `unison-experience-renderer`; browser/AT matrix per release |
| Model routing | Candidate must satisfy location, disclosure, cost, risk, and offline profile simultaneously | No eligible candidate fails closed; compatible provider replacement remains explicit | `unison-inference`; provider/model policy reviewed independently |
| Capability ecosystem | Trusted Ed25519 publisher, exact canonical manifest, least authority, compatibility, sandbox, revocation | Tamper/unknown publisher/revocation/incompatible host deny; permission expansion requires review | Capability maintainer, incident contact, SBOM/provenance, revocation ID and end-of-support required |

T-06, T-11, T-12, T-14, T-21, T-22, T-26, and T-28 are directly exercised.
No adapter, model, or delegated agent gains authority from modality presence or
model output.

## Acceptance matrix

| Requirement | Evidence |
| --- | --- |
| Semantic equivalence | Canonical v1 outcome requires preserved fallback actions |
| Voice and caption parity | Partial/final captions, explicit stop and voice/control barge-in |
| Adaptive accessibility | Keyboard control, live caption, high contrast, reduced motion, simplified-language preferences |
| Graceful/offline fallback | Modality negotiation and local-only offline model route |
| Model replacement/risk routing | Disclosure, location, cost, risk, and availability constraints fail closed |
| Supply chain | Ed25519 verification rejects tamper and unknown publisher |
| Permission update | Added action/data/recipient/egress/file/device authority requires explicit review |
| Revocation/compatibility | Revoked and incompatible packages deny |
| Documentation | Supported matrix, experimental labels, adapter conformance and public boundary |

## Evidence required before final expansion approval

- Full component and aggregate regressions.
- Hosted component and workspace security/CI.
- Strict public-site build and real-browser accessibility audit.
- Recursive fresh clone with the Phase 8 aggregate gate.

Research with disabled people is not fabricated or replaced by simulation. It
remains a prerequisite for promoting specialized access adapters.
