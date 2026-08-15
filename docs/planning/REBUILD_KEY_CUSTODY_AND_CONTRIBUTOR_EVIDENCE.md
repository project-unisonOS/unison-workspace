# Derived-view rebuild, durable custody, and contributor readiness

Status: implemented software foundation  
Date: 2026-08-14

## Derived-view rebuild and embedding migration

Unison now uses `dual-index-rebuild-and-swap`:

1. Keep the active source index available.
2. Persist one person-scoped rebuild job per authorized source record, bound to
   its exact revision, target algorithm, and target namespace.
3. Workers claim bounded batches and cannot complete a job if the source
   revision changed.
4. Mark migration ready only when every job completes.
5. Atomically supersede the person's old namespace while the rebuilt namespace
   remains active.
6. Retain the old views for explicit rollback; rollback invalidates the new
   views and restores the old namespace.

Models and indexes remain non-authoritative. Authorization still filters by
person, space, and domain before semantic ranking. Physical load, rebuild-time,
capacity, and GPU evidence remain deferred.

## Key custody and recovery

`MountedSecretKeyBroker` reads a root only from a regular, non-symlink mounted
file, requires at least 32 bytes, and on POSIX rejects group/world access. It
preserves opaque key handles and associated-data binding while removing the root
from environment variables and application databases.

`unison-infrastructure/environments/appliance-candidate.yaml` defines the
mount, rotation authority, independent checkpoint witness, backup journal,
local non-voice restore confirmation, replacement-device revocation, and
90-day drill interval. The accompanying runbook covers provision, backup,
restore, rotation, failure, and evidence boundaries.

This is software/configuration evidence. The profile is deliberately deferred:
it does not prove TPM/HSM sealing, encrypted-volume resistance, theft response,
or a witnessed human recovery drill.

## Organization contributor templates

`project-unisonOS/.github#5` was reviewed and is merged at `24f18afc`. The organization
now supplies agent-first issue and pull-request templates plus `AGENTS.md` and
`CONTRIBUTING.md`. The templates require objectives, authority, evidence,
privacy/security/accessibility constraints, validation, rollback, and durable
handoff information while remaining readable by people.

## Validation

- shared contract/schema and mounted-key tests;
- person-scoped dual-index rebuild, cutover, and rollback tests;
- infrastructure environment-schema validation;
- workspace schema and task-packet validation;
- hosted component and workspace CI after publication.
