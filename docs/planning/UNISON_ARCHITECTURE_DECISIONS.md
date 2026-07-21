# Unison Architecture Decisions

Status: authoritative decision register  
Last updated: 2026-07-20

## How to use this register

This file records decisions that shape the product promise, security boundaries, data ownership, household isolation, recovery model, runtime topology, and developer experience.

Decision states:

- **Accepted**: mandated by the approved product vision or confirmed implementation constraint.
- **Proposed**: recommended by the audit but requires human review before implementation.
- **Deferred**: intentionally postponed until prerequisites are met.
- **Superseded**: replaced by a later numbered decision.

Changing an accepted decision affecting the product promise, principal isolation, private-data ownership, external disclosure, or recovery requires explicit human review and a recorded replacement decision.

## Decision summary

| ID | Decision | State |
| --- | --- | --- |
| AD-001 | Product form is a household-hosted private assistant appliance | Accepted |
| AD-002 | Each assistant serves one primary human principal | Accepted |
| AD-003 | Sharing occurs only through explicit context spaces | Accepted |
| AD-004 | The home node is the primary authority | Accepted |
| AD-005 | Models and providers are replaceable capabilities | Accepted |
| AD-006 | Logical modules do not imply separate appliance processes | Accepted |
| AD-007 | Consolidate the default runtime into six principal boundaries plus optional adapters | Accepted |
| AD-008 | Principal binding replaces caller-controlled person identity | Accepted |
| AD-009 | Personal and shared data use independent key domains | Accepted |
| AD-010 | Policy is default deny for unknown authority or disclosure dimensions | Accepted |
| AD-011 | The semantic response model is the accessibility source | Accepted |
| AD-012 | Communications become a normalized Channel Gateway | Accepted |
| AD-013 | Remote access is outbound-first and does not expose the appliance by default | Accepted |
| AD-014 | Backup, sync, and remote access are separate subsystems | Accepted |
| AD-015 | Backup is provider-blind and user-key controlled | Accepted |
| AD-016 | Canonical contracts live in one versioned specification source | Accepted |
| AD-017 | WSL2/Linux owns implementation commands; PowerShell is a thin host wrapper | Accepted |
| AD-018 | Public documentation labels maturity and never presents plans as implementation | Accepted |
| AD-019 | No engagement or third-party commercial objective enters product ranking | Accepted |
| AD-020 | Household administrators are not omniscient data administrators | Accepted |
| AD-021 | People own independent key hierarchies and provider-blind recovery | Accepted |
| AD-022 | Ubuntu 24.04 x86_64 is the initial appliance target | Accepted |
| AD-023 | Capability Host naming is canonicalized | Accepted |
| AD-024 | Unison and UnisonOS have distinct product meanings | Accepted |
| AD-025 | Revenue and partnerships cannot distort person-aligned behavior | Accepted |

## AD-001: Household-hosted private assistant appliance

State: **Accepted**

UnisonOS's first practical product form is a downloadable appliance runtime installed on a capable trusted edge device, typically in a home. The operating-surface vision remains the generated experience layer; UnisonOS does not need to replace the host operating system, smartphone, or applications.

Consequences:

- Ubuntu 24.04 x86_64 remains the initial supported installation target until revised.
- Installation, updates, recovery, export, and replacement-device restore are product capabilities.
- Resource consumption and operational complexity must fit a personal appliance.

## AD-002: One primary human principal per assistant

State: **Accepted**

Each `AssistantInstance` acts for one primary `Person`. A single appliance can host multiple assistant instances, but it cannot treat household membership as authorization to read another person's private domain.

Consequences:

- Assistant authority, keys, credentials, memory, goals, charter, audit views, backup, export, and deletion are independently governed.
- Cross-person actions require an explicit shared space, delegation, or disclosure decision.

## AD-003: Explicit context spaces are the only sharing mechanism

State: **Accepted**

Private records never become shared because of device co-location, family membership, an inferred relationship, or an administrator role. Sharing creates or references a record in an explicit `ContextSpace` with membership and purpose controls.

Consequences:

- No implicit private-to-household promotion.
- Relationships inform policy but do not grant access by themselves.
- Cross-space retrieval and inference require negative boundary tests.

## AD-004: Local authority

State: **Accepted**

The trusted node is authoritative for identity, assistant identity, context, relationships, memory, charter, policy, credentials, audit, capability grants, and keys. External services may provide transport, models, storage, or execution but cannot become authoritative for the person.

Consequences:

- External results require provenance and memory-admission decisions.
- Provider outages or replacement must not erase assistant continuity.

## AD-005: Model independence

State: **Accepted**

Models are reasoning resources selected by capability, privacy, latency, cost, accessibility, terms, local availability, risk, and user preference. Identity and continuity are not embedded solely in a model prompt or provider account.

## AD-006: Logical and deployment boundaries differ

State: **Accepted**

The architecture retains explicit modules for identity, orchestration, memory, policy, consent, channels, capabilities, models, and rendering. The personal-appliance profile does not require a network service or container for every module.

Consequences:

- Module APIs can be typed in-process interfaces.
- Separate processes are reserved for privilege, compromise containment, resource control, hardware drivers, independent lifecycle, or optional scale.

## AD-007: Proposed appliance process topology

State: **Accepted — approved 2026-07-20**

The default appliance will converge toward these principal process/security boundaries:

1. **Unison Core**: trusted request intake after authentication, intent normalization, orchestration, planning, context/relationship queries, task/commitment logic, model routing, semantic outcomes.
2. **Personal Data and Trust Store**: identity, principal binding, key brokering, credentials, governed storage, policy/consent/disclosure decisions, append-only audit.
3. **Capability Host**: sandboxed tools, connectors, browser/VDI/actuation workers, MCP and remote APIs.
4. **Channel Gateway**: channel adapters, identity binding, replay protection, assurance, normalized inbound/outbound envelopes.
5. **Inference Broker/Runtime**: local model resources and minimized remote-provider calls.
6. **Unison Surface**: accessible local web/visual/voice experience and administration.

Privileged lifecycle/update code remains separately constrained. Speech, vision, Braille, sign, BCI, and device drivers may be optional adapter processes. PostgreSQL, Redis, NATS, Neo4j, and tracing infrastructure are implementation choices, not mandatory product boundaries.

Migration must be incremental. Existing APIs remain behind compatibility adapters until replacement tests pass.

## AD-008: Trusted principal binding

State: **Accepted**

Requests may contain person or space hints, but authority is derived from cryptographically verified principal claims and server-side membership. A caller-supplied `person_id`, `user_id`, household, assistant, audience, or channel identity is never sufficient authorization.

Required claims or derived context include requesting principal, assistant instance, household, channel identity/assurance, active space, purpose, audience, data classes, requested capability, risk, confirmation, and trace ID.

## AD-009: Independent key domains

State: **Accepted**

Each person receives an independent master-key hierarchy. Shared spaces use distinct shared keys. Service-global encryption keys are migration-only and cannot satisfy the household isolation promise.

Key decisions still requiring design review:

- hardware-backed root options and supported fallback;
- recovery mechanism and whether social recovery is supported;
- rotation and member-removal semantics for shared spaces;
- metadata visible to household administrators.

## AD-010: Default-deny policy and disclosure

State: **Accepted**

Unknown scopes, purposes, audiences, data classes, principals, spaces, or channel assurance levels deny by default. The engine can return allow, deny, redact, minimize, require confirmation, or require stronger authentication. Denials must be understandable without revealing protected facts.

## AD-011: Semantic response as accessibility source

State: **Accepted**

Every outcome is first represented semantically with meaning, urgency, status, actions, confirmation, privacy state, provenance, errors, cancellation, and recovery. Text, speech, visual, haptic, Braille, sign, simplified language, keyboard, switch, and future renderers consume the same meaning.

A capability is incomplete when its confirmation, error, cancellation, or recovery path is unavailable through the selected modality.

## AD-012: Normalized Channel Gateway

State: **Accepted**

Email, SMS, telephone, Telegram, WhatsApp, local web/voice, mobile, AAC, and future adapters are transports to one assistant. They normalize to one message contract containing provider, channel, bound principal, participants, thread, assurance, content, attachments, capabilities, privacy characteristics, idempotency, and replay protection.

Outbound communication remains draft-first unless a narrow standing policy explicitly permits sending.

## AD-013: Outbound-first remote access

State: **Accepted**

The appliance establishes outbound connections to an optional relay or provider. Direct public inbound exposure is disabled by default. Low-assurance channels cannot authorize sensitive actions without step-up authentication.

## AD-014: Separate backup, sync, and remote access

State: **Accepted**

- Backup protects against loss.
- Synchronization replicates explicitly approved state across trusted devices.
- Remote access transports interaction to the authoritative home node.

The initial home node remains the authoritative writer. Multi-writer sync is deferred until backup and recovery are proven.

## AD-015: Provider-blind backup

State: **Accepted**

Encryption occurs locally with user-controlled keys. Providers receive ciphertext and minimal metadata, never decryption keys. Backends are replaceable. Manifests are signed/versioned; restore, export, and deletion are independently testable per person and shared space.

## AD-016: Canonical contract source

State: **Accepted — approved 2026-07-20**

Canonical versioned machine-readable schemas live in `unison-common/schemas`, with generated language bindings and drift-checked explanatory references in `unison-docs`. `unison-spec` remains archived. Root aggregate schemas and manually copied duplicates are non-authoritative.

## AD-017: Windows/WSL responsibility split

State: **Accepted — approved 2026-07-20**

- WSL2/Linux scripts are authoritative for bootstrap, test, build, Compose, install packaging, and validation.
- PowerShell provides a thin discoverable wrapper that validates WSL/Docker integration and delegates to the same commands.
- No separate generated topology or Windows-only implementation path is maintained.

## AD-018: Truthful public maturity labels

State: **Accepted**

Public pages distinguish implemented, experimental, planned, and long-term vision. Claims require links to evidence or current-state records. Pages do not promise that data always remains local when configured remote models, channels, or providers can receive minimized disclosures.

## AD-019: Person-aligned economic design

State: **Accepted**

Ranking, recommendations, actions, and notifications cannot optimize advertising, sponsored placement, engagement, attention capture, third-party data acquisition, or provider lock-in. Product measures focus on time returned, commitments completed, administrative outcomes, recoverability, accessibility, and zero privacy-boundary incidents.

Business-model terms, partnership agreements, telemetry, and provider integrations must be reviewed against this decision.

## AD-020: Household administrator power

State: **Accepted — approved 2026-07-20**

A household/device administrator may manage hardware health, membership invitations, updates, resource limits, encrypted backup health, and assistant lifecycle. Administration does not grant access to adult members' private data or keys. Administrators may see minimized operational metadata, but not private titles, contacts, messages, prompts, or activity details. They may suspend or remove an assistant from hardware they control without gaining its keys.

The initial household product supports independently consenting adults. Child, dependent, caregiving, incapacity, and emergency-access models are deferred to a dedicated review. Schemas may reserve extension points but must not simulate these roles through administrator access.

## AD-021: Key ownership and recovery principles

State: **Accepted — approved 2026-07-20**

Each person owns an independent on-device master-key hierarchy, hardware-backed where practical, with a documented secure software fallback for development/evaluation hardware. Shared spaces use distinct keys. Providers never receive decryption keys. Recovery is user-controlled through encrypted recovery material or separately enrolled trusted devices; provider-operated recovery cannot bypass encryption. Exact algorithms, TPM integration, rotation, and recovery ceremonies require focused security review before implementation.

## AD-022: Initial supported appliance target

State: **Accepted — approved 2026-07-20**

Ubuntu 24.04 LTS on x86_64 is the first supported appliance target. WSL2 and Linux VM installations are development/evaluation channels. ARM64 is planned only after the x86_64 appliance profile, model compatibility, update path, and replacement restore are validated.

## AD-023: Capability naming

State: **Accepted — approved 2026-07-20**

“Capability Host” is the architectural component name. `unison-capability` is the canonical repository name and `unison-capability-host` is the runtime service identifier. Existing plural repository references will be migrated or redirected without breaking active checkouts.

## AD-024: Unison and UnisonOS terminology

State: **Accepted — approved 2026-07-20**

“Unison” names the private assistant platform and user-facing assistant. A “Unison assistant” is one independently governed assistant instance. “UnisonOS” names the downloadable appliance runtime, distribution, and operating surface. It is not positioned as a replacement for a smartphone or general-purpose operating system.

## AD-025: Person-aligned economic constraint

State: **Accepted — approved 2026-07-20**

Unison does not use advertising, sponsored placement, engagement optimization, or the sale, licensing, or commercialization of personal context. Revenue must come from products and services purchased for the person's benefit. Partnerships and affiliate relationships may not influence recommendations, routing, or capability selection without explicit disclosure and user control.

## Deferred decisions

- Multi-writer synchronization and conflict-free replicated data types.
- Federation between independent household appliances.
- Autonomous spending or financial execution.
- Robotics and generalized physical actuation.
- BCI data retention and raw-signal governance.
- Marketplace economics and third-party capability certification.
- Cloud-hosted Unison authority; this is incompatible with the current local-authority decision unless explicitly reconsidered.
