# Changelog

All notable workspace-level architecture, planning, migration, and product-status changes are recorded here. Service-specific implementation changes remain in their repositories and are summarized here when they alter the authoritative product state.

## Unreleased

- Added the Phase 7 bounded assistant-workflow candidate: seven governed
  workflow families, inspectable plans, exact approvals, minimized provider
  disclosure, idempotent recovery and compensation, accessible controls,
  synthetic record/replay fixtures, and local time-return outcome evidence.
- Added the authorized Phase 6 provider-blind backup v1 candidate: canonical
  encrypted chunk/manifest/checkpoint contracts, independent person/shared
  scopes, hostile and S3-compatible backends, scheduled verification,
  retention/deletion/export, provider migration, clean replacement-device
  restore, recovery authority, accessible controls, and acceptance evidence.

### Added

- Phase 3 canonical Trust API contracts, default-deny disclosure evaluator,
  expiring one-use confirmations, encrypted task credential broker, explicit
  grant migration, governed remote inference, bounded capability manifests,
  adversarial/minimization gates, policy simulator, and accessible decision review.

- Phase 2 governed-context v2 contracts for spaces, memberships, relationships,
  memory governance, charters, goals, commitments, and semantic privacy state.
- Durable governed repository/API, private-by-default legacy migration, explicit
  shared-space invitation/copy flows, retention/deletion reconciliation, and
  purpose-bound prompt construction.
- Accessible context/privacy controls and a two-person canary fixture/gate suite.
- Governed-context architecture, privacy/denial examples, migration guidance,
  and Phase 2 acceptance evidence.

- Phase 1 transactional identity schema for people, assistant instances, households, memberships, devices, channels, workloads, sessions, passkeys, invitations, and independent isolation handles.
- Versioned signed principal-context and trusted-request-envelope contracts plus shared fail-closed binding middleware.
- First-person enrollment, additional-adult invitation, passkey, session/device/channel revocation, workload audience/delegation, and encrypted legacy-admin migration flows.
- One-command Phase 1 endpoint, boundary, migration, canary, and sibling-service validation.
- Principal trust-boundary architecture guide and Phase 1 acceptance evidence package.

- Authoritative implementation plan for the household-hosted private assistant product direction.
- Verified current-state audit covering the broader Project Unison repository checkout.
- Architecture decision register distinguishing accepted mandates from proposed decisions.
- Living threat model with required household, channel, model, capability, backup, recovery, accessibility, and supply-chain threats.
- Phase status record with observed test/configuration evidence and explicit unverified areas.
- Deterministic Python 3.12 bootstrap and common Phase 0 validation/unit entrypoints.
- Machine-readable component/topology, canonical schema, household fixture, and threat-test manifests.
- Thin PowerShell-to-WSL command wrapper and Linux/Windows Phase 0 CI jobs.
- Phase 0 acceptance evidence package and public website content inventory.

### Changed

- The final Phase 7 engineering gate was approved on 2026-07-23 after hosted
  CI/security, fresh recursive clone, browser accessibility, and public-site
  deployment passed. Phase 7 is **Complete** within its recorded limits;
  Phase 8 remains not started and unauthorized.
- The final Phase 2 gate was approved on 2026-07-21; Phase 2 is **Complete** and
  separately authorized Phase 3 implementation is **In progress**.
- `unison-context` is the authoritative governed-context API; `unison-context-graph`
  is an operational adapter and does not grant access or retain durable personal memory.
- The final Phase 1 gate was approved on 2026-07-21; Phase 1 is recorded Complete and Phase 2 remains Not started and unauthorized.
- Protected orchestrator, context, storage, renderer, policy, consent, payments, communications, capability, replay, and actuation paths now derive authority from the verified principal instead of caller identity hints.
- Context, storage, communications, cache, index, replay, vault, object, audit, and payment paths use person-specific namespace or key handles.
- The hardened Compose profile disables reusable broad service secrets and static/HS256 authentication in favor of audience-scoped signed tokens and unique service root keys.

- `unison-workspace` is designated as the home for authoritative planning because the aggregate parent checkout is not a Git repository.
- Prior milestone and production plans are treated as historical evidence when they conflict with `docs/planning/UNISON_IMPLEMENTATION_PLAN.md`.
- Approved the six-boundary default appliance topology: Unison Core, Personal Data and Trust Store, Capability Host, Channel Gateway, Inference Broker/Runtime, and Unison Surface, with privileged lifecycle operations and optional hardware adapters isolated separately.
- Approved canonical schema ownership, WSL/Linux development authority, adult-member administrator privacy, initial key/recovery principles, Ubuntu 24.04 x86_64 targeting, capability naming, Unison/UnisonOS terminology, and the person-aligned economic constraint.
- Prepared the valid `unison-context` gitlink, made submodule synchronization fail loudly, and deprecated the prototype devstack installers.
- Reconciled the core test harness to 596 passed and 1 skipped, including temporary key paths and expired-token rejection.
- Rebuilt the public product-truth foundation and added a strict real-Chromium accessibility gate; 42 substantive pages pass axe WCAG A/AA checks.

### Known issues

- Two declared non-authoritative schema copies differ from their canonical `unison-common/schemas` sources and remain migration items.
- The enumerated pre-existing `unison-common`, private-GHCR container, orchestrator, and platform actionlint failures remain tracked debt after the Phase 1 gate.
- Deep historical website pages still require phase-specific claim review even though the new entry pages state maturity accurately.
