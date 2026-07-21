# Post-Phase 3 stabilization evidence

Status: Complete

Completed: 2026-07-21

Authorization: post-Phase 3 technical-debt stabilization; Phase 4 excluded

## Scope and result

The four debt groups retained at the Phase 3 gate are resolved:

- Consent, capabilities, and inference now define repository-owned Python test,
  Bandit, Semgrep, Trivy, and SBOM workflows using the immutable shared workflow.
- The complete inference suite passes. Stale model and provider expectations were
  reconciled, consent reload state is isolated, and remote fallback tests now
  provide the Phase 3 local-alternative and disclosure authority they require.
- GitHub-owned checkout, Python, Node, cache, artifact, Pages, and shared SBOM
  actions used by the affected repositories are pinned to Node 24-capable commits.
- The obsolete documentation event-envelope copy was removed. The richer packaged
  multimodal schema was promoted into canonical authority and now matches its
  packaged copy exactly. Schema validation reports zero migration items.

Hosted CI also exposed and closed three directly related defects: incomplete
inference dependency installation, vulnerable capability/consent dependency
pins, and a renderer accessibility-server startup race. Container bind findings
have narrow Bandit annotations documenting the intentional namespace bind; no
Bandit rule was disabled globally.

## Published commits

- shared workflows: `45118ffb52ee397cf7a510767154ee5b3705a850`
- common schema and workflows: `52d4b3dfdd71f15d8169b70e1dec05dc8a0c6f30`
- policy workflows: `83eb4e8fd5a60148cd7d28a85cb64f6e6e1335cb`
- consent CI and dependencies: `7c5e44e95e0c13974773ba5221acdbfeeed4612d`
- capability CI and dependencies: `ec72f59d58375b7f0fc825d1a68c332083db3813`
- inference regressions, CI, and image install: `6550ca7bbdc16f400b80b6d5f3e9efd24784fefa`
- renderer workflows and readiness: `201cf67a13867c10b1f24e0ed82a1f9f522465ac`
- public-site workflows: `d19d2c80690c03a8783d422fc6fb845871b45884`
- canonical-schema documentation cleanup: `8d474395e237ace9808a872bccd0bed2dc6651a3`
- integrated workspace candidate: `f239aae7b84f0a1860e508909d1aab3e07c0f124`

The component work remains attached to the existing Phase 3 draft pull requests.
The documentation schema cleanup was published directly to the `unison-docs`
default branch because that checkout was already on `main`; the workspace pins
the immutable resulting commit.

## GitHub Actions evidence

- [common contracts, Python 3.12/3.13, lint, security, and build](https://github.com/project-unisonOS/unison-common/actions/runs/29871178018)
- [policy tests](https://github.com/project-unisonOS/unison-policy/actions/runs/29871177990)
- [consent tests and security](https://github.com/project-unisonOS/unison-consent/actions/runs/29871752011)
- [capability tests and security](https://github.com/project-unisonOS/unison-capabilities/actions/runs/29871487770)
- [inference tests and security](https://github.com/project-unisonOS/unison-inference/actions/runs/29871754716)
- [renderer tests and real-browser accessibility](https://github.com/project-unisonOS/unison-experience-renderer/actions/runs/29871488469)
- [site build and accessibility](https://github.com/project-unisonOS/project-unisonos.github.io/actions/runs/29871179092)
- [workspace unit, Phase 0-3, PowerShell, and security](https://github.com/project-unisonOS/unison-workspace/actions/runs/29871785199)

All named checks passed. The shared workflow runs exercised tests, Bandit,
Semgrep, Trivy, and SBOM generation without global security-check exceptions.

## Fresh-clone evidence

A recursive clone of workspace commit
`f239aae7b84f0a1860e508909d1aab3e07c0f124` initialized all 19 submodules and
passed using only the clone's locked development environment:

- `scripts/bootstrap-dev.sh`;
- `scripts/test-unit.sh`: 707 passed, 1 skipped, including inference 9/9;
- `scripts/validate-phase0.sh`: 35 topology records, 7 canonical schemas, zero
  migration items, and 30 threat mappings;
- `scripts/test-phase1.sh`: passed;
- `scripts/test-phase2.sh`: passed;
- `scripts/test-phase3.sh`: 34 passed.

Existing deprecation warnings in application/test libraries are not failures and
were not expanded into this bounded sprint. They remain candidates for a future
dependency-modernization effort rather than authorization to begin Phase 4.

## Boundary

The authorized post-Phase 3 stabilization effort is **Complete**. Phase 3 remains
**Complete**. Phase 4 remains **Not started** and is not authorized.
