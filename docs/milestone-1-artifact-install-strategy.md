# Milestone 1 Artifact and Install Strategy

This document defines the artifact, install, and release-shape decisions for the first installable UnisonOS milestone.

It exists to reconcile three realities that currently coexist across the repos:

- the broader public alpha/evaluation artifact story
- the newer Milestone 1 production-track plan
- the current state of real installer and validation assets in `unison-platform`

The goal is to remove ambiguity about what the first installable product actually is.

## 1. Purpose

Milestone 1 is not trying to ship every UnisonOS target or modality.

Milestone 1 is trying to ship one trustworthy, installable, local-first UnisonOS system that a non-developer can install on a supported machine and use successfully.

This document locks:

- the canonical install path
- the primary artifact strategy
- the supported target
- the evaluation-only targets
- the minimum installable runtime profile
- the release acceptance expectations
- the documentation reconciliation work required across public and repo-local docs

## 2. Canonical Install Decision

Canonical Milestone 1 install route:

- Ubuntu 24.04 native install on x86_64

Canonical installer and control surface:

- installer: `unison-platform/installer/install-native.sh`
- operations CLI: `unison-platform/installer/unisonctl.sh`
- primary install docs:
  - `unison-platform/docs/install.md`
  - `unison-platform/docs/deployment/ubuntu-native.md`

This is the primary supported installable product path for Milestone 1.

## 3. Artifact Strategy

### 3.1 Primary artifact

The primary Milestone 1 artifact should be a native Ubuntu installation bundle centered on the canonical installer flow.

Acceptable packaging forms for this milestone include:

- native installer bundle staged from `unison-platform`
- versioned platform bundle plus `install-native.sh`
- release assets sufficient to drive the documented Ubuntu native install path

The important constraint is not branding of the package shape.
The important constraint is that the public install path is singular, documented, reproducible, and supportable.

### 3.2 Evaluation-only artifacts

The following remain useful, but they are evaluation channels, not the canonical Milestone 1 install route:

- WSL2 artifact
- Linux VM artifact
- bare-metal ISO artifact

These may continue to exist for:

- demos
- developer evaluation
- hardware exploration
- packaging experiments

They must be labeled clearly as evaluation-only until they satisfy the same acceptance and support expectations as the native Ubuntu path.

### 3.3 Release publication expectations

Each Milestone 1 release should publish at minimum:

- one canonical Ubuntu native install path
- release notes
- a versioned manifest / bill of materials
- checksums
- compatibility notes
- recovery / rollback notes

Additional evaluator artifacts may be attached, but they must not obscure the supported install path.

## 4. Supported Target

Primary supported target:

- Ubuntu 24.04 LTS
- x86_64
- reference machine profile aligned with the Milestone 1 production plan
- local microphone and speakers
- local-first inference profile supported

Milestone 1 support intent:

- one person
- one machine
- local-first runtime
- text + voice as first-class modalities
- renderer-led operating surface

## 5. Evaluation Targets

Allowed evaluation targets:

- WSL2 on Windows 11
- Linux VM image
- bare-metal ISO installer

These channels are explicitly not the canonical supported Milestone 1 route unless and until the program reclassifies them.

## 6. Minimum Installable Runtime Profile

Milestone 1 should ship a narrow runtime profile that optimizes for successful installation and a trustworthy end-to-end experience.

### 6.1 Required core services

The first installable profile should include at least:

- `postgres`
- `redis`
- `auth`
- `orchestrator`
- `context`
- `policy`
- `storage`
- `inference`
- `experience-renderer`
- `io-core`
- `io-speech`
- `comms`
- `actuation`
- `agent-vdi`

### 6.2 Likely required integration services

Include these when current contracts require them for the golden path:

- `consent`
- `intent-graph`
- `context-graph`

### 6.3 Explicitly non-blocking or excluded by default

Do not treat these as required for the first installable profile unless a concrete runtime dependency proves otherwise:

- `io-bci`
- `io-braille`
- `io-sign`
- `network-vpn`
- broad observability extras
- experimental or stub-heavy connectors
- optional update services that are not yet release-ready

### 6.4 Runtime profile requirements

The installable profile must have:

- deterministic service set
- deterministic startup ordering
- generated or explicitly supplied production-safe secrets
- persistent data locations
- health/readiness checks tied to the install profile
- a documented first-start flow
- a documented recovery path

## 7. Milestone 1 Required User Journeys

The first binary is only useful if these journeys work end to end:

1. Install on a clean supported Ubuntu machine.
2. Start the system and reach a ready state without developer-only intervention.
3. Complete first admin bootstrap safely.
4. Reach the renderer-led operating surface.
5. Complete a first text interaction.
6. Complete a first voice interaction.
7. Receive a coherent personal briefing.
8. Use the first comms flow safely (Gmail onboarding, summarize, draft).
9. Complete one bounded VDI document retrieval/download flow.
10. Reboot and return to a ready state.
11. Use health/doctor/recover tooling successfully.

## 8. Release Acceptance Checklist

### 8.1 Installability

- clean-machine install succeeds from public docs only
- no internal repo knowledge is required
- no unsafe template defaults remain before first start
- install creates persistent config/data structure correctly

### 8.2 First boot and onboarding

- stack converges deterministically
- first admin bootstrap is explicit and one-time
- local model state is validated or guided clearly
- onboarding does not look like a developer bring-up flow

### 8.3 Experience fidelity

- renderer is the primary surface
- first interaction feels product-like rather than service-like
- core failures are bounded, visible, and understandable

### 8.4 Capability utility

- briefing path passes
- diagnostics/help path passes
- Gmail onboarding + summarize + draft path passes
- bounded VDI retrieval/download path passes

### 8.5 Recovery and operations

- reboot persistence passes
- `unisonctl health` passes
- `unisonctl doctor` produces actionable output
- `unisonctl recover` returns the system to service cleanly

### 8.6 Release engineering

- versioned artifact is published
- manifest / bill of materials is published
- checksums are published
- release notes are published
- compatibility matrix is updated
- rollback / recovery instructions are verified

## 9. Documentation Reconciliation Required

The current repo landscape contains both a newer native-install Milestone 1 story and an older alpha artifact story.

Both can continue to exist, but they must not compete for the same user expectation.

### 9.1 Canonical sources that already align well

These already support the intended Milestone 1 direction:

- `unison-platform/docs/install.md`
- `unison-platform/docs/deployment/ubuntu-native.md`
- `unison-platform/installer/install-native.sh`
- `unison-platform/installer/unisonctl.sh`
- `UNISONOS_PRODUCTION_IMPLEMENTATION_PLAN.md`
- `docs/milestone-1-acceptance-matrix.md`

### 9.2 Sources that need explicit review or revision

These still present or imply an alpha evaluator artifact set as the main delivery story:

- `unison-docs/dev/releases/evaluate-alpha.md`
- `unison-docs/dev/releases/alpha-0.5.0.md`
- `project-unisonos.github.io` install/download/release pages
- any repo README that frames WSL2, VM, or ISO images as co-equal with the primary native install path

### 9.3 Required documentation outcomes

Public and repo-local docs should be updated so they clearly state:

- the supported Milestone 1 install path is Ubuntu native
- WSL2, VM, and bare-metal image artifacts are evaluation-only
- the first installable product is a narrow local-first system, not a broad all-target release
- release assets and release notes should foreground the canonical supported route

## 10. Immediate Follow-Up Work

### 10.1 Product/release alignment

- confirm the exact first-binary runtime service list in `unison-platform`
- confirm which services are strictly required versus still dev/evaluator extras
- bind install acceptance to that exact profile

### 10.2 Documentation audit

Perform a doc audit across:

- `project-unisonos.github.io`
- `unison-docs`
- `unison-platform`
- `unison-workspace`

Expected outputs:

- list of pages that still present the old artifact story as primary
- list of pages that already align with the canonical install path
- required wording changes to remove ambiguity

### 10.3 Release engineering alignment

- verify the release workflow emits assets that support the canonical native install path cleanly
- ensure release notes foreground the supported route first
- ensure manifests, checksums, and compatibility information are tied to the supported artifact strategy

## 11. Decision Summary

Locked for Milestone 1 unless explicitly revised:

- canonical supported install path: Ubuntu 24.04 native on x86_64
- canonical installer: `unison-platform/installer/install-native.sh`
- canonical control CLI: `unisonctl`
- WSL2, Linux VM, and bare-metal ISO remain evaluation-only
- first installable product must ship a narrow runtime profile and pass install, first-run, core journey, and recovery acceptance
- public docs must foreground the canonical route and demote evaluator artifacts accordingly
