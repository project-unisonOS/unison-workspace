# DJ-0 contract and fixture lock

Status: **Review package complete; candidate contracts are not canonical runtime contracts**  
Completed: 2026-08-14  
Gap analysis: [DJ0_ARCHITECTURE_GAP_ANALYSIS.md](DJ0_ARCHITECTURE_GAP_ANALYSIS.md)

## Scope

DJ-0 establishes a model-independent, synthetic requirements package for the
first two demonstrations. It deliberately stops before runtime implementation,
real sensors, real health or financial data, external providers, physical
actuation, or safety/support claims.

## Artifacts

- `tests/fixtures/dj0/dj0-fixtures.v1.json`: candidate contract inventory,
  synthetic people, interaction profiles, shared incident space, sensor
  observations, equipment, offline knowledge-pack fixture, health/insurance/
  finance/transport sources, expiring cross-domain view, expected evidence,
  deterministic cost scenario, private artifact receipts, expression
  expectations, and positive/negative cases.
- `tests/fixtures/dj0/dj0-gates.v1.json`: privacy, accessibility, safety,
  resilience, integrity, correctness, lifecycle, authority, and truth gates.
- `scripts/validate-dj0-fixtures.py`: dependency-free structural and invariant
  validator suitable for local use and CI.

## Candidate contracts

| Contract | Purpose | Proposed canonical owner |
| --- | --- | --- |
| `sensor-observation.v1` | Ordered, fresh, integrity-labeled physical or simulated observation | `unison-common` |
| `household-equipment.v1` | Stable household equipment, location, component, source, and procedure identity | `unison-common` |
| `household-incident.v1` | Shared incident facts, uncertainty, assignments, timeline, and retention | `unison-common` |
| `offline-knowledge-pack.v1` | Signed, regional, versioned, reviewable offline guidance and stop rules | `unison-common` |
| `incident-assignment.v1` | Person-bound incident action and acknowledgement lifecycle | `unison-common` |
| `cross-domain-view.v1` | Expiring, selected-field, purpose-bound computation view | `unison-common` |
| `evidence-state.v1` | Confirmed, stale, conflicting, missing, or uncertain claim state | `unison-common` |
| `cost-scenario.v1` | Deterministic source-bound range with explicit uncertainty and no guarantee | `unison-common` |
| `derived-artifact-receipt.v1` | Provenance, revision, view, disclosure, retention, and recomputation record | `unison-common` |
| `journey-expression-expectation.v1` | Cross-modality semantic acceptance fixture | `unison-workspace` test authority |

## Contract lock rule

“Lock” means that DJ-1/DJ-2 implementation must either consume these candidate
semantics or record an explicit reviewed change. It does not make this
meta-repository the runtime schema authority. Accepted runtime forms must be
implemented in `unison-common`, exported as JSON Schema, and pinned through the
existing schema manifest.

## Threat, privacy, accessibility, and prohibited-action coverage

The gate matrix requires:

- explicit shared-incident fields and private canary absence;
- non-oracular cross-person denial;
- visual/Braille/conversational equivalence and fallback;
- deterministic hazard stop rules before repair guidance;
- offline/no-model deterministic paths;
- duplicate, stale, reordered, and unverifiable sensor handling;
- purpose and field approval before cross-domain access;
- exact model-independent arithmetic;
- urgent-health interruption and no affordability-based treatment ranking;
- correction invalidation, view expiry, deletion, and index cleanup;
- no physical actuation, diagnosis, prescription, treatment selection,
  coverage guarantee, money movement, claim submission, external sending,
  widened disclosure, or unapproved combined profile; and
- permanent simulation and synthetic-data truth labels for DJ-0.

## Baseline values

DJ-0 is not a performance baseline. Its initial measurable baseline is contract
completeness:

- 10 unique candidate contracts;
- 2 synthetic model-independent journey packages;
- 12 cross-cutting review gates;
- 6 primary/failure cases per journey;
- 0 real personal records;
- 0 external calls;
- 0 physical actions; and
- 0 model dependencies.

DJ-1 and DJ-2 must add behavioral, privacy, latency, concurrency, and semantic-
equivalence measurements without changing the DJ-0 evidence label.

## Review decisions required before DJ-1

1. Approve, revise, or reject the ten candidate contract boundaries.
2. Decide whether `incident-assignment.v1` should extend the accepted workflow
   step/commitment contract instead of becoming independent.
3. Decide whether `evidence-state.v1` belongs in a general provenance module or
   only the life-operations package.
4. Approve the temporary-view lifecycle and destruction/recomputation receipt.
5. Select authoritative, redistributable real sources and a signing policy for
   the first non-synthetic offline water-safety pack.
6. Approve the accessibility research plan before interpreting synthetic
   Braille/visual equivalence as user evidence.

## Validation command

```bash
python3 scripts/validate-dj0-fixtures.py
```

Expected result:

```text
DJ-0 fixture validation passed: 10 contract candidates, 2 journeys, 12 gates
```

## DJ-0 exit decision

DJ-0 is complete when the validator passes, the architecture mapping and
fixtures are published for review, and all artifacts retain their candidate,
synthetic, and simulation labels. Completion authorizes contract review and
DJ-1 planning; it does not authorize physical actuation, real personal data,
clinical use, or a supported-product claim.

