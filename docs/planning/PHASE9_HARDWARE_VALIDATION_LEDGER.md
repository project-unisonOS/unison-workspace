# Phase 9 hardware validation ledger

Status: Deferred until compatible physical hardware is available

This ledger is the human-readable index for
`manifests/phase9-hardware-validation.v1.json`. It prevents CI, simulation, VM,
or WSL evidence from being mistaken for physical appliance validation.

## Rules

- Every physical test has a stable `HW-nnn` identifier.
- `pending-hardware` is expected and does not block environment-independent
  implementation work.
- An item may become `passed` only for an exact immutable release candidate,
  with a checked-in evidence record identifying system model, CPU, RAM,
  storage, firmware, peripherals, model profile, commands, results, maintainer,
  and date.
- VM and container tests may validate installer logic and failure handling, but
  cannot satisfy UEFI, firmware, Secure Boot, TPM, audio, Bluetooth, suspend,
  thermal, power, or physical fresh-install items.
- Phase 9 cannot be marked complete while any item remains pending or blocked.

## Deferred test groups

| IDs | Gate | Physical evidence still required |
| --- | --- | --- |
| HW-001–004 | 9.1 | Cold start, reboot, pressure/fault behavior, shutdown and recovery |
| HW-005–007 | 9.2 | Clean UEFI install, interrupted lifecycle operations, accessible first run |
| HW-008–009 | 9.3 | Real promoted update and rollback cycles under failure |
| HW-010–014 | 9.4 | Reference systems, probes, audio, models, power states, replacement restore |
| HW-015 | 9.5 | Public-download install on a fresh external machine |
| HW-016–017 | 9.6 | Full-matrix pilot, support, export, removal, and reset |

CI-verifiable work may continue for manifest determinism, Compose isolation,
secret generation, installer transactions, update metadata attacks, artifact
signing, SBOM/provenance, documentation generation, and simulated failure
injection. Its evidence must retain a `simulation` or `ci` environment label.
