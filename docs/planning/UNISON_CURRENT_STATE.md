# Unison Current State

Status: verified audit snapshot; not a completion claim  
Audit date: 2026-07-21
Authoritative scope: `unison-workspace` plus the sibling Project Unison repositories present in `/home/dadam/unison-wsl`

## Purpose and evidence standard

This document records what was observed in source code, schemas, configuration, tests, deployment assets, workflows, and the public documentation checkout. Documentation was treated as a lead, not as proof. A capability is described as implemented only when code and focused tests or runnable configuration support the claim. Live hardware, provider, installation, and end-to-end claims remain unverified unless explicitly listed as executed evidence.

The root checkout is an aggregate working directory, not itself a Git repository. `unison-workspace` is the Git meta-repository and documented developer front door, so the authoritative planning set lives here. Repositories absent from its submodule list were still audited as sibling implementation evidence.

## Phase 8 expansion 8.1 candidate delta

The initial Phase 8 candidate adds a canonical semantic modality/fallback
contract, local speech interruption and caption-only output negotiation,
adaptive visual preferences, fail-closed privacy/cost/risk/offline model
routing, and Ed25519 capability verification with permission diff,
compatibility, and revocation controls.

This is a bounded engineering candidate, not a claim that every modality or
ecosystem package is production-ready. Braille, sign, switch/AAC, and haptic
remain experimental pending representative disabled-user and hardware evidence.
BCI, robotics, spatial control, and autonomous financial execution remain
deferred.

## Phase 7 accepted delta

The accepted Phase 7 implementation adds canonical task-plan, exact-approval,
failure/recovery, outcome-evidence, and synthetic record/replay contracts. One
governed engine implements seven bounded workflow families: calendar
coordination; email triage, summary, and draft; reminder and commitment review;
shared-household coordination; contact recall; document/web research; and travel
planning.

External steps declare their provider, recipients, and allowlisted disclosed
fields. Context and recipient authority are checked before execution;
advertising, engagement, sponsorship, and provider-lock-in ranking signals fail
closed. Stable idempotency, cancellation, compensation, retry, and provider
replacement are covered by deterministic provider tests. The renderer exposes
semantic plan, approval, running, success, failure, cancellation, retry,
replacement, and outcome paths.

Local acceptance completes all seven journeys with 81 estimated minutes
returned, one safe recovery, no duplicate actions, and zero boundary incidents.
This does not enable production providers, automatic sending, booking,
purchasing, payments, or generalized autonomous action.

## Phase 0 closeout delta

The local review candidate now provides a pinned Python 3.12 bootstrap, shared
static/unit entrypoints, Linux and Windows CI definitions, a component/topology
manifest, canonical schema/drift manifest, synthetic household fixture, complete
threat-to-test map, repaired context gitlink, and fail-loud synchronization.

The executed core unit baseline is now 596 passed and 1 skipped across common,
auth, consent, context, storage, policy, renderer, and orchestrator. Both current
Compose profiles validate. The public site builds strictly and the real Chromium
axe audit reports zero WCAG A/AA violation groups across all 42 substantive built
pages. This evidence improves repository truth; it does not implement the target
multi-principal household security model.

The public foundation now explicitly labels UnisonOS pre-release, distinguishes
Unison from UnisonOS, and describes the approved personal node, separate adult
assistants, explicit shared context spaces, local authority, replaceable providers,
accessibility, and person-aligned economic constraint as design commitments rather
than completed product features.

## Phase 1 implementation delta

The accepted Phase 1 implementation replaces JSON identity authority with a migration-managed
transactional store and introduces stable people, assistant instances, households,
memberships, login accounts, devices, channel identities, workload principals,
sessions, passkeys, invitations, and per-person isolation handles. Signed
`PrincipalContext` v1 is now the authority contract. Protected service middleware
validates signature, active session, audience, and caller identity hints before a
route executes.

Orchestrator, context, storage, renderer, policy, consent, payments,
communications, capability, replay, and actuation paths now consume derived
principal context. Context/storage/comms caches, credentials, objects, vault,
audit, replay, payment, and local message data are owner-partitioned. The hardened
Compose overlay disables reusable static/HS256 secrets and requires unique key
roots. Published CI and fresh-clone evidence passed and the Phase 1 gate was
approved on 2026-07-21. Later accepted phases build on that boundary.

## Phase 2 accepted delta

The accepted Phase 2 implementation adds canonical governed-context v2 contracts and a durable,
migration-managed repository in `unison-context`. Every assistant can own an
independent private space; shared spaces require explicit creation, invitation,
and acceptance. Relationship edges provide context but never membership. Search,
summary/index records, and prompt assembly are authorized by explicit spaces,
with purpose restrictions and restrictive inference/action/disclosure/backup/sync
defaults.

Memory admission distinguishes assertions, imports, hypotheses, corrections,
summaries, indexes, calendar events, and groceries. Correction history and
provenance survive restart; deletion and retention redact current and historical
content. Explicit sharing creates an auditable copy without reclassifying the
private source. Member removal revokes access and advances the space key version.
The renderer exposes semantic, keyboard-native inspection, space, correction,
deletion, share-preview, charter, goal, and commitment controls. Publication,
component/workspace CI, browser accessibility, recursive fresh-clone evidence,
and the final human gate were completed on 2026-07-21.

## Phase 3 accepted delta

The accepted Phase 3 implementation consolidates policy, consent, disclosure, minimization,
confirmation, delegated capability authority, credential brokerage, and audit
behind a versioned, default-deny Trust API. Remote inference requires a recorded
local-alternative check and an allowing disclosure decision. Capability execution
requires a bounded manifest and expiring, nonce-protected grant; legacy unknown
authority is disabled. An accessible semantic review exposes the exact action,
recipients, data, purpose, consequence, reversibility, cost, and alternatives.
Publication, component/workspace Actions, recursive fresh-clone evidence,
accessibility review, and the final human gate completed on 2026-07-21.

## Phase 4 accepted delta

The accepted Phase 4 implementation composes the accepted identity and governed
context boundaries into a bounded two-independent-adult household proof. It adds
minimal household administration, explicit shared calendar/grocery contracts,
coordination with zero private-source reads, fair per-assistant resource budgets,
non-oracular cross-person denials, removal/key-rotation/restart recovery, and
accessible household controls. The 50-check proof, hosted CI/security,
accessibility audit, recursive fresh clone, and human gate passed on 2026-07-21.
This remains pre-release engineering rather than a supported product release.

## Phase 5 accepted boundary

The accepted Phase 5 boundary adds canonical remote-channel contracts, auth-owned strong
local pairing and revocation, a Telegram private-chat long-poll adapter, encrypted
per-person provider accounts and drafts, replay/rate/outage defenses, low-assurance
step-up, orchestration guards, accessible disclosure/recovery controls, and a
private-network deployment with no inbound appliance listener. It preserves the
Gmail adapter and validates the provider path with a credential-free fake. This
boundary passed its final human architecture/security gate on 2026-07-21. Phase 6
provider-blind backup and replacement restore remain not started.

## Reconciled product state

The implemented system is an early, local-first assistant platform assembled as a large Python/FastAPI microservice stack. The completed Phase 1 establishes the first household identity and principal boundary, but the broader household product remains pre-release:

- protected Phase 1 services bind authenticated people and workloads, but remaining optional modality/research services still require later integration review;
- household identity plus governed relationship, context-space, charter, goal, and commitment models are implemented in accepted Phase 2;
- per-person credentials, encryption keys, data/cache/index namespaces, and audit ownership exist locally; provider-blind backup domains remain Phase 6 work;
- accepted Phase 3 provides default-deny disclosure decisions over purpose, audience, relationship, sensitivity, and channel assurance;
- a bounded Telegram remote-text boundary is accepted for low-assurance private-chat access; provider-blind encrypted backup remains unstarted Phase 6 work.

The current product should therefore be described publicly as an experimental developer platform with a native-install path under active validation, not as a production private household assistant.

## Repository inventory

The audit found 32 top-level Git repositories and one nested `unison-devstack` repository. The recommendations below are planning dispositions, not completed migrations.

| Repository | Verified implementation role | Observed maturity | Planned disposition |
| --- | --- | --- | --- |
| `unison-workspace` | Meta-repo, submodules, developer scripts, local validation wrappers | Active but incomplete front door | Retain as source checkout and authoritative planning home |
| `unison-platform` | Compose distribution, Ubuntu native installer, `unisonctl`, images, release/update/recovery tooling | Active; strongest delivery assets | Retain as appliance distribution and privileged lifecycle boundary |
| `unison-orchestrator` | Intake, routing, planning, policy gate, skills, replay, startup and experience flows | Active; extensive unit coverage | Retain logic; evolve into modular Unison Core |
| `unison-common` | Contracts, envelopes, response model, telemetry, validation, shared utilities | Active; extensive unit coverage | Retain; make the single generated-contract implementation package |
| `unison-auth` | Password/service authentication, JWTs, local JSON user store, bootstrap admin | Development-grade | Replace persistence and identity model; consolidate into Trust boundary |
| `unison-context` | Person-keyed profile, conversation, dashboard, KV and encryption helpers | Active but coarse | Retain data migration value; redesign as governed memory/context modules |
| `unison-context-graph` | In-memory context state plus SQLite replay, capability and telemetry data; optional Neo4j readiness | Active, early, overlapping | Consolidate graph behavior into governed context/relationship modules |
| `unison-intent-graph` | Placeholder FastAPI front end ahead of orchestrator | Early placeholder | Consolidate intent normalization into Unison Core |
| `unison-policy` | Signed rules, action evaluation, grants and confirmation decisions | Active; tested | Retain evaluator concepts; consolidate with consent/disclosure in Trust boundary |
| `unison-consent` | JWT-like scoped grants, revocation and introspection | Early; overlaps policy grants | Consolidate with policy grant service; replace permissive unknown-scope behavior |
| `unison-storage` | KV, memory, vault, audit and object tables/APIs | Early; global service-token/key model | Consolidate access mediation into Personal Data and Trust Store; retain storage adapters |
| `unison-security` | Starter threat model, SPIRE/Envoy/OPA examples, logging and policy artifacts | Reference/configuration | Retain useful guidance; authoritative threat model moves to this planning set |
| `unison-capability` | Capability discovery, manifest validation, install/run, MCP and command execution | Active, early | Retain and harden as Capability Host |
| `unison-inference` | Ollama/OpenAI/Azure provider gateway | Active | Retain as model broker/resource boundary; add disclosure-aware routing |
| `unison-experience-renderer` | FastAPI/web operating surface, onboarding, events, semantic-ish rendering | Active | Retain as Unison Surface; expand semantic and accessible control flows |
| `unison-comms` | Email-shaped adapter protocol, Gmail IMAP/SMTP, local Unison messaging, meeting stubs | Active, bounded | Refactor into normalized Channel Gateway |
| `unison-actuation` | Policy-gated action envelopes and mock/logging drivers | Active, early | Move execution into Capability Host; retain action contract and safety logic |
| `unison-agent-vdi` | Browser/form/download tasks and renderer telemetry | Active, bounded | Run as an optional sandboxed capability worker |
| `unison-network-vpn` | WireGuard sidecar for VDI egress | Specialized | Retain as optional capability-network profile, not general remote access |
| `unison-io-core` | Development event forwarding stub | Optional stub | Consolidate generic intake into channel/core adapters |
| `unison-io-speech` | Local STT/TTS, streaming facade and orchestrator forwarding | Active | Retain as optional hardware/resource adapter |
| `unison-io-vision` | Capture/description stubs | Development stub | Defer real implementation; retain adapter contract only |
| `unison-io-braille` | Translation, simulated driver, discovery/server scaffolding | Scaffolding | Retain accessibility R&D; integrate through semantic surface contract |
| `unison-io-sign` | Sign schemas, detector/interpreter/provider scaffolding | Library/scaffolding | Retain as optional modality package |
| `unison-sign-orchestrator` | Sign-to-intent gateway stub | Redundant early gateway | Consolidate into sign adapter and canonical channel intake |
| `unison-io-bci` | BCI ingest/decoder scaffold with broad device ambitions | Experimental | Defer until household trust boundaries are proven |
| `unison-payments` | Mock/tokenized payment service | Experimental/high risk | Defer autonomous financial work; retain isolated research only |
| `unison-capability` | Resolver and capability runtime | Active, early | Canonical repository name; runtime identifier is `unison-capability-host` |
| `unison-os` | Base Ubuntu container image | Supporting infrastructure | Retain for container profiles; do not confuse with appliance product |
| `unison-spec` | Deprecated pointer to docs | Superseded | Archive/read-only; no new work |
| `unison-docs` | Canonical engineering/product docs by prior convention | Active but contains mixed-era claims | Retain; reconcile to this planning set and status-label claims |
| `project-unisonos.github.io` | MkDocs public site with accessibility overrides/audit script | Builds; IA and claims are stale | Retain and overhaul early |
| `unison-io-sign`, `unison-io-braille`, modality repos | Specialized modality work | Uneven | Keep optional; do not require separate default appliance processes |
| `.github` | Organization templates and reusable workflows | Supporting | Retain; standardize required CI from here |

## Current runtime topology

### Developer stack

`unison-devstack/docker-compose.yml` resolves to 23 default services:

`redis`, `postgres`, `storage`, `neo4j`, `context-graph`, `inference`, `intent-graph`, `experience-renderer`, `network-vpn`, `agent-vdi`, `capability`, `consent`, `context`, `policy`, `actuation`, `auth`, `jaeger`, `orchestrator`, `io-bci`, `comms`, `io-core`, `io-speech`, and `io-vision`.

This is too large for the intended personal appliance default. It mixes logical domains, optional modalities, developer infrastructure, security-sensitive execution, and product-critical services as peer network processes.

### Native platform profile

`docker compose -f unison-platform/compose/compose.native.yaml config --quiet` succeeded. The profile currently resolves to 13 services:

`postgres`, `redis`, `auth`, `nats`, `io-speech`, `context`, `intent-graph`, `context-graph`, `policy`, `orchestrator`, `storage`, `inference`, and `experience-renderer`.

The native installer shell scripts pass `bash -n`. A real Ubuntu install, reboot, first-run, update, recovery, and replacement-device restore were not executed during this audit.

### Developer environment

- WSL2 Ubuntu and Linux-native Python/container tooling are the effective implementation environment.
- `scripts/bootstrap-dev.sh` is the authoritative pinned Python 3.12 bootstrap; Linux/WSL owns implementation commands.
- `scripts/unison.ps1` is a thin Windows wrapper that validates WSL availability and delegates to the same commands.
- The devstack `install.ps1` and `install.sh` remain only for migration history and emit explicit deprecation warnings; they are not appliance installers.
- `scripts/sync.sh` now fails loudly and resolves each submodule's upstream default branch.
- Phase 0 replaced unavailable context gitlink `60e5e8a` with valid `origin/main` commit `852bef92ab79e0422be17651a5345631ac35063c`; publication and fresh-clone verification passed its gate.

## Contracts and schemas

Useful retained contracts exist, but there are multiple copies and incompatible generations:

- `unison-common` provides `InputEventEnvelope`, `ActionEnvelope`, `PolicyDecision`, `ResponseObjectModel`, renderer events, replay events, and validation helpers.
- The current `InputEventEnvelope.person_id` is optional and `auth` is an untyped dictionary; it does not establish trusted principal binding.
- `ResponseObjectModel` supports text/cards and a generic metadata dictionary, but does not require urgency, privacy state, confirmation, cancellation, recovery, provenance, or modality-equivalent actions.
- Capability manifest v0.1 includes origin digest/signature, basic network/filesystem/device permissions, sandbox type, resources, secrets references, trust level, and implementation kind. It does not yet declare data classes, recipients, purpose, reversibility, cost, confirmation, accessibility, or audit behavior.
- Action-envelope schemas exist in `unison-actuation`, `unison-docs`, aggregate root files, and Python contracts. Canonical ownership and generation are unresolved.
- The aggregate root `schemas/phase1` directory is outside a Git repository and must not remain an authoritative schema location.

## Identity, context, policy, and data findings

- `unison-auth` uses SQLite migration v1 for the Phase 1 identity graph and binds signed tokens to active membership, assistant, resource handles, session, audience, and assurance.
- Revocation/introspection failure is fail closed for protected operations.
- `unison-context` rejects mismatched identity hints, derives person/cache/index authority from signed context, and is the authoritative governed-context v2 repository/API.
- Profile/dashboard encryption derives purpose-specific keys from the person's opaque key handle and fails closed in the hardened product profile.
- `unison-context-graph` uses `user_id`, while newer contracts prefer `person_id`.
- `unison-storage` derives data, memory, vault, audit, and object ownership from the signed person and prefixes namespaces before lookup.
- Object encryption derives a per-person purpose key from the configured product root.
- Both `unison-policy` and `unison-consent` implement grant/introspection concepts. Consent validation warns on unknown scopes rather than denying them.
- Devstack Compose contains development passwords and secrets. These are acceptable only in an explicitly isolated test profile and must never flow into an appliance bundle.

## Communications and remote access findings

- `unison-comms` has an `EmailAdapter` protocol, an in-memory adapter, a Gmail IMAP/SMTP adapter, and a local encrypted Unison messaging adapter.
- Gmail bootstrap credentials and local Unison message stores are partitioned by the authenticated person's credential/data namespace and key handle.
- Production `local-user` and `local-person` authority defaults are rejected by the Phase 1 validator.
- The adapter contract is email-shaped; SMS, telephone, Telegram, WhatsApp, AAC, and mobile clients do not share a canonical channel envelope.
- `unison-network-vpn` protects VDI egress and is not a remote-person-to-home-node access architecture.
- No outbound relay, channel assurance model, replay-proof channel binding, or step-up authentication flow was verified.

## Backup, sync, and recovery findings

- Platform scripts include conventional PostgreSQL/Vault archive backups and S3 upload examples.
- Release/update artifact staging and recovery validators exist.
- No provider-blind per-person encryption, shared-space keys, signed backup manifest, incremental snapshot protocol, provider-neutral backend, independent person export/deletion, or replacement-device restore flow was verified.
- Backup, synchronization, and remote access are not yet separated as product concepts.

## Appliance lifecycle audit, 2026-07-23

Phase 9.0 now has a local candidate: lifecycle and update ownership are
versioned workspace pins, and the supported-target/support-policy contract is
machine validated. This removes the unversioned update-service gap identified
below. It does not make an artifact supported; deterministic runtime and all
later Phase 9 gates remain open.

The merged Phase 9.1 runtime-contract slice now requires digest references for
all 13 candidate services and removes broad developer port exposure, retaining
two loopback-only product/health surfaces. Real release digests and physical
runtime acceptance remain open.

The first Phase 9.3 trust slice now verifies threshold-signed channel metadata,
expiration, monotonic versions, channel/hardware binding, artifact integrity,
and dual-authority root rotation. Activation health and physical rollback
cycles remain open.

The verified-bundle slice now assembles the supported manifest and its declared
runtime inputs under a canonical Ed25519-signed index. Pre-privilege bootstrap
verification rejects tamper, inventory drift, service/image reassignment, and
trust-root substitution; exact plan acceptance gates transactional activation,
and the resulting receipt binds the installed tree to the release manifest and
source commit. Real promoted images, SBOM/provenance publication, public
download, and physical installation remain open.

- `unison-platform` contains the active native Ubuntu installer, native Compose
  entrypoint, `unisonctl`, first-start default checks, evaluator image builders,
  release staging, and staged-update/recovery validators.
- The workspace pins `unison-platform` at
  `86a53cb9f455a6d203e71849164892881c99966d`, including the constrained
  runtime, reproducible manifest, installer simulation, transaction, verified
  bundle, bootstrap, and receipt gates.
- `unison-os` contains documentation only, despite its README describing a base
  image build. The component inventory correctly classifies it as a legacy
  prototype for archival rather than the appliance authority.
- The supported runtime requires 13 immutable image digests and exposes only
  two loopback surfaces. Real promoted digests are not yet published.
- `unison-updates` is a pinned Git submodule with threshold-signed metadata and
  attack simulations. Platform still keeps update activation optional, and a
  real promoted update has not run end to end.
- Platform staged-update tests validate plan/artifact/finalize state, but the
  acceptance matrix records that real promoted package/image updates and
  rollback are not exercised end to end.
- The tag release workflow signs the platform image and stages release assets,
  but action references are not commit-pinned, the downloaded Cosign binary is
  not checksum-verified, and verification of evaluator images is skipped.
- The evaluator bare-metal ISO embeds a known password, permits SSH password
  login, makes Ubuntu ISO checksum verification optional, and invokes the broad
  Compose file. It is not eligible for supported status.
- Hardware guidance names Ubuntu 24.04 x86_64 and general CPU, RAM, storage, and
  audio expectations, but there is no named reference-device matrix,
  machine-readable compatibility probe, firmware/peripheral evidence, or
  completed physical clean-install record.
- Phase 9 of the implementation plan converts these assets into a gated supported
  appliance program. No current artifact is credited as supported.

## CI and test baseline

The shared WSL virtual environment used Python 3.12.3, pytest 8.3.3, FastAPI 0.115.0, and Pydantic 2.12.4. Tests were run with bytecode and pytest cache writes disabled. Results are environment-specific evidence, not universal CI status.

| Check | Result | Interpretation |
| --- | --- | --- |
| `unison-common` tests | 248 passed, 1 skipped | Strong contract/library baseline at the repaired workspace pin |
| `unison-orchestrator` tests | 203 passed | Strong focused orchestration baseline; no live stack |
| `unison-policy` tests | 71 passed | Existing action/grant behavior covered |
| `unison-capability` tests | 21 passed | Resolver/auth/audit flows have focused coverage |
| `unison-comms` tests | 20 passed | Bounded email/local adapter behavior covered |
| `unison-experience-renderer` tests | 22 passed | Terminology guard passes |
| `unison-auth` tests | 19 passed | Shared bootstrap provides dependencies and temporary keys |
| `unison-context` tests | 18 passed | Shared bootstrap provides SQLAlchemy and test-safe tracing |
| `unison-storage` tests | 3 passed | Shared bootstrap provides SQLAlchemy and test-safe tracing |
| `unison-consent` tests | 12 passed | Temporary key path works; expired-token rejection is tested |
| Devstack Compose config | passed | Static merged configuration parses |
| Native Compose config | passed | Supported native bundle parses when invoked alone |
| Native install and E2E | not run | Requires representative target and explicit evidence run |

Repository CI remains inconsistent across sibling repos. Phase 0 added workspace
Linux bootstrap/static/unit enforcement and Windows wrapper parsing while retaining
the reusable security job. Phase 1 workspace and security Actions passed, and the
published evidence identifies the pre-existing sibling CI/container failures that
remain tracked debt. All newly touched action references are pinned to commit SHAs.

## Public website findings

- MkDocs strict build completed successfully.
- Six documentation pages exist but are omitted from navigation.
- The audit discovers all generated pages instead of skipping stale hard-coded URLs.
- JSDOM/axe reports zero WCAG A/AA violation groups across 45 generated pages; Chromium/Playwright/axe reports zero across 42 substantive pages after excluding redirect stubs.
- All 1,767 generated internal links resolve. Keyboard first-focus, reduced-motion, and forced-colors smoke checks pass.
- The site has a skip link, visible focus, keyboard-reachable scroll regions, forced-colors and reduced-motion rules, semantic landmarks, and pinned real-browser CI.
- The visual foundation now uses calm navy/blue/teal design tokens and responsive content cards while retaining the accessible MkDocs shell.
- New public pages label pre-release maturity and explain household assistants, explicit context spaces, channel assurance, provider-blind backup principles, accessibility, product terminology, and honest provider boundaries.
- Deep historical pages remain scheduled for phase-specific claim review and are not treated as current product evidence.

## Verified strengths to retain

- A substantial tested orchestration core.
- Shared Pydantic contracts and validation infrastructure.
- Action risk and confirmation concepts.
- Signed policy/capability artifact concepts.
- Local and remote model-provider abstraction.
- Native Ubuntu distribution, update, recovery, and release scaffolding.
- A renderer with explicit event/experience and modality-oriented design.
- Local speech implementation and broader accessibility research.
- Capability sandbox metadata and network allowlist concepts.
- Structured logging, tracing, replay, and audit foundations.
- Draft-first Gmail behavior and bounded VDI workflows.

## Areas not verified

- A clean Ubuntu 24.04 native installation on physical or representative appliance hardware.
- Reboot persistence, update rollback, factory reset, and replacement-device restoration on a real install.
- Live Gmail provider flows with real credentials.
- A live Telegram flow with real credentials, or any supported telephone channel.
- Production timing-side-channel certification for household or remote-channel isolation.
- Hardware-backed keys or per-person encryption.
- Provider-blind backup or multi-device synchronization.
- Real Braille, sign, BCI, vision, microphone, speaker, or switch-access hardware.
- Browser automation against adversarial websites and documents.
- Production supply-chain provenance for every image and dependency.
- Cloud-provider/model data retention behavior.
- Full end-to-end stack validation after the repository sync.

## Superseded and contradictory planning material

Prior production plans, milestone matrices, roadmaps, repo maps, and public pages remain useful historical evidence. They are no longer execution authority when they conflict with this planning set. They must be labeled or reconciled incrementally; they must not be silently deleted before useful decisions and evidence are migrated.
