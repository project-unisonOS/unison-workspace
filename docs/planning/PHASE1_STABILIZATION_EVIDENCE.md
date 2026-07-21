# Phase 1 post-gate stabilization evidence

Status: Complete

Prepared: 2026-07-21

Scope: the four pre-existing CI/container debt items retained at the final Phase 1 gate. This work does not start or implement Phase 2.

## Resolution summary

| Tracked debt | Resolution | Evidence |
| --- | --- | --- |
| `unison-common` lint, Bandit, packaging, dependency installation, and audit failures | Repaired lint/type defects, replaced unsafe or overbroad patterns, migrated common JWT handling to PyJWT, modernized runtime/test dependencies, isolated the runtime audit, and repaired stale Actions dependencies | 268 passed/1 skipped locally; Ruff, MyPy, Bandit, build, Twine, and dependency audit pass; all PR checks green |
| Private `unison-common-wheel:latest` authentication failures | Context, storage, policy, and orchestrator container builders now build the common wheel from an immutable public source commit (`5337e80894bb2430341e3210e2821c8dd8ca643e`) | Every affected container supply-chain job builds and passes remotely without private-registry credentials |
| Orchestrator repository test/container failures | Pinned the repaired common source, modernized compatible dependencies, and explicitly loaded the asyncio pytest plugin while plugin autoload remains disabled | 203/203 tests execute and pass; repository and both container checks pass |
| Platform `release.yml` SC2231 | Quoted the invariant portion of the release-asset glob while preserving `.part*` expansion | Both platform actionlint jobs pass |

## Published component commits

| Repository | Commit |
| --- | --- |
| `unison-common` | `38a00afa63e021d77743dc8162f49a1816083758` |
| `unison-context` | `68491e4aa47e2014f2933fc22ef95cbb6e1622e5` |
| `unison-storage` | `59a9517908a1364df196ec2bce3fc74b7b0d0b83` |
| `unison-policy` | `e13f9c33222ed247b4dfd2adc7108ff6806745e2` |
| `unison-orchestrator` | `17bce356f8ef6912e3e8121b47b4c293008b9311` |
| `unison-platform` | `88bfd76317e49824496e7770ece4592ab96645c8` |

## GitHub Actions evidence

- Common: runs `29857130742`, `29857132053`, and `29857130948` pass package tests, Python 3.12/3.13 tests, contracts, lint/type checks, Bandit/dependency audit, and package build.
- Context: runs `29857076299`, `29857071985`, and `29857076279` pass both container builds and the test suite.
- Storage: runs `29857076995` and `29857076452` pass both container builds.
- Policy: runs `29857079070`, `29857075880`, and `29857079067` pass both container builds and the test suite.
- Orchestrator: runs `29857081635`, `29857078396`, `29857081602`, and `29857081540` pass both container builds, the repository build, and the 203-test suite.
- Platform: runs `29857083757` and `29857082471` pass actionlint.

## Local integration evidence

- A new isolated workspace bootstrap completed with Python 3.12 and `pip check` reported no broken requirements.
- The workspace lock now uses the compatible OpenTelemetry 1.44/0.65 stack, PyJWT 2.13, pytest 9.1, and non-vulnerable bootstrap tooling.
- `validate-phase0.sh` passes all seven validation stages.
- `test-unit.sh` passes across all nine core repositories: common 268 passed/1 skipped, auth 35, consent 12, context 18, storage 3, policy 71, renderer 24, payments 3, and orchestrator 203.
- `test-phase1.sh` passes endpoint/product-profile validation, 40 trusted-principal tests, and the 11/4/2 communications/capability/actuation gates.
- Runtime dependency audits for common, context, storage, policy, and orchestrator report no known vulnerabilities; the local common package is correctly reported as not published on PyPI.

## Closeout

The enumerated Phase 1 technical debt is resolved. Phase 1 remains **Complete**; this stabilization does not reopen its approved architecture gate. Phase 2 remains **Not started** and requires separate authorization.

Workspace publication and recursive fresh-clone evidence are recorded in the final stabilization publication commit.
