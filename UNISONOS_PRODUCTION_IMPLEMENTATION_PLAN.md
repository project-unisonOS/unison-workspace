# UnisonOS Production Implementation Plan

This file is intentionally kept at the workspace root for ongoing planning and status tracking.

## Current Status Snapshot

This copy was reconstructed from recovered plan content and updated against the verified workspace state on this machine.

Verified current state:

- supported Milestone 1 target remains Ubuntu 24.04 native on x86_64
- all active repos in the local workspace were audited directly from git and code
- `unison-platform`, `unison-orchestrator`, `unison-auth`, `unison-experience-renderer`, and `unison-workspace` were updated, committed, and pushed to `main`
- local runtime was re-established on Ubuntu with Docker and a user-managed Ollama service
- Ollama is running locally with model `qwen3.5:0.8b`
- `unison-platform` is now validated against env-driven inference model selection
- `unison-platform` now has a first-class local-source workflow:
  - `make up-local`
  - `make validate-golden`
- the default platform bring-up no longer depends on the missing `unison-updates` implementation
- the end-to-end golden path now validates successfully:
  - inference ready
  - first-admin bootstrap working
  - startup state converging to `READY_LISTENING`
  - onboarding state converging to `ready_to_finish: true`

Progress reflected from prior work and current verification:

- Priority 0: advanced
- P1.1: advanced
- P1.2: advanced
- P1.3: advanced
- P1.5: advanced
- P1.6: partially advanced

Important open gaps:

- `unison-updates` is still missing as a real implementation and remains optional behind a compose profile
- this restored plan content was recovered from a clipped email source; lower sections beyond the recovered excerpt still need reconstruction if the original full text is required

## Purpose

Translate the public UnisonOS vision into a production-quality delivery plan that gets the project from:

- evaluator/devstack-centric,
- partially stubbed,
- multi-repo research platform

to:

- downloadable,
- installable,
- supportable,
- trustworthy,
- and visibly aligned with the intended UnisonOS experience.

## Fundamental Product Understanding

Based on the GitHub Pages documentation, UnisonOS is trying to be:

- an intention-centric operating surface, not an app launcher or chatbot
- a calm, presence-first experience that reduces cognitive load
- local-first, privacy-preserving, and policy/consent-governed
- modality-complete, with no assumed primary interface
- capable of abstracting tools, legacy systems, and future embodiments behind a coherent experience

The stated product promise is not "a collection of services." It is:

- a person can install UnisonOS,
- express intent naturally,
- see or hear an experience that feels calm and coherent,
- trust how the system behaves,
- and successfully complete meaningful outcomes without wrestling with software structure.

## Non-Negotiable Experience Constraints

The docs establish these constraints:

- no app-centric primary flow
- no dashboard-as-product outcome
- no keyboard/screen dependency
- no hidden cloud dependency
- no unsafe or opaque high-trust behavior
- no "feature demo" that breaks trust or calmness

These are product constraints, not branding language. The implementation plan must preserve them.

## Production-Quality Definition

For UnisonOS, "production quality" should mean all of the following are true:

1. A person can install a supported release on a clearly documented target without reading internal docs.
2. First boot leads to a reliable onboarding flow, not a developer bring-up flow.
3. Core interaction works end to end with strong defaults:
   text and voice at minimum for the first production milestone.
4. The renderer expresses the intended calm, generated operating surface rather than a developer shell.
5. Capabilities are real, useful, and safe; they are not placeholders or thin demos.
6. Policy, consent, auth, storage, and audit are enforced in the actual runtime path.
7. Updates, logs, recovery, and support diagnostics exist.
8. Release artifacts are reproducible, verifiable, and tied to a compatibility matrix.

## Current Reality vs Vision

The public docs describe a mature edge-first operating surface, but the current codebase still shows major gaps:

- install and release flows are still alpha/evaluator-oriented
- many repos are active but not yet integrated into a polished product experience
- the renderer is a useful service shell, but not yet the complete intended operating surface
- several modality and capability paths remain stub-heavy or early-library-stage
- production topology, service contracts, and release packaging are not yet fully aligned
- the platform still lacks a narrow, production-ready "golden path" scope

## Strategic Recommendation

Do not try to make the entire vision production-ready at once.

The first production-quality outcome should target:

- one primary supported deployment target:
  Ubuntu 24.04 native on reference hardware
- two evaluator channels:
  WSL2 and Linux VM
- one primary interaction set:
  text + voice
- one primary operating surface:
  the calm renderer experience
- one primary set of valuable capabilities:
  local system help, personal briefing, communications summary/draft, and one safe browser-based legacy workflow

Defer from first production milestone:

- payments as a headline feature
- robotics and smart-home actuation
- sign, Braille, and BCI as first-class shipping experiences
- broad connector sprawl
- multi-agent orchestration as a person-facing differentiator

These can continue in parallel, but they should not block the first trustworthy installable experience.

## Golden Path Release Scope

The first release should prove these journeys end to end:

1. Install and boot UnisonOS on supported hardware.
2. Complete first-run onboarding for microphone, local models, and privacy/consent defaults.
3. Ask for a briefing and receive a calm multimodal response.
4. Ask for system help or diagnostics and get a reliable answer.
5. Connect one comms source and summarize/draft safely.
6. Run one browser-based outcome through VDI when no direct API exists.
7. Reboot, update, and recover without losing core functionality.

If these are not excellent, the rest of the vision will not matter.

## Priority 0 Milestone Contract

This section is the working contract for the first production-quality milestone.

### Milestone Name

Production Milestone 1:
- installable local-first UnisonOS on reference Ubuntu hardware

### Milestone Objective

Ship a release that lets a non-developer install UnisonOS on a supported machine, complete first-run setup, and experience the intended UnisonOS vision through a calm, trustworthy, voice-plus-renderer interaction model with a small set of real outcomes.

### Primary Supported Target

Primary supported target:
- Ubuntu 24.04 LTS native install on a published reference hardware profile

Reference hardware profile:
- x86_64 machine
- 8 CPU cores recommended
- 16 GB RAM recommended
- 100 GB SSD minimum practical target
- working microphone and speakers
- GPU optional for Milestone 1, but local inference profile must be documented for both CPU-only and GPU-enabled systems

### Secondary Evaluation Channels

Secondary evaluation channels:
- WSL2 on Windows 11
- Linux VM image

These channels are evaluation paths, not first-class production targets, for Milestone 1.

### Explicitly Unsupported for Milestone 1

Not in Milestone 1 support scope:
- bare-metal consumer installer as a polished turnkey path
- non-Ubuntu native installs
- ARM hardware
- robotics and smart-home actuation
- payments as a headline workflow
- sign, Braille, and BCI as polished end-user modalities
- multi-agent orchestration as a required person-facing feature

### Milestone 1 Product Shape

Milestone 1 is not "the whole platform."

It is:
- a local-first personal operating surface
- one person on one machine
- text plus voice as the complete first-class modalities
- a calm renderer as the primary perceptual surface
- a small, reliable set of useful capabilities

It is not:
- a generalized enterprise orchestration platform
- a broad connector marketplace
- a robotics platform
- an accessibility-modality-complete shipping release

### Milestone 1 Required Journeys

The release is only acceptable if all of these work end to end.

#### Journey 1: Install and Boot

Success definition:
- a person follows the public installation guide
- installs on the reference Ubuntu target
- reboots into a working UnisonOS environment
- can access the operating surface without reading internal docs

#### Journey 2: First-Run Onboarding

Success definition:
- first-run flow explains what UnisonOS is doing
- microphone setup is checked and confirmed
- local model availability is validated or guided to completion
- privacy, wakeword, and network-dependent capabilities are explicitly configured
- the person reaches a ready state with no ambiguous "developer setup" steps

#### Journey 3: Presence and First Interaction

Success definition:
- first-run presentation reflects the published doctrine
- the default state feels calm, present, and non-dashboard-like
- the first spoken or typed intent receives immediate acknowledgment
- the person gets a useful answer without needing to understand services, apps, or repos

#### Journey 4: Personal Briefing

Success definition:
- the system can provide a coherent local briefing
- output is rendered through the intended operating surface
- voice and text outputs remain aligned
- the interaction feels like an experience, not a service debug screen

#### Journey 5: System Help and Diagnostics

Success definition:
- the person can ask what machine they are on, basic health questions, or for a diagnostics summary
- capability selection is accurate and bounded
- answers are reliable enough to trust operationally

#### Journey 6: One Real Connector Outcome

Success definition:
- one communications connector can be onboarded explicitly
- the system can summarize recent messages and draft a reply safely
- secrets remain local and policy-governed
- failure cases are understandable and recoverable

#### Journey 7: One Real Legacy Workflow

Success definition:
- one browser-driven workflow can be executed through VDI safely
- the system can communicate progress and outcome coherently
- artifacts are persisted and retrievable when relevant

#### Journey 8: Reboot, Update, Recover

Success definition:
- reboot returns the system to a working state
- update flow is explicit and reversible
- a broken service or failed update has a documented recovery path

### Milestone 1 Capability Set

Required capabilities for Milestone 1:
- local greeting and orientation
- local device/system information
- local diagnostics summary
- daily/personal briefing
- one comms connector with summarize + draft
- one safe browser/VDI outcome

Allowed but non-blocking:
- richer capability inventory
- calendar integration
- advanced workflow design and recall

Explicitly deferred:
- payments
- broad third-party connector catalog
- physical actuation

### Milestone 1 Modality Contract

Required:
- text input
- voice input
- text output
- voice output
- renderer-based visual operating surface

Must degrade safely:
- voice unavailable
- microphone denied
- speaker unavailable
- display unavailable in evaluator channels

Deferred from first-class product readiness:
- sign
- Braille
- BCI
- gesture-first flows

### Release Gates

The release cannot ship unless all gates pass.

#### Gate A: Installability
- public docs are sufficient
- clean install succeeds on reference hardware
- no evaluator default credentials remain in supported production path

#### Gate B: Core Reliability
- all golden-path services pass health and readiness checks
- startup ordering is deterministic
- reboot preserves functional state

#### Gate C: Experience Fidelity
- first-run presence and first-turn interaction are doctrine-aligned
- primary surface is not a dashboard, admin console, or service shell
- confirmation flows for high-trust actions are explicit

#### Gate D: Safety and Trust
- auth, policy, consent, and storage are enforced on the actual golden path
- secrets are not stored in plaintext in config or manifests
- logs are redacted and supportable

#### Gate E: Capability Utility
- all required Milestone 1 capabilities succeed on a clean install
- connector onboarding is explicit and recoverable
- VDI workflow is bounded and observable

#### Gate F: Release Engineering
- versioned artifacts, manifest, and checksums are published
- compatibility matrix is updated
- rollback instructions are verified

### Definition of Done for Priority 0

Priority 0 is done when:
- this contract is accepted as the working scope
- every in-scope repo can map current work to Milestone 1 or deferred status
- acceptance tests are derived from the required journeys
- all new work is prioritized against these release gates

## Priority 0 Locked Decisions

These decisions are now locked for Milestone 1 unless a later issue forces revision.

### Locked Decision 1: Reference Hardware Profile

Milestone 1 reference profile:
- Ubuntu 24.04 LTS
- x86_64
- 8 physical or logical CPU cores
- 16 GB RAM
- 100 GB SSD
- integrated or discrete GPU optional
- microphone and speakers required

Rationale:
- this is achievable for local inference and Dockerized service runtime without forcing high-end hardware
- it is materially more realistic than the lighter evaluator minimums in the current docs
- it gives enough headroom for renderer, orchestrator, local inference, storage, and observability without turning the first release into a workstation-only product

### Locked Decision 2: CPU-Only Local Inference Baseline

Milestone 1 CPU-only baseline:
- provider: Ollama
- text model class: compact instruction-tuned local model in the Qwen family
- validated local workspace profile: `qwen3.5:0.8b`
- one documented default CPU-safe model profile
- one documented recommended higher-quality profile for GPU-enabled machines

Operational rule:
- Milestone 1 must work fully offline and locally on the CPU-safe baseline
- cloud fallback remains optional and disabled by default

Rationale:
- the public docs already position local-first Ollama as the default inference provider
- production scope needs one known-good baseline, not open-ended provider choice
- CPU-only success is critical for trust, installability, and repeatability
- the local workspace was revalidated against env-driven model selection using `qwen3.5:0.8b`

### Locked Decision 3: Wakeword Default

Wakeword posture for Milestone 1:
- disabled by default
- explicitly opt-in during onboarding
- reversible from settings/profile without manual config editing

Rationale:
- the public security and experience docs emphasize calmness, privacy, and explicit consent
- wakeword is useful, but not required to prove the first trustworthy operating-surface release
- shipping it off by default avoids undermining trust during first-run evaluation

### Locked Decision 4: First Real Communications Provider

First real connector path:
- Gmail

Milestone 1 comms capability scope:
- explicit Gmail onboarding
- inbox/message fetch
- summarization
- draft reply
- compose draft

Not required for Milestone 1:
- send by default without explicit confirmation
- multi-provider support
- calendar integration as a release blocker

Rationale:
- Gmail is already the clearest code-and-doc path in `unison-comms`
- it is common enough to create a credible first real outcome
- narrowing to one provider allows real hardening of secrets, onboarding, normalization, and failure handling

### Locked Decision 5: First Real VDI Workflow

First real legacy browser workflow:
- bounded document retrieval and download from an allowlisted web destination

Concrete Milestone 1 flow:
- navigate to an allowlisted URL
- optionally click through one or more known selectors
- download a targeted file or report
- store the artifact through `unison-storage`
- present status and artifact result through the operating surface

What is out of scope for Milestone 1:
- open-ended autonomous browsing
- arbitrary site exploration
- multi-account general browser automation
- high-risk transactional web flows

Rationale:
- this fits the current `browse` and `download` task model in `unison-agent-vdi`
- it proves the value of legacy-actuation fallback without requiring a general browser agent
- it keeps policy, auditability, and failure recovery bounded enough to productionize

## Priority 0 Scope Lock

Milestone 1 is now locked to:

- primary target:
  Ubuntu 24.04 native on the reference hardware profile
- evaluation targets:
  WSL2 and Linux VM
- interaction:
  text + voice
- visual surface:
  calm renderer
- inference:
  local-first Ollama with CPU-safe default
- wakeword:
  off by default, opt-in
- first connector:
  Gmail
- first VDI legacy outcome:
  bounded document retrieval/download from an allowlisted site

Anything outside that scope must justify itself against Milestone 1 release gates before being treated as priority work.

## Prioritized Implementation Plan

### Priority 0: Freeze the First Production Target

Objective:
- reduce scope ambiguity and force real release decisions

Deliverables:
- choose the primary supported hardware profile
- define the exact first-release golden journeys
- publish a versioned "production milestone contract"
- mark all non-blocking areas as post-milestone

Repos:
- `project-unisonos.github.io`
- `unison-docs`
- `unison-platform`
- `unison-workspace`

Exit criteria:
- one target hardware profile is named
- one release artifact set is named
- one acceptance test matrix exists
- all repos align to the same first-release scope

### Priority 1: Make Installation and First Boot Real

Objective:
- get from evaluator artifact to installable product

Deliverables:
- production-grade installer flow for the primary target
- first-boot service bring-up and readiness gating
- onboarding flow for local model availability, mic permissions, and core privacy defaults
- removal of evaluator defaults such as placeholder credentials
- versioned release manifest, checksums, and rollback instructions

Repos:
- `unison-platform`
- `unison-workspace`
- `project-unisonos.github.io`
- `unison-os`

Exit criteria:
- a new machine can be installed by following public docs only
- first boot ends in a usable operating surface
- service startup ordering is deterministic
- failures surface clearly and recover cleanly

### Priority 1 Execution Checklist

This section breaks Priority 1 into concrete implementation work that can be assigned and tracked.

#### P1.1 Unify the Supported Install Path

Goal:
- one canonical installation path for the primary Ubuntu target

Required changes:
- choose one native installation mechanism and retire the parallel "alpha evaluator" ambiguity
- align `unison-platform/docs/install.md` and `docs/deployment/ubuntu-native.md`
- stop pointing people at incomplete or developer-only install surfaces
- ensure the public docs, platform repo, and release assets all describe the same path

Repos:
- `unison-platform`
- `project-unisonos.github.io`

Done when:
- there is one public Ubuntu install document
- it references one supported artifact and one supported bootstrap process
- all conflicting or evaluator-only instructions are clearly labeled or removed from the production path

Current progress:
- canonical path selected: `unison-platform/installer/install-native.sh`
- `unison-platform/docs/install.md` now points to Ubuntu native first and labels WSL2, VM, and bare metal as evaluation-only
- public release docs now reflect Ubuntu native as the supported Milestone 1 route
- workspace validation confirmed the native/local Ubuntu path can be brought up and revalidated end to end

#### P1.2 Replace Evaluator Defaults with Production-Safe Install Behavior

Current progress:
- first-admin bootstrap is now explicit and validated in the live runtime path
- startup readiness now reflects live service convergence instead of a stale startup snapshot
- local onboarding can now converge to `ready_to_finish: true`
- default runtime behavior no longer assumes missing `updates` implementation

#### P1.3 Deterministic Bring-Up and First-Boot Gating

Current progress:
- `unison-platform` compose/runtime path has been hardened for deterministic local bring-up
- `unison-orchestrator` `/startup/status` now re-checks live renderer/auth readiness
- validated golden path now reaches:
  - inference ready
  - bootstrap complete
  - startup `READY_LISTENING`
  - onboarding `ready_to_finish: true`

#### P1.5 Local Model Baseline and Inference Selection

Current progress:
- `unison-platform/compose/compose.yaml` is env-driven for inference model selection
- local Ubuntu runtime restored with Ollama reachable from Docker on `127.0.0.1:21434` via host bridge mapping
- validated model in the current workspace runtime: `qwen3.5:0.8b`
- `make validate-golden` now checks inference readiness and model identity

#### P1.6 Onboarding Reliability and Golden-Path Validation

Current progress:
- `make up-local` added as the first-class local-source developer/runtime path
- `make validate-golden` added as a reproducible end-to-end validator
- `unison-workspace` submodule pins were aligned to the validated runtime SHAs
- remaining gap: reconstruct any unrecovered lower-plan tasks and extend acceptance checks to fresh-machine install testing

## Recovery Note

The source email provided for this restoration was clipped after the beginning of Priority 1. This file now preserves the recovered content and incorporates verified status updates from the current workspace, but additional lower-priority sections may still need to be restored from the original full plan if they are required verbatim.
