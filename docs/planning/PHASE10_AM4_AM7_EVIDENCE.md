# Phase 10 AM-4 through AM-7 evidence

Status: Software scope passed 2026-07-24; physical qualification and real pilot pending

## Pinned implementation

| Boundary | Commit | Evidence |
| --- | --- | --- |
| Canonical contracts | `unison-common` `b27f64c72ddc407e069b799f2c71dd9474091940` | Exact autonomy grants and categorically non-executable community claims |
| Lifecycle operations | `unison-platform` `e95cf86207b2b18fe9fc0655bb2c81143b15d402` | Bounded executor, sandboxed collectors, full-stack eligibility, calibration, pilot gates, and runbooks |
| Accessible experience | `unison-experience-renderer` `8207f285e7b48ccb7262c4376ba3da319253dede` | Allowlisted receipt history and discovery-only test proposals |

## AM-4

The executor rejects expired or revoked grants, unknown action classes,
exhausted action or downtime budgets, missing checkpoints, unsigned artifacts,
discovery-only evidence, and an open circuit breaker. A failed canary health
gate restores the checkpoint and emits a content-free receipt.

Supported bounded classes are service restart or failover, disposable cache
housekeeping, signed patch staging, and model or configuration rollback.

## AM-5

Community collectors are restricted to enabled discovery-only registry entries,
allowlisted hosts, bounded payloads, and non-instruction content. Claims receive
immutable hashes, duplicate clustering, corroboration, and conflict detection.
Their strongest authority is `test-proposal-only`; they cannot create a grant,
select an executable artifact, or invoke Lifecycle.

## AM-6

Signed artifact, rollback, and exact-hardware eligibility is implemented for OS
packages, containers, drivers, model runtimes, models, capabilities, and
data/configuration. Firmware fails closed until vendor recovery is verified.

The physical validation ledger remains authoritative for power interruption,
reboot, boot failure, firmware failure, thermal/load, update, rollback, backup,
and restore. Those rows remain pending without compatible hardware.

## AM-7

Calibration records recommendation acceptance, rejection, realized benefit,
rollback, and alert burden without personal content. Pilot readiness requires
privacy, security, accessibility, incident, source-governance, and support
reviews plus a passed physical matrix and explicit human promotion.

CI-verifiable reviews and operational runbooks pass. No autonomous action class
is promoted. The real opt-in pilot remains pending until hardware and
participants are available.

## Validation

Run `UNISON_DEV_VENV=<venv> ./scripts/validate-phase10.sh`.

The suite exercises hostile community instructions and hosts, unsigned
artifacts, missing checkpoints, revoked grants, exhausted budgets, failed
health gates, rollback, unsupported firmware, and blocked pilot promotion.
