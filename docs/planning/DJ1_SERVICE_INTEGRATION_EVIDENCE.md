# DJ-1 service integration evidence

Status: candidate, simulation evidence  
Date: 2026-08-14  
Environment: Ubuntu `dev-nuc`, Python 3.12.3, isolated clean worktrees

## Scope

This evidence covers the deployable service boundary that follows the DJ1-C0
through DJ1-C3 in-process simulation. It does not cover physical sensors, real
Braille hardware, participatory accessibility research, GPU behavior, power,
thermal, RF, or production security qualification.

## Candidate revisions

| Component | Commit | Review |
| --- | --- | --- |
| `unison-storage` | `ac46894` | `project-unisonOS/unison-storage#25` |
| `unison-orchestrator` | `25e9e38` | `project-unisonOS/unison-orchestrator#34` |
| `unison-experience-renderer` | `fb3f49c` | `project-unisonOS/unison-experience-renderer#20` |

## Results

| Boundary | Result |
| --- | --- |
| Storage full suite | 37 passed |
| Orchestrator full suite | 247 passed |
| Renderer full suite | 56 passed |
| Renderer legacy-UI vocabulary guard | passed |
| DJ-0 fixture gates | 12 passed |
| Workspace focused acceptance | 33 passed across isolated component invocations |

The orchestrator route is explicitly named and labeled as simulation. It
persists the incident before publishing an experience envelope. Renderer loss
does not roll back or alter incident authority. Storage derives the production
shared space from trusted household principal claims; client-provided authority
is accepted only when the existing test bypass is explicitly enabled.

## Deferred

- container-to-container NUC Compose exercise with service-issued principal;
- signed offline knowledge-pack verification rather than structural validation;
- retry queue for renderer delivery after an outage;
- physical sensor and modality adapters;
- GPU, sustained load, energy, and thermal qualification pending the workstation.
