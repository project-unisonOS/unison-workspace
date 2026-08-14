# DJ-1 service integration evidence

Status: accepted integration simulation evidence  
Date: 2026-08-14  
Environment: Ubuntu `dev-nuc`, Python 3.12.3, Docker 29.1.3, Compose 2.40.3,
isolated clean checkout

## Scope

This evidence covers the deployable service boundary that follows the DJ1-C0
through DJ1-C3 in-process simulation. It does not cover physical sensors, real
Braille hardware, participatory accessibility research, GPU behavior, power,
thermal, RF, or production security qualification.

## Candidate revisions

| Component | Commit | Review |
| --- | --- | --- |
| `unison-storage` | `3278e37` | merged `project-unisonOS/unison-storage#25` |
| `unison-orchestrator` | `9e4beda` | `project-unisonOS/unison-orchestrator#35` |
| `unison-experience-renderer` | `2a4426f` | merged `project-unisonOS/unison-experience-renderer#21` |
| `unison-workspace` | `45e009c` | `project-unisonOS/unison-workspace#40` |

## Results

| Boundary | Result |
| --- | --- |
| Storage full suite | 37 passed |
| Orchestrator full suite | 247 passed |
| Renderer full suite | 56 passed |
| Renderer legacy-UI vocabulary guard | passed |
| DJ-0 fixture gates | 12 passed |
| Workspace focused acceptance | 33 passed across isolated component invocations |
| Three-service container build and health | passed |
| Normal storage-to-renderer delivery | passed; `renderer_delivered=true` |
| Renderer outage | incident remained `action-needed`; `renderer_delivered=false` |
| Restart-safe renderer replay | passed; 1 delivered, 0 remaining |

The orchestrator route is explicitly named and labeled as simulation. It
persists the incident before publishing an experience envelope. Renderer loss
does not roll back or alter incident authority. The failed semantic envelope is
written atomically to a persistent outbox and can be replayed after renderer
recovery. Storage derives the production
shared space from trusted household principal claims; client-provided authority
is accepted only when the existing test bypass is explicitly enabled.

The Compose acceptance uses that explicit principal-binding bypass and is not
production authentication evidence. All three services run as separate
containers over the Compose network; storage and outbox volumes are removed by
the test teardown.

## Deferred

- container-to-container exercise with a real auth-service-issued principal;
- signed offline knowledge-pack verification rather than structural validation;
- automatic scheduled outbox draining; the current replay trigger is explicit;
- physical sensor and modality adapters;
- GPU, sustained load, energy, and thermal qualification pending the workstation.
