# Phase 0 acceptance evidence package

Status: **Complete; final Phase 0 gate approved**

Evidence date: 2026-07-21

Approval date: 2026-07-21

Environment: WSL2 Ubuntu 24.04, Python 3.12.3, Docker Compose v2, Chromium via Playwright

## Decision and scope evidence

- AD-001 through AD-025 are recorded as accepted; recommendations 1–9 were approved on 2026-07-20.
- The six-boundary topology is recorded without beginning its Phase 1 runtime migration.
- `manifests/components.v1.json` maps 35 repositories/support components to an owner, maturity, target boundary, and disposition and drift-checks both current Compose profiles.
- `manifests/schemas.v1.json` declares `unison-common/schemas` authoritative. At
  the Phase 0 gate, two legacy copies were explicitly marked
  `migration-required`; the post-Phase 3 stabilization sprint subsequently
  resolved both without changing the authority rule.
- `tests/security/phase0-boundary-test-map.json` maps all threats T-01 through T-30 to planned phase evidence.
- The synthetic two-adult fixture contains independent private canaries and one explicitly shared household space.

## Reproducible developer path

Authoritative commands:

```bash
./scripts/bootstrap-dev.sh
./scripts/validate-phase0.sh
./scripts/test-unit.sh
```

Windows delegates to the same path with `scripts/unison.ps1`. A local invocation
of `unison.ps1 validate-phase0` completed successfully through WSL2. The Python
profile pins direct and transitive dependencies for Python 3.12. Legacy devstack
installers emit deprecation warnings and are not presented as appliance installers.

## Executed results

| Check | Result |
| --- | --- |
| Deterministic bootstrap/environment validation | Pass |
| Component/topology manifest | Pass: 35 records; devstack 23 services; native profile 13 services |
| Canonical schema JSON/drift check | Pass with 2 declared migration warnings |
| Synthetic household fixture | Pass |
| Threat-to-test mapping | Pass: 30/30 |
| Devstack and native Compose config | Pass |
| Shell syntax | Pass |
| PowerShell parser/delegation | Pass locally; Windows CI parser job added |
| Core Python unit suites | Pass: 596 passed, 1 skipped |
| Python security workflow | Pass: Bandit, Semgrep, Trivy filesystem scan, and SBOM |
| MkDocs clean strict build | Pass: 45 generated pages including redirect stubs |
| JSDOM/axe baseline | Pass: 45 pages, zero WCAG A/AA violation groups |
| Chromium/Playwright/axe | Pass: 42 substantive pages, zero WCAG A/AA violation groups |
| Built internal-link inventory | Pass: 1,767 local links resolve |
| Keyboard/media-preference smoke | Pass: skip link first; reduced-motion and forced-colors media active |

Unit totals: common 248 pass/1 skip; auth 19; consent 12; context 18;
storage 3; policy 71; renderer 22; orchestrator 203. The harness uses temporary
key directories and disables exporter delivery without disabling tracing behavior.

## Publication and remote CI evidence

| Published check | Result | Evidence |
| --- | --- | --- |
| Workspace Linux Phase 0 and unit suites | Pass | [GitHub Actions job](https://github.com/project-unisonOS/unison-workspace/actions/runs/29843469200/job/88677948008) |
| Workspace Windows PowerShell parser | Pass | [GitHub Actions job](https://github.com/project-unisonOS/unison-workspace/actions/runs/29843469200/job/88677947813) |
| Workspace security and supply-chain scan | Pass: Bandit, Semgrep, Trivy, SBOM | [GitHub Actions job](https://github.com/project-unisonOS/unison-workspace/actions/runs/29843469200/job/88677948218) |
| Renderer isolated CI | Pass: 22 tests | [GitHub Actions run](https://github.com/project-unisonOS/unison-experience-renderer/actions/runs/29840419083) |
| Website build and accessibility | Pass; deploy intentionally skipped for pull request | [GitHub Actions run](https://github.com/project-unisonOS/project-unisonos.github.io/actions/runs/29800442079) |

The reusable Python security workflow is restored at the GitHub-required path
and pinned by immutable commit `317183a033ed22031a06d6a757f55fd482f0c63f`.
The renderer installs `unison-common` from immutable commit
`17ad69a4eb91704f9286dc1694b71c4b455d815a`.

## Fresh-clone evidence

A new recursive clone of workspace commit
`9c7abc1874876a8fc8a4425a839fa3f7454d0be6` resolved every submodule,
including the repaired context gitlink, renderer commit
`b38a7a916ba9969dd3bce2c4921cbb15ee59954a`, and orchestrator commit
`63f5e2c35e02ee9eafcdc0a98769ed882fc24a4c`. From that clean checkout, the
documented sequence completed successfully:

```bash
./scripts/bootstrap-dev.sh
./scripts/validate-phase0.sh
./scripts/test-unit.sh
```

The standalone clone reported absent optional sibling repositories as notes,
validated the available development Compose profile, and passed all 596 tests
with one intentional skip. The six existing orchestrator schema contracts are
now versioned with their consumer, removing the former parent-directory
dependency.

## Repository coherence

- The previous `unison-context` gitlink `60e5e8a` is unavailable remotely.
- This review candidate updates the gitlink to valid `origin/main` commit
  `852bef92ab79e0422be17651a5345631ac35063c`.
- `scripts/sync.sh` no longer suppresses checkout/pull failures and resolves each
  submodule's upstream default branch.

## Website truth and accessibility

The public foundation now distinguishes Unison from UnisonOS, states the
pre-release status, explains the personal node and explicit context spaces,
documents honest external-provider limits, and avoids claiming a supported
appliance exists. Dark design tokens, visible focus, reduced-motion handling,
forced-colors fallbacks, keyboard-reachable code blocks, and real-browser axe CI
are present. See `UNISON_WEBSITE_INVENTORY.md` for page dispositions.

## Final gate conditions and residual items

The two named publication checks are complete, and the final Phase 0 gate was
approved on 2026-07-21. Phase 1 remains **Not started** and requires separate
authorization. The two declared legacy schema copies may migrate later behind
the new drift check; they cannot regain canonical status. Existing
dependency/deprecation warnings and unreviewed deep historical website pages
are recorded debt, not product guarantees.

The schema-only orchestrator pull request inherits two repository-level failures
that also fail on its unchanged `main` baseline: an obsolete shared-workflow
reference and an unauthenticated pull of the private `unison-common-wheel` image.
The schema change itself passes all 203 orchestrator tests through both the
workspace Actions job and the clean clone. Those pre-existing orchestrator
container/CI repairs are recorded debt and are not represented as healthy by
this package.

## Final gate decision

The final Phase 0 gate was approved on 2026-07-21. Phase 0 is **Complete**.
Phase 1 is **Not started** and no Phase 1 implementation is authorized without a
separate explicit approval.
