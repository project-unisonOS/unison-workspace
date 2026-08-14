# Unison integrated system program

Status: **Discovery draft; not an accepted architecture or product claim**  
Opened: 2026-08-14  
Decision authority: project owner, with recorded contributor review  
Planning horizon: incremental systems now through a target hardware generation in Winter 2027 or Spring 2028

## Purpose

This document is the durable record for evolving Unison from an open-source
software platform into a complete, local-first solution spanning software,
compute, storage, networking, radios, sensors, security, power, cooling,
industrial design, installation, and lifecycle support.

It records the initial context, working hypotheses, proposed program structure,
and questions that require further reasoning. A statement in this document is
not an implementation or support claim unless it links to executed evidence.

The foundational privacy, security, orchestration, memory, storage, concurrent
household, and multimodal promises are reconciled in
[UNISON_SYSTEM_FOUNDATIONS.md](UNISON_SYSTEM_FOUNDATIONS.md).
The initial end-to-end product requirements are developed in
[UNISON_REFERENCE_JOURNEYS.md](UNISON_REFERENCE_JOURNEYS.md).
The first executable product slices are specified in
[UNISON_DEMONSTRATION_JOURNEYS.md](UNISON_DEMONSTRATION_JOURNEYS.md).

## Product north star

Unison should turn electricity into useful, private, person-aligned
intelligence. The system is conceived as household infrastructure rather than
another disposable personal computer: durable, modular, inspectable,
repairable, locally authoritative, and able to improve as compute and I/O
hardware evolve.

The phrase “turn electricity into intelligence” is a product direction, not an
excuse for unbounded power use. Useful outcomes per watt, lifecycle energy,
noise, heat recovery or rejection, embodied cost, reliability, and household
value are first-class design measures.

## Context recorded at program opening

- The Project Unison organization currently uses `unison-workspace` as the
  developer front door and authoritative planning repository, with many
  service repositories pinned as Git submodules.
- The software is an experimental local-first assistant platform with strong
  foundations in identity, governed context, policy, consent, semantic
  experiences, model lifecycle, release trust, and accessible interaction.
- The current supported-release candidate remains a signed Ubuntu 24.04 LTS
  native bundle on x86_64 UEFI hardware. Physical qualification is still open.
- The project owner’s primary command environment is Windows with the GPT/Codex
  desktop app.
- The project owner intends to direct work remotely and by voice using the GPT
  mobile app on an iPhone.
- `dev-nuc` is an Ubuntu development system reachable on the local network and
  through Tailscale. Its current Unison checkout is
  `/home/darryl-adams/project-unisonOS/unison-workspace`.
- An older dual-GPU workstation is expected during the week of 2026-08-17. It
  is intended to become an interim Unison deployment and integration system.
- The long-range hardware target is expected to use components available in
  Winter 2027 or Spring 2028, while supporting useful incremental hardware
  improvements before then.
- New contributors will be invited, especially for input/output capabilities.
  Contributor boundaries, guidance, reproducibility, and truthful maturity
  labels therefore need to become substantially clearer.

## Product-system scope

The integrated system may include:

- modular compute and memory blades;
- accelerator modules for local inference and media processing;
- redundant or resilient storage with explicit backup and restore boundaries;
- switching and network-service modules;
- radios and a governed sensor gateway;
- firewall, hardware-root-of-trust, and security infrastructure;
- power distribution, metering, protection, and serviceability;
- cooling sized for real sustained loads, not nominal component ratings;
- an accessible service and status interface;
- a distinctive enclosure that contributes to the Unison brand; and
- professional planning or installation when power, heat, noise, weight,
  wiring, ventilation, or code requirements exceed ordinary consumer setup.

The project must not assume that the final household system requires a
dedicated circuit, HVAC integration, or professional installation. Those are
credible product tiers to evaluate with measured loads, acoustics, thermal
models, electrical-code review, and user research. A quiet sub-kilowatt system,
a dedicated-circuit system, and a higher-power utility installation should be
treated as different envelopes rather than one prematurely fixed design.

## Working product tiers

These tiers are hypotheses for evaluation, not SKU commitments.

| Tier | Purpose | Initial physical hypothesis | Evidence needed |
| --- | --- | --- | --- |
| Developer node | Software and adapter development | Existing PC or NUC; no custom enclosure | Reproducible bootstrap and test profile |
| Household node | Continuous private services and moderate local inference | Quiet single-node or short-depth enclosure on ordinary household power | Sustained power, acoustic, thermal, reliability, and journey tests |
| Household rack | Whole-house inference, storage, networking, and sensor integration | Modular rack or cabinet, potentially using a dedicated circuit | Electrical, structural, ventilation, service, and installer review |
| Lab/reference rack | Maximum contributor and qualification coverage | Multiple accelerators, hardware-in-the-loop fixtures, and instrumentation | Repeatable reference configuration and evidence capture |

## Architecture principles to test and preserve

1. **Stable contracts, replaceable implementations.** Software must target
   capability and modality contracts rather than a specific GPU, radio, sensor,
   or model generation.
2. **Local authority.** Identity, policy, consent, durable context, exact action
   binding, and recovery remain under local owner control.
3. **Graceful hardware scaling.** The same signed release should discover
   hardware, select qualified profiles, degrade safely, and explain what is
   unavailable.
4. **Modular fault domains.** Compute, storage, network, radio, sensor, and
   security modules should fail, update, and be replaced without silently
   widening authority or losing recoverability.
5. **Semantic I/O before device-specific behavior.** Contributors implement
   adapters and composers against versioned semantic, capability, privacy, and
   safety contracts.
6. **Measured power and thermal behavior.** Idle, typical, burst, and sustained
   workloads must have recorded energy, temperature, throttling, and acoustic
   evidence.
7. **Open and serviceable by default.** Custom electrical, PCB, mechanical, and
   enclosure sources should be published in editable source formats with
   generated interchange artifacts, BOMs, assembly guidance, and revision
   history whenever licensing, safety, and third-party rights permit.
8. **Safety and claims follow evidence.** Simulation does not establish
   electrical safety, EMC, RF compliance, thermal safety, accessibility, or
   production readiness.

## Assessment of the current software repository model

The existing multi-repository/submodule model has useful properties: isolated
histories, per-service ownership, and explicit immutable release pins. It also
creates substantial friction for a growing contributor community:

- a fresh contributor must understand and synchronize more than twenty
  repositories;
- cross-service changes require coordinated branches, pull requests, releases,
  and submodule-pointer updates;
- repository boundaries currently mirror a microservice topology more closely
  than stable contributor or product boundaries;
- local validation and documentation can drift from the exact implementation
  set; and
- I/O contributors face a high discovery cost before reaching an adapter.

The structure should not be replaced immediately. The current pins are valuable
release evidence, and a migration without dependency and ownership analysis
would create unnecessary risk. The working recommendation is to simplify
toward a small number of cohesive repositories while preserving immutable
release manifests:

| Proposed repository | Responsibility |
| --- | --- |
| `unison` | Software monorepo: core services, shared contracts, first-party I/O adapters, test fixtures, developer tooling |
| `unison-hardware` | System architecture, KiCad electronics, mechanical/enclosure sources, interfaces, BOMs, qualification plans |
| `unison-infrastructure` | Reproducible development, lab, CI, deployment, observability, and hardware-in-the-loop automation |
| `unison-docs` | Product, contributor, operator, research, safety, and public documentation |
| `unison-releases` | Signed manifests, SBOM/provenance indexes, compatibility matrices, and promoted release evidence; write authority tightly restricted |

The final count and names remain open. A software monorepo is favored for the
current tightly coupled Python services and cross-cutting trust contracts, but
independently versioned SDKs, large model artifacts, sensitive security
operations, and hardware CAD may still justify separate repositories.

Before migration, produce a repository decision record using measured change
coupling, CI duration, ownership, release cadence, artifact size, security
boundary, and contributor-path data. Until that decision is accepted,
`unison-workspace` remains authoritative.

## Proposed GitHub program structure

Use one organization-level GitHub Project as the program index. Repositories
remain the source of truth for code and durable technical documents; the
Project provides cross-repository planning and views.

Recommended Project fields:

- track: product, software, I/O, hardware, infrastructure, security,
  accessibility, research, documentation, release;
- horizon: now, interim GPU system, 2027/2028 target, later;
- maturity: concept, research, prototype, candidate, qualified, supported;
- evidence environment: static, simulation, CI, VM, physical, participatory;
- owner and reviewers;
- target system or hardware revision;
- risk and safety class;
- dependency/blocker;
- decision required; and
- acceptance/evidence link.

Repository-level labels and issue forms should derive from the same vocabulary.
Do not use a Project card as the only record of an architecture decision,
interface, safety finding, or qualification result.

## Hardware source and lifecycle structure

The proposed `unison-hardware` repository should begin with system interfaces
and evidence, not a premature motherboard or enclosure design.

```text
architecture/           system diagrams, power/thermal budgets, module interfaces
interfaces/             electrical, mechanical, network, management, and data contracts
bom/                    normalized BOM sources, cost snapshots, alternates, lifecycle risk
electronics/            KiCad projects, fabrication outputs, bring-up and test fixtures
mechanical/             editable CAD, neutral STEP exports, drawings, tolerance notes
enclosure/              industrial design, ergonomics, service access, acoustic design
thermal/                models, assumptions, instrumentation, test results
power/                  distribution, protection, metering, UPS and shutdown behavior
compliance/             safety, EMC, RF, environmental, labeling, and review plans
qualification/          revision-specific procedures and immutable evidence indexes
prototypes/             bounded experiments with explicit maturity labels
```

Every BOM item should have a stable identifier and record manufacturer part
number, function, quantity, approved alternates, lifecycle state, source,
currency, unit price, price-quantity basis, observed date, lead time, region,
license or usage constraint, power/thermal contribution, and target hardware
revision. Cost is a dated estimate, not a timeless property. Automated price
collection may inform planning, but human-reviewed snapshots should back design
decisions.

Preferred editable formats should be open where practical: KiCad for schematics
and PCBs, an agreed source CAD format for mechanical work, STEP for exchange,
and text-based interface/BOM metadata for review and automation. Hardware and
documentation licenses require an explicit project-owner decision before broad
external contribution; CERN Open Hardware Licence v2 is a candidate, not yet a
selection.

## Development and test topology

### Control plane: Windows workstation

- Primary human interaction through GPT/Codex desktop.
- Voice and remote direction may originate from the GPT mobile app.
- Holds convenient local checkouts, planning documents, and review tools.
- Should not become the sole builder, deployment authority, or secrets store.
- Long-running work must write progress, commands, commits, evidence, and next
  actions into durable repository artifacts so mobile or desktop sessions can
  resume without relying on chat history.

### Development plane: `dev-nuc`

- Ubuntu development and integration runner.
- Reachable by local network and Tailscale SSH path.
- Current workspace:
  `/home/darryl-adams/project-unisonOS/unison-workspace`.
- Near-term role: canonical interactive build/test host until environments are
  reproducibly declared and the GPU deployment host is commissioned.
- Must not be treated as production or as the only copy of uncommitted work.

### Interim deployment plane: dual-GPU workstation

- Expected during the week of 2026-08-17.
- Proposed role: persistent pre-production deployment, model qualification,
  sustained-load tests, GPU contention tests, update/rollback exercises, and
  early hardware-in-the-loop integration.
- Baseline inventory must capture exact chassis, board, CPU, RAM, GPUs, VRAM,
  storage, NICs, firmware, power supply, operating system, drivers, idle/load
  power, temperatures, and acoustics before it is accepted as evidence.

### Hosted plane: GitHub

- Fast deterministic checks, security scanning, reproducible builds, signed
  metadata validation, documentation, and review.
- Hosted CI must not be presented as physical hardware, participatory, RF,
  thermal, or electrical evidence.

### Network posture

- Prefer outbound-initiated management and Tailscale identity over public
  inbound ports.
- Separate management, trusted service, untrusted/guest, sensor/IoT, and test
  traffic as the lab grows; implement segmentation when suitable managed
  network hardware is available.
- Keep device identity and workload identity distinct.
- Record firewall policy, DNS, addressing, certificates, secrets sources,
  backup targets, observability paths, and emergency access in versioned
  infrastructure documents without committing secrets.
- A mobile command channel may request work but must not bypass repository
  review, deployment approval, policy, or destructive-action safeguards.

## Reproducible environment model

Define named, versioned profiles instead of relying on individually maintained
machines:

| Profile | Intended use | Minimum gate |
| --- | --- | --- |
| `dev` | Fast component development | Formatting, static checks, focused unit tests |
| `integration` | Cross-component and contract tests | Pinned dependencies, synthetic journeys, fault injection |
| `gpu-lab` | Model and accelerator work | Exact driver/runtime manifest, model registry, resource and energy telemetry |
| `appliance-candidate` | Release rehearsal | Clean install, update, rollback, backup/restore, failure recovery |
| `hardware-in-loop` | Sensors, radios, I/O, power and thermal behavior | Revision-bound fixtures, calibration, physical evidence capture |

Each profile should be machine-readable and expose one documented entrypoint.
Toolchains, containers, OS packages, drivers, firmware, models, and test data
must be pinned or fingerprinted. Environment validation should fail clearly and
produce an inspectable report.

## Contributor experience, especially I/O

An I/O contributor should be able to start with one short guide and one
reference adapter. The target path is:

1. choose an input, output, or bidirectional modality;
2. implement the versioned adapter/capability interface;
3. run a local contract kit with simulated hardware;
4. run privacy, permission, failure, cancellation, and semantic-equivalence
   tests;
5. attach physical and participatory evidence when claiming qualification;
6. publish the adapter with an explicit maturity and support level.

Required contributor assets include a repository map, glossary, architecture
tour, development profiles, contract reference, adapter template, fixture
library, test matrix, threat checklist, accessibility research guidance,
evidence template, contribution policy, code of conduct, review ownership, and
support/maturity definitions.

## Long-running development sessions

Long-running work should be organized as resumable execution packets. Every
packet should contain:

- objective and explicit non-goals;
- authority and decisions already accepted;
- repository and immutable starting revisions;
- environment profile and machine target;
- dependency and access preflight;
- ordered checkpoints with bounded validation;
- safety and destructive-action limits;
- progress journal and machine-readable status;
- evidence locations and exact commands;
- commit/branch/PR state; and
- stop conditions, recovery steps, and next action.

The project should add root `AGENTS.md` guidance only after repository
boundaries and authoritative documents are reconciled. It should stay concise,
route agents to versioned runbooks, require truth labels for simulated versus
physical evidence, preserve uncommitted contributor work, and forbid secrets
or unsupported product claims.

Skills and tools needed over time include GitHub issue/PR/CI operations,
remote-shell and deployment runbooks, CAD/BOM validation, hardware inventory,
energy and thermal telemetry ingestion, accessibility test harnesses, release
signing with separated authority, evidence packaging, and persistent task
monitoring. Access should be least-privileged, machine-specific, auditable, and
recoverable; convenience access from mobile or an agent must not collapse
release or security separation.

## Initial risks

- **Premature hardware fixation:** selecting 2026 parts may distort a 2027/2028
  design. Define interfaces, envelopes, and qualification methods first.
- **Power and cooling assumption:** “whole-house inference” does not yet imply a
  dedicated circuit or HVAC-class installation. Measure workload value and
  deployment tiers before committing.
- **Repository sprawl:** adding hardware repositories without simplifying the
  software contributor path would make the program harder to enter.
- **Microservice tax:** current boundaries may consume more integration and
  release effort than their isolation value justifies.
- **Evidence inflation:** CI and simulated adapters can look complete while
  physical reliability, accessibility, safety, and user value remain unknown.
- **Supply volatility:** price, availability, export restrictions, vendor lock,
  firmware policy, and end-of-life risk require alternates and dated BOMs.
- **Open-hardware safety:** editable designs improve inspectability but do not
  confer regulatory approval or make high-voltage work safe.
- **Remote orchestration:** voice/mobile convenience increases ambiguity and
  requires explicit confirmation for consequential operations.

## Decisions already preserved

This discovery does not supersede the accepted software decisions in
`UNISON_ARCHITECTURE_DECISIONS.md`. In particular, local authority, semantic
experience before modality, replaceable model lifecycle, signed releases,
rollback, truthful evidence, and representative research for specialized access
claims remain foundational unless deliberately reconsidered.

## Decisions to make through the reasoning sessions

1. Who is the primary customer and what household outcomes justify a dedicated
   local system?
2. Which capabilities must remain available offline, and which may use remote
   providers under explicit policy?
3. What privacy, latency, availability, cost, energy, acoustic, and service-life
   targets define the product?
4. Which initial I/O modalities and household integrations earn first-class
   support?
5. Should the physical product begin as a quiet node, rack, professionally
   installed utility, or a family of tiers?
6. What should be modular at the user, installer, and engineering levels?
7. Which hardware interfaces can be made stable before target components exist?
8. Which custom hardware is strategically necessary versus sourced from
   commodity ecosystems?
9. What licensing model should apply to software, hardware, documentation,
   models, datasets, and brand assets?
10. Which current repositories should merge, remain independent, be archived,
    or become packages within the software monorepo?
11. What governance and maintainer model can safely accept broad external I/O
    contributions?
12. What evidence is required before calling any configuration a developer,
    reference, compatible, or supported system?

## Proposed next sequence

1. Define the intended people, household outcomes, constraints, and explicit
   non-goals.
2. Derive workload and I/O scenarios without selecting final hardware.
3. Convert scenarios into latency, throughput, storage, network, availability,
   privacy, power, thermal, acoustic, and cost envelopes.
4. Inventory the dev NUC and dual-GPU workstation against named environment
   profiles.
5. Decide the repository target and migration plan using measured dependency
   and change-coupling evidence.
6. Establish the hardware repository, interface registry, BOM schema, and first
   reference-system evidence template.
7. Build incremental reference systems and preserve physical evidence while
   monitoring the 2027/2028 component horizon.

## Session log

### 2026-08-14: Integrated product pivot opened

Recorded the shift from software-only platform planning toward a complete
Unison solution with incremental reference hardware and a 2027/2028 target
generation. Established the Windows/Codex control environment, remote Ubuntu
dev NUC, expected dual-GPU interim deployment host, mobile/voice direction,
open-hardware intent, modular rack concept, possible utility-class installation,
and the need for contributor-ready I/O boundaries. Proposed—but did not
accept—a smaller GitHub repository model, named environment profiles, hardware
source tree, and evidence-driven product tiers.

### 2026-08-14: Security, memory, orchestration, and interaction foundations

Recorded the multi-layer security and per-person privacy promise; sensitive
health, finance, identity, communications, and general-data containment;
hardware-rooted security intent; intrusion monitoring and bounded response;
privacy-preserving external query requirement; deterministic algorithm, skill,
and tool preference around bounded non-deterministic inference; local evolving
context as the primary product differentiator; continuous and simultaneous
household workloads; native multimodal interaction; shared understanding;
replaceable models; and a relational, object, graph, search, vector, event,
archive, and provider-blind backup storage hierarchy. Reconciled these ideas
against existing accepted architecture and identified the new physical and
system-design work without changing accepted decisions.

### 2026-08-14: Six reference journeys and cross-domain value

Expanded the product requirements into six journeys: private health record and
visit preparation; financial attention and planning; continuous home awareness,
safety, and control; research, learning, and curriculum assistance; shared
household coordination across privacy and modality boundaries; and offline
“MacGyver” resilience mode. Added a blind/sighted shared-understanding reference
demonstration and cross-domain journeys spanning health, finance, insurance,
home environment, education, care, and resilience. Established that emergency
knowledge must combine reviewed local sources and deterministic hazard rules
with models rather than relying on fine-tuned model weights alone.

### 2026-08-14: First demonstration specifications

Specified a simulated water-leak response shared by blind and sighted household
members and a synthetic health-preparation journey governed by financial and
insurance constraints. Each demonstration now records actors, source domains,
excluded information, preconditions, primary and failure flows, deterministic
and model responsibilities, fixture packages, acceptance gates, shared
primitives, and a staged path from contract review through simulation and later
physical/participatory evidence.
