# Unison demonstration journeys

Status: **Proposed executable specifications; not implementation or safety claims**  
Opened: 2026-08-14  
Derived from: [UNISON_REFERENCE_JOURNEYS.md](UNISON_REFERENCE_JOURNEYS.md)

## Purpose

These demonstrations turn the reference journeys into bounded, testable product
slices. They are selected to expose Unison's differentiators—local context,
person-level privacy, deterministic orchestration, bounded models, shared
understanding, multimodal expression, and safe cross-domain reasoning—without
starting with autonomous high-risk actions.

## Demonstration A: Shared response to a simulated household water leak

### Product question

Can a blind household member and a sighted household member understand the same
developing household problem, coordinate safely through different modalities,
and use local offline guidance without exposing unrelated private context?

### Scope

The first version is a simulation using fixtures. It does not operate a real
valve, make a plumbing diagnosis, or claim emergency certification. A later
hardware-in-the-loop version may use a low-voltage leak sensor and a
non-pressurized demonstration valve before any residential installation.

### Actors

- **Alex:** blind household member; primary output is speech and refreshable
  Braille; input is speech, keyboard, or Braille controls.
- **Jordan:** sighted household member; primary output is a visual mobile or
  desktop surface; input is touch, camera, text, or speech.
- **Unison household coordinator:** may use only the explicit shared incident
  space and approved household equipment records.
- **MacGyver resilience service:** supplies reviewed offline safety, isolation,
  and equipment guidance without gaining general household authority.
- **Simulated sensor:** emits normal, leak-detected, uncertain, offline, and
  recovered states.

The names are synthetic fixture identities, not assumptions about eventual
users.

### Authorized information

- shared location names needed for the incident;
- synthetic leak-sensor state and provenance;
- shared shutoff-valve location and an approved photo/diagram;
- reviewed local water-isolation instructions;
- a shared household emergency contact;
- explicit task assignments, acknowledgements, and incident timeline; and
- each person's interaction profile, visible only as needed to compose that
  person's expression.

### Information excluded

- either person's private conversations, health, finance, browsing, or
  unrelated schedule;
- inferred disability details beyond the governed interaction profile;
- camera content outside the selected incident capture;
- continuous audio or video recording;
- precise household location in external calls unless explicitly approved; and
- control of a real utility or valve in the initial demonstration.

### Preconditions

1. Alex and Jordan have independent authenticated principals.
2. Both have accepted membership in a shared household incident space.
3. Each has a reversible interaction profile and tested fallback modality.
4. The synthetic sensor and equipment records have stable identifiers.
5. The offline water-safety pack is signed, versioned, and available.
6. No internet, remote model, or cloud speech service is required.
7. The system clock, local audit, and emergency-lane scheduler are healthy.

### Primary flow

1. The simulated sensor reports a probable leak with time, location, confidence,
   and device health.
2. Deterministic rules classify the event as requiring prompt inspection but
   not yet proving flooding or structural danger.
3. Unison creates a shared incident artifact and alerts both people through
   their selected modalities.
4. Alex hears and reads in Braille: the location, confidence, immediate safe
   action, what remains unknown, and who else was notified.
5. Jordan sees the same semantic content plus the selected equipment diagram.
6. Jordan chooses to inspect and submits a bounded camera image of the valve
   area. The image remains incident-scoped.
7. A local vision model proposes object and spatial relationships. Deterministic
   validation binds only approved equipment identifiers and marks uncertainty.
8. Unison expresses the shared result visually for Jordan and spatially in
   speech/Braille for Alex, for example by stable component name and relative
   position rather than color alone.
9. Alex asks what Jordan has confirmed. Unison reports the shared observations,
   not Jordan's private notes or the raw image unless it was explicitly shared.
10. The reviewed offline pack provides a bounded safe-isolation checklist. The
    system presents one step at a time and includes stop conditions.
11. Jordan records a simulated manual shutoff; Alex acknowledges the shared
    state. No physical action occurs.
12. The sensor transitions to dry/recovered. Unison waits for a configured
    observation interval before declaring the simulated condition stable.
13. Unison creates a cited incident summary, follow-up inspection task, and
    reminder to restore service only after confirmation.

### Alternative and failure flows

- **Sensor uncertainty:** request observation; do not assert a leak.
- **Sensor offline:** label loss of visibility; preserve last observation and
  recommend bounded manual checks.
- **Local model unavailable:** use deterministic component names, equipment
  record, and textual checklist without image interpretation.
- **Conflicting observations:** preserve both with attribution; do not invent
  consensus.
- **Alex's Braille display unavailable:** fall back to local speech and keyboard
  navigation without losing semantic position.
- **Jordan's display unavailable:** offer local speech or text on another
  authenticated device.
- **Internet unavailable:** no functional loss for the simulated core flow.
- **Power constrained:** emergency lane preempts research or batch workloads;
  reduced local models and essential I/O remain available.
- **Unsafe evidence:** if the fixture indicates contaminated water, electrical
  contact, structural damage, or an inaccessible shutoff, stop repair guidance
  and present reviewed escalation instructions.
- **Unauthorized household member:** reveal neither incident details nor the
  existence of private notes; apply the explicit shared-space policy.

### Deterministic responsibilities

- authentication, membership, and disclosure;
- sensor integrity, freshness, and state machine;
- hazard and stop-rule classification;
- semantic incident identifiers and event ordering;
- task assignment and acknowledgement;
- modality-equivalence requirements;
- equipment-record lookup and exact checklist steps;
- cancellation, incident closure, retention, and audit; and
- resource priority and degraded-mode selection.

### Bounded model responsibilities

- interpret the selected image;
- propose spatial relationships with confidence;
- understand flexible natural-language questions;
- phrase explanations appropriate to each person; and
- summarize the completed incident from accepted facts.

Model output cannot classify the event as safe, authorize a physical action,
change membership, broaden camera access, or remove a stop condition.

### Fixture package

- two synthetic people and interaction profiles;
- household incident-space membership records;
- leak sensor event sequences, including noisy and adversarial cases;
- equipment registry with valve identifiers and synthetic manuals;
- selected valve-area images and descriptions;
- signed offline water-safety pack;
- expected semantic incident artifacts;
- expected visual, speech, and Braille expressions;
- cross-person and unrelated-data canaries; and
- power/network/model failure schedules.

### Acceptance gate

- both people receive semantically equivalent facts, uncertainty, actions,
  cancellation, and recovery;
- the task completes without requiring either person to use the other's
  modality;
- no unrelated private or camera data enters the shared artifact;
- every factual and safety instruction has provenance;
- unsafe fixture variants always stop or escalate;
- model loss preserves a useful deterministic offline path;
- duplicate or reordered events do not create duplicate actions;
- the emergency workload is not starved under simulated concurrent load;
- corrections and disagreement remain attributed and inspectable; and
- automated results are labeled simulation until representative people and
  physical fixtures validate the experience.

## Demonstration B: Health preparation under financial and insurance constraints

### Product question

Can Unison help a person prepare for a health decision and the surrounding
administrative reality using private health, financial, insurance, schedule,
transportation, and accessibility information without collapsing those domains
or making clinical and financial decisions for the person?

### Scope

The initial demonstration uses a fully synthetic person, records, insurance
plan, claims, finances, appointments, transportation options, and provider
directory. It prepares questions and administrative options for an upcoming
specialist visit. It does not diagnose, rank treatments, determine clinical
necessity, guarantee coverage, move money, submit claims, or contact a provider
or insurer.

### Actor

**Morgan** is a synthetic person with low vision and a chronic health condition.
Morgan has an upcoming specialist appointment, an incomplete referral,
uncertain network status, a deductible balance, limited discretionary funds,
transportation constraints, and a preference for concise speech plus
high-contrast structured text.

These attributes exist only to exercise the system. They are not a template for
profiling real people.

### Source compartments

- **Health:** synthetic clinical documents, medication list, referrals,
  appointment purpose, person observations, and questions.
- **Insurance:** plan document, network directory snapshot, explanation of
  benefits, deductible state, authorization rules, and contact channels.
- **Finance:** selected budget range and upcoming obligations; no unrestricted
  transaction history is required.
- **Schedule and transportation:** selected calendar availability, travel time,
  accessible transport options, and support-person availability.
- **Interaction profile:** Morgan's selected expression and navigation needs.

Each compartment remains independently authorized and encrypted. The
demonstration creates a short-lived cross-domain view containing only the
approved fields needed for the stated purpose.

### Primary flow

1. Morgan asks: “Help me get ready for this appointment and understand what I
   need to verify so the visit doesn't create a bill I cannot handle.”
2. Unison identifies two linked but distinct outcomes: clinically useful visit
   preparation and administrative/financial verification.
3. It shows the exact domains and fields proposed for the temporary analysis.
   Morgan can remove finance, insurance, transportation, or other fields and
   still receive a reduced result.
4. Deterministic services verify source dates, parse exact plan terms and
   amounts, calculate the synthetic deductible position, and identify missing
   referral/network/authorization evidence.
5. Models may summarize the health timeline, explain insurance language, and
   propose questions, but every material claim links to a source and retains
   uncertainty.
6. Unison creates separate sections:
   - health priorities and questions for the clinician;
   - documents and medication information to verify;
   - insurance questions and unresolved coverage facts;
   - visibly uncertain cost scenarios based on selected source values;
   - schedule, transport, and accessibility preparation; and
   - deadlines and reversible next steps.
7. Unison highlights that affordability does not determine clinical
   appropriateness and that only the clinician/insurer can resolve specified
   uncertainties.
8. Morgan reviews the result through concise speech and high-contrast text,
   corrects one source fact, and sees all affected conclusions recomputed.
9. Morgan creates two private artifacts: a clinician question list and an
   insurer call checklist. Neither is sent.
10. The temporary cross-domain view expires. The artifacts retain selected
    citations and purpose but do not create a general combined health-finance
    profile.

### Alternative and failure flows

- **Stale network directory:** label it stale and create a verification
  question; do not assert in-network status.
- **Conflicting plan documents:** preserve conflict and request authoritative
  confirmation.
- **Missing finance permission:** omit affordability calculations while keeping
  clinical and insurance preparation useful.
- **Model unavailable:** use deterministic source extraction, plan rules,
  calculations, templates, and checklists.
- **Remote provider proposed:** require a local-alternative result, minimized
  field preview, and explicit disclosure; the baseline remains fully local.
- **Coverage uncertainty:** show scenarios rather than a guaranteed price.
- **Urgent symptom language:** interrupt administrative planning and present the
  reviewed urgent-help path without diagnosing.
- **Another household member requests the result:** deny unless Morgan shares a
  selected artifact through an explicit context space.
- **Correction or deletion:** recompute affected derived results and remove the
  temporary view and relevant indexes according to policy.

### Deterministic responsibilities

- identity, domain authorization, and temporary-view construction;
- source freshness, exact amounts, dates, arithmetic, plan-rule parsing, and
  scenario calculation;
- citation and provenance binding;
- urgent-language and prohibited-action rules;
- disclosure, artifact sharing, expiration, correction, and deletion; and
- exact separation of clinician, insurer, and personal questions.

### Bounded model responsibilities

- extract candidate concepts from synthetic documents;
- summarize the authorized health timeline;
- explain complex administrative language;
- propose questions and organize the preparation brief; and
- adapt expression without changing exact values or uncertainty.

Models cannot diagnose, rank treatment by affordability, guarantee coverage,
authorize disclosure, calculate authoritative amounts, or create a durable
combined profile.

### Fixture package

- one synthetic person and interaction profile;
- synthetic clinical notes, medications, referral, and appointment;
- synthetic plan, directory, EOB, deductible, and authorization rules;
- bounded synthetic budget and obligation data;
- schedule, transportation, and accessibility constraints;
- stale, contradictory, incomplete, and adversarial document variants;
- expected calculations, citations, questions, and uncertainty labels;
- cross-domain, cross-person, secret, and unsupported-claim canaries; and
- expected speech and high-contrast semantic expressions.

### Acceptance gate

- no domain is accessed before field-level purpose approval;
- removal of any optional domain produces a valid reduced result;
- every material health, coverage, and financial statement cites a source;
- exact arithmetic is deterministic and model-independent;
- stale, conflicting, or incomplete data never becomes certainty;
- affordability never becomes a clinical recommendation;
- no prohibited clinical, financial, claim, contact, or disclosure action
  occurs;
- the temporary cross-domain view expires and is deletable;
- corrections deterministically invalidate and recompute derived claims;
- private artifacts remain private until Morgan explicitly shares them; and
- speech and high-contrast expressions preserve facts, uncertainty, actions,
  and recovery equivalently.

## Shared implementation primitives

The demonstrations should reuse the same platform primitives rather than create
journey-specific authority:

- signed `PrincipalContext` and authenticated workload identity;
- governed private and shared context spaces;
- per-person/per-domain key and storage handles;
- immutable sources plus relational facts and derived indexes;
- provenance, freshness, correction, deletion, and retention;
- short-lived purpose-bound cross-domain views;
- Semantic Experience Model and modality composers;
- typed plans, skills, tools, capabilities, approvals, and receipts;
- deterministic model eligibility and local-first routing;
- signed offline knowledge packs;
- fair scheduler with emergency/accessibility lanes; and
- content-free audit, security, performance, energy, and thermal evidence.

## Proposed delivery sequence

### DJ-0: Contract and fixture lock

- select canonical schemas and identify reuse versus required extensions;
- create synthetic identities, data, sensor, equipment, knowledge, and expected
  semantic fixtures;
- write threat, privacy, accessibility, and prohibited-action matrices;
- define measurable baselines and simulation truth labels; and
- decide exact repositories before implementation begins.

Exit: fixtures and contracts can be reviewed without running a model.

The source-backed reuse and gap decisions for this slice are recorded in
[DJ0_ARCHITECTURE_GAP_ANALYSIS.md](DJ0_ARCHITECTURE_GAP_ANALYSIS.md).

### DJ-1: Shared incident simulation

- implement the deterministic incident state machine and shared artifact;
- render equivalent visual, speech-text, and Braille-structured expressions;
- add model-independent water-isolation guidance;
- exercise sensor, network, model, concurrency, and modality failures; and
- add image interpretation only after the deterministic path passes.

Exit: Demonstration A passes its simulation gate without real physical control.

### DJ-2: Cross-domain preparation simulation

- implement short-lived selected-field views;
- add exact plan, date, and cost-scenario calculations;
- produce cited clinician and insurer checklists;
- verify correction, expiry, deletion, and reduced-domain behavior; and
- add bounded local-model summaries after deterministic outputs pass.

Exit: Demonstration B passes its synthetic privacy and safety gate.

### DJ-3: Physical and participatory expansion

- use a low-voltage non-pressurized water fixture and instrumented test sensor;
- validate with blind and sighted participants through an approved research
  protocol;
- measure latency, comprehension, workload, privacy, power, and failures;
- revise before considering household plumbing integration; and
- conduct separate representative research for health/insurance expression.

Exit: revision-bound evidence exists; no supported-product claim is automatic.
