# Unison reference journeys

Status: **Discovery draft; not a capability or safety claim**  
Opened: 2026-08-14  
Parent documents:

- [UNISON_INTEGRATED_SYSTEM_PROGRAM.md](UNISON_INTEGRATED_SYSTEM_PROGRAM.md)
- [UNISON_SYSTEM_FOUNDATIONS.md](UNISON_SYSTEM_FOUNDATIONS.md)

## Purpose

These six reference journeys translate the Unison product vision into
testable household outcomes. They are deliberately broader than feature lists:
each journey exercises person-level privacy, governed memory, deterministic
orchestration, replaceable models, multimodal expression, recovery, and
hardware or environment constraints.

The journeys are requirements sources. They do not claim that the current
software implements the complete experience. Each journey must eventually have
synthetic, adversarial, accessibility, physical-hardware, and participatory
evidence appropriate to its risk.

The first two bounded demonstrations derived from these journeys are specified
in [UNISON_DEMONSTRATION_JOURNEYS.md](UNISON_DEMONSTRATION_JOURNEYS.md).

## Common journey contract

Every reference journey must specify:

- person or people served and their distinct authority;
- desired outcome rather than only an input command;
- authorized private and shared context spaces;
- source provenance, freshness, confidence, and correction state;
- required input and output modalities;
- deterministic algorithms, skills, tools, and external capabilities;
- bounded model contributions and fallbacks;
- disclosure, recipient, risk, cost, confirmation, and recovery policy;
- online, degraded, and fully offline behavior;
- latency, availability, compute, storage, energy, and thermal class;
- durable-memory admission and retention behavior;
- explicit prohibited outcomes; and
- measurable evidence of value, privacy, safety, and accessibility.

## Journey 1: Private health record and visit preparation

### Outcome

A person can assemble a trustworthy longitudinal health picture from records,
wearables, medication lists, personal observations, appointments, questions,
and corrections, then prepare for a clinical visit without surrendering the
archive to a cloud assistant.

### Experience

Unison imports authorized records and documents into the person's health
compartment, preserves the original sources, extracts structured facts with
citations, distinguishes clinical statements from personal observations and
model inferences, reconciles contradictions, and identifies missing or stale
information. Before a visit it creates an accessible brief containing the
person's priorities, relevant timeline, current medications as recorded,
unresolved questions, follow-ups, insurance considerations selected by the
person, and exact source references.

The person can correct any fact, exclude a source, change what appears in the
brief, and approve the exact artifact or fields shared with a clinician or
caregiver. A household administrator or other family member cannot inspect the
health compartment merely because they manage the appliance.

### Modalities

- conversational interview by speech, text, switch/AAC, or sign interface;
- camera or scanner intake for documents and medication labels;
- navigable visual, spoken, Braille, or simplified-language timeline;
- concise visit brief in the person's and clinician's selected formats; and
- accessible uncertainty, correction, disclosure, and cancellation controls.

### Deterministic and model roles

Deterministic services own identity, source hashing, authorization, clinical
code and date handling, exact values, medication-list reconciliation rules,
citations, disclosure, retention, and document assembly. Models may extract
candidate facts, summarize authorized sources, explain terminology, group
questions, and propose a narrative. Every proposal retains provenance and
cannot become a diagnosis or treatment order.

### Safety boundary

Unison does not diagnose, prescribe, change medication, dismiss emergency
symptoms, or impersonate a clinician. Urgent-language detection and escalation
instructions use reviewed deterministic rules. Advice must distinguish general
information from personalized clinical guidance and identify when professional
or emergency help is needed.

### Initial measures

- source-to-claim citation coverage;
- extraction and reconciliation precision;
- correction and deletion completeness;
- time required to prepare a useful visit brief;
- prohibited-action and cross-person disclosure count;
- comprehension across supported modalities; and
- clinician/person usefulness ratings from approved research.

## Journey 2: Financial attention and planning

### Outcome

A person or explicitly defined household can understand obligations, unusual
changes, upcoming constraints, and practical choices without granting an
assistant authority to move money or monetize the underlying data.

### Experience

Unison ingests authorized statements, bills, receipts, subscriptions,
insurance documents, benefits information, and person-entered goals into the
appropriate private compartments. It identifies recurring obligations,
duplicate charges, price changes, missed refunds, deadlines, unusual activity,
and visibly uncertain cash-flow ranges. It produces a low-noise attention brief
that explains why each item matters and cites the source.

Joint views contain only explicitly contributed records or derived fields.
Unison can draft questions, cancellation requests, or dispute correspondence,
but it cannot send, transact, trade, borrow, close an account, file a return, or
accept a contract without separately designed authority.

### Modalities

- spoken or text questions with exact-value confirmation;
- visual, tactile/Braille, or structured summaries of trends and exceptions;
- accessible comparisons that do not rely on charts or color alone;
- document and email intake; and
- private review followed by an explicitly shared household artifact.

### Deterministic and model roles

Deterministic services calculate amounts, dates, reconciliations, thresholds,
and contribution boundaries. Models may classify documents, explain terms,
propose categories, summarize exceptions, or draft correspondence. Model
arithmetic is never authoritative when source values can be computed.

### Initial measures

- precision of high-value attention items;
- false-alarm and notification burden;
- exact-value and citation accuracy;
- detected versus missed obligations;
- time returned;
- cross-person and prohibited-action incidents; and
- accessible comprehension of uncertainty and household boundaries.

## Journey 3: Continuous home awareness, safety, and control

### Outcome

Unison observes authorized household systems continuously, recognizes
conditions that deserve attention, explains them without surveillance creep,
and performs only bounded, reversible control actions.

### Experience

The system can integrate selected environmental sensors, energy and water
meters, leak/smoke/air-quality devices, appliances, network state, maintenance
records, and home-automation systems. It learns normal operating envelopes
without treating every resident's activity as household property. It identifies
leaks, unsafe temperature or air conditions, failing equipment, unusual energy
use, open security boundaries, expiring maintenance, and degraded sensors.

Alerts identify the observation, confidence, affected area, urgency, suggested
response, and data used. Bounded actions such as stopping a supported water
valve or changing a thermostat require pre-established policy and expose
confirmation, cancellation, device state, and recovery. Safety-critical
behavior must not rely on a general-purpose model alone.

### Privacy and monitoring boundary

Continuous observation needs an explicit household sensor charter defining
purpose, placement, access, retention, inference, guests, children, private
rooms, microphones/cameras, law-enforcement requests, and deletion. Sensor data
does not automatically authorize behavioral profiling or entry into a person's
private memory.

### Modalities

- ambient audio, light, tactile, mobile, visual, sign, or Braille alerts;
- speech, switch, gesture, accessible control panel, or remote text input;
- personalized expression of the same shared safety state; and
- redundant alarm paths when one modality or network is unavailable.

### Initial measures

- detection latency, precision, and missed-event rate;
- safe behavior during network, sensor, model, and power failure;
- false-alarm and interruption burden;
- action reversibility and duplicate-action count;
- privacy-policy conformance and non-member/guest handling;
- sustained resource and energy cost; and
- accessible alarm recognition and response.

## Journey 4: Research, learning, and curriculum assistance

### Outcome

Several people can simultaneously research, learn, teach, and build curricula
with assistance adapted to their goals, prior understanding, accessibility
needs, and privacy choices.

### Experience

Unison decomposes questions, searches authorized local sources first, performs
privacy-governed external research when allowed, compares sources, cites claims,
marks uncertainty, and produces explanations or learning activities in an
appropriate form. It remembers reviewed learning goals, demonstrated mastery,
preferred pacing, accommodations, and corrections without turning engagement
or time-on-device into the objective.

For curriculum support it can map goals to a sequence, create accessible
materials, provide practice, assess specific skills, vary explanation style,
and show the learner or educator why it recommends the next activity. It must
distinguish evidence from generated examples and avoid silently importing
another household member's profile.

### Modalities

- conversational, visual, tactile, spatial, sign, Braille, switch/AAC, and
  document-based interaction where supported;
- equivalent access to equations, tables, charts, images, demonstrations, and
  feedback; and
- transitions between modalities without losing semantic position or progress.

### Deterministic and model roles

Search plans, source policy, citation binding, calculations, assessment scoring,
curriculum prerequisites, permissions, and durable progress records are
deterministic. Models may explain, synthesize, generate examples, translate
modalities, propose practice, and respond to open-ended questions. Unsupported
claims remain labeled and cannot enter durable knowledge as verified facts.

### Initial measures

- source and citation quality;
- factual and semantic equivalence across modalities;
- learning outcome rather than engagement;
- successful resumption over time;
- privacy leakage between learner profiles;
- interactive latency under concurrent household load; and
- educator/learner control and correction burden.

## Journey 5: Shared household coordination across privacy and modality boundaries

### Outcome

People with different private information, roles, languages, and interaction
modalities can reach shared understanding and coordinate action without
flattening their perspectives or exposing their private source material.

### Reference demonstration: blind and sighted household members

A blind person and a sighted person plan a household repair or shared event.
The sighted person may inspect a photo, diagram, calendar, or spatial layout;
the blind person may use speech and Braille. Unison creates one shared semantic
artifact containing the agreed facts, open questions, assignments, timing,
risks, and decisions. Each person receives a native expression suited to them:
a structured visual/spatial presentation for one and a navigable spoken or
Braille presentation for the other.

References such as “the valve below the left gauge” are resolved into stable
semantic identifiers and described spatially. Either person can ask what the
other currently understands, but Unison reports only the shared artifact—not
private notes, inferred feelings, unrelated context, or inaccessible raw media.
Corrections update the shared proposition with attribution and preserve prior
versions rather than rewriting another person's memory.

This pattern should later be tested with Deaf/speaking, sign/non-sign,
speech-disabled/speaking, cognitive-access, language, and remote/local
combinations. No single pairing stands in for all people or modalities.

### Deterministic and model roles

Deterministic services own membership, field-level disclosure, semantic IDs,
assignments, decisions, approvals, versioning, and modality-equivalence checks.
Models may describe visual or spatial material, interpret natural language or
sign input, summarize viewpoints, and propose clarifying language. Uncertainty
and perspective are preserved; a model cannot invent consensus.

### Initial measures

- shared-fact agreement and unresolved-question visibility;
- private-source leakage count;
- semantic equivalence across expressions;
- correction, disagreement, and withdrawal behavior;
- task completion without requiring one person to adopt another's modality;
- cognitive and interaction burden; and
- participatory assessment by people who use the relevant modalities.

## Journey 6: MacGyver resilience mode

### Outcome

When external internet, cloud services, or normal professional support are
unavailable, Unison provides useful offline guidance for immediate safety,
emergency stabilization, household utilities, maintenance, diagnosis, and
repair while clearly respecting the boundary between information and qualified
professional work.

“MacGyver mode” is the memorable product name. Internally, the architecture
should distinguish at least:

- **emergency stabilization:** immediate life, fire, gas, electrical, water,
  structural, environmental, or security risk;
- **safe shutdown and isolation:** stop escalation without attempting a repair;
- **assessment:** identify observations, uncertainty, tools, hazards, and when
  to stop;
- **maintenance and repair:** ordinary bounded guidance when conditions are
  safe; and
- **recovery:** document actions, inspect results, restore service, replenish
  supplies, and arrange qualified follow-up.

### Offline knowledge system

A fine-tuned local model may improve language, reasoning patterns, and
interaction, but safety-critical knowledge should not live only in model
weights. The preferred system combines:

- reviewed, versioned, locally stored emergency and repair sources;
- regional emergency numbers, household shutoff locations, equipment manuals,
  service history, building information, medical details authorized for the
  current person, and household emergency plans;
- deterministic hazard, contraindication, triage, tool, material, and stop
  rules;
- exact source citations and edition/effective dates;
- retrieval and device-specific procedures;
- a qualified local model for interpretation, dialogue, explanation, and
  adaptation; and
- a deterministic safe fallback when the model, source, sensor, or power state
  is uncertain.

The offline corpus and model are signed release components with update,
rollback, expiration, provenance, regional scope, and storage requirements.
Unison should warn when guidance may be stale without preventing access to the
best locally available emergency information.

### Emergency interaction

The system first identifies immediate hazards and whether emergency services
are reachable. It prioritizes escape, isolation, first aid, and qualified help
over completing a repair. It asks only questions that can change the safe next
step, provides one manageable step at a time, checks whether the step was
understood or completed, and offers hands-free, visual, sign, Braille, tactile,
or simplified-language expression as available.

If communication networks are available, it can prepare or initiate a bounded
emergency contact under pre-established policy. It must not delay emergency
services to continue questioning or create false confidence from an uncertain
model answer.

### Medical boundary

Offline guidance can provide recognized first-aid and emergency-stabilization
information, use person-authorized allergies, medications, conditions, and
emergency plans to surface reviewed contraindications, and help communicate
facts to responders. It cannot diagnose, prescribe, perform clinician-only
decision making, or represent model confidence as medical certainty.

### Utility and repair boundary

Gas, mains electricity, fire, pressurized systems, structural damage,
refrigerants, hazardous materials, generators, batteries, and contaminated
water require deterministic hazard classification. Guidance should prefer
shutoff, evacuation, lockout, verification, and qualified service whenever the
task exceeds the supported household skill and equipment profile.

### Resilience hardware implications

- local inference and complete local authority without WAN access;
- independently powered networking and selected sensors;
- graceful shutdown plus optional UPS-backed emergency runtime;
- offline manuals, maps, contacts, plans, and knowledge corpus;
- local speech and other required I/O without cloud dependencies;
- emergency status visible when normal surfaces fail;
- optional local peer/device communication during internet loss; and
- tested behavior under power, network, sensor, accelerator, and storage
  degradation.

### Initial measures

- correct hazard classification and stop/escalation behavior;
- harmful-instruction and false-confidence rate;
- source citation, freshness, and regional applicability;
- completion time for safe isolation or stabilization;
- usability under stress and across modalities;
- fully offline task success;
- degraded-power runtime and thermal behavior; and
- retention of an accurate, private incident record.

## Cross-domain intersection journeys

Unison's strongest differentiation may emerge where domains meet. Cross-domain
reasoning also creates the greatest privacy and authority risk. An intersection
is never authorized merely because Unison stores both domains. It requires a
named purpose, selected fields, current person authority, provenance, an
explanation of the relationship, and an inspectable result.

### Health choices under financial and insurance constraints

At a person's request, Unison combines an authorized care plan or health need
with selected insurance terms, deductible state, provider network, benefits,
transportation, schedule, caregiving, and budget constraints. It can identify
questions for a clinician or insurer, compare administrative options, surface
deadlines and assistance programs, estimate visibly uncertain out-of-pocket
ranges, and prepare calls or draft correspondence.

Clinical appropriateness must not be ranked by affordability alone. The system
does not select treatment, deny care, change coverage, or make binding financial
commitments. Health and finance stores remain separately encrypted; a bounded
cross-domain computation receives only approved fields and writes a derived
artifact with purpose, provenance, expiration, and sharing policy.

### Home environment and health

At a person's request, Unison can compare private symptom or accessibility
needs with selected household air quality, temperature, allergens, noise,
lighting, energy, and maintenance observations. It can surface correlations as
hypotheses, recommend measurements or questions, and propose safe household
changes. It cannot represent correlation as diagnosis or expose a person's
health condition to the household through an unexplained shared alert.

### Education, disability, health, and household schedule

Unison can adapt learning pace, modality, breaks, environment, and schedule
using information a learner or guardian is authorized to apply. It should
share accommodations and outcomes rather than diagnoses or private source
records unless explicitly selected.

### Household resilience under financial constraints

Unison can prioritize emergency supplies, maintenance, backup power, repairs,
and risk reduction using household budget, equipment condition, local hazards,
accessibility requirements, insurance terms, and likely service disruptions.
Recommendations expose safety benefit, cost range, urgency, dependencies, and
lower-cost alternatives without sponsorship or affiliate ranking.

### Shared care without collapsed privacy

A person can authorize a caregiver or household member to receive selected
tasks, warning signs, schedules, or emergency instructions without disclosing
the full health, finance, or communications archive. Unison tracks the exact
shared artifact, source fields, purpose, recipient, duration, corrections, and
revocation.

## Cross-domain computation contract

Every cross-domain result should record:

- requesting and approving person;
- exact purpose and time bound;
- source domains and selected fields;
- source revisions and freshness;
- deterministic computations and model/version contributions;
- uncertainties, alternatives, and excluded information;
- intended recipient and expression modality;
- whether the result is private, shared, or ephemeral;
- retention and revalidation policy; and
- available correction, revocation, deletion, and recovery actions.

General-purpose model runtimes should not receive unrestricted mounts of all
participating domains. The preferred mechanism is a short-lived, policy-created
view or capability containing the minimum approved facts. The derived result
does not silently become a new permanent cross-domain profile.

## Cross-journey system requirements

The six journeys collectively require:

- independent per-person and sensitive-domain keys and stores;
- source, relational, graph, event, exact-search, vector, working-memory, and
  archive layers with consistent provenance and deletion;
- fair concurrent scheduling with protected emergency and accessibility lanes;
- continuous workloads separated from interactive requests;
- signed skill, tool, model, knowledge-pack, and capability lifecycles;
- local-first and fully offline execution paths;
- privacy-governed external research and provider access;
- semantic continuity and equivalence across modalities;
- explicit shared understanding rather than implicit memory sharing;
- content-free security, reliability, power, and thermal monitoring;
- provider-blind off-prem backup and tested replacement recovery; and
- versioned evidence that distinguishes CI, simulation, physical hardware, and
  participatory validation.

## Recommended elaboration order

1. Journey 5 shared understanding, because it tests Unison's central person and
   modality model without requiring dangerous autonomy.
2. Journey 1 health preparation and Journey 2 financial attention as separate,
   read-only domains with strong provenance.
3. The health/finance/insurance intersection using short-lived authorized
   cross-domain views.
4. Journey 4 research and learning with privacy-preserving external egress and
   concurrent scheduling.
5. Journey 3 continuous home awareness using simulated sensors before physical
   control.
6. Journey 6 MacGyver resilience mode, beginning with curated offline sources,
   deterministic hazard rules, and safe-shutdown guidance before broader repair
   or emergency claims.

## Decisions to make next

1. Which two people and modality combination define the first shared-
   understanding demonstration?
2. What is the first concrete shared task: household repair, calendar/event,
   shopping, document review, navigation, or another outcome?
3. Which health, finance, and insurance sources are in the first synthetic
   cross-domain fixture?
4. Which regions and reviewed authorities define the first MacGyver emergency
   knowledge pack?
5. Which continuous sensors are acceptable for the first home-awareness proof,
   and which are explicitly excluded?
6. What response-time and offline-runtime targets should influence the interim
   GPU system and future hardware?
