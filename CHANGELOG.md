# Changelog

All notable workspace-level architecture, planning, migration, and product-status changes are recorded here. Service-specific implementation changes remain in their repositories and are summarized here when they alter the authoritative product state.

## Unreleased

### Added

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
- Remote CI links and a truly fresh-clone run can only be captured after the review candidate is committed and published.
- Deep historical website pages still require phase-specific claim review even though the new entry pages state maturity accurately.
