# Unison phase status

Status date: 2026-07-23

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
| 7. High-value assistant workflows | In review | Candidate gate | Seven bounded workflow families pass local journey, boundary, recovery, disclosure, and accessibility gates under AD-035 through AD-040. |
| 8. Expanded multimodal surface and ecosystem | Not started | Not evaluated | Modality repositories remain uneven and experimental. |

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

Complete Phase 7 hosted workspace CI/security, recursive fresh-clone
validation, and post-merge public-site deployment; then record the final gate.
Phase 8 remains **Not started** and is not authorized.

## Final Phase 5 gate decision

The final Phase 5 gate was approved on 2026-07-21. Phase 5 is **Complete**. The
authoritative closeout record is `PHASE5_ACCEPTANCE_EVIDENCE.md`. Phase 6 was
separately authorized on 2026-07-22 and completed on 2026-07-23.

## Final Phase 6 gate decision

The final Phase 6 gate was approved on 2026-07-23. Provider-blind backup and
replacement-device restore are **Complete** within the recorded residual
limits. The authoritative closeout record is `PHASE6_ACCEPTANCE_EVIDENCE.md`.
Phase 7 was separately authorized on 2026-07-23 and is **In review**. Phase 8
remains **Not started**.
