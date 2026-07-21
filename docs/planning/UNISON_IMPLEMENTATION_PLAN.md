<!-- markdownlint-configure-file {"MD024": {"siblings_only": true}} -->

# Unison Authoritative Implementation Plan

Status: proposed execution source of truth; awaiting human review  
Plan version: 0.1  
Last updated: 2026-07-20

## Authority and maintenance

This is the single implementation plan for Project Unison. Future work updates this file rather than creating a disconnected plan. The verified baseline is in [UNISON_CURRENT_STATE.md](UNISON_CURRENT_STATE.md), decisions are in [UNISON_ARCHITECTURE_DECISIONS.md](UNISON_ARCHITECTURE_DECISIONS.md), security obligations are in [UNISON_THREAT_MODEL.md](UNISON_THREAT_MODEL.md), and evidence/status is in [UNISON_PHASE_STATUS.md](UNISON_PHASE_STATUS.md).

Planned work is never represented as implemented. A phase becomes complete only after every required acceptance criterion has evidence, unresolved exceptions are explicitly reviewed, and the status/current-state/decision/threat/changelog/public documentation set is updated.

## Reconciled vision

Unison is a downloadable, privately owned personal-assistant platform whose first product form is a capable household edge appliance. One appliance can host one or more independently governed personal assistants. Each assistant serves one primary person. Assistants may coordinate through explicit shared context spaces, but no assistant or household administrator implicitly gains another person's private memory, credentials, goals, charter, or keys.

Unison coordinates the person's existing devices, applications, services, websites, models, and communication channels. It is not a replacement for phones, desktop operating systems, or enjoyable applications. Its purpose is to return time, attention, control, and agency to the person while respecting the consent, rights, safety, and autonomy of others.

The product promise is an engineering constraint:

> **Unison is a private personal assistant that works only for you, understands the people and contexts in your life, and helps you reclaim time without selling, exploiting, or commercializing your personal context.**

## Verified starting point

The present implementation offers strong orchestration/common-contract unit coverage, working policy/capability/comms slices, a native Ubuntu Compose bundle, local/remote inference abstraction, a web renderer, modality projects, release/recovery tooling, and a large devstack. It does not yet provide trusted multi-principal identity, explicit context spaces, relationship-aware disclosure, per-person keys/credentials/indexes, a normalized remote channel, or provider-blind backup.

Key debt to address before capability expansion:

- caller-controlled identity fields and `local-user`/`local-person` defaults;
- overlapping policy/consent and context/context-graph/intent-graph services;
- storage namespaces and encryption not bound to authenticated principals;
- service-global connector credentials;
- permissive or optional authorization paths and a fail-open token blacklist;
- duplicated schemas and installation paths;
- inconsistent CI/bootstrap across repositories;
- public claims that mix implementation and vision;
- a 23-service developer default that is disproportionate for an appliance.

## Target architecture

### Logical layers

- **Unison Core**: authenticated intent intake, normalization, orchestration, planning, context/relationship retrieval, memory admission, charter evaluation, model routing, task/commitment management, semantic outcomes.
- **Personal Data and Trust Store**: principals, assistant/household membership, keys, credentials, governed data, policy, consent, disclosure decisions, and append-only audit.
- **Capability Host**: sandboxed tools, skills, connectors, browser/VDI/actuation, MCP servers, APIs, and future delegated agents.
- **Channel Gateway**: normalized local/remote transports, channel identity, assurance, replay protection, and draft-first outbound communication.
- **Inference Broker**: local and remote model routing with disclosure minimization and provider policy.
- **Unison Surface**: accessible conversation, approval, privacy, audit, context-space, household, capability, backup, and recovery experience.
- **Appliance Lifecycle**: privileged install, update, rollback, health, backup scheduling, and factory/reset operations.

### Proposed default deployment boundaries

The six principal boundaries above should become the default processes, with appliance lifecycle separately privileged and modality/hardware adapters optional. This proposal requires approval in AD-007. Migration preserves existing services behind adapters until tests prove equivalent behavior.

### Domain primitives

The canonical schema set will add:

`Person`, `AssistantInstance`, `Household`, `Relationship`, `ContextSpace`, `Membership`, `MemoryRecord`, `Goal`, `Commitment`, `ChannelIdentity`, `DisclosureDecision`, `CapabilityGrant`, and `PersonalCharter`.

Every memory record carries ownership, space, source/provenance, sensitivity, audiences, purposes, retention, confidence, inference/action/disclosure/backup/sync permissions, and version/deletion state.

### Trusted request flow

1. Authenticate a person, device, workload, or bound channel identity.
2. Derive the assistant instance and allowed household/space memberships.
3. Treat supplied identifiers as untrusted hints and reject mismatches.
4. Infer/select context; ask when ambiguous or disclosure-sensitive.
5. Retrieve only authorized context for the stated purpose.
6. Plan using capabilities granted to this principal/purpose.
7. Evaluate action and disclosure policy, including minimization.
8. Require confirmation or step-up authentication as needed.
9. Execute through the Capability Host with minimum credentials/context.
10. Return one semantic outcome adapted to the channel/modality.
11. Record an understandable, owner-visible audit entry.

## Dependency graph

```text
Phase 0: truth, contracts, DX, public status foundation
  |
  v
Phase 1: principals, assistant binding, keys, namespaces
  |
  v
Phase 2: spaces, relationships, governed memory, charter
  |
  v
Phase 3: default-deny action + disclosure + capability governance
  |
  +---------------------+
  |                     |
  v                     v
Phase 4: household proof   Phase 5: channel gateway
  |                     |
  +----------+----------+
             v
Phase 6: encrypted backup + replacement restore
             |
             v
Phase 7: high-value assistant workflows and outcome measurement
             |
             v
Phase 8: expanded modalities, channels, models, capability ecosystem
```

Phase 5 contract design can begin after Phase 1, but remote product access cannot pass its gate until Phase 3 policy and replay controls exist. Phase 6 depends on Phases 1–4 because backups must preserve person/shared-space isolation. Product workflows in Phase 7 may be prototyped earlier but cannot be considered product-ready before the relevant trust gates.

## Cross-phase execution rules

- Preserve working behavior with compatibility adapters and versioned migrations.
- Prefer small, reviewable changes with negative security tests before broad refactors.
- Treat security and accessibility as acceptance dimensions, not later hardening.
- Use synthetic household fixtures only; no real personal data in tests.
- Every external disclosure records recipient, purpose, minimized fields, and decision.
- Every destructive migration has backup, rollback, and recovery instructions.
- Public documentation changes in the same phase as behavior/status changes.
- Stop for review when a change affects the product promise, data ownership, household isolation, or recovery authority.

## Phase 0: Repository truth and architecture reconciliation

### Objective and rationale

Establish one truthful repository map, plan, threat model, architecture decision register, baseline test matrix, reproducible developer entrypoint, and accurate public status foundation. This prevents implementation from extending contradictory service, schema, installer, and maturity assumptions.

### Prerequisites

- Synchronized local repositories.
- Human review of proposed AD-007, AD-016, AD-017, and AD-020.
- Decision on whether singular `unison-capability` or plural `unison-capabilities` is canonical.

### Architecture and schema changes

- Record proposed process consolidation without moving runtime code yet.
- Select the canonical schema source and add drift checks.
- Define versioning rules for contracts and database migrations.
- Mark aggregate root schemas and `unison-spec` non-authoritative.

### Implementation tasks

- Complete and approve this planning set.
- Correct the invalid `unison-context` submodule pin.
- Inventory service ports, dependencies, data stores, credentials, health, and ownership in a machine-readable component manifest.
- Create one WSL/Linux bootstrap command that installs locked dev dependencies for the selected profile.
- Create a thin PowerShell wrapper that checks WSL2/Docker and delegates to the same bootstrap/test commands.
- Replace or clearly deprecate the devstack's standalone generated installers.
- Remove tracked cache/build artifacts and add hygiene checks.
- Standardize `test-unit`, `test-boundaries`, `test-integration`, and `test-e2e` entrypoints.
- Wire core unit/schema/security checks into GitHub Actions; do not call a local shell sequence “CI” unless it actually runs in CI.
- Add sample two-person household fixtures with canary private/shared records.
- Create the website status vocabulary and canonical terminology draft.
- Inventory website pages into preserve/rewrite/obsolete/redirect/missing/claim-review categories.
- Establish dark design tokens, semantic page shell, and real-browser accessibility CI as an early website foundation; full content migration continues per phase.

### Tests and runnable evidence

- Clean bootstrap on a fresh WSL2 Ubuntu environment and a Linux CI runner.
- Every core repo test suite collects from the authoritative bootstrap.
- Compose config validation for devstack, native, local-source, and optional profiles.
- Schema drift/generation checks.
- Installer shell syntax and PowerShell static analysis.
- MkDocs strict build, link check, current-URL audit, Playwright/axe real-browser audit, keyboard smoke, reduced-motion and forced-colors checks.

### Threat-model and accessibility work

- Turn the threat register into test identifiers and owners.
- Pin/verify CI actions, release tools, dependencies, and image sources.
- Require text plus stable machine-readable results from scripts; color is never the only signal.
- Document nonvisual ways to complete every developer validation.

### Documentation and developer experience

- This planning set becomes authoritative.
- Root README links here and labels older plans historical.
- Document Windows host versus WSL responsibilities and safe secrets handling.
- Public site gains “Implemented / Experimental / Planned / Vision” labels and canonical terminology.

### Migration, rollback, and risks

- Do not delete historical docs or installers until redirects and replacement commands exist.
- Bootstrap changes remain reversible by retaining repo-local requirements during transition.
- Website design changes ship behind build/a11y checks and can revert independently.

### Acceptance gate and evidence

Phase 0 passes when a fresh contributor can clone, bootstrap, run the defined unit/schema checks, validate Compose, and build/audit the site using documented commands; all active repos have an owner/disposition; no broken submodule pin remains; human decisions are recorded; and public status no longer conflates vision with implementation.

Required evidence: command logs, CI links, component manifest, schema drift report, website inventory, real-browser accessibility report, decision approvals, updated status/current-state/threat/changelog/site.

## Phase 1: Multi-principal identity and trusted request binding

### Objective and rationale

Make identity and data authority cryptographically meaningful before adding shared memory or remote channels. This phase removes the current ability to influence authority using a request path/body identifier.

### Prerequisites

- Phase 0 gate.
- Approved device/person/assistant/household administrator semantics.
- Approved key/recovery design at least for local development and migration.

### Architecture and schema changes

- Add `Person`, `AssistantInstance`, `Household`, device/workload principal, `ChannelIdentity` shell, and membership/role identifiers.
- Define signed `PrincipalContext` and canonical trusted request envelope.
- Add per-person credential, key, namespace, cache, and index identifiers.
- Replace username-as-person assumptions; distinguish display name, login handle, stable person ID, and principal ID.

### Implementation tasks

- Replace JSON user persistence with transactional, migration-managed identity storage.
- Implement first-person enrollment and additional-member invitation/pairing.
- Bind JWT/passkey/session/workload claims to assistant/household membership server-side.
- Add workload audience/delegation and remove reusable broad service secrets from product profiles.
- Refactor orchestrator, context, storage, renderer, comms, capability, replay, and action paths to consume derived principal context.
- Reject mismatched `person_id`, `user_id`, assistant, household, and channel hints.
- Implement per-person key handles, credential broker interfaces, namespace enforcement, cache/index partitioning, and lock/revocation.
- Remove `local-user`/`local-person` defaults from production code paths.
- Make auth/consent dependency failure safe for sensitive actions.
- Provide migration of the existing first admin/profile into the first `Person` and `AssistantInstance` with explicit confirmation.

### Tests

- Forged identifier matrix across every externally reachable endpoint.
- Cross-person read/write/search/cache/replay/object/vault/audit denial tests.
- Workload confused-deputy and audience tests.
- Session/device/channel revocation and dependency-outage tests.
- Migration round trip, rollback, duplicate enrollment, interrupted migration, and recovery tests.
- Key/credential canaries absent from logs, prompts, errors, and other principals.

### Threat-model and accessibility work

- Update T-01, T-02, T-03, T-07, T-08, T-15, T-22, T-24, and T-29.
- Enrollment, authentication, lockout, revocation, error, and recovery flows work by keyboard and screen reader and expose semantic status/cancellation.
- Do not use voice alone for sensitive enrollment or recovery.

### Documentation, DX, and migration

- Publish principal/assistant/household terminology and diagrams with text alternatives.
- Add synthetic two-person fixtures and one-command boundary tests.
- Version APIs and database migrations; retain compatibility adapters only where they cannot weaken binding.
- Document downgrade limitations and encrypted pre-migration backup.

### Acceptance gate and evidence

Phase 1 passes when no protected operation derives authority from caller-controlled identity, every person has isolated keys/credentials/namespaces/indexes, cross-principal tests pass, first-user migration and rollback are demonstrated, and enrollment/revocation are accessibly completable.

Required evidence: schema/migration versions, endpoint coverage inventory, negative test report, key/log scan, enrollment accessibility report, updated architecture/threat/status/current-state/changelog/site.

## Phase 2: Context spaces, relationships, governed memory, and personal charter

### Objective and rationale

Create the domain model that lets an assistant understand overlapping relationships while preserving explicit boundaries and user control.

### Prerequisites

- Phase 1 gate.
- Approved relationship semantics, shared-space membership rules, and personal-charter ownership.

### Architecture and schema changes

- Add `Relationship`, `ContextSpace`, `Membership`, `MemoryRecord`, `Goal`, `Commitment`, and `PersonalCharter`.
- Add provenance, sensitivity, purpose, audience, confidence, retention, inference/action/disclosure/backup/sync flags, version and deletion state.
- Distinguish asserted facts, imported data, inferred hypotheses, user corrections, summaries, and derived indexes.
- Define private, shared, system/operational, and ephemeral spaces.

### Implementation tasks

- Consolidate `unison-context` and useful `context-graph` behavior behind a governed repository/query API.
- Implement private-space creation for every assistant and explicit shared-space creation/invitation.
- Implement relationship edges that inform decisions but do not grant access.
- Partition retrieval, embeddings/indexes, summaries, caches, and model prompts by authorized spaces.
- Implement memory admission, correction, deletion, retention, provenance, confidence, and “do not remember” controls.
- Implement charter/goals/commitments with user-visible origins and change history.
- Add shared calendar and grocery-list data models as the first governed shared artifacts, without completing the full household demo yet.
- Provide inspectable views: what is known, why, where stored, who can access, and how to correct/delete/share.

### Tests

- Private record never appears in shared retrieval, search, summarization, embedding, cache, or inference output.
- Same contact in multiple relationships does not collapse contexts.
- Ambiguous context prompts rather than guesses across a boundary.
- Explicit share creates auditable shared data without reclassifying the private source.
- Member removal/key rotation and retention/deletion/export coverage.
- Provenance and correction survive restart/migration.

### Threat-model and accessibility work

- Update T-02, T-16, T-18, T-19, T-25, T-27, and T-30.
- Context/privacy state is present in the semantic response.
- Space creation, membership, correction, deletion, goal/commitment review, and share preview are operable without drag, color, vision, speech, or precise pointer input.

### Documentation, DX, and migration

- Publish schemas, privacy examples, and non-oracular denial rules.
- Migrate existing profiles/conversations/dashboard records into the owner's private space; never infer shared promotion.
- Create fixture builders for overlapping relationships and canary secrets.

### Acceptance gate and evidence

Phase 2 passes when two synthetic people have isolated private spaces, can explicitly share selected records, manage relationships/charters/goals/commitments, and pass retrieval/inference/deletion/export/accessibility tests across restarts.

Required evidence: schema/migrations, isolation and inference report, retention/deletion reconciliation, accessible UX evidence, updated docs/status/threat/changelog/site.

## Phase 3: Default-deny policy, consent, disclosure, and capability governance

### Objective and rationale

Ensure actions and external disclosures are authorized, minimized, understandable, reversible where possible, and denied when authority is incomplete.

### Prerequisites

- Phase 2 gate.
- Approved policy vocabulary, channel assurance levels, delegation/standing-permission rules, and confirmation semantics.

### Architecture and schema changes

- Unify action policy, consent grants, disclosure decisions, redaction/minimization, delegated authority, and confirmation state.
- Extend capability manifests with actions, data read/write, recipients, execution location, risk, reversibility, cost, confirmation, accessibility, audit, and retention behavior.
- Add versioned `DisclosureDecision` and `CapabilityGrant` records.

### Implementation tasks

- Consolidate overlapping policy and consent grant implementations behind one Trust API/evaluator.
- Deny unknown scopes, purposes, audiences, data classes, principals, spaces, and assurance levels.
- Implement allow/deny/redact/minimize/ask/step-up outcomes.
- Add local-alternative and minimum-context checks before remote model/capability calls.
- Build a credential broker that injects task-scoped secrets without revealing them to planners/models.
- Harden Capability Host sandbox, egress allowlist, filesystem/device permissions, time/resource limits, package signatures, and revocation.
- Treat email/web/document/tool/model content as untrusted data with provenance and taint boundaries.
- Make audit explanations owner-readable and safe from protected-existence leaks.
- Preserve draft-first outbound messages and explicit high-risk confirmation.

### Tests

- Unknown-policy property tests deny.
- Recipient/purpose/sensitivity/relationship/channel matrices.
- Prompt-injection corpora for email, web, documents, tools, and model output.
- Capability manifest overreach, egress, filesystem, secret, timeout, replay, and revocation tests.
- Confirmation replay, expiry, cancellation, step-up, undo/compensation, and dependency-outage tests.
- External disclosure canaries and minimization measurements.

### Threat-model and accessibility work

- Update T-08 through T-12, T-15 through T-17, T-22 through T-29.
- Every decision exposes action, recipient, affected data, consequence, reversibility, cost, and options semantically.
- Confirmation and denial parity across text, speech, keyboard, screen reader, reduced-motion, and simplified-language modes.

### Documentation, DX, and migration

- Publish policy/disclosure/capability schemas and safe examples.
- Migrate existing scopes/rules to explicit versions; unknown legacy grants remain disabled until reviewed.
- Provide a policy simulator and explain command using synthetic data.

### Acceptance gate and evidence

Phase 3 passes when unknown authority fails closed, disclosure minimization is enforced, capabilities cannot exceed manifests, adversarial content cannot gain authority, sensitive actions require valid confirmation/step-up, and decisions are accessibly understandable.

Required evidence: policy matrix, adversarial test report, sandbox report, disclosure metrics, accessible decision audit, migration/rollback record, updated plan set/site.

## Phase 4: Two-assistant household proof

### Objective and rationale

Demonstrate the core product boundary before adding more channels or skills: two independently governed assistants on one appliance with useful explicit coordination and no private leakage.

### Prerequisites

- Phase 3 gate.
- Approved household-administrator and dependent/caregiving scope for this proof.

### Architecture and schema changes

- Finalize household membership/admin schemas for adult independent principals.
- Finalize shared calendar and grocery-list artifact/event contracts.
- Add coordination requests that reveal only necessary shared facts.

### Implementation tasks

- Enroll two people and two assistant instances on one representative appliance.
- Give each private messages, credentials, goals, charter, memory, indexes, audit, and backup boundary.
- Create one household space with shared calendar and grocery list.
- Implement accessible membership/invitation/removal and share-preview flows.
- Coordinate calendar/grocery outcomes through the shared space without private-memory reads.
- Add quotas/resource scheduling so one assistant cannot starve another.

### Tests

- Cross-person API, storage, search, cache, embedding, prompt, model, trace, log, audit, credential, backup, and error-oracle tests.
- Canary inference tests asking each assistant to reveal/guess the other's private facts.
- Concurrent workloads, quota exhaustion, restart, member removal, shared-key rotation, rollback, and recovery.
- Denials/redactions/confirmations remain understandable without revealing private record existence.

### Threat-model and accessibility work

- Close applicable T-01, T-02, T-18, T-19, T-25, T-28, and T-29 for the proof profile.
- Both people can administer their assistant and shared artifacts independently through accessible flows.

### Documentation, DX, and migration

- Publish a reproducible synthetic household demo/runbook and architecture diagram with text equivalent.
- Label the proof as bounded; do not claim child/caregiving/emergency models unless tested.

### Acceptance gate and evidence

Phase 4 passes only when the target household demonstration works on a representative appliance and all positive coordination and negative isolation tests pass, including accessible audit/denial/recovery experiences.

Required evidence: recorded configuration and commands, test artifacts, canary report, performance/resource profile, accessibility report, known limitations, updated plan set/site.

## Phase 5: General Channel Gateway and secure remote text access

### Objective and rationale

Let each person reach the same authoritative assistant away from home through one secure remote text transport without exposing the appliance or weakening principal boundaries.

### Prerequisites

- Phases 1–3 gates; Phase 4 is preferred before product release.
- Human selection of the first provider after current API/privacy/operational review.
- Approved relay ownership, metadata, availability, and cost model.

### Architecture and schema changes

- Add normalized channel envelope, channel capability/assurance profile, binding/pairing, provider privacy metadata, delivery state, idempotency, nonce, replay window, and step-up state.
- Make connector credentials per person and provider account.

### Implementation tasks

- Refactor `unison-comms` into Channel Gateway modules; preserve Gmail behind an adapter.
- Implement one remote text adapter and an outbound-only appliance relay/provider connection.
- Pair external identity to a principal using a stronger local/authenticated ceremony.
- Implement revocation, reassignment defense, replay protection, rate limits, abuse controls, delivery/audit, and degraded/offline behavior.
- Adapt semantic outcomes to channel capabilities while preserving privacy/confirmation state.
- Keep outbound communication draft-first except narrowly approved standing policies.

### Tests

- Pairing, wrong-person binding, stolen token, provider replay, duplicate/out-of-order event, delayed message, account reassignment, revocation, relay compromise, outage/reconnect, and rate-limit tests.
- Low-assurance channel cannot perform sensitive action or recovery.
- Per-person channel credentials and threads remain isolated.
- Appliance has no default public listener.

### Threat-model and accessibility work

- Update T-04, T-05, T-06, T-13, T-17, T-23, and T-28.
- Remote text flow supports accessible clients, concise/simplified output, explicit confirmation/cancel/recovery, and does not require visual local administration.

### Documentation, DX, and migration

- Publish provider data-flow/privacy/metadata disclosures and pairing/revocation runbooks.
- Adapter conformance kit uses a fake provider and requires no real credentials.
- Migrate Gmail credentials to per-person broker storage with disconnect/reset verification.

### Acceptance gate and evidence

Phase 5 passes when each demo person can independently reach their assistant through the chosen channel, sensitive actions step up, replay/reassignment/revocation tests pass, provider/appliance exposure is documented, and no direct inbound appliance exposure is enabled.

Required evidence: data-flow diagram, provider review, channel conformance/replay report, network scan, accessible flow evidence, updated plan set/site.

## Phase 6: Provider-blind backup and replacement-device restore

### Objective and rationale

Make loss, replacement, and provider failure survivable without giving a provider or household administrator access to private data.

### Prerequisites

- Phase 4 gate and stable key/data models.
- Approved key recovery, shared-space rotation, retention, deletion, and provider backend interface.

### Architecture and schema changes

- Add encrypted object/chunk, signed versioned manifest, snapshot lineage, person/space key references, tombstones, restore plan, backend capability, and verification records.
- Keep backup, synchronization, and remote access APIs separate.

### Implementation tasks

- Implement client-side envelope encryption and signed incremental manifests.
- Add provider-neutral filesystem/object backend plus one evaluated remote backend.
- Back up each person and shared space independently with minimal metadata.
- Implement scheduled verification, corruption detection, retention, deletion, export, and restore dry run.
- Implement replacement-device enrollment/recovery and post-restore key rotation/revocation.
- Preserve audit/provenance and demonstrate provider migration.
- Keep home node authoritative; defer multi-writer synchronization.

### Tests

- Provider reads ciphertext only; wrong person/admin/provider cannot decrypt.
- Manifest tampering, rollback, truncation, reordering, missing chunks, corruption, and replay are detected.
- Interrupted backup/restore resumes safely.
- Independent person deletion/export and shared-member removal semantics.
- Restore on clean representative hardware and verify household isolation/golden paths.

### Threat-model and accessibility work

- Close bounded controls for T-07, T-13, T-17, T-20, T-21, and T-30.
- Backup status, failure, recovery key handling, restore selection, cancellation, and recovery are accessible and never depend on color or visual QR alone.

### Documentation, DX, and migration

- Publish cryptographic format/version, backend contract, residual metadata, recovery ceremony, provider migration, and disaster runbooks.
- Add a deterministic fake backend and corruption harness.

### Acceptance gate and evidence

Phase 6 passes after repeated automated backup verification and a clean replacement-device restore preserve both private isolation and shared-space access while the backend/provider remains unable to decrypt or forge accepted state.

Required evidence: cryptographic review, threat test report, restore logs, provider portability test, accessibility report, updated plan set/site.

## Phase 7: High-value personal and executive-assistant workflows

### Objective and rationale

Deliver measurable time-returning competence on the trusted foundation rather than broad ungoverned autonomy.

### Prerequisites

- Phases 3–6 gates for product-connected workflows.
- Approved success metrics and no-engagement product analytics policy.

### Architecture and schema changes

- Add task plans, reminders, follow-ups, commitments, approvals, outcome evidence, failure/recovery, and time-return estimates.
- Extend provider/capability profiles as needed without weakening prior boundaries.

### Implementation tasks

- Scheduling/calendar coordination.
- Email triage, summarization, draft/reply with relationship/disclosure awareness.
- Reminders, task tracking, follow-up and commitment review.
- Household coordination using shared spaces.
- Relationship-aware contact memory.
- Document retrieval/summarization, website research, and travel planning.
- Inspectable planning, cancellation, retry, compensation, and recovery.
- Outcome metrics: administrative tasks completed, commitments completed, interruptions avoided, corrections, recoveries, minimized external calls, and estimated time returned.

### Tests

- Golden journeys using fake providers plus bounded live-provider acceptance.
- Adversarial email/web/document inputs and wrong-context recipients.
- Partial failure, timeout, duplicate action, cancellation, rollback/compensation, and provider replacement.
- No engagement/sponsored/provider-lock-in signals affect ranking.
- Private/shared and model-disclosure boundary regression suite.

### Threat-model and accessibility work

- Reassess every external recipient/capability against the threat register.
- Every workflow's primary, confirmation, error, cancellation, and recovery path has semantic and modality-equivalent tests.

### Documentation, DX, and migration

- Publish exactly supported workflows, permissions, providers, limitations, and evidence.
- Provide fake-provider fixtures and record/replay contracts without personal data.

### Acceptance gate and evidence

Phase 7 passes when a bounded workflow set reliably returns measurable time, respects charter/commitments/context/disclosure, recovers from failures, and completes accessibly with zero boundary incidents in acceptance runs.

Required evidence: journey reports, outcome metrics, provider/disclosure audit, recovery and accessibility results, updated plan set/site.

## Phase 8: Expanded multimodal surface and governed ecosystem

### Objective and rationale

Expand accessibility, channels, models, and capabilities after the trust and competence core is proven.

### Prerequisites

- Phase 7 gate.
- Per-modality/provider/capability threat and maintenance review.

### Architecture and schema changes

- Mature semantic response and modality capability negotiation.
- Versioned capability packaging/certification and model policy profiles.
- Additional channel adapters conform to the Phase 5 contract.

### Implementation tasks

- Improve local voice, barge-in, captions, and non-voice parity.
- Build the adaptive visual surface and accessible household/privacy/admin controls.
- Mature Braille, sign, keyboard, switch/AAC, haptic, high-contrast, reduced-motion, and simplified-language support according to real-user priorities.
- Add selected channels, local/remote models, MCP/capability packages, and governed delegated agents.
- Add ecosystem signing, review, permission diff, update/revocation, compatibility, and incident response.
- Keep BCI, robotics, spatial, and autonomous financial actions deferred until separately approved.

### Tests

- Semantic equivalence and accessible completion across supported modalities.
- Hardware/provider matrix, graceful fallback, resource contention, and offline behavior.
- Capability supply-chain, permission upgrade, revocation, sandbox and data-minimization tests.
- Model replacement and privacy/cost/risk routing tests.

### Threat-model and accessibility work

- Accessibility research includes disabled users and does not use simulation as sole evidence.
- Each new adapter documents assurance, privacy, metadata, errors, cancellation, and fallback.

### Documentation, DX, and migration

- Publish supported hardware/provider matrices and explicit experimental labels.
- Provide adapter SDK/conformance suites and accessible reference implementations.

### Acceptance gate and evidence

Each ecosystem expansion ships independently only after its contract, security, privacy, recovery, accessibility, and maintenance evidence passes. Phase 8 is a continuing program, not a blanket “all modalities implemented” milestone.

## GitHub Pages program

The public site is overhauled across phases, beginning in Phase 0. Proposed information architecture:

- Home
- Vision
- Product Promise
- How Unison Works
- Personal Node
- Household and Context Spaces
- Privacy and Security
- Accessibility
- Architecture
- Capabilities and Channels
- Installation
- Current Status
- Roadmap
- Developer Documentation
- Contributing
- Terminology

Content inventory must classify every current page as preserve, rewrite, merge, obsolete/redirect, missing, or requiring implementation-status review. Public pages use semantic HTML, CSS design tokens, minimal JavaScript, skip links, correct headings, keyboard navigation, visible focus, strong contrast, reduced-motion/forced-colors support, responsive layout, accessible diagrams with text equivalents, and no color-only status.

Visual direction is calm, dark, restrained, technical, precise, and trustworthy. The reference site may inform tone and spacing but is not copied. Avoid oversized/heavily bold hero typography. Tokens cover backgrounds, surfaces, text hierarchy, accents, focus, borders, spacing, typography, status, code, and diagrams.

Canonical terminology must define Unison, UnisonOS, operating surface, personal-intelligence runtime, personal node, assistant, assistant instance, household, context space, memory, context, profile, relationship, capability, skill, tool, connector, channel, model, and semantic response.

## Product success measures

No engagement metric is used as a success objective. Phase 7 establishes baselines and targets for:

- estimated and user-confirmed time returned;
- commitments and administrative tasks reliably completed;
- interruptions avoided;
- corrections and unnecessary confirmations declining without weakening safety;
- successful cancellation and recovery;
- accessible flow completion;
- external calls using minimized context;
- backup/restore verification success;
- disclosure and cross-principal incidents remaining zero.

Metrics must be locally inspectable, optional where possible, privacy-minimized, and never become a third-party behavioral-data product.

## Human-review decisions before Phase 1

1. Approve or revise the proposed six-boundary appliance topology.
2. Decide canonical contract/schema ownership.
3. Approve WSL/Linux authority with thin PowerShell wrappers.
4. Define household administrator power versus adult-member privacy.
5. Define dependent/child/caregiving scope for the first product.
6. Select hardware-backed key targets and user-controlled recovery principles.
7. Confirm Ubuntu 24.04 x86_64 remains the first supported appliance target.
8. Decide the canonical capability repository name.
9. Confirm the public naming relationship between Unison and UnisonOS.
10. Approve the no-advertising/no-engagement/no-personal-data-commercialization business constraint.

## Phase-close maintenance checklist

After every phase:

1. Run every acceptance and negative-boundary check.
2. Record commands, versions, results, unresolved issues, and residual risks.
3. Update `UNISON_PHASE_STATUS.md` and `UNISON_CURRENT_STATE.md`.
4. Record new/superseded decisions.
5. Update this threat model and later phases.
6. Update `CHANGELOG.md`.
7. Update GitHub Pages content and maturity labels.
8. Validate migration, rollback, recovery, and accessible completion.
9. Do not mark complete while a required criterion lacks evidence.
