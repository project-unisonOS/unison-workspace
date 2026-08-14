# DJ-1 shared incident implementation plan

Status: **DJ1-C0 complete; DJ1-C1 foundation published for review**  
Opened: 2026-08-14  
Prerequisites:

- [UNISON_DEMONSTRATION_JOURNEYS.md](UNISON_DEMONSTRATION_JOURNEYS.md)
- [DJ0_ARCHITECTURE_GAP_ANALYSIS.md](DJ0_ARCHITECTURE_GAP_ANALYSIS.md)
- [DJ0_CONTRACT_AND_FIXTURE_PLAN.md](DJ0_CONTRACT_AND_FIXTURE_PLAN.md)
- [UNISON_RESOLUTION_AND_SKILL_EVOLUTION.md](UNISON_RESOLUTION_AND_SKILL_EVOLUTION.md)

## Objective

Implement a deterministic, fully local simulation of the shared water-leak
incident for two independent people with equivalent visual and Braille/
conversational semantic expressions. Preserve an optional bounded local-model
path for novel questions and image/spatial proposals without making the model a
requirement or authority source.

## Contract review decisions

The DJ-0 candidates are resolved for initial implementation as follows:

| Candidate | Decision for DJ-1 | Rationale |
| --- | --- | --- |
| `sensor-observation.v1` | Create canonical contract | Generic event envelopes do not express freshness, sequence, confidence, integrity, unit, and device health together |
| `household-equipment.v1` | Extend life-operation `DomainRecord`; add a typed equipment view, not a second persistence authority | Household item/manual/procedure records already exist |
| `household-incident.v1` | Create canonical contract | Incident state, uncertainty, timeline, assignments, and retention need one shared semantic authority |
| `offline-knowledge-pack.v1` | Create canonical manifest contract | Reviewed offline procedures require region, version, freshness, digest, signature, hazards, and stop rules |
| `incident-assignment.v1` | Extend accepted workflow-step/commitment semantics | Assignment should not create a parallel task authority |
| `cross-domain-view.v1` | Defer runtime implementation to DJ-2; retain canonical candidate | Not needed for the water incident |
| `evidence-state.v1` | Create as a general provenance/evidence contract | Stale, conflicting, missing, and uncertain evidence applies beyond life operations |
| `cost-scenario.v1` | Defer to DJ-2 life operations | Health/insurance/finance-specific deterministic calculation |
| `derived-artifact-receipt.v1` | Extend accepted outcome evidence and derived-record provenance | Avoid another durable receipt authority |
| `journey-expression-expectation.v1` | Keep as workspace test fixture | It is acceptance evidence, not a runtime payload |

Two additional candidates are introduced by `AD-056`:

- `resolution-attempt.v1`: private attempt state, routes, budgets, partial
  outcomes, recovery, and content-free structural fingerprint;
- `determinization-candidate.v1`: non-executable repeated-pattern proposal,
  evidence, privacy classification, expected benefit, and review state.

DJ-1 should implement only the minimum `resolution-attempt.v1` fields needed to
preserve novel-question and fallback state. Determinization detection and
promotion remain a later slice after real repeated-request evidence exists.

## Repository sequence

### 1. `unison-common`: canonical contracts

Add strict versioned models and generated JSON Schemas for:

- sensor observation;
- evidence state;
- household incident and legal transitions;
- offline knowledge-pack manifest;
- workflow-compatible incident assignment; and
- minimal resolution attempt.

Add negative contract tests for extra fields, duplicate sequences, invalid
confidence, expired/future-invalid knowledge, illegal incident transitions,
unscoped assignments, executable physical action, private content in structural
fingerprints, and missing stop rules.

### 2. `unison-storage`: incident repository

Add restart-safe persistence for:

- one incident scoped to an explicit governed shared space;
- idempotent observation admission by sensor/sequence/event identity;
- accepted facts and separately attributed conflicting observations;
- timeline transitions and assignment receipts;
- selected incident media handles, never unrestricted camera directories;
- retention and closure cleanup; and
- private-source and unrelated-domain denial.

The repository consumes authenticated principal context and context-space
membership. It does not implement physical device control.

### 3. `unison-orchestrator`: deterministic incident engine

Implement:

- observation freshness/integrity gate;
- water-leak state machine;
- deterministic hazard/stop-rule evaluation;
- shared assignment and acknowledgement flow;
- no-model deterministic checklist path;
- minimal resolution-attempt state for novel questions;
- optional governed local-model route for language/spatial proposals;
- proposal reconciliation against selected equipment IDs and approved sources;
- replay/idempotency and cancellation/recovery; and
- emergency/accessibility priority class as an extension of the household
  scheduler.

The initial scheduler extension covers priority and starvation prevention only.
Accelerator, energy, and thermal admission remains a separate infrastructure
slice with the interim GPU system.

### 4. `unison-experience-renderer`: equivalent expressions

Implement native fixture-backed expressions for:

- incident detection and uncertainty;
- shared status and who was notified;
- assignment, acknowledgement, cancellation, and recovery;
- spatial/equipment description without color-only identification;
- stepwise offline guidance and stop conditions; and
- degraded sensor, model, Braille, display, network, and power states.

The first Braille path is a structured semantic representation suitable for a
future device adapter. It is not a physical Braille support claim.

### 5. `unison-workspace`: acceptance orchestration

Add a `test-dj1.sh` entrypoint that:

- validates DJ-0 fixtures;
- runs focused component contract and behavior tests;
- runs cross-person/privacy canaries;
- compares visual and Braille/conversational required semantics;
- injects duplicate, stale, reordered, unverifiable, stop-rule, no-model,
  modality-loss, and concurrency cases; and
- emits one simulation-labeled evidence package pinned to exact component
  commits.

## Incident state machine

```text
observed
  -> assessing
      -> action-needed
          -> isolating
              -> monitoring
                  -> recovered
                      -> closed
      -> monitoring
      -> escalated
          -> monitoring
          -> closed
  -> closed (false/invalid observation with recorded reason)
```

Any active state may move to `escalated` when a deterministic stop rule becomes
true. A model cannot create `recovered`, clear `escalated`, or skip monitoring.
Closure requires a deterministic reason and final source state.

## Natural resolution behavior

Known incident questions use deterministic facts and procedures. Novel
questions follow the resolution ladder:

1. retrieve approved equipment and knowledge sources;
2. compose available tools and deterministic facts;
3. use an eligible local model for bounded interpretation or explanation;
4. reconcile every material proposal against sources, authority, hazards, and
   current state;
5. ask one route-changing clarification when necessary;
6. provide a partial answer, safe stop, or handoff when completion is not
   possible; and
7. preserve a private resumable attempt plus a content-free structural
   fingerprint.

Example novel requests in DJ-1 fixtures should include:

- “Could the water be coming from the appliance next to the valve?”
- “Explain why we are waiting before calling this recovered.”
- “What can I safely check if the sensor stops responding?”
- “Give Jordan the visual details and give me only what I need in Braille.”

The system must not respond as though only prewritten commands are supported.
It also must not infer a leak source, safety state, or physical action without
evidence.

## Implementation gates

### DJ1-C0: Contracts

- canonical contracts and schemas pass strict positive/negative tests;
- state transitions and stop rules are deterministic;
- resolution fingerprints contain no request content; and
- no contract grants physical actuation.

### DJ1-C1: Repository and engine

- explicit membership and person binding pass;
- replay/reorder/stale/integrity cases fail or degrade correctly;
- no-model primary flow completes;
- hazardous cases always escalate; and
- restart preserves incident and assignment state.

### DJ1-C2: Expressions

- required facts, uncertainty, provenance, actions, cancellation, and recovery
  are equivalent across visual and Braille/conversational expressions;
- modality loss retains semantic position and available actions;
- no private or unselected media canary appears; and
- expression remains natural for novel questions in synthetic evaluation.

### DJ1-C3: Workspace simulation

- all twelve applicable DJ-0 gates pass;
- emergency/accessibility work is not starved by background load;
- exact component commits and commands are recorded;
- evidence is labeled simulation; and
- physical and participatory claims remain explicitly open.

## Branch and review strategy

Use one component branch per repository with the prefix
`agent/dj1-shared-incident`. Publish component draft PRs in dependency order.
Update the workspace gitlinks only after each component candidate is pushed and
its focused checks pass. The workspace PR remains the cross-repository review
and evidence index.

Do not mix the existing NUC branches `rocky/journey6-validation` or
`rocky/tranche-bc-checkpoint` into DJ-1. Use clean worktrees to preserve that
work.

## First authorized implementation chunk

Begin with `unison-common` contract models and tests only. Stop before storage
or runtime changes if contract tests expose ambiguity in incident assignment,
knowledge-pack signing, or resolution privacy. This creates a small reviewable
dependency for every later slice.

## Progress record

### 2026-08-14: Contract candidate published

- Component: `unison-common`
- Commit: `8ef6b99` (`Add shared incident contracts`)
- Review: `project-unisonOS/unison-common#25` (draft)
- Environment: clean NUC worktree, Ubuntu, Python 3.12.3
- Focused result: 8 passed
- Adjacent contract result: 24 passed across shared incident, life operations,
  semantic experience, semantic runtime, and model runtime suites

Implemented strict models for sensor observations, general evidence state,
typed household equipment views, signed offline knowledge-pack structure,
workflow-bound incident assignments, legal incident transitions, deterministic
escalation, physical-actuation prohibition, natural resolution budgets, useful
partial outcomes, and content-free structural fingerprints.

### 2026-08-14: Repository foundation published

- Component: `unison-storage`
- Commit: `cc82810` (`Add restart-safe shared incident repository`)
- Review: `project-unisonOS/unison-storage#23` (draft)
- Environment: clean NUC worktree, Ubuntu, Python 3.12.3
- Full component result: 35 passed

Implemented encrypted atomic restart persistence, shared-space authorization,
idempotent sensor/sequence admission, stale and integrity rejection,
append-only incident history, household-member assignment checks, opaque
selected-media handles, and delete-at-close cleanup. HTTP integration and
separately attributed conflict presentation remain later DJ1-C1 work.

### 2026-08-14: Deterministic engine foundation published

- Component: `unison-orchestrator`
- Commit: `986aab3` (`Add deterministic shared incident orchestration`)
- Review: `project-unisonOS/unison-orchestrator#33` (draft)
- Environment: paired clean NUC worktrees, Ubuntu, Python 3.12.3
- Full component result: 241 passed with the repository's CI auth bypass

Implemented deterministic water-leak assessment, freshness and integrity
gates, electrical hazard escalation, manual no-actuation assignments, offline
checklists, partial/blocked no-model resolution attempts, and emergency through
background scheduler priority lanes. A governed optional model route,
equipment proposal reconciliation, assignment acknowledgement endpoints, and
end-to-end storage integration remain later DJ1-C1 work.
