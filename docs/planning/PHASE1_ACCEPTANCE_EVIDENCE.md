# Phase 1 acceptance evidence

Status: review candidate
Prepared: 2026-07-21
Gate owner: human architecture/security review

## Acceptance mapping

| Criterion | Implementation | Evidence |
| --- | --- | --- |
| Server-derived identity | Signed `PrincipalContext` and trusted request envelope in `unison-common`; auth introspection and audience checks in shared middleware | `test_principal.py`, `test_principal_middleware.py`, endpoint inventory |
| Transactional identity domain | SQLite migration v1 for person, assistant, household, membership, account, device, channel, workload, session, passkey, invitation, and resource handles | `0001_phase1_identity.sql`, `test_identity_store.py` |
| First and additional people | Explicit first-person bootstrap plus single-use household invitation acceptance | auth API/store tests and renderer enrollment tests |
| Passkey/session/workload binding | One-time Ed25519 challenge flow, monotonic counters, revocable sessions/devices/channels, narrow workload audiences and delegation | auth store/API tests |
| Protected endpoint coverage | Orchestrator, context, storage, renderer, policy, consent, payments, comms, capability, and actuation consume bound principal context | `phase1-endpoints.v1.json`; validator inventory |
| Cross-person isolation | Key, credential, data, cache and index handles; owner-derived replay/object/vault/audit/payment/action paths | synthetic two-person boundary matrix |
| Dependency failure safety | Token introspection and Redis-backed revocation deny when unavailable for protected operations | middleware and auth API negative tests |
| Migration safety | Encrypted backup, explicit confirmation, transaction rollback, interrupted-migration recovery and batch rollback | identity migration tests and migration CLI |
| Accessible enrollment | Labelled keyboard-operable form, confirmation, cancel control, live semantic status, and no voice-only sensitive flow | renderer accessibility tests and browser report below |
| Product profile hardening | Security Compose overlay disables HS256/static/broad secrets, uses auth audiences and unique root keys | Compose configuration validation and secret scan |

## Local command evidence

The local candidate produced the following green results on 2026-07-21:

```text
./scripts/validate-phase0.sh
./scripts/test-unit.sh
./scripts/test-phase1.sh
docker compose -f unison-devstack/docker-compose.yml -f unison-devstack/docker-compose.security.yml config --quiet
docker compose -f ../unison-platform/compose/compose.yaml config --quiet
mkdocs build --strict  # project-unisonos.github.io
```

- `test-unit.sh`: exit 0 across all ten core repositories; notable totals include
  268 passed/1 skipped in common, 35 passed in auth, and 203 passed in orchestrator.
- `test-phase1.sh`: 125 protected and 63 intentionally public endpoints inventoried;
  40 focused principal/identity/isolation tests plus 11 communications, 4 capability,
  and 2 actuation gate tests passed.
- Full sibling suites: communications 21 passed, capability 21 passed, actuation
  8 passed.
- Both Compose renders, the native installer shell check, the strict public-site
  build, and `git diff --check` passed.

`test-phase1.sh` is the single-command gate. It inventories protected endpoints,
runs principal/auth/migration/accessibility and two-person negative tests, runs the
available comms/capability/actuation sibling suites, and rejects production
`local-user` or `local-person` fallbacks.

## Negative-test and canary report

- Two independent people in one household are tested across read, write, search,
  cache, replay, object, vault, audit, key, credential, data, and index boundaries.
- Forged person/user/assistant/household/channel hints are rejected before route
  execution with the same non-oracular response.
- Workload tokens cannot be reused for an unlisted audience or substitute another
  person's authority.
- Session, device, channel, and person lock revocation invalidate authority.
- Key and credential canaries are absent from safe logs, errors, prompts, and the
  other principal's outputs.

## Enrollment accessibility report

Automated source/DOM checks verify associated labels, an explicit confirmation,
a cancel action, a live status region, keyboard-native controls, and text stating
that voice alone cannot complete sensitive enrollment or recovery. Renderer CI
installs Chromium and runs Playwright plus axe against WCAG A/AA, keyboard focus,
forced-colors, reduced-motion, and semantic-status checks. The published Actions
run is recorded below.

## Publication and fresh-clone evidence

Published component commits:

| Repository | Commit |
| --- | --- |
| `unison-common` | `d7ce26691dc187db7f7e2e87f767f4143078d412` |
| `unison-auth` | `03b72b6d4631caed3fbda3737f968ffffb0a5034` |
| `unison-consent` | `29b5631a376d6ec49a61bf308c635af6ae5dcb38` |
| `unison-context` | `dd97595f744622c0a4b138941344a4d8923142a1` |
| `unison-storage` | `d44cfe3700c1d5c2e90c8a6e3afccd9baa845423` |
| `unison-policy` | `ea33a6fbf2dc40fed81aa7aecc141aa94f6f9889` |
| `unison-payments` | `c3d793996097a1aac7c24fc681a5ad9c0720fb9a` |
| `unison-experience-renderer` | `7fa8e3f30eceb2a04995634ac7b2bb7f09cab86c` |
| `unison-orchestrator` | `f7e2ef87a64f60bb8b37bd83014a3a1cf35cf5d7` |
| `unison-devstack` | `bec610193d5e2ba4d6f7e1e1a14e4db4723f25ad` |
| `unison-comms` | `79df1270c8103103a98ae89ba22d05fec17d8082` |
| `unison-capabilities` | `19e8a73a889afe14600eabd4acccf1eb30159ff3` |
| `unison-actuation` | `1a61c135ba79e5904a07dfc9cf8a7063b9a492d0` |
| `unison-platform` | `a9f7254a3f8beb48ecf414ba0734b8818fa1d4ee` |
| `project-unisonos.github.io` | `7a345d7ba13a4c7547b7b1f0e06bdf1d6dfe7424` |

Workspace implementation and gitlinks are published through
`a06949b` on `agent/phase1-trusted-identity`.

## Review pull requests

The complete candidate is split into intentionally scoped draft PRs:

- [workspace](https://github.com/project-unisonOS/unison-workspace/pull/2),
  [common](https://github.com/project-unisonOS/unison-common/pull/2),
  [auth](https://github.com/project-unisonOS/unison-auth/pull/9),
  [consent](https://github.com/project-unisonOS/unison-consent/pull/2),
  [context](https://github.com/project-unisonOS/unison-context/pull/13),
  [storage](https://github.com/project-unisonOS/unison-storage/pull/10),
  [policy](https://github.com/project-unisonOS/unison-policy/pull/11), and
  [payments](https://github.com/project-unisonOS/unison-payments/pull/1).
- [renderer](https://github.com/project-unisonOS/unison-experience-renderer/pull/2),
  [orchestrator](https://github.com/project-unisonOS/unison-orchestrator/pull/17),
  [devstack](https://github.com/project-unisonOS/unison-devstack/pull/10),
  [communications](https://github.com/project-unisonOS/unison-comms/pull/1),
  [capabilities](https://github.com/project-unisonOS/unison-capabilities/pull/1),
  [actuation](https://github.com/project-unisonOS/unison-actuation/pull/1),
  [platform](https://github.com/project-unisonOS/unison-platform/pull/1), and
  [public site](https://github.com/project-unisonOS/project-unisonos.github.io/pull/2).

## Published CI evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Workspace Phase 0, unit, and Phase 1 suite | Pass | [GitHub Actions job](https://github.com/project-unisonOS/unison-workspace/actions/runs/29852937851/job/88710079089) |
| Workspace PowerShell wrapper | Pass | [GitHub Actions job](https://github.com/project-unisonOS/unison-workspace/actions/runs/29852937851/job/88710079221) |
| Workspace Bandit, Semgrep, Trivy, and SBOM | Pass | [GitHub Actions job](https://github.com/project-unisonOS/unison-workspace/actions/runs/29852937851/job/88710079382) |
| Context isolated tests | Pass: 18 tests | [GitHub Actions job](https://github.com/project-unisonOS/unison-context/actions/runs/29852386924/job/88708233007) |
| Policy isolated tests | Pass: 71 tests | [GitHub Actions job](https://github.com/project-unisonOS/unison-policy/actions/runs/29852391019/job/88708246436) |
| Renderer isolated tests and Chromium accessibility | Pass: Python tests plus Playwright/axe | [GitHub Actions job](https://github.com/project-unisonOS/unison-experience-renderer/actions/runs/29852394168/job/88708258112) |
| Public-site strict build and accessibility | Pass; deploy intentionally skipped for PR | [GitHub Actions run](https://github.com/project-unisonOS/project-unisonos.github.io/actions/runs/29852058678) |

Auth, consent, payments, devstack, communications, capabilities, and actuation
do not currently define PR-triggered Actions checks; their published commits
are covered by the workspace and repository-local evidence above.

## Fresh-clone evidence

A recursive clone of workspace implementation commit `c036b24` resolved every
declared submodule at its published commit. From that clone, the following
documented sequence passed:

```bash
./scripts/bootstrap-dev.sh
./scripts/validate-phase0.sh
./scripts/test-unit.sh
./scripts/test-phase1.sh
```

The final security-only `a06949b` delta adds Bandit justifications to test
assertions and does not change the recursive runtime or test topology. The
standalone clone reported optional siblings as notes, validated 94 protected
and 53 public core endpoints, passed all core unit suites, and passed all 40
focused Phase 1 tests. Sibling suites were separately green in the complete
development checkout.

## Tracked pre-existing CI debt

The following failures reproduce on each repository's default branch and are
not caused by the Phase 1 candidate:

- `unison-common` has legacy whole-repository lint, Bandit, packaging, and
  dependency-install failures ([candidate run](https://github.com/project-unisonOS/unison-common/actions/runs/29852017610)).
- Context, storage, and policy container builds cannot anonymously pull the
  private `unison-common-wheel` image from GHCR; isolated tests pass after the
  Phase 1 dependency repair.
- The previously accepted orchestrator test/container failures remain tracked
  debt ([candidate test run](https://github.com/project-unisonOS/unison-orchestrator/actions/runs/29852041681)).
- Platform actionlint reports the pre-existing `release.yml` SC2231 warning
  ([candidate run](https://github.com/project-unisonOS/unison-platform/actions/runs/29852055009)).

Phase 1 remains **In review** until this publication section is complete and the
human gate is approved. Phase 2 is not authorized by this candidate.
