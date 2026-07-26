# Semantic experience SE11 and SE12 acceptance evidence

Status: **SE11 software scope complete; SE12 software tooling and simulation complete; physical qualification open**

Acceptance date: 2026-07-25

## SE11 accepted scope

- Golden semantic journeys compare required facts, required meaning, actions,
  provenance, recovery, disclosure, modality equivalence, and latency.
- Comparison data is synthetic unless a non-synthetic source carries an
  explicit approval reference.
- Shadow evaluation cannot change the active route.
- A candidate enters a bounded canary only after every golden journey passes.
- Health gates use content-free contract, semantic, fallback, error, and latency
  signals. A failing canary rolls back automatically.
- The compatible prior model remains available until the rollback window closes.
- Model changes do not own or migrate identity, memory, permissions, pending
  actions, or interaction-profile state.
- A deliberately regressed candidate is rejected before canary, and a degraded
  canary rolls back without changing person state.

## SE12 completed software scope

- Versioned qualification records capture model, runtime, hardware, processor,
  architecture, accelerator, RAM, storage, task latency, energy, thermals,
  concurrency, offline operation, update, rollback, semantic quality, safe
  fallback, limitations, evidence kind, and support state.
- Compatibility matrices derive their supported model list solely from passing
  qualification records.
- A support claim fails validation unless evidence is from a physical device
  and includes energy, thermals, offline, update, rollback, semantic quality,
  and safe-fallback results.
- Synthetic realistic-load, offline, update, rollback, and semantic-quality
  paths pass without creating a supported-hardware claim.

## Accepted component commits

| Repository | Commit | Scope |
| --- | --- | --- |
| unison-common | cea3558fd3d85b5a9a816093446b0bedfed70bef | Golden journey, evaluation, health, deployment, qualification, and compatibility contracts |
| unison-inference | 100a4277183a2ce70926c0564a8974effb52e612 | Shadow, canary, promotion, health gates, rollback, invariance, and matrix generation |
| unison-docs | 91a3f18d3f6ea3b6cb508ba969e82766e91a819a | Developer lifecycle and qualification guidance |
| project-unisonos.github.io | 51f4018d481b779f290b406db5330fcdbf069303 | Evidence-bounded public lifecycle, current-status, architecture, and roadmap content |

## Open physical qualification

- SE-HW-07 remains open for representative CPU, GPU, RAM, storage, latency,
  energy, thermals, and contention evidence.
- SE-HW-04 and SE-HW-05 remain open for vision and sign model/runtime paths.
- No model/runtime/hardware combination is currently listed as supported by the
  semantic experience program.
- The supported-appliance acceptance statement in SE12 is not marked passed.

## Publication decision

Public documentation may describe the implemented governance flow: signed
manifests, hard eligibility, untrusted proposals, golden evaluation, bounded
canary use, content-free health gates, and automatic rollback. It must also say
that model/hardware combinations remain unqualified and that no supported model
matrix has been published yet.
