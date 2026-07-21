# Phase 2 acceptance evidence

Status: Complete

Prepared: 2026-07-21

Gate owner: human architecture/security review

Gate decision: Approved 2026-07-21

## Acceptance mapping

| Criterion | Implementation | Evidence |
| --- | --- | --- |
| Canonical domain model | Governed context v2 models/schema for spaces, memberships, relationships, memory, charter, goals, commitments, and privacy state | Common contract/schema tests and schema manifest |
| Durable authority | Migration-managed SQL repository and `/v2` API in `unison-context`; graph service explicitly non-authoritative | Repository/API/authority tests |
| Private/shared isolation | Independent private spaces; explicit shared create/invite/accept/copy; relationship edges never grant access | Two-person canary and non-oracular API tests |
| Retrieval/inference partitioning | Search defaults private; explicit-space prompt assembly checks membership, purpose, and inference flag | Repository and orchestrator client tests |
| Memory lifecycle | Admission, provenance, confidence, correction history, deletion, retention, inspection, and export | Restart/migration and reconciliation tests |
| Person-aligned objectives | Versioned personal charter with prohibited third-party objectives; origin-bearing goals/commitments | Repository tests |
| First shared artifacts | Calendar-event and grocery-item record kinds plus synthetic shared artifacts | Contract/repository/fixture tests |
| Accessible controls | Semantic privacy response and labelled keyboard-native create/correct/delete/share/charter/goal/commitment controls | Renderer source/API tests plus Chromium and axe browser evidence |

## Isolation and inference report

The Phase 2 fixture defines Alice and Bob with separate assistant/private-space
identifiers and unique memory, summary, and derived-index canaries. The gate tests
prove Alice's canaries are absent from Bob's default search and export, explicit
access to Alice's space is denied, and Bob cannot build a prompt from it. The same
contact appears as both friend and business; omitting the relationship label
requires an explicit context choice. A selected grocery record can be copied into
an accepted shared space without reclassifying its private source.

## Retention, deletion, migration, and restart

Ephemeral retention disables backup/sync and expires content. Delete/expiry redact
current and correction-history payloads. Export includes only currently authorized
active records. Member removal revokes all record/summary/index access and advances
the space key version. Correction provenance and revisions survive repository
restart. Legacy profile/conversation/dashboard migration is private-only and
idempotent.

## Local gate command

```text
./scripts/test-phase2.sh
```

This validates the fixture, canonical contracts, repository/API, explicit prompt
client, renderer accessibility source/response, graph authority, and cross-person
boundary tests. The pinned local run passed 26 combined tests plus the isolated
context-graph authority test. The complete regression also passed:

- deterministic bootstrap and `pip check`;
- Phase 0 validation: 35 components, 5 canonical schemas, 30 threat mappings,
  both Compose profiles, and shell syntax;
- all nine core unit suites, including common 275 passed/1 skipped, context 29
  passed, renderer 27 passed, and orchestrator 206 passed;
- Phase 1 endpoint inventory (156 protected/63 public), 40 core boundary tests,
  and the communications/capability/actuation gates.

Real Chromium plus axe reports zero WCAG A/AA violations over 34 identity and
context controls. It also performs shared-space creation using native form/button
interaction and observes semantic status feedback. The public site builds strict,
resolves 1,767 internal links, and has zero Playwright/axe violations across all
42 substantive pages.

## Publication and CI evidence

Published component commits and draft review PRs:

| Repository | Commit | Review |
| --- | --- | --- |
| `unison-common` | `f17a28de8421fabf94118375e7be98b4ca5eee97` | [PR 3](https://github.com/project-unisonOS/unison-common/pull/3) |
| `unison-context` | `4be90f569204bba5f9df15310c1efd1cef0fe885` | [PR 14](https://github.com/project-unisonOS/unison-context/pull/14) |
| `unison-orchestrator` | `311164c3256b9971f5b460dca2b3b6d5fc2a6721` | [PR 18](https://github.com/project-unisonOS/unison-orchestrator/pull/18) |
| `unison-experience-renderer` | `e6af5d2cffa5e61520c558c4265f8ebbb05e9a27` | [PR 3](https://github.com/project-unisonOS/unison-experience-renderer/pull/3) |
| `unison-context-graph` | `092da683f6cd8b10905a8cb5cd21ca9c8566b944` | [PR 3](https://github.com/project-unisonOS/unison-context-graph/pull/3) |
| `.github` | `352fdb0092da216d48062549598740c14eb37e53` | [PR 2](https://github.com/project-unisonOS/.github/pull/2) |
| `project-unisonos.github.io` | `890c982815533985734935f7d6e90cd6333a35c7` | [PR 3](https://github.com/project-unisonOS/project-unisonos.github.io/pull/3) |
| `unison-workspace` candidate | `3fe046c3942a02dc83f677128019337dc4421584` | [PR 3](https://github.com/project-unisonOS/unison-workspace/pull/3) |

All workflows for the published component commits completed successfully:

| Scope | GitHub Actions evidence |
| --- | --- |
| Common contracts | [Build unison-common](https://github.com/project-unisonOS/unison-common/actions/runs/29861844117) |
| Context authority | [Build](https://github.com/project-unisonOS/unison-context/actions/runs/29863725124), [tests](https://github.com/project-unisonOS/unison-context/actions/runs/29863725175), and [reusable security/container supply chain](https://github.com/project-unisonOS/unison-context/actions/runs/29863725965) |
| Orchestration | [build](https://github.com/project-unisonOS/unison-orchestrator/actions/runs/29863725740), [tests](https://github.com/project-unisonOS/unison-orchestrator/actions/runs/29863725725), [Docker build](https://github.com/project-unisonOS/unison-orchestrator/actions/runs/29863725721), and [reusable security/container supply chain](https://github.com/project-unisonOS/unison-orchestrator/actions/runs/29863726175) |
| Experience renderer | [CI and real-browser accessibility](https://github.com/project-unisonOS/unison-experience-renderer/actions/runs/29861849860) |
| Context graph | [CI](https://github.com/project-unisonOS/unison-context-graph/actions/runs/29862804755) |
| Public site | [strict build and deployment](https://github.com/project-unisonOS/project-unisonos.github.io/actions/runs/29861854757) |
| Workspace candidate | [Linux full regression, Phase 2 gate, Windows wrapper, Bandit, Semgrep, Trivy, and SBOM](https://github.com/project-unisonOS/unison-workspace/actions/runs/29865061799) |

The workspace security job recursively initialized the pinned topology, installed
the workspace lock plus immutable common contract, ran repository-owned boundary
tests, scanned production source with Bandit and Semgrep, scanned the workspace
lock with Trivy, and published an SBOM. The root lock was upgraded to fixed
releases for every finding exposed by that scan; component manifests remain the
responsibility of their independently scanned repositories.

## Recursive fresh-clone evidence

A new recursive clone was created at
`/tmp/unison-phase2-fresh-3fe046c` from the published branch. Its HEAD was verified
as `3fe046c3942a02dc83f677128019337dc4421584` before executing:

```text
./scripts/bootstrap-dev.sh
./scripts/validate-phase0.sh
./scripts/test-unit.sh
./scripts/test-phase1.sh
./scripts/test-phase2.sh
```

All commands passed on WSL2 Ubuntu 24.04 / Python 3.12.3. The recursive clone
resolved every required gitlink. Optional sibling repositories not represented by
gitlinks were reported as absent, as designed. The clone reproduced the Phase 0
validation and nine core unit suites, the Phase 1 boundary gate, and the Phase 2
26-test combined suite plus isolated context-graph authority test.

## Final gate decision

The final Phase 2 gate was approved on 2026-07-21 after publication, green
component/workspace Actions, and recursive fresh-clone evidence. Phase 2 is
**Complete**. Phase 3 was separately authorized and completed on 2026-07-21.
