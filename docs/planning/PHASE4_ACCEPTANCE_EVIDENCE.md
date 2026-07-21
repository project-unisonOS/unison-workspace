# Phase 4 acceptance evidence

Status: In review

Prepared: 2026-07-21

Gate owner: human architecture/security review

Gate decision: Pending

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
- membership administration `5a9efed`:
  [unison-auth#10](https://github.com/project-unisonOS/unison-auth/pull/10)
- household coordination `9a339f6`:
  [unison-context#15](https://github.com/project-unisonOS/unison-context/pull/15)
- resource scheduler `d0bb761`:
  [unison-orchestrator#19](https://github.com/project-unisonOS/unison-orchestrator/pull/19)
- accessible controls `921fdcf`:
  [unison-experience-renderer#5](https://github.com/project-unisonOS/unison-experience-renderer/pull/5)
- appliance profile `9678768`:
  [unison-platform#7](https://github.com/project-unisonOS/unison-platform/pull/7)

Workspace, public-site, GitHub Actions, and recursive fresh-clone identifiers are
filled during publication closeout before the final gate decision.

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

## Gate condition

Phase 4 remains **In review** until component/workspace/site Actions, a recursive
fresh clone, published accessibility evidence, and human approval are recorded.
Phase 5 is **Not started** and is not authorized by this candidate.
