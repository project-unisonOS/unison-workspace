# Phase 4 acceptance evidence

Status: Complete

Prepared: 2026-07-21

Gate owner: human architecture/security review

Gate decision: Approved 2026-07-21

## Bounded acceptance claim

The review candidate demonstrates two independently governed adult assistants on
one Ubuntu 24.04 x86_64 development appliance profile. Each has a distinct
identity, assistant, key, credential, data, cache, index, private context, goal,
charter, memory, audit, and backup-policy boundary. Both coordinate through one
explicit household space containing only calendar and grocery artifacts. The
proof does not authorize or represent child, dependent, caregiving, incapacity,
or emergency-access relationships.

## Implemented evidence

- Versioned common contracts define household membership summaries, explicit
  coordination requests, shared facts, calendar events, grocery items, share
  previews, and per-assistant quotas.
- Household administration returns minimized operational membership fields.
  Member removal revokes membership, assistant, login, and sessions without
  transferring or decrypting private resources.
- Governed context requires a household identifier for shared spaces. Calendar
  and grocery coordination authorizes only explicit shared-space membership and
  records `private_sources_read: 0`.
- A round-robin scheduler enforces per-assistant concurrency, queue, CPU, and
  memory budgets. Its operational snapshot excludes task identifiers and content.
- Semantic web controls cover invitation, removal, share preview, calendar,
  groceries, audit, resource status, cancellation, and recovery with labelled
  controls, keyboard-native operation, and live status regions.

## Local execution

`./scripts/test-phase4.sh` passed 50 contract, component, integration, isolation,
canary, concurrency, quota, rollback, restart, removal, key-rotation, recovery,
denial, and accessibility checks. The synthetic report recorded:

| Metric | Result |
| --- | --- |
| Assistants | 2 |
| Shared artifacts created | 2 |
| Negative surfaces | 13/13 |
| Private sources read for coordination | 0 |
| Private canary values in report | false |
| Total concurrent tasks | 2 |
| Per-assistant concurrent limit | 1 |
| Per-assistant memory budget | 512 MiB |
| Proof runtime | 258.61 ms |
| Phase 5 started | false |

Focused component results are common/auth 21 passed, context 13 passed,
orchestrator scheduling 3 passed, and renderer accessibility 2 passed. The
platform household Compose overlay also resolves successfully with a synthetic
environment file.

The expanded workspace regression gate also passes: common 283/1 skipped, auth
36, consent 14, context 31, storage 3, policy 77, renderer 31, capability 24,
inference 9, payments 3, and orchestrator 209. Phase 0 static validation and the
complete Phase 1, Phase 2, and Phase 3 boundary gates pass unchanged.

Strict MkDocs rendering passes. The browser/axe audit checked 1,851 internal
links and reported zero WCAG A/AA violations across all 43 substantive pages,
including the updated household proof and status pages.

## Canary and boundary report

Distinct SHA-256 canaries represent API, storage, search, cache, embedding,
prompt, model, trace, log, audit, credential, backup, and error-oracle surfaces.
Every cross-person read and every missing-resource probe returns the same
non-oracular denial. The inference probe refuses both retrieval and guessing.
Actual governed search/export/audit state is independently checked for both
people, and shared coordination output contains no private canary.

## Published component candidates

- common contracts `7d8ac82fd5605dba2791c9ed34148c69f40897cc`:
  [unison-common#5](https://github.com/project-unisonOS/unison-common/pull/5)
- membership administration `5a9efed96568a38a075d568efba0273787dd6fea`:
  [unison-auth#10](https://github.com/project-unisonOS/unison-auth/pull/10)
- household coordination `9a339f6c17248f3e17f3b2fc1c4e5195504f2447`:
  [unison-context#15](https://github.com/project-unisonOS/unison-context/pull/15)
- resource scheduler `d0bb76106773c13f3d47c51cb437ac126f3fb225`:
  [unison-orchestrator#19](https://github.com/project-unisonOS/unison-orchestrator/pull/19)
- accessible controls `921fdcfea564d6405db9cc7fc0138aca816b4059`:
  [unison-experience-renderer#5](https://github.com/project-unisonOS/unison-experience-renderer/pull/5)
- appliance profile `96787683ef12af00e7beaf584c9006f14daf17ca`:
  [unison-platform#7](https://github.com/project-unisonOS/unison-platform/pull/7)
- integrated workspace `a1909e580b6e38f1669f566b06d8b775a5ecbed9`:
  [unison-workspace#5](https://github.com/project-unisonOS/unison-workspace/pull/5)
- public status `339307a85226a916bbfb08064eb331f76ce4c183`:
  [project-unisonos.github.io#5](https://github.com/project-unisonOS/project-unisonos.github.io/pull/5)

GitHub-hosted evidence is green where repository workflows exist:

- [common lint, contracts, Python 3.12/3.13, security, build, and package](https://github.com/project-unisonOS/unison-common/actions/runs/29876214748)
- [context tests](https://github.com/project-unisonOS/unison-context/actions/runs/29876218835)
  and [container build](https://github.com/project-unisonOS/unison-context/actions/runs/29876218844)
- [orchestrator tests](https://github.com/project-unisonOS/unison-orchestrator/actions/runs/29876221225)
  and [container build](https://github.com/project-unisonOS/unison-orchestrator/actions/runs/29876221186)
- [renderer tests](https://github.com/project-unisonOS/unison-experience-renderer/actions/runs/29876223122)
- [workspace static, unit, Phase 1-4, Windows, Bandit, Semgrep, Trivy, and SBOM gates](https://github.com/project-unisonOS/unison-workspace/actions/runs/29877079547)
- [site strict build and browser accessibility](https://github.com/project-unisonOS/project-unisonos.github.io/actions/runs/29876862543)

Auth and platform do not currently define repository-owned Actions workflows.
Their suites/configuration run locally and from the workspace's pinned recursive
checkout; this absence is reported rather than represented as hosted evidence.

## Fresh-clone evidence

A new recursive clone of workspace commit
`a1909e580b6e38f1669f566b06d8b775a5ecbed9` initialized all 19 submodules,
including the five Phase 4 component pins above. From only that clone, the locked
Python 3.12 bootstrap, Phase 0 static validation, Phase 1 trusted-principal gate,
Phase 2 governed-context gate, Phase 3 trust-governance gate, and 50-check Phase 4
household proof passed. The synthetic Phase 4 runtime was 321.47 ms. The temporary
clone was deleted after its commit and gitlink evidence was recorded.

## Known limitations

- This is a synthetic development-appliance proof, not a supported installer or
  production hardware qualification.
- Host-root compromise, hardware-backed keys, secure deletion, provider-blind
  backup/restore, and recovery ceremonies remain outside this phase.
- The surface matrix combines real identity/context/export/audit checks with
  explicit namespace/canary adapters for services not run as a live distributed
  stack. It is isolation evidence, not a timing side-channel certification.
- Resource quotas are an in-process scheduler proof; kernel/container enforcement
  and sustained-load characterization remain platform hardening work.
- Remote channels remain Phase 5 and provider-blind backup remains Phase 6.

## Final gate decision

The final Phase 4 gate was approved on 2026-07-21 after component, workspace,
and site Actions; recursive fresh-clone validation; and published accessibility
evidence completed. Phase 4 is **Complete**. Phase 5 was separately authorized
after this decision and starts from this accepted boundary.
