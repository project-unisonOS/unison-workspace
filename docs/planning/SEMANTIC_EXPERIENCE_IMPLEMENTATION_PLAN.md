# Semantic experience implementation plan

Status: **Proposed execution plan; implementation not started**  
Last updated: 2026-07-25  
Design authority: [SEMANTIC_EXPERIENCE_DESIGN.md](SEMANTIC_EXPERIENCE_DESIGN.md)

## Objective

Implement a semantic-first experience system that can natively compose
conversational, visual, tactile, sign, and combined experiences around each
person's needs and context. Add governed translation of existing visual
experiences without making screen-reader behavior the primary Unison model.

This program is divided into slices `SE0` through `SE7` so it can proceed within
the broader Phase 8 multimodal program without reusing completed project phase
numbers. Each slice requires evidence before the next slice can claim its
behavior.

## Program invariants

- SEM is the authoritative meaning contract; modality output is derived.
- Input and output modalities are selected independently.
- The interaction profile is private, person-owned, inspectable, and reversible.
- Native composers do not serialize another modality's presentation.
- Consequential actions remain bound to existing policy, consent, confirmation,
  disclosure, audit, and capability controls.
- Legacy content is untrusted and cannot grant authority.
- Simulation can establish software behavior but cannot close a hardware or
  disabled-person validation gate.
- Public claims follow evidence and are updated in the same slice that earns
  them.

## Dependency sequence

```text
SE0 decisions and baseline
          |
          v
SE1 semantic contracts
          |
          +------------------+
          |                  |
          v                  v
SE2 interaction profile   SE3 native composers
          |                  |
          +--------+---------+
                   v
          SE4 modality planner
                   |
          +--------+---------+
          |                  |
          v                  v
SE5 continuity/equivalence  SE6 legacy interpreter
          |                  |
          +--------+---------+
                   v
          SE7 qualification and messaging
```

## SE0: Decisions, inventory, and measurable baseline

### Deliverables

- Accept the semantic-first and native-composition architecture decisions.
- Inventory current response, renderer, speech, Braille, sign, vision,
  switch/AAC, haptic, VDI, browser, preference, policy, and audit contracts.
- Identify every path that derives output solely from input modality, mirrors
  visual focus, or treats screen-reader compatibility as the final experience.
- Define representative synthetic journeys:
  - calendar conflict and rescheduling;
  - comparison table and trend chart;
  - bill review and payment proposal;
  - privacy-sensitive confirmation;
  - website form completion;
  - recovery from modality or device loss.
- Capture current comprehension, completion, interruption, error recovery,
  latency, and semantic-loss baselines.

### Acceptance

- Inventory accounts for every active output path and canonical contract copy.
- Journey fixtures contain no personal data and identify required meaning,
  actions, risk, provenance, and recovery.
- Known screen-reader and visual-first dependencies are recorded as migration
  work rather than silently retained.

## SE1: Semantic Experience Model v1

### Deliverables

- Add canonical versioned SEM schemas to `unison-common/schemas` and generate
  language bindings.
- Model outcomes, entities, relationships, groups, sequences, comparisons,
  trends, spatial meaning, actions, confirmation, recovery, provenance,
  uncertainty, privacy, and attention.
- Give semantic nodes and actions stable identifiers.
- Define summarization and exact-preservation constraints.
- Extend capability results and orchestration to produce SEM.
- Provide a ROM compatibility adapter during migration; prevent new features
  from adding presentation-only meaning to ROM metadata.
- Add schema drift, serialization, migration, malformed-input, and adversarial
  metadata tests.

### Acceptance

- Every SE0 journey can be represented without visual-control vocabulary.
- The same SEM can drive at least two independent test expressions.
- Unknown fields and invalid action bindings fail according to the versioning
  and compatibility policy.
- Policy, provenance, recipient, disclosure, and confirmation data survive
  round trips unchanged.

## SE2: Governed personal interaction profile

### Deliverables

- Define a versioned interaction-profile contract with durable preferences,
  needs, device associations, situational overrides, learned adaptations, and
  provenance.
- Store profiles in each person's governed private context and key domain.
- Add conversational inspect, propose, approve, correct, reset, export, and
  delete flows.
- Distinguish explicit choices, observed preferences, inferred adaptations, and
  temporary context.
- Add confidence, expiry, reversibility, and disclosure-minimization rules.
- Migrate applicable renderer and speech preferences without inventing values.

### Acceptance

- Cross-person and household-administrator reads fail without revealing whether
  a private preference exists.
- A person can understand and reverse every learned adaptation.
- Temporary overrides expire and restore durable preferences correctly.
- A fresh-device restore preserves approved profile state and provenance.

## SE3: Native expression composers

### Deliverables

- Build a conversational composer over SEM with summaries, progressive detail,
  stable references, interruption, resumption, confirmation, and recovery.
- Refactor the visual composer to consume SEM rather than text/card assumptions.
- Build a Braille composer over semantic structure rather than visual focus.
- Define composer SDK and conformance tests for sign, haptic, switch/AAC, and
  future adapters.
- Separate semantic composition from ASR, TTS, display, and device transport.
- Preserve captions as a coherent alternate expression of spoken content.

### Acceptance

- Conversational and visual composers independently complete all native SE0
  journeys from the same SEM.
- Conversation supports “more detail,” relative references, interruption,
  correction, cancellation, and resumption without visual state.
- Braille simulation navigates semantic groups and actions without renderer
  focus text.
- Composer failures return an explicit fallback plan and never omit required
  safety or confirmation content.

## SE4: Person-aware experience and modality planner

### Deliverables

- Replace `renderer`/`voice`/`both` routing with a versioned expression plan.
- Combine interaction profile, live capability reports, environment, privacy,
  content structure, risk, latency, resources, and explicit choice.
- Select input and output independently and support multiple coherent outputs.
- Add shared-room, bystander, quiet-mode, offline, degraded-device, and
  sensitive-content rules.
- Explain material modality decisions and allow immediate conversational
  override.
- Keep deterministic safety constraints outside model discretion.

### Acceptance

- Tests demonstrate voice input with non-voice output and keyboard input with
  conversational output.
- A missing or failed modality triggers the correct fallback without losing a
  pending action.
- Sensitive content is not spoken or displayed when situational policy forbids
  it.
- Planner decisions are reproducible from recorded inputs and produce an
  understandable audit explanation.

## SE5: Cross-modal continuity and equivalence

### Deliverables

- Add a modality-neutral interaction session that tracks semantic focus,
  dialogue references, pending actions, confirmations, progress, and recovery.
- Define and automate the modality equivalence contract from the design.
- Support mid-turn and mid-workflow changes among implemented modalities.
- Add semantic-diff tooling that detects omitted meaning, unavailable actions,
  altered risk, or lost provenance across expressions.
- Add interruption, reconnect, restart, and replacement-device cases.

### Acceptance

- Every SE0 journey can switch between conversational and visual expressions
  without restarting or losing semantic focus.
- Required meaning and operations pass automated equivalence checks.
- Confirmation cannot be replayed, transferred between people, or weakened by
  changing modality.
- Failure and recovery remain understandable in every qualified expression.

## SE6: Existing-experience interpreter

### Deliverables

- Define provenance-bearing observations for APIs, documents, accessibility
  trees, computer-use state, and vision analysis.
- Build an interpreter that reconciles those observations into SEM with
  confidence and ambiguity.
- Prefer structured sources and use vision only where it adds missing meaning.
- Bind semantic actions to authenticated capability targets and revalidate state
  immediately before consequential action.
- Add conversational exploration of documents, forms, tables, charts, images,
  and spatial layouts.
- Detect stale pages, moving targets, prompt injection, deceptive controls,
  conflicting sources, and inaccessible content.

### Acceptance

- Synthetic website, document, and desktop fixtures complete through
  conversation without exposing control labels or coordinates to the person.
- Table, chart, image, form, error, and confirmation meaning meets the
  equivalence contract.
- Untrusted page content cannot change policy, recipients, confirmation, or
  capability authority.
- Ambiguous or stale targets stop before consequential action and produce an
  understandable recovery path.

## SE7: Qualification, real-person validation, and truthful publication

### Deliverables

- Run complete security, privacy, recovery, performance, offline, and resource
  contention suites.
- Conduct participatory testing with people who use conversational, Braille,
  low-vision, switch/AAC, sign, and other prioritized interaction modes.
- Validate representative microphones, speakers, Braille displays, cameras,
  switches, and appliance profiles.
- Publish supported device/modality matrices, limitations, and evidence.
- Update architecture, developer, release, status, ecosystem, accessibility,
  multimodal, renderer, and homepage documentation.
- Replace screen-reader-centered public messaging only for behavior supported by
  accepted evidence.

### Acceptance

- Representative participants can understand, inspect, act, confirm, cancel,
  recover, and switch modality across the qualified journeys.
- No critical semantic-loss, privacy, authority, or inaccessible-recovery issue
  remains open.
- Latency and resource budgets pass on supported hardware.
- Every public claim maps to a supported slice, compatibility record, and
  acceptance artifact.

## Hardware and participatory validation backlog

The following work can be designed, implemented, simulated, and continuously
tested without physical hardware, but cannot be marked supported until later
validation:

| ID | Validation item | Earliest slice | Closure evidence |
| --- | --- | --- | --- |
| SE-HW-01 | Microphone, speaker, echo cancellation, TTS interruption, and reconnect matrix | SE3 | Qualified device runs and spoken-journey evidence |
| SE-HW-02 | Refreshable Braille discovery, input, tactile navigation, reconnect, and first-run recovery | SE3 | Representative devices plus Braille-user review |
| SE-HW-03 | Switch/AAC discovery, timing, scanning, cancellation, and recovery | SE3 | Representative devices plus switch/AAC-user review |
| SE-HW-04 | Camera description, chart/image interpretation, privacy indicators, lighting, and reconnect | SE6 | Camera matrix and participatory validation |
| SE-HW-05 | Sign capture and expression quality under realistic camera, lighting, occlusion, and latency | SE6 | Signer-led acceptance on supported hardware |
| SE-HW-06 | Haptic timing and distinguishability | SE3 | Device matrix and participant evidence |
| SE-HW-07 | Appliance CPU, GPU, RAM, thermals, and latency under simultaneous composition and local models | SE7 | Supported-hardware performance report |
| SE-HW-08 | Cross-device modality handoff and replacement-device restore | SE5 | Multi-device and clean-restore evidence |

These items remain visible in phase status and release documentation. Simulation
evidence must never be presented as physical-device or lived-experience proof.

## Cross-repository work map

- `unison-common`: SEM, expression-plan, interaction-profile, observation, and
  equivalence contracts.
- `unison-orchestrator`: SEM construction, modality planning, dialogue/session
  continuity, safety binding, and audit.
- `unison-context`: governed profile storage, provenance, learning, reset,
  export, and deletion.
- `unison-experience-renderer`: SEM-aware visual composition, expression
  dispatch, continuity, and fallback.
- `unison-io-speech`: conversational transport, ASR/TTS, interruption, pacing,
  and device capability reporting.
- `unison-io-braille`, sign, vision, BCI, haptic, and switch/AAC adapters: native
  composer/transport contracts and device reports.
- `unison-capability`: legacy-observation and semantic-action interfaces,
  sandboxing, target revalidation, and adversarial-content boundaries.
- VDI/browser/computer-use components: structured state extraction,
  accessibility-tree capture, visual observation, and stable action targets.
- `unison-workspace`: integration fixtures, equivalence gates, hardware backlog,
  evidence, and coordinated pins.
- GitHub Pages: evidence-matched public explanation after SE7 acceptance.

## Required evidence package per slice

Each slice publishes:

- versioned contract and migration notes;
- unit, integration, negative-security, privacy, accessibility, recovery, and
  performance results appropriate to the slice;
- a semantic-equivalence report for affected journeys;
- current-state, architecture decision, threat-model, status, and compatibility
  updates;
- unresolved software, hardware, and participatory-validation items;
- exact public claim changes, or an explicit statement that public messaging
  remains unchanged.

