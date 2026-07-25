# Phase 10 AM-4 through AM-7 evidence

Status: Software scope passed 2026-07-24; physical qualification and real pilot pending

## Pinned implementation

| Boundary | Commit | Evidence |
| --- | --- | --- |
| Canonical contracts | `unison-common` `b27f64c72ddc407e069b799f2c71dd9474091940` | Exact autonomy grants and categorically non-executable community claims |
| Lifecycle operations | `unison-platform` `a8f2cb87b9ac948ba51b731b81598542d7c46ba1` | Bounded executor, persistent Phase 9 bridge, signed scheduled collectors, packaged service, calibration, pilot gates, and runbooks |
| Accessible experience | `unison-experience-renderer` `2ef3b8c5f24ac8f6d2c0d22c9d1294fa6fcecdac` | Allowlisted receipt history, discovery-only test proposals, and authenticated owner decisions |

## AM-4

The executor rejects expired or revoked grants, unknown action classes,
exhausted action or downtime budgets, missing checkpoints, unsigned artifacts,
discovery-only evidence, and an open circuit breaker. A failed canary health
gate restores the checkpoint and emits a content-free receipt.

Supported bounded classes are service restart or failover, disposable cache
housekeeping, signed patch staging, and model or configuration rollback.

The persistent coordinator now delegates signed patch staging to the Phase 9
checkpoint, activation, bounded health, and rollback transaction. Grants,
action budgets, recommendation decisions, cooldowns, circuit breakers, source
runs, and receipts survive service restart. A renderer decision is a mode-0600
queue record and must pass independent Lifecycle verification.

## AM-5

Community collectors are restricted to enabled discovery-only registry entries,
allowlisted hosts, bounded payloads, and non-instruction content. Claims receive
immutable hashes, duplicate clustering, corroboration, and conflict detection.
Their strongest authority is `test-proposal-only`; they cannot create a grant,
select an executable artifact, or invoke Lifecycle.

The preview bundle now contains a release-signed registry and an hourly
recommend-first service. Initial read-only sources are Unison releases, Ubuntu
security notices, GitHub reviewed advisories, and discovery-only Hacker News
story identifiers. Tests reject changed registry payloads and source redirects
outside the signed host boundary.

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
health gates, rollback, restart-persistent authority and receipts, tampered
source registries, unsupported firmware, and blocked pilot promotion.
