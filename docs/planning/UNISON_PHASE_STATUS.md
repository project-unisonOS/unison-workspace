# Unison phase status

Status date: 2026-07-25

Plan version: 0.1

## Status rules

- **Not started**: no phase implementation is authorized or evidenced.
- **In progress**: work has begun, but the gate is not ready for review.
- **In review**: the local review candidate and evidence package are ready; human approval and any named publication checks remain.
- **Complete**: every acceptance criterion has recorded evidence and human approval.
- **Blocked**: a named dependency prevents meaningful progress.

Tests or documents alone do not complete a phase. Planned architecture is never
credited as implemented.

## Phase overview

| Phase | Status | Gate | Summary |
| --- | --- | --- | --- |
| 0. Repository truth and architecture reconciliation | Complete | Passed 2026-07-21 | Final gate approved after publication, green workspace CI/security scans, and fresh-clone evidence. |
| 1. Multi-principal identity and trusted request binding | Complete | Passed 2026-07-21 | Final gate approved after publication, green workspace CI/security scans, fresh-clone validation, and review of the retained pre-existing debt. |
| 2. Context spaces, relationships, governed memory, charter | Complete | Passed 2026-07-21 | Final gate approved after publication, green component/workspace CI, browser accessibility, and recursive fresh-clone validation. |
| 3. Default-deny policy, disclosure, capability governance | Complete | Passed 2026-07-21 | Final gate approved after publication, green component/workspace CI, accessibility review, and recursive fresh-clone validation. |
| 4. Two-assistant household proof | Complete | Passed 2026-07-21 | Final gate approved after publication, hosted CI/security, browser accessibility, and recursive fresh-clone validation. |
| 5. Channel Gateway and remote text | Complete | Passed 2026-07-21 | Final gate approved after hosted CI, accessibility, channel isolation, replay/revocation, and fresh-clone evidence. |
| 6. Provider-blind backup and replacement restore | Complete | Passed 2026-07-23 | Final gate approved after hostile-provider, clean replacement restore, MinIO portability, browser accessibility, hosted security/CI, site deployment, and fresh-clone evidence. |
| 7. High-value assistant workflows | Complete | Passed 2026-07-23 | Final gate approved after seven bounded journeys, recovery/disclosure/security checks, hosted CI, browser accessibility, site deployment, and recursive fresh-clone evidence. |
| 8. Expanded multimodal surface and ecosystem | In progress | Expansion 8.1 passed 2026-07-23 | Initial speech/caption, adaptive surface, model-routing, and capability supply-chain slice is complete; specialized adapters remain experimental. |
| 9. Supported appliance release and lifecycle | In progress | Public software preview published 2026-07-24 | Lifecycle authority, deterministic runtime/manifest, installer and signed bundle, signed update authorization, checkpointed activation, rollback simulations, hardened image publication, signing/scanning, and public-download verification are merged. `v0.6.0-preview.1` is explicitly unsupported; seventeen physical checks remain deferred without being treated as passed. |
| 10. Adaptive maintenance and continuous improvement | In progress | AM-0 through AM-5 software gates passed; AM-6 and AM-7 software scope passed 2026-07-24 | Bounded reversible execution, hostile-source isolation, full-stack eligibility, calibration, support gates, and accessible history are implemented. Physical qualification, the real opt-in pilot, and human promotion of autonomous action classes remain pending. |
| 11. Private life operations and conversational data onboarding | In progress | LO-0 through LO-6 software gates and LO-7 synthetic gate passed 2026-07-25 | Household, health, finance, and governed cross-domain packages are implemented over the private intake foundation. A real opt-in value pilot and explicit human support decisions remain before closure. |

## Semantic experience program

| Slice | Status | Evidence |
| --- | --- | --- |
| SE0. Decisions, inventory, baseline | Complete | Active-path inventory and six synthetic journeys accepted 2026-07-25 |
| SE1. Semantic Experience Model v1 | Complete | Canonical schemas, strict bindings, orchestration output, and ROM compatibility accepted 2026-07-25 |
| SE2. Governed interaction profile | Complete | Private lifecycle, reversibility, expiry, export/delete, and cross-person denial accepted 2026-07-25 |
| SE3. Native expression composers | Complete | Conversational/visual equivalence and independent Braille simulation accepted 2026-07-25 |
| SE4. Person-aware expression planner | Complete | Reproducible mixed-I/O planning, deterministic privacy rules, audit explanations, and fallback accepted 2026-07-25 |
| SE5. Cross-modal continuity | Complete | Session continuity, one-time person-bound confirmations, and semantic equivalence gates accepted in simulation 2026-07-25 |
| SE6. Existing-experience interpreter | Complete | Provenance reconciliation, structured-source priority, injection isolation, and stale-target stopping accepted with synthetic sources 2026-07-25 |
| SE7. Qualification and publication | In progress | Software and simulated qualification complete; physical hardware, participatory testing, supported matrices, and public claims remain gated |
| SE8. Model task taxonomy and signed registry | Complete | Strict task requirements, signed immutable manifests, inventory separation, and fail-closed integrity accepted 2026-07-25 |
| SE9. Deterministic eligibility and routing | Complete | Hard eligibility, inspectable ranking, minimized per-operation disclosure, and negative-security gates accepted 2026-07-25 |
| SE10. Bounded model contribution | Complete | Typed untrusted proposals, source/fact/recipient/action reconciliation, and deterministic high-risk language accepted 2026-07-25 |
| SE11. Evaluation, canary, promotion, rollback | Complete | Golden journeys, approved comparison data, bounded canary, content-free health gates, state invariance, and automatic rollback accepted 2026-07-25 |
| SE12. Hardware qualification and publication | In progress | Qualification/matrix tooling and synthetic load/offline/update/rollback gates pass; physical appliance evidence and supported matrix remain open |

The accepted packages are
[SEMANTIC_EXPERIENCE_SE0_SE3_EVIDENCE.md](SEMANTIC_EXPERIENCE_SE0_SE3_EVIDENCE.md)
and [SEMANTIC_EXPERIENCE_SE4_SE7_EVIDENCE.md](SEMANTIC_EXPERIENCE_SE4_SE7_EVIDENCE.md).
SE8 through SE10 evidence is in
[SEMANTIC_EXPERIENCE_SE8_SE10_EVIDENCE.md](SEMANTIC_EXPERIENCE_SE8_SE10_EVIDENCE.md).
SE11 and SE12 evidence is in
[SEMANTIC_EXPERIENCE_SE11_SE12_EVIDENCE.md](SEMANTIC_EXPERIENCE_SE11_SE12_EVIDENCE.md).
All physical-device and participatory validation items remain open and keep the
SE7 supported-release gate in progress.

## Phase 0 review package

The authoritative evidence is in `PHASE0_ACCEPTANCE_EVIDENCE.md`. The local
candidate includes:

- all architecture recommendations 1-9 recorded as accepted in AD-007 and AD-016 through AD-025;
- a 35-component owner/maturity/disposition/topology inventory;
- canonical schema authority plus executable drift accounting;
- a deterministic Python 3.12 bootstrap, common unit/static commands, and a thin PowerShell-to-WSL wrapper;
- repaired local `unison-context` gitlink and fail-loud submodule synchronization;
- CI jobs for Linux Phase 0 validation and Windows wrapper parsing;
- synthetic two-adult private/shared fixtures and T-01 through T-30 test mapping;
- deprecated legacy prototype installer messaging;
- a truthful public product foundation, page inventory, dark design tokens, and real-browser accessibility CI.

## Executed evidence

| Evidence | Result |
| --- | --- |
| `./scripts/bootstrap-dev.sh` | Pass on WSL2 Ubuntu 24.04 / Python 3.12.3 |
| `./scripts/validate-phase0.sh` | Pass: manifests, schemas, fixtures, threat map, both Compose profiles, shell syntax |
| `.\scripts\unison.ps1 validate-phase0` | Pass; delegated to the authoritative WSL path |
| Core unit suites | 596 passed, 1 skipped |
| Workspace GitHub Actions | Pass: Linux Phase 0/unit, Windows parser, Bandit, Semgrep, Trivy, SBOM |
| Fresh recursive clone | Pass at `9c7abc1874876a8fc8a4425a839fa3f7454d0be6` |
| MkDocs clean strict build | Pass |
| JSDOM/axe | 45 generated pages, zero WCAG A/AA violation groups |
| Chromium/Playwright/axe | 42 substantive pages, zero WCAG A/AA violation groups |
| Internal links and preference smoke | 1,767 links resolve; skip-link keyboard order, reduced motion, and forced colors pass |

The post-Phase 3 stabilization sprint removed the obsolete event-envelope copy
and promoted the complete multimodal schema into canonical authority; schema
validation now reports zero migration items. The expired-consent-token test
matches the secure implementation and proves expiration is rejected.

## Final Phase 0 gate decision

The final Phase 0 gate was approved on 2026-07-21 after the named publication
checks completed. Phase 0 is **Complete**. Phase 1 was separately authorized and
completed on 2026-07-21.

## Phase 1 closeout package

The authoritative acceptance evidence is in `PHASE1_ACCEPTANCE_EVIDENCE.md`. It
includes identity migration v1, signed principal contracts, endpoint coverage,
two-person negative tests, key/log canaries, accessible enrollment, and a hardened
security Compose overlay. Publication, remote CI, recursive fresh-clone validation,
and the final human gate decision are complete.

## Final Phase 1 gate decision

The final Phase 1 gate was approved on 2026-07-21. Phase 1 is **Complete** and
Phase 2 is **Not started**. The four pre-existing CI/container debt items retained
at that gate were resolved in the separately authorized post-gate stabilization
sprint. Component commits, green Actions runs, local integration results, and
fresh-clone closeout are recorded in `PHASE1_STABILIZATION_EVIDENCE.md`.

## Final Phase 2 gate decision

The final Phase 2 gate was approved on 2026-07-21. Phase 2 is **Complete** and
Phase 3 was separately authorized. The authoritative closeout record is
`PHASE2_ACCEPTANCE_EVIDENCE.md`.

## Final Phase 3 gate decision

The final Phase 3 gate was approved on 2026-07-21. Phase 3 is **Complete** and
Phase 4 is **Not started**. Repository-owned CI gaps, inference regressions,
deprecated Actions runtimes, and legacy schema drift are assigned to the
separately authorized post-gate stabilization sprint. The authoritative closeout
record is `PHASE3_ACCEPTANCE_EVIDENCE.md`.

## Final Phase 4 gate decision

The final Phase 4 gate was approved on 2026-07-21. Phase 4 is **Complete**. The
authoritative closeout record is `PHASE4_ACCEPTANCE_EVIDENCE.md`. Phase 5 was
separately authorized after the gate and begins only after the ordered Phase 4
merges finish.

## Decisions awaiting human review

The Phase 6 software cryptographic profile, rotation, recovery ceremony,
retention/deletion behavior, and backend contract were approved on 2026-07-22
in AD-026 through AD-034. TPM-specific production integration remains a
separately validated backend and is not claimed by the software fallback.

## Next authorized action

Define the next independently authorized Phase 8 expansion. Later
modality/provider/capability expansions need their own threat, maintenance,
accessibility-research, and acceptance evidence.

## Final Phase 5 gate decision

The final Phase 5 gate was approved on 2026-07-21. Phase 5 is **Complete**. The
authoritative closeout record is `PHASE5_ACCEPTANCE_EVIDENCE.md`. Phase 6 was
separately authorized on 2026-07-22 and completed on 2026-07-23.

## Final Phase 6 gate decision

The final Phase 6 gate was approved on 2026-07-23. Provider-blind backup and
replacement-device restore are **Complete** within the recorded residual
limits. The authoritative closeout record is `PHASE6_ACCEPTANCE_EVIDENCE.md`.
Phase 7 was separately authorized on 2026-07-23 and is **Complete**. Phase 8
subsequently began as a continuing program.

## Final Phase 7 gate decision

The final Phase 7 gate was approved on 2026-07-23. Seven bounded high-value
assistant workflow families are **Complete** within the recorded residual
limits. The authoritative closeout record is
`PHASE7_ACCEPTANCE_EVIDENCE.md`. Phase 8 expansion 8.1 was subsequently
authorized and completed.

## Phase 8 expansion 8.1 gate decision

Expansion 8.1 was approved on 2026-07-23 after green component and workspace
CI, security scans, strict public-site accessibility and deployment checks, and
recursive fresh-clone validation. Its bounded speech/caption, adaptive surface,
model-routing, and signed capability-package scope is **Complete**. The
authoritative record is `PHASE8_EXPANSION_8_1_EVIDENCE.md`.

Phase 8 remains **In progress** as a continuing expansion program. Specialized
access adapters and every later model, channel, capability, or agent expansion
require independent authorization and acceptance; deferred categories remain
deferred.
