# Agent task packets

Task packets are durable, machine-readable execution contracts for human and
agent contributors. Validate them with `python scripts/validate-task-packets.py`.

Each packet names its objective, authority boundaries, writable repositories,
exact validation, evidence class, rollback, and handoff state. A packet grants
no authority beyond its explicit `allowed_changes` and `external_actions`.
