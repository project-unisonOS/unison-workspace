# Phase 10 AM-0 through AM-3 evidence

Status: Passed 2026-07-24

## Scope

This evidence covers:

- AM-0 decisions, contracts, and deterministic simulation;
- AM-1 private system observability and the System wellbeing experience;
- AM-2 installed-state exposure analysis and authoritative patch intelligence;
  and
- AM-3 deterministic recommendations, capacity forecasting, and hardware fit.

It does not claim AM-4 privileged execution, AM-5 live community collection,
AM-6 physical full-stack qualification, or AM-7 pilot readiness.

## Pinned implementation

| Boundary | Commit | Evidence |
| --- | --- | --- |
| Canonical contracts | `unison-common` `c266699e9ca15858521bce640b02c3963aee3d54` | Adaptive-maintenance v1 canonical and packaged schemas; privacy and source-trust negative tests |
| Analysis and Lifecycle input | `unison-platform` `058d641da92512f8326ab6c2c5743bf26bb3a9cd` | Device profile, health evaluation, source registry, exposure graph, recommendations, hardware fit, forecast, simulator, wellbeing projection |
| Accessible experience | `unison-experience-renderer` `6ea7c4353ad297cfa8be9e12495a3ce9fed07afd` | Privacy-enforcing wellbeing endpoint and semantic System wellbeing surface |

## AM-0 gate

The approved default policy is Recommend. The versioned policy keeps
internet-content authority false, emergency protection disabled, hardware
purchase execution disabled, and mutation dependent on independent Lifecycle
verification, a checkpoint, a health gate, and rollback.

The canonical schema covers device profiles, observations, external evidence,
candidates, recommendations, receipts, maintenance policy, and source
registries. The deterministic simulator produces byte-equivalent logical
results for identical scenarios.

Negative tests prove:

- personal-content observations are invalid;
- external evidence remains marked untrusted;
- a source cannot promote its configured trust tier;
- unsigned authoritative evidence is rejected; and
- discovery-only community evidence cannot enter the exposure graph.

## AM-1 gate

The host collector records architecture, CPU capacity, total memory, root
storage capacity, OS/kernel, installed component inventory, support tier, and
explicit redactions. It does not collect prompts, messages, contacts, document
titles, serial numbers, or network hardware addresses.

Initial content-free healthy envelopes cover CPU saturation, memory pressure,
storage use, service errors, backup age, and model first-token latency.
Thresholds are explicitly software-only until physical calibration.

The renderer exposes System wellbeing with:

- semantic headings, definition lists, ordered recommendations, and live status;
- plain-language privacy and autonomy boundaries;
- measured indicators and recommendation explanations;
- no privileged action control; and
- an allowlisted projection that rejects any status without an explicit
  `personal_content_collected: false` contract.

## AM-2 gate

The signed-product source registry model distinguishes authoritative,
corroborating, and discovery-only sources. The initial development registry
defines Unison releases, Ubuntu security data, GitHub reviewed advisories, and a
community discovery source. It requires a signed registry before product use.

The exposure graph matches ecosystem, component name, installed version,
introduced version, and fixed version. Tests prove affected fixtures are found,
unaffected components are not flagged, fix availability is preserved, and
community claims do not produce security exposure or patch authority.

This slice provides ingestion contracts and deterministic normalization. It
does not yet operate a scheduled live network collector; that remains AM-5.

## AM-3 gate

The recommendation engine ranks locally applicable security fixes, memory
pressure, storage pressure, and storage-growth forecasts. Recommendations
include rationale, alternatives, expected effects, risk, authority,
confirmation, rollback, rank, and confidence.

Hardware candidates fail closed unless their class, architecture, support tier,
free upgrade topology, firmware compatibility, and power budget match the
device profile. Memory pressure recommends a smaller or more quantized model
before suggesting a purchase. Tests prove an incompatible memory candidate is
rejected and a compatible candidate is only recommended after the software
alternative.

## Validation

- `unison-common`: 302 passed, 1 skipped locally; Python 3.12/3.13, contracts,
  package, lint, build, and security checks passed in hosted CI.
- `unison-platform`: existing manifest, installer, signed bundle, and update
  rollback suites passed with the new adaptive-maintenance acceptance suite;
  static contract and actionlint checks passed in hosted CI.
- `unison-experience-renderer`: 46 tests passed locally; both hosted CI runs
  passed.
- Workspace validator:
  `UNISON_DEV_VENV=<venv> ./scripts/validate-phase10.sh`.

## Residual boundary

AM-0 through AM-3 are analysis and recommendation capabilities. They cannot
install, restart, patch, purchase, or change the appliance. AM-4 must connect
plans to exact revocable grants and independently verified typed Lifecycle
operations before any autonomous mutation is possible.
