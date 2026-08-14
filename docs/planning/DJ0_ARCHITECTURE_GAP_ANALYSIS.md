# DJ-0 architecture gap analysis

Status: **Verified source audit for contract planning; not implementation acceptance**  
Audit date: 2026-08-14  
Workspace revision at audit start: `4e1dd04` with pinned submodules

## Purpose

This analysis maps the two proposed demonstration journeys to code, contracts,
tests, and deployment assets in the current multi-repository workspace. Source
and executable tests were treated as evidence; planning prose alone was not.

Disposition vocabulary:

- **Reuse:** sufficient canonical foundation; consume without creating a new
  authority path.
- **Extend:** preserve the existing contract or service and add bounded fields
  or behavior.
- **New:** no suitable implementation was found.
- **Consolidate:** overlapping behavior exists and needs one canonical owner.
- **Defer:** not needed for the DJ-0 through DJ-2 simulation gates.

## Executive result

The demonstrations should be built as extensions of the accepted architecture,
not as a parallel prototype. Most trust and semantic primitives already exist.
DJ-0 requires new model-independent contracts and fixtures, but it does not
justify a repository migration yet.

The strongest implemented foundations are:

- signed principal context and service middleware;
- explicit private/shared governed context spaces;
- life-operation source, derived-record, domain-record, cross-domain-link,
  safety, brief, draft, and pilot contracts;
- encrypted restart-safe life-domain storage with health, finance, household,
  insurance, and cross-domain behavior;
- Semantic Experience Model, expressions, interaction profiles, and
  modality-independent session planning;
- typed task plans, exact approvals, recoverable execution, and outcomes;
- privacy-, risk-, hardware-, cost-, and offline-aware model routing;
- fair per-assistant CPU/memory/concurrency scheduling;
- provider-blind per-scope backup and recovery; and
- deterministic urgent-health rules and prohibited health/finance actions.

The largest gaps are:

- canonical household incident, sensor observation, equipment, and incident
  timeline contracts;
- signed, region/version/freshness-aware offline knowledge packs;
- explicit emergency/accessibility scheduling lanes and accelerator/energy/
  thermal admission;
- expiring selected-field cross-domain views with materialized-view deletion
  and recomputation receipts;
- deterministic insurance-plan, deductible, network, referral, authorization,
  transportation, and cost-scenario contracts;
- a production Braille composer/device adapter and physical modality evidence;
- purpose-bound selected camera capture and image-to-equipment binding; and
- complete DJ-specific threat, privacy, accessibility, and failure fixtures.

## Cross-cutting mapping

| Requirement | Disposition | Current owner and evidence | Required DJ extension |
| --- | --- | --- | --- |
| Authenticated person/workload | Reuse | `unison-common/src/unison_common/principal.py`; middleware tests in `unison-common/tests/test_principal*.py` | Add only fixture principals and negative cases |
| Independent private/shared spaces | Reuse | `unison-common/src/unison_common/governed_context.py`; `unison-context/src/governed_repository.py`; Phase 2/4 tests | Add incident-space fixture and exact membership cases |
| Interaction preferences | Reuse | `unison-common/.../interaction_profile.py`; `unison-context/src/interaction_profiles.py` | Add Alex/Jordan/Morgan profiles and fallback cases |
| Semantic experience | Extend | `unison-common/.../semantic_experience.py`; orchestrator semantic runtime; renderer composers/tests | Define DJ semantic node conventions for incident, uncertainty, assignments, citations, and cross-domain sections |
| Modality planning | Extend | `semantic_runtime.py`; `test_semantic_runtime_se4_se6.py`; browser composers | Add emergency fallback priority and fixture expressions |
| Braille representation | Extend | Braille is a canonical modality and exercised structurally in tests | Implement and qualify a real composer/device path later; DJ-0 uses structured expected expression only |
| Typed workflow/approval/recovery | Reuse | `unison-common/src/unison_common/workflows.py`; Phase 7 engine/tests | Represent incident and preparation as bounded workflow families later |
| Local-first model routing | Reuse | `unison-inference/src/governed_models.py`; SE8-SE12 tests | Add task requirements for image interpretation and bounded summarization after deterministic gates |
| Provenance and corrections | Reuse/extend | life-operation contracts and storage; governed context correction/deletion tests | Ensure DJ results cite source revision and deterministic rule; add view invalidation receipt |
| Per-domain storage | Extend | `unison-storage/src/domain_operations.py` uses person/domain records in one encrypted state file | Preserve logical model; physical per-domain keys/stores are a later security extension |
| Cross-domain authorization | Extend | `DomainLink`, `LifeDomainStore.link`, `cross_domain_packet`; tests in `test_domain_operations.py` | Replace durable pairwise link as the only mechanism with an expiring selected-field view contract |
| Backup/recovery | Reuse | provider-blind backup contracts and Phase 6 tests | Add DJ fixture scope classification; physical restore remains outside DJ-0 |
| Fair concurrency | Extend | `HouseholdResourceScheduler` with per-assistant round-robin CPU/memory quotas | Add priority class, accelerator/energy/thermal budgets, protected emergency/accessibility lane, and starvation tests |
| Intrusion/supply-chain lifecycle | Reuse | threat map, signed package/model/update contracts, adaptive-maintenance schemas | Add signed knowledge-pack lifecycle and DJ-specific integrity failures |

## Demonstration A mapping: simulated water leak

| Primitive | Disposition | Evidence | Gap or action |
| --- | --- | --- | --- |
| Synthetic people and household | Reuse | household contracts and `tests/fixtures/household/two-adults.v1.json` | Create DJ-specific identities without real personal data |
| Shared incident space | Extend | governed context supports explicit shared spaces and membership | Define purpose, retention, membership, and incident artifact conventions |
| Sensor event | New | no canonical sensor-event contract found | Define source identity, observation, unit/state, confidence, sequence, time, freshness, integrity, and health |
| Incident state machine | New | only generic workflow/events exist | Define observed, assessing, action-needed, isolating, monitoring, recovered, closed, and escalated states with legal transitions |
| Equipment registry | Extend/new | household records support product/manual/procedure and repair briefs | Define stable equipment/location/component identifiers and selected media references |
| Offline safety guidance | New | household procedure briefs exist; no signed knowledge-pack contract found | Define signed manifest, region, authority, edition, effective/expiry dates, hazards, stop rules, steps, and fallback |
| Deterministic hazard rules | Extend | urgent health and prohibited-action rules provide pattern | Add water/electrical/contamination/structural/inaccessible-shutoff rule fixtures; implementation begins DJ-1 |
| Selected camera capture | New | generic source/camera imports and vision input exist | Define incident-scoped capture, selected region, retention, disclosure, and equipment-binding proposal |
| Spatial interpretation | Extend | SEM supports `SPATIAL`; model proposal/runtime contracts exist | Add fixture proposal plus deterministic binding/uncertainty expectations |
| Shared task/acknowledgement | Extend | workflow steps, household coordination, commitments exist | Define incident assignment and acknowledgement fields or reuse after contract review |
| Emergency scheduling | New/extend | fair scheduler has no priority lanes or accelerator/energy/thermal quotas | Add contract first; implementation begins after DJ-0 |
| Physical valve control | Defer | physical actuation is explicitly prohibited in current life operations | Simulation records manual action only; later isolated low-voltage fixture requires a separate gate |

## Demonstration B mapping: health preparation with financial and insurance constraints

| Primitive | Disposition | Evidence | Gap or action |
| --- | --- | --- | --- |
| Health sources and normalized records | Reuse | FHIR mapping, health records, timeline, contradictions, safety, and visit brief in `unison-storage` | Create synthetic visit fixture and stale/conflicting cases |
| Finance sources and attention | Reuse | finance records and deterministic attention behavior | Limit fixture to selected budget range and obligations |
| Insurance domain | Extend | insurance domain/type and cross-domain packets exist | Add structured plan terms, directory snapshot, deductible, referral, authorization, and contact facts |
| Source provenance/correction | Reuse/extend | source/extracted/derived contracts; delete/reconcile tests | Add source revision/freshness and expected recomputation graph |
| Selected-field cross-domain analysis | Extend | approved `DomainLink.allowed_fields` and draft packet exist | Define explicit expiring view, excluded fields, purpose, output policy, and destruction receipt |
| Exact deductible/cost scenarios | New | no deductible rules or health-cost calculator found | Define deterministic inputs/outputs, uncertainty, exclusions, rounding/currency, and no-guarantee rule |
| Network/referral/authorization checks | New | insurance records are generic | Define evidence states: confirmed, unconfirmed, stale, conflicting, missing |
| Transportation/schedule | Extend | calendar workflow exists; no unified preparation contract | Use synthetic selected availability/options; avoid importing full calendars |
| Visit and insurer checklists | Extend | health brief and cross-domain draft mechanisms exist | Define separate private artifacts with exact citations and prohibited sending |
| Urgent-language interruption | Reuse/extend | deterministic urgent-health rules exist | Add fixture asserting administrative work stops and reviewed urgent path appears |
| Accessible speech/high-contrast expression | Extend | semantic expressions and visual accessibility tests exist | Add expected expression fixtures; physical/participatory proof deferred |
| Remote-provider disclosure | Reuse | trust governance and governed model routing fail closed | Baseline fixture is fully local; add negative remote-disclosure case |

## Repository ownership recommendation for DJ-0 through DJ-2

Do not migrate repositories during DJ-0. Use the present authorities:

- `unison-common`: canonical runtime contracts after review;
- `unison-storage`: source/domain/view persistence and deterministic domain
  calculations;
- `unison-context`: governed spaces and interaction-profile persistence;
- `unison-orchestrator`: incident/preparation workflow composition, scheduling,
  model calls, and semantic construction;
- `unison-experience-renderer`: visual/conversational expressions and later
  native modality composers;
- `unison-io-vision` and future adapters: bounded observations only;
- `unison-inference`: governed model selection and proposal validation;
- `unison-workspace`: cross-repository fixtures, acceptance gates, evidence,
  and authoritative planning.

This preserves current authority while collecting the change-coupling evidence
needed for the later repository decision. If DJ-1 and DJ-2 require coordinated
changes across most of these repositories, that becomes concrete evidence for
software consolidation.

## Contract candidates for DJ-0

The DJ-0 fixture manifest defines candidates for review, not canonical runtime
schemas:

- `sensor-observation.v1`;
- `household-equipment.v1`;
- `household-incident.v1`;
- `offline-knowledge-pack.v1`;
- `incident-assignment.v1`;
- `cross-domain-view.v1`;
- `cost-scenario.v1`;
- `evidence-state.v1`;
- `derived-artifact-receipt.v1`; and
- `journey-expression-expectation.v1`.

After review, accepted contracts should move into `unison-common` with generated
JSON Schema and contract tests. The meta-repository fixtures should consume the
published/pinned contracts rather than become a second schema authority.

## Validation completed for this audit

- recursive source/file search across the pinned repositories;
- direct inspection of principal, life-operation, storage, interaction,
  semantic, scheduling, workflow, inference, and backup implementations;
- comparison to existing unit, boundary, semantic, and phase evidence tests;
- explicit searches for incident, sensor, knowledge-pack, temporary-view,
  priority-lane, insurance, deductible, and Braille implementation anchors.

This audit did not execute the complete existing unit suite and is not a fresh
security review. DJ-0 validation covers fixture integrity and planning
consistency only.

