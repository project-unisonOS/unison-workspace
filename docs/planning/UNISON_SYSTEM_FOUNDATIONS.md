# Unison system foundations

Status: **Discovery draft; reconciles accepted foundations with proposed extensions**  
Opened: 2026-08-14  
Parent program: [UNISON_INTEGRATED_SYSTEM_PROGRAM.md](UNISON_INTEGRATED_SYSTEM_PROGRAM.md)

## Purpose

This document records the foundational product promises developed during the
integrated system reasoning sessions. It distinguishes accepted architecture,
implemented evidence, and proposed extensions. It does not upgrade a software
or simulation result into a hardware, security, privacy, accessibility, or
supported-product claim.

## Foundational promise

Unison is a locally authoritative, continuously useful intelligence system for
individuals and households. It keeps evolving personal context and memory under
the control of the person it serves; combines deterministic algorithms, tools,
and governed workflows with replaceable non-deterministic models; and can
understand and express intent through the forms of interaction appropriate to
each person.

Trust is not one appliance-wide permission. It is scoped by person, context,
data domain, purpose, recipient, action, device, channel, and time. A household
administrator is not automatically authorized to read another person's data.
Compromise of one adapter, workload, domain, or person's account should not
automatically disclose the household archive.

## Reconciliation with the current design

| Foundation | Current design and evidence | Required extension or validation |
| --- | --- | --- |
| Per-person privacy | Accepted primary-person principals, private assistants, independent key domains, explicit shared context spaces, non-oracular denials | Hardware-backed key release, physical-host validation, side-channel characterization, and operator procedures |
| Sensitive-domain separation | Person and context-space isolation exists; life-operations packages distinguish health, finance, household, care, benefits, and other records | Add explicit per-person/per-domain cryptographic and execution compartments; demonstrate blast-radius containment |
| Local context and memory | Governed context, provenance, corrections, retention, encrypted stores, and local model preference exist | Define a unified storage hierarchy, schema evolution, capacity planning, index rebuild, archival media, and hardware failure behavior |
| External disclosure | Remote inference requires a disclosure decision, local-alternative check, minimization, and provider policy | Add a privacy egress broker, unlinkability goals, isolated sessions, query decomposition, provider/account separation, and measurable leakage tests |
| Deterministic orchestration | Accepted plans, exact approvals, typed capabilities, tools, skills, deterministic validation, and recoverable execution | Standardize workflow runtime, skill/tool conformance, temporal execution, concurrency, and household resource scheduling |
| Replaceable models | Signed model registry, task routing, eligibility, canary, lifecycle journal, and rollback are implemented in software | Physical accelerator qualification, real model manifests, energy/thermal/load evidence, and supported compatibility matrix |
| Multimodal inclusion | Semantic Experience Model precedes modality; person-owned interaction profile and modality-independent continuity exist | Physical-device matrices and participatory research with Deaf, blind, mobility-disabled, speech-disabled, and other represented users |
| Backup and recovery | Provider-blind encrypted backup, per-scope keys, signed manifests, replacement-device recovery, and deletion semantics exist in candidate software | Physical clean-restore exercises, off-prem operating model, media lifecycle, disaster exercises, and recovery usability evidence |
| Threat monitoring | Threat register, supply-chain controls, content-free health gates, signed updates, rollback, and adaptive-maintenance design exist | Deploy host/network/runtime sensors, incident state machine, independent watchdog, threat-intelligence ingestion, and response exercises |
| Hardware security | Threat model requires hardware-backed/per-person keys and full-disk protection | Select root-of-trust profile and validate measured boot, key sealing, IOMMU/DMA policy, tamper evidence, secure recovery, and firmware lifecycle |

## Multi-layer security posture

Security should use mutually reinforcing layers with explicit failure and
recovery behavior:

1. **Supply chain and release:** reproducible builds where practical, pinned
   dependencies, SBOM and VEX, signed provenance, threshold-controlled update
   authority, immutable release manifests, staged activation, and automatic
   last-known-good rollback.
2. **Platform boot and firmware:** UEFI Secure Boot, measured boot, TPM-backed
   device identity and key release, signed firmware, rollback protection,
   auditable firmware inventory, IOMMU/DMA isolation, and a recovery path that
   does not silently bypass personal data boundaries.
3. **Host isolation:** minimal immutable or transactionally updated host,
   least-privileged services, mandatory access control, read-only release trees,
   restricted system calls and devices, namespace or VM boundaries, encrypted
   swap, and denial of unnecessary lateral traffic.
4. **Workload identity:** every service, adapter, model runtime, scheduled job,
   and maintenance operation has authenticated identity and an explicit
   audience. Network location is not identity.
5. **Person and household authority:** server-derived principal context,
   independent assistants, explicit shared spaces, scoped delegation, step-up
   for consequential operations, and separation of household administration
   from private-data authority.
6. **Data compartments:** independent cryptographic and authorization domains
   for person, shared space, and sensitive data class, with minimized
   cross-domain joins and separately governed derived indexes.
7. **Capability containment:** signed manifests, exact grants, sandboxing,
   filesystem/device/network allowlists, resource limits, credential brokerage,
   tainted-input handling, confirmation, cancellation, and revocation.
8. **Inference containment:** minimized context, deterministic eligibility,
   model output treated as an untrusted proposal, schema and provenance checks,
   no model-held durable authority, and content-free health monitoring.
9. **Network and external privacy:** segmented networks, outbound-first access,
   authenticated encrypted transport, controlled DNS and egress, isolated
   external sessions, and explicit disclosure records.
10. **Detection and response:** tamper-evident security events, host/network and
    workload signals, anomaly rules, canaries, integrity checking, independent
    watchdogs, quarantine, credential/key rotation, restoration, and accessible
    owner notification.
11. **Physical and operational security:** enclosure access policy, service
    modes, recovery ceremony, removable-media controls, theft response,
    installer authority, backup custody, and safe decommissioning.

No single mechanism—container, disk encryption, VPN, TPM, firewall, or model
policy—is sufficient by itself.

## Breach containment and data compartments

Container boundaries alone should not be described as strong protection from a
compromised host kernel. The design should select isolation strength according
to sensitivity and attack surface. Candidate mechanisms include separate OS
identities and mandatory access-control domains, rootless containers, sandboxed
processes, microVMs or VMs for high-risk adapters, independent encrypted
datasets, and hardware-backed key release.

The proposed key and storage hierarchy is:

```text
device root of trust
  -> release and platform state
  -> person root (one per person; not derivable by household admin)
       -> domain keys: health | finance | identity | communications | general
       -> private context-space keys
       -> source-object, database, index, and backup epochs
  -> shared-space roots (membership-governed; independent of person roots)
       -> shared domain and epoch keys
```

Keys should be independently rotatable and revocable. Cross-domain operations
must request the minimum fields through an authorized broker; they should not
mount every domain into one general-purpose model or process. Highly sensitive
workloads may run in stronger isolation and receive short-lived plaintext views
or handles rather than direct store access.

The containment objective is reduced blast radius, not an impossible promise
that a sufficiently privileged physical or host compromise can never reach
multiple domains. Threat models and product claims must identify which
compromises a boundary resists and which require detection, shutdown, rotation,
or recovery.

## Detection, response, and continuous security improvement

Unison needs a security lifecycle, not merely periodic patching:

- maintain an exact hardware, firmware, OS, container, package, model, skill,
  tool, and capability inventory;
- correlate signed advisories, CVE/VEX data, vendor bulletins, dependency
  changes, exploit evidence, local integrity results, and measured behavior;
- treat all threat feeds and web content as untrusted evidence that cannot
  authorize a change;
- produce an inspectable, deterministic remediation plan with compatibility,
  exposure, reversibility, and owner-impact analysis;
- use isolated canaries, health gates, maintenance windows, checkpoints, and
  last-known-good rollback;
- detect suspicious authentication, cross-domain access, process, device,
  network, resource, integrity, and update behavior without logging personal
  content;
- respond in bounded stages: observe, restrict, isolate, preserve evidence,
  notify, rotate/revoke, restore, verify, and learn; and
- provide a physical or independently controlled emergency mode when the main
  software authority may be compromised.

Automatic response should favor reversible containment. Destructive wiping,
irreversible key destruction, firmware changes, or broad network isolation need
explicitly designed authority and recovery because a false positive could harm
the people who depend on the system.

## Privacy-preserving external queries

Private browsing/incognito mode mainly limits local browser history and cookie
persistence; it does not make traffic anonymous. A conventional VPN shifts
network visibility from the local ISP to the VPN provider and does not remove
account identity, cookies, browser fingerprints, query contents, timing, or
provider-side correlation. Neither mechanism alone supports a de-identification
claim.

Unison should use a governed privacy egress service with explicit threat-model
profiles. Depending on the task and risk, it can:

- answer locally from authorized data or cached public sources;
- separate a personal question into minimally identifying public subqueries;
- remove names, exact addresses, rare combinations, stable identifiers, and
  unnecessary context before egress;
- use an isolated ephemeral browser or HTTP client with no personal account,
  cross-task cookie jar, or household-stable application identifier;
- select a reviewed privacy search provider, relay, proxy, VPN, or stronger
  anonymity network when its latency and abuse tradeoffs fit the task;
- encrypt DNS and prevent direct fallback around the selected egress path;
- keep provider credentials and logged-in browsing in a different profile from
  de-identified research;
- record what fields and residual metadata left the appliance; and
- refuse or ask for consent when a useful query cannot meet its privacy goal.

The system should describe outcomes as minimized, isolated, unlinkability-
seeking, or provider-disclosed according to measured properties. “Anonymous”
or “de-identified” should require a precise threat model and verification.

## Algorithm orchestration and model routing

Unison is best understood as an algorithm orchestrator. A user request can be
resolved by a composition of deterministic code, retrieval, rules, optimization,
search, a signed skill, typed tool calls, specialized local models, optional
approved remote models, and modality composers.

The preferred execution sequence is:

```text
authenticated person and current situation
  -> intent and outcome contract
  -> authorized context selection
  -> typed plan and dependency graph
  -> deterministic algorithm/tool/skill where sufficient
  -> governed model route for bounded ambiguous work
  -> typed untrusted proposal
  -> fact, policy, recipient, action, and provenance validation
  -> exact approval where required
  -> execution, observation, recovery, and durable receipt
  -> governed memory admission
```

Models should be used where ambiguity, synthesis, perception, language, or
generalization adds value. Exact calculation, identity, policy, permissions,
storage, schedules, action binding, confirmations, execution, auditing,
retention, and recovery remain deterministic. Repeated work should migrate
toward tested skills, tools, workflows, caches, or conventional algorithms when
that improves reliability and cost without losing needed flexibility.

Deterministic routes are preferred implementations, not a closed catalog of
what Unison can attempt. Novel requests follow the governed resolution ladder
and repeatable patterns enter the reviewed skill-incubation lifecycle in
[UNISON_RESOLUTION_AND_SKILL_EVOLUTION.md](UNISON_RESOLUTION_AND_SKILL_EVOLUTION.md).
Unison should provide safe research, composition, partial progress, or handoff
before falling back to a generic statement that it cannot help.

Model replacement must not migrate or strand personal memory. Durable person
state lives in model-independent schemas and source objects. Model-specific
embeddings, summaries, caches, and indexes are derived products with provenance,
version, policy, and rebuild paths.

## Context, memory, and storage architecture

The storage system needs several data representations without confusing their
roles:

| Layer | Role | Authority rule |
| --- | --- | --- |
| Immutable source objects | Original documents, media, messages, sensor batches, and import receipts | Authoritative evidence; encrypted, content-addressed where appropriate, provenance-preserving |
| Relational records | People, permissions, events, facts, transactions, relationships, corrections, retention, and audit metadata | Authoritative structured state with migrations and constraints |
| Time-series/event stores | Sensor observations, workload health, energy, environmental state, and append-only lifecycle events | Policy-scoped retention; personal content separated from operational telemetry |
| Graph views | Relationships among people, sources, entities, commitments, and provenance | Derived or controlled canonical edges; never implicit sharing authority |
| Text/search indexes | Exact and lexical retrieval | Derived, person/domain scoped, deletable and rebuildable |
| Vector indexes | Semantic retrieval candidates | Derived, model/version identified, non-authoritative, independently encrypted or isolated, rebuildable |
| Working memory | Bounded task/session state | Short-lived, purpose-bound, cancellable, and admission-gated |
| Durable memory | Reviewed facts, preferences, commitments, corrections, summaries, and relationships | Explicit provenance, confidence, ownership, domain, retention, and correction semantics |
| Archive and backup | Local redundancy, snapshots, provider-blind off-prem copies, and disaster recovery | Independent failure domains, signed checkpoints, tested restore, per-scope deletion/rotation |

“Memory” must not become one undifferentiated vector database. Retrieval should
combine authorization, structured filters, exact search, graph relationships,
time, provenance, and semantic similarity. A vector match proposes relevance;
it does not prove truth, identity, ownership, permission, or recency.

Local redundancy protects availability but is not backup. The design should
separate:

- device redundancy for component failure;
- local snapshots against error or corruption;
- an independently powered local backup where useful;
- provider-blind off-prem backup for site loss; and
- tested replacement-device recovery with per-person authority.

Storage placement should account for sensitivity, latency, write endurance,
capacity, energy, acoustics, replacement, and rebuild time. SSDs may serve
active databases and indexes while economical disks or other media serve
versioned object storage and backup, but the final layout must follow measured
workloads and reliability goals.

## Concurrent household operation

The platform must support several people and continuous background workloads
without allowing one person or task to infer, starve, or silently consume the
resources of another. Scheduling should include:

- per-person and per-workload identity, queues, budgets, and cancellation;
- interactive latency classes distinct from background monitoring, indexing,
  backup, model evaluation, and maintenance;
- admission control for CPU, accelerator memory, RAM, storage I/O, network,
  energy, and thermal headroom;
- preemption or graceful degradation with an explanation;
- fair accelerator scheduling and bounded model residency;
- privacy-preserving resource telemetry; and
- a safety lane for alarms, accessibility, security, and shutdown that cannot
  be starved by shopping, research, or batch inference.

## Native multimodal and shared understanding

Input and output are independent dimensions. Speech input need not imply speech
output, and a visual source need not require a visual experience. Unison should
identify the intended outcome, construct a semantic representation, and compose
an appropriate expression using the person's governed preferences, abilities,
devices, context, privacy, and current choice.

Native support for Deaf, blind, speech-disabled, mobility-disabled, cognitively
diverse, and other people requires co-design and representative validation, not
only translation or conformance tests. Semantic equivalence must preserve facts,
uncertainty, actions, confirmation, cancellation, provenance, privacy, and
recovery across modalities.

Shared understanding does not mean shared raw memory. It should be facilitated
through explicit shared context spaces, purpose-bound derived artifacts,
perspective and provenance labeling, controlled disclosure, accessible
expressions for each participant, and the ability to correct, withdraw, or
disagree without rewriting another person's private record.

## Product capabilities recorded in this session

- ad hoc questions and commands comparable in immediacy to current voice
  assistants, but grounded in authorized evolving local context;
- long- and short-term recommendations from health, finance, household, goals,
  preferences, commitments, and other approved sources;
- continuous household monitoring and bounded control;
- simultaneous research, shopping, education/curriculum, household assistance,
  recommendation, and communication workloads for multiple people;
- any supported input to any appropriate supported output;
- accessible interaction native to each modality rather than a visual-first
  interface with accommodations added later;
- explicit mechanisms for shared understanding without collapsing personal
  privacy; and
- frequent replacement of models and algorithms without losing or redefining
  durable context and memory.

## Decisions and questions carried forward

1. Define the exact per-domain compartment taxonomy and whether health,
   finance, identity, communications, and general context require different
   process/VM and hardware-key boundaries.
2. Define the hardware root-of-trust and owner/recovery key ceremony without
   making a household administrator universal data authority.
3. Define external-query privacy profiles and the residual metadata each one
   permits; do not use “incognito” as a security boundary.
4. Define what continuous household monitoring may observe, how long it is
   retained, who owns it, and which physical actions remain prohibited.
5. Define the canonical source/record/event/index/archive storage contracts and
   data migration invariants.
6. Define interactive and background service-level objectives plus accelerator,
   energy, thermal, and safety scheduling policy.
7. Select the first end-to-end household outcomes that exercise privacy,
   memory, deterministic orchestration, model routing, and multimodal access
   without attempting every domain at once.
