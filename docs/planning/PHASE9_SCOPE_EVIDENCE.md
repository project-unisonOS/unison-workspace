# Phase 9.0 scope and lifecycle evidence

Status: Candidate gate passed locally on 2026-07-23

## Decisions and exact scope

AD-046 through AD-049 establish the lifecycle owners, one support candidate,
TUF update authority, rollback authority, release/support window, telemetry
default, and hardware tiers. The machine-readable authority is
`manifests/appliance-lifecycle.v1.json`; the public-facing engineering policy is
`docs/product/APPLIANCE_SUPPORT_POLICY.md`.

The support candidate is a signed native Ubuntu 24.04 LTS x86_64 UEFI bundle.
No existing WSL2, VM, ISO, arm64, or native artifact is promoted by this gate.

## Repository reconciliation

- `unison-platform` is pinned at `bd80a4a5ad84dc852a9e6d17ff793ba1a70d6a45`,
  the audited lifecycle implementation baseline.
- `unison-updates` is now a real workspace submodule pinned at
  `7f8056960c5057b52ae846a90a3477bc281e83c8`.
- Its GitHub `main` branch requires one approving review, dismisses stale
  reviews, requires resolved conversations and linear history, and disallows
  force pushes and branch deletion.
- `unison-os` remains explicitly legacy/archive in the component manifest.

## Validation

`./scripts/validate-phase9.sh` verifies the locked target, immutable runtime
requirement, telemetry default, TUF authority, reversible stable migrations,
and initialized immutable lifecycle repository pins.

Phase 9.0 does not claim that the runtime, installer, update channel, hardware
matrix, release pipeline, or pilot gates have passed. Those remain Phase
9.1 through 9.6.
