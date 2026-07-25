# Unison adaptive maintenance and continuous improvement

Status: proposed architecture and implementation plan

Date: 2026-07-24

## Purpose

Unison should continuously help keep its appliance secure, reliable, responsive,
and well matched to the way it is actually used. It should detect degradation,
find relevant improvements, explain what matters, safely perform authorized
maintenance, verify the result, and recover automatically when a change makes
the system worse.

This capability is called **Adaptive Maintenance**. "Self-healing" does not
mean unconstrained self-modification. Every change must be:

- supported by measured local evidence;
- compatible with the exact hardware and installed software inventory;
- traceable to trustworthy source material;
- evaluated against security, privacy, accessibility, cost, and reversibility;
- governed by the person's maintenance policy;
- staged, verified, and automatically reversible where technically possible;
- understandable before and after execution; and
- recorded without turning operational telemetry into a copy of personal life.

The primary objective is sustained time returned to the person. Engagement,
novelty, affiliate revenue, popularity alone, and benchmark scores disconnected
from local needs are not optimization objectives.

## Product experience

Adaptive Maintenance appears as a quiet part of Unison, not a separate
administrator console.

### Everyday behavior

- A concise **System wellbeing** surface reports Security, Reliability,
  Performance, Capacity, Compatibility, and Improvement opportunity.
- Normal operation is silent. Unison interrupts only for urgent risk, required
  consent, imminent capacity failure, or a maintenance window the person asked
  it to announce.
- Recommendations state the observed symptom, likely cause, supporting
  evidence, expected benefit, risks, downtime, download size, resource and
  energy cost, reversibility, and why the recommendation fits this machine.
- The person can ask, "Why is Unison slow?", "Is everything secure?", "What
  changed?", "What should I upgrade?", or "Keep this healthy while I sleep?"
- After action, Unison reports what changed and whether measured outcomes
  improved. If they did not, it rolls back where possible and says so.

### Autonomy levels

Autonomy is independently configurable by action class:

| Level | Behavior |
| --- | --- |
| Observe | Measure and explain only |
| Recommend | Create ranked recommendations; never execute |
| Prepare | Download, verify, snapshot, and stage; ask before activation |
| Maintain | Execute pre-authorized, reversible low-risk work in a maintenance window |
| Emergency protect | Apply narrowly defined urgent containment or security actions, then notify immediately |

The default is Recommend. Emergency protect is opt-in except for actions that
are already necessary to preserve a documented secure product invariant.
Firmware, kernel transitions, model replacement, capability permission
expansion, destructive cleanup, paid services, and hardware purchases always
require explicit review. The person can pause maintenance, exclude a component,
set bandwidth or energy limits, defer an action, or permanently change its
autonomy class.

## Architectural placement

Adaptive Maintenance spans existing boundaries without creating a new
all-powerful agent.

```text
signed upstream advisories     community observations     local sensors
           |                            |                      |
           v                            v                      v
     Source Intake -----> Evidence Normalizer <----- Health Collector
                              |
                              v
                    Maintenance Reasoner
                     /       |        \
                    v        v         v
             Hardware Fit  Policy   Outcome Model
                    \        |         /
                     v       v        v
                    Recommendation Plan
                              |
                        Unison Surface
                              |
                  consent / standing authority
                              |
                              v
                    Appliance Lifecycle
                 stage -> checkpoint -> apply
                    -> verify -> promote/rollback
```

### Boundary responsibilities

- **Appliance Lifecycle** owns the host inventory, privileged probes, signed
  updates, checkpoints, activation, rollback, repair, and maintenance journal.
  It exposes narrow typed operations, never a general root shell.
- **Unison Core** correlates symptoms, local usage patterns, candidate changes,
  and owner preferences. It creates plans but cannot execute privileged changes.
- **Personal Data and Trust Store** evaluates maintenance policy, standing
  authority, disclosure, notification, and confirmation requirements.
- **Inference Broker** may help summarize evidence or predict workload fit.
  A model recommendation is never sufficient authority to install anything.
- **Capability Host** runs network-facing source collectors and sandboxes
  untrusted community content. Collectors have no lifecycle credentials.
- **Unison Surface** renders one semantic maintenance plan consistently across
  text, speech, keyboard, screen reader, captions, and reduced-motion modes.
- **Channel Gateway** may deliver alerts and approval requests, subject to
  channel assurance. Low-assurance channels cannot authorize protected changes.

No maintenance component receives both arbitrary internet content and
privileged execution authority.

## Core records and contracts

All records are versioned, canonical, and locally inspectable.

### Device profile

`DeviceProfile` records stable and slowly changing facts:

- board/system identity, CPU architecture/features, cores and thermal limits;
- RAM capacity, speed where available, pressure history, and upgrade topology;
- storage devices, filesystem, capacity, health, endurance, and performance;
- GPU/NPU identity, driver/runtime/firmware compatibility, and memory;
- network and audio devices;
- firmware, UEFI, Secure Boot, TPM, kernel, OS, container runtime, and drivers;
- power, acoustic, thermal, and enclosure constraints;
- installed Unison release, images, models, capability packages, schemas, and
  trust roots; and
- support tier and compatibility-matrix version.

Raw serial numbers, MAC addresses, and equivalent identifiers remain local and
are redacted from exported support reports by default.

### Operational observations

`HealthObservation` contains a metric name, time window, aggregation, unit,
component, severity, confidence, collection method, and retention class.
Initial indicators include:

- boot and ready time, service restarts, failed health checks, rollback events;
- CPU saturation, run queue, throttling, temperature, and power state;
- memory pressure, swap, OOM events, cache effectiveness, and model residency;
- disk latency, free space, growth rate, SMART/NVMe health, and write endurance;
- model load time, first-token latency, tokens per second, task success, fallback
  rate, and local-versus-remote routing;
- request latency by product journey, queue delay, cancellation, and error rate;
- network loss, DNS failure, update reachability, and download reliability;
- backup freshness, verification, restore drill, and recovery-point age;
- package, image, model, capability, firmware, and configuration age; and
- vulnerability exposure, exploit relevance, fix availability, and support
  window.

Operational collection must not store prompt text, message content, contact
names, document titles, URLs containing personal identifiers, or another
person's private activity. Per-person workload data is aggregated inside that
person's domain before device-level planning. Household administrators receive
only the minimum device-health result.

### External evidence

`MaintenanceEvidence` records:

- canonical source, publisher, source class, retrieval time, and immutable hash;
- signature or transport verification and source-trust policy;
- affected products and version constraints;
- hardware/software prerequisites;
- security identifiers and severity where relevant;
- claimed benefit, risks, limitations, license, cost, and data behavior;
- independent corroboration and conflict indicators;
- untrusted-content labels and extracted factual claims; and
- expiration or recheck time.

`MaintenanceCandidate` links evidence to the exact local inventory. A candidate
cannot become a recommendation until compatibility, provenance, policy, and
local relevance checks pass.

### Recommendation and execution

`MaintenanceRecommendation` includes:

- observed need and baseline;
- proposed action and alternatives, including doing nothing;
- exact target versions and artifact digests;
- hardware-fit decision and confidence;
- expected security, reliability, performance, capacity, privacy, accessibility,
  cost, energy, and downtime effects;
- authority class, confirmation requirement, maintenance window, checkpoint,
  health gate, rollback method, and recovery instructions;
- source evidence and locally measured rationale; and
- expiry, supersession, and feedback state.

`MaintenanceReceipt` binds the approved plan to downloaded artifacts, system
checkpoint, executed steps, before/after observations, health decision,
promotion or rollback, and owner-visible explanation.

## Evidence acquisition

Sources are registered in a signed `SourceRegistry`. Each entry defines allowed
endpoints, parser, cadence, data license, authentication, rate limit, trust
weight, expected signatures, and whether the source is authoritative,
corroborating, or discovery-only.

### Source tiers

1. **Authoritative security and compatibility**: Unison signed channels,
   Ubuntu security notices and OVAL data, package/container advisories, vendor
   firmware and driver notices, GitHub-reviewed advisories, and signed
   dependency releases.
2. **Authoritative software and model releases**: upstream release feeds,
   signed GitHub releases, model registries and model cards, capability
   registries, and documented hardware compatibility databases.
3. **Independent technical evidence**: reproducible benchmarks, issue trackers,
   maintainer discussions, research, and established technical publications.
4. **Community discovery**: public forums, Hacker News, Reddit communities,
   blogs, videos, and other places where people share configurations and tips.

Tier 4 content can create a research lead, never an executable plan. Popularity
is a discovery signal, not proof. A community claim must be reduced to a
testable proposition and corroborated by authoritative documentation, code,
multiple independent reports, or a safe local experiment.

Collectors prefer documented APIs, Atom/RSS, release feeds, or explicit
permission over scraping. They honor robots directives, terms, attribution,
rate limits, deletion, and source-specific retention. The registry can disable
a compromised, legally unsuitable, low-quality, or hostile source without a
software release.

All retrieved text is untrusted data. Prompt injection, embedded commands,
download links, popularity manipulation, affiliate content, and astroturfing
cannot supply action authority or change source policy.

## Analysis and ranking

The reasoner evaluates candidates in five stages.

1. **Applicability**: match exact component versions, architecture, hardware
   features, support tier, dependencies, and configured product profile.
2. **Need**: compare local observations with versioned healthy envelopes,
   forecasts, SLOs, and the person's actual workload.
3. **Safety**: verify provenance, signatures, vulnerability state,
   compatibility, resource headroom, migration path, backup freshness, health
   gate, and rollback.
4. **Value**: estimate time returned, risk reduced, reliability gained, local
   responsiveness, privacy effect, energy, cost, downtime, and opportunity cost.
5. **Decision**: suppress, observe longer, recommend, stage, execute under
   standing authority, or escalate urgently.

The ranking function is deterministic and inspectable. Learned estimates may
contribute confidence-bounded inputs, but cannot bypass hard policy.
Recommendations identify uncertainty and evidence disagreement.

### Hardware recommendations

Hardware advice begins with a diagnosed workload bottleneck, not a generic
upgrade list. It requires sustained evidence and predicts the benefit on the
person's real workload:

- RAM only when pressure, eviction, swap, or model-residency limits are causal;
- storage only for forecast capacity, health/endurance risk, or measured I/O
  bottlenecks;
- CPU/GPU/NPU only when compute is causal and the proposed device is supported
  by the power, thermal, driver, model, and enclosure profile;
- network or audio only when observed quality affects supported journeys.

Advice includes compatible specifications, expected benefit range, installation
complexity, data migration or downtime, power/thermal impact, support status,
and a no-purchase alternative such as model quantization, scheduling, cleanup,
or remote routing. Recommendations never include paid placement or undisclosed
affiliate influence.

## Action classes and safety rules

| Class | Examples | Default |
| --- | --- | --- |
| Read-only diagnosis | health probes, inventory, signature checks | Automatic |
| Reversible housekeeping | bounded cache cleanup, log compaction | Recommend |
| Application/model/capability update | signed compatible target | Prepare |
| OS package security update | signed supported patch with checkpoint | Prepare |
| Urgent containment | disable revoked capability, isolate vulnerable service | Explicit emergency policy |
| Restart or failover | restart unhealthy service, use last-known-good model | Automatic when bounded |
| Kernel/driver/firmware | boot-critical or device-level update | Confirm |
| Schema/data migration | reversible migration with verified backup | Confirm |
| Destructive cleanup | delete personal artifacts or reduce retention | Confirm |
| Hardware purchase/change | RAM, storage, accelerator, peripheral | Recommend only |

Automatic work requires a valid standing grant scoped to action class, target,
maximum downtime, maintenance window, cost, bandwidth, and rollback behavior.
Grants expire and are revocable. A plan change invalidates approval.

The Lifecycle boundary performs: preflight, artifact verification, backup and
checkpoint verification, canary or staged activation, bounded health checks,
promotion, and rollback. Boot-critical changes use an external watchdog or
bootloader-level last-known-good mechanism so the component judging health is
not solely the component being replaced.

## Learning loop

Each completed action becomes a local experiment:

1. record a privacy-minimized baseline;
2. state predicted outcomes and stop conditions;
3. apply to a canary, optional component, or bounded window where possible;
4. compare the same indicators after warm-up;
5. promote, retain for observation, or roll back;
6. update local confidence and suppress repeatedly unhelpful advice; and
7. show the person the result.

Local outcomes are not uploaded by default. Opt-in aggregate contribution
requires differential/minimum-cohort review, strips identifiers and personal
content, and is never required for product functionality.

## Failure and threat model

Adaptive Maintenance adds important risks:

- compromised advisory or release sources;
- prompt injection and malicious commands in community content;
- typosquatting, dependency confusion, malicious models, and unsafe model code;
- telemetry exposing personal activity;
- false diagnosis, benchmark gaming, and popularity manipulation;
- maintenance loops, restart storms, resource oscillation, or alert fatigue;
- a privileged deputy executing a plan it did not independently verify;
- rollback that restores software but corrupts schema or personal data;
- firmware or boot failure beyond application-level recovery;
- recommendations distorted by commercial incentives; and
- another household member inferring private usage from device metrics.

Controls include signed allowlisted sources, sandboxed parsing, provenance and
taint labels, quorum/corroboration, immutable targets, independent privileged
verification, rate and change budgets, cooldowns, circuit breakers, typed
operations, precondition hashes, checkpoints, external watchdogs, non-oracular
health summaries, accessible consent, and append-only receipts.

## Phased implementation

### AM-0: Decisions, contracts, and simulation harness

- Approve the autonomy model, operational-data boundary, source policy,
  administrator visibility, and emergency authority.
- Add canonical schemas for the records in this design.
- Build a deterministic simulator for metrics, faults, candidate evidence,
  decisions, execution, health checks, and rollback.
- Define initial SLOs and healthy envelopes without claiming physical validity.

Gate: contract validation and adversarial simulations prove that internet
content cannot reach privileged execution and unknown authority denies.

### AM-1: Private system observability

- Implement inventory and privacy-minimized health collection.
- Add retention, aggregation, redaction, export, and deletion controls.
- Render System wellbeing and answer read-only diagnostic questions.
- Establish workload baselines and anomaly detection with explainable rules.

Gate: metrics diagnose injected CPU, memory, disk, service, model, backup, and
network faults without recording personal-content canaries or leaking
per-person activity to administrators.

### AM-2: Security posture and patch intelligence

- Ingest Unison channels, Ubuntu notices/OVAL, GitHub advisories, package,
  container, runtime, model, capability, driver, and firmware advisories.
- Build a software bill of materials and exposure graph for the installed state.
- Rank by local reachability, exploit relevance, fix availability, and support.
- Add security posture explanations, patch deadlines, and urgent containment.

Gate: known-vulnerable fixtures are detected across every shipped layer;
unaffected hardware/software is not flagged; signatures, versions, revocation,
and false-feed attacks fail closed.

### AM-3: Recommendation engine and hardware fit

- Add bottleneck diagnosis, forecasts, candidate comparison, and deterministic
  multi-objective ranking.
- Generate software, configuration, model, scheduling, and hardware advice.
- Benchmark safe candidate models/configuration in a resource-bounded sandbox.
- Show alternatives, uncertainty, provenance, and measured local rationale.

Gate: recommendations improve seeded workloads in simulation, reject
incompatible hardware, avoid unnecessary purchases, and never rank sponsored
or popularity-only candidates.

### AM-4: Safe self-healing

- Implement autonomy grants, maintenance windows, budgets, staging, canaries,
  health gates, receipts, cooldowns, and circuit breakers.
- Enable bounded service restart/failover, housekeeping, signed patch staging,
  and last-known-good model/configuration recovery.
- Integrate with Phase 9 update, backup, and rollback transactions.

Gate: repeated fault, interruption, disk-full, bad update, degraded
performance, migration failure, and restart-storm tests preserve data and
return to last known good without exceeding action budgets.

### AM-5: Community improvement intelligence

- Implement the signed source registry and sandboxed feed/API collectors.
- Add claim extraction, duplicate clustering, reputation history,
  corroboration, conflict detection, and local test proposal generation.
- Begin with read-only discovery from a small reviewed source set.
- Add accessible source and rationale inspection plus feedback controls.

Gate: prompt injection, affiliate manipulation, coordinated popularity,
malicious downloads, deleted posts, conflicting claims, parser failure, and
source compromise cannot authorize or install a change.

### AM-6: Full-stack maintenance and hardware guidance

- Extend safe execution to OS packages, container runtime, drivers, model
  runtime, models, capability packages, databases/configuration, and firmware
  where vendor recovery permits.
- Validate upgrade advice against the versioned physical compatibility matrix.
- Add capacity and hardware-benefit forecasting based on sustained local use.
- Qualify external-watchdog and boot rollback on named reference systems.

Gate: the physical matrix passes power interruption, reboot, boot failure,
firmware failure, thermal/load, update, rollback, backup, and restore tests.
Hardware advice demonstrates predicted benefit within an approved tolerance.

### AM-7: Pilot, calibration, and supported operation

- Run a time-bounded opt-in pilot across the reference matrix.
- Measure detection precision, recommendation acceptance, realized benefit,
  rollback success, alert burden, patch latency, and time returned.
- Complete accessibility, privacy, security, incident, source-governance, and
  commercial-influence reviews.
- Publish support boundaries and operational runbooks.

Gate: approved targets are met with zero cross-person disclosure, unauthorized
maintenance, uncontained supply-chain execution, or unrecoverable update
incidents. Human review explicitly promotes each autonomous action class.

## Success measures

- time to detect and recover from supported faults;
- percentage of security exposure patched within severity policy;
- successful maintenance and rollback rates;
- reduction in unplanned downtime and repeated incidents;
- recommendation precision and realized local benefit;
- unnecessary hardware purchases avoided;
- maintenance interruption and notification burden;
- accessibility completion for explanation, approval, deferral, and recovery;
- zero personal-content telemetry, cross-person disclosure, sponsored ranking,
  or community-content-to-execution incidents; and
- person-confirmed time and attention returned.

## Initial source integration notes

The first implementation should prefer machine-readable authoritative inputs.
Ubuntu publishes security notices and OVAL data suitable for determining
release-specific applicability. GitHub exposes reviewed global security
advisories. Hugging Face exposes a versioned Hub API and model metadata.
Hacker News provides an official public API suitable only for discovery.

These examples do not create a permanent allowlist. Every integration still
requires legal/terms review, source-registry approval, rate controls, parser
tests, and a clear trust tier.
