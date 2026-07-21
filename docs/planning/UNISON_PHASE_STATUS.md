# Unison phase status

Status date: 2026-07-21

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
| 3. Default-deny policy, disclosure, capability governance | In progress | Not yet ready | Authorized implementation of the accepted Phase 3 policy, disclosure, confirmation, credential, capability, audit, and accessibility scope. |
| 4. Two-assistant household proof | Not started | Not evaluated | No household isolation demonstration exists. |
| 5. Channel Gateway and remote text | Not started | Not evaluated | Existing adapters do not satisfy normalized remote-channel requirements. |
| 6. Provider-blind backup and replacement restore | Not started | Not evaluated | Target cryptographic backup/recovery is not implemented. |
| 7. High-value assistant workflows | Not started | Not evaluated | Existing Gmail/VDI/briefing slices are prototypes only. |
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

Two schema copies remain intentionally marked `migration-required`; the drift
validator warns but prevents untracked canonical drift. The expired-consent-token
test now matches the secure implementation and proves expiration is rejected.

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

## Decisions awaiting human review

Exact algorithms, TPM integration, rotation, and recovery ceremonies remain
reserved for a focused security review before their implementation.

## Next authorized action

Implement and evidence the complete Phase 3 acceptance scope, then request its
final human gate decision. Phase 4 remains **Not started** and is not authorized.
