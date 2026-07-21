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
| 1. Multi-principal identity and trusted request binding | Not started | Not evaluated | No Phase 1 implementation is authorized; separate approval is required. |
| 2. Context spaces, relationships, governed memory, charter | Not started | Not evaluated | Target schemas do not exist. |
| 3. Default-deny policy, disclosure, capability governance | Not started | Not evaluated | Existing logic is retained evidence, not target completion. |
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
checks completed. Phase 0 is **Complete**. Phase 1 remains **Not started** and
requires separate explicit authorization.

The schema-only orchestrator pull request still exposes pre-existing
repository-level CI/container failures that also occur on its unchanged `main`
baseline; the schema-dependent orchestrator suite passes all 203 tests in
workspace CI and the clean clone. The baseline orchestrator failures remain
tracked debt and are not represented as resolved by the Phase 0 gate.

## Decisions awaiting human review

No Phase 0 product-architecture decision remains open. Exact algorithms, TPM
integration, rotation, and recovery ceremonies remain reserved for a focused
security review before their implementation.

## Next authorized action

Maintain the Phase 0 evidence and review its published changes. Do not begin
Phase 1 unless it receives separate explicit authorization.
