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
| `unison-auth` | `02c0e26` | pinned workspace revision |
| `unison-storage` | `3278e37` | merged `project-unisonOS/unison-storage#25` |
| `unison-orchestrator` | `2700358` | merged `project-unisonOS/unison-orchestrator#35` |
| `unison-experience-renderer` | `2a4426f` | merged `project-unisonOS/unison-experience-renderer#21` |
| `unison-workspace` | pending authenticated-profile review | pending |

## Results

| Boundary | Result |
| --- | --- |
| Storage full suite | 37 passed |
| Orchestrator full suite | 247 passed |
| Renderer full suite | 56 passed |
| Renderer legacy-UI vocabulary guard | passed |
| DJ-0 fixture gates | 12 passed |
| Workspace focused acceptance | 33 passed across isolated component invocations |
| Four Unison service containers plus Redis build and health | passed |
| Auth bootstrap and person token issuance | passed |
| Missing bearer token | denied with HTTP 401 |
| Forged `person_id` with a valid token | denied with HTTP 403 |
| Auth outage after token issuance | failed closed with HTTP 403 |
| Normal storage-to-renderer delivery | passed; `renderer_delivered=true` |
| Renderer outage | incident remained `action-needed`; `renderer_delivered=false` |
| Restart-safe renderer replay | passed; 1 delivered, 0 remaining |

The orchestrator route is explicitly named and labeled as simulation. It
persists the incident before publishing an experience envelope. Renderer loss
does not roll back or alter incident authority. The failed semantic envelope is
written atomically to a persistent outbox and can be replayed after renderer
recovery. Storage derives the shared space from trusted household principal
claims; client-provided authority is not accepted by this profile.

The Compose acceptance bootstraps an ephemeral first person through
`unison-auth`, obtains an RS256 token whose audience covers orchestrator,
storage, and renderer, and forwards that token across both downstream service
hops. No principal-binding or service-auth test bypass is enabled. All four
Unison services run as separate containers over the Compose network; Redis is
the auth support dependency. Fixture identities, signing keys, storage, and the
outbox are removed by teardown.

This is authenticated integration evidence, not production security
qualification. Auth identity and key paths use UID-owned tmpfs because the
current auth image cannot write to root-owned named volumes while running as its
non-root user. A durable deployment must solve volume provisioning and key
custody explicitly rather than copy this ephemeral choice.

## Deferred

- signed offline knowledge-pack verification rather than structural validation;
- automatic scheduled outbox draining; the current replay trigger is explicit;
- durable auth identity/key volume provisioning, backup, and recovery;
- physical sensor and modality adapters;
- GPU, sustained load, energy, and thermal qualification pending the workstation.
