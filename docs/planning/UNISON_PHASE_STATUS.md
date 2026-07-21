# Unison phase status

Status date: 2026-07-20  
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
| 0. Repository truth and architecture reconciliation | In review | Ready for human review; not passed | Local closeout candidate and evidence package complete; publication CI/fresh-clone checks remain after commit/push. |
| 1. Multi-principal identity and trusted request binding | Not started | Not evaluated | No implementation authorized before the final Phase 0 gate decision. |
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
| MkDocs clean strict build | Pass |
| JSDOM/axe | 45 generated pages, zero WCAG A/AA violation groups |
| Chromium/Playwright/axe | 42 substantive pages, zero WCAG A/AA violation groups |
| Internal links and preference smoke | 1,767 links resolve; skip-link keyboard order, reduced motion, and forced colors pass |

Two schema copies remain intentionally marked `migration-required`; the drift
validator warns but prevents untracked canonical drift. The expired-consent-token
test now matches the secure implementation and proves expiration is rejected.

## Remaining gate-verification items

These require publication of the reviewed working tree and therefore are not
performed implicitly:

1. Capture successful GitHub Actions links for the Linux and Windows jobs.
2. Run the documented sequence from a genuinely fresh clone and confirm the
   repaired context gitlink resolves.
3. Record the human Phase 0 gate decision.

## Decisions awaiting human review

No Phase 0 product-architecture decision remains open. Exact algorithms, TPM
integration, rotation, and recovery ceremonies remain reserved for a focused
security review before their implementation.

## Next authorized action

Review the Phase 0 acceptance evidence and working-tree changes. If accepted,
publish them and complete the two publication checks. Do not begin Phase 1 until
the final Phase 0 gate decision is recorded.
