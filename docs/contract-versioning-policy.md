# Contract and compatibility policy

- Cross-service contracts live in `unison-common` under an explicit versioned namespace such as `contracts.v1`.
- Additive, optional fields may remain within a major version when old readers continue to behave safely.
- Required-field changes, semantic reinterpretation, authority expansion, and removal require a new major contract version and a migration plan.
- Producers and consumers must carry contract tests. Workspace acceptance pins compatible revisions and records them as evidence.
- Security, privacy, consent, retention, physical-actuation, and safety fields are never silently defaulted to broader authority.
- Generated clients must be reproducible from the canonical schema, identify the source contract revision, and must not be edited manually.
- Deprecation requires a named owner, consumer inventory, replacement, deadline, rollback, and removal evidence.
