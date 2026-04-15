# Milestone 1 Acceptance Matrix

This document converts `UNISONOS_PRODUCTION_IMPLEMENTATION_PLAN.md` into concrete Milestone 1 acceptance coverage.

Scope note:
- this file mixes two related but different evidence domains: broader platform validation material and the current `unison-workspace` snapshot
- references to `unison-platform` below describe the larger Milestone 1 delivery path, not something fully contained inside this workspace checkout
- use this matrix as the Milestone 1 target-state acceptance map, not as proof that `unison-workspace` alone currently contains every required repo, script, or validation asset

It reflects the verified workspace/runtime state as of the current validated Ubuntu 24.04 local bring-up.

## Scope

Locked Milestone 1 scope:

- primary target: Ubuntu 24.04 native on x86_64
- evaluation targets: WSL2 and Linux VM
- first-class modalities: text + voice
- primary surface: renderer-led operating surface
- inference baseline: local-first Ollama
- wakeword: off by default, opt-in
- first real comms provider: Gmail
- first real legacy workflow: bounded VDI document retrieval/download

## Current Acceptance Assets

Existing automated assets:

Platform-scoped assets outside the current `unison-workspace` submodule set:

- `unison-platform/scripts/validate-golden-path.sh`
- `unison-platform/qa/test_smoke.py`
- `unison-platform/qa/test_native_install_acceptance.py`
- `unison-platform/installer/unisonctl.sh` health/doctor checks

Workspace-visible or service-level evidence available from repos present in this workspace:

- authenticated briefing acceptance through `POST /ingest` with `intent=dashboard.refresh`
- renderer onboarding/status endpoints
- service health/readiness endpoints
- `unison-devstack/scripts/e2e_smoke.py`
- `unison-devstack/scripts/test_multimodal.py`

Validated current local runtime:

- inference `ready: true` with model `qwen3.5:0.8b`
- auth bootstrap enabled and first admin created
- orchestrator startup converges to `READY_LISTENING`
- renderer onboarding converges to `ready_to_finish: true`

## Journey Matrix

### Journey 1: Install and Boot

Evidence boundary note:
- this journey is primarily platform-scoped today, not workspace-scoped

Acceptance requirement:
- public docs are sufficient for supported Ubuntu install
- installed stack reaches a working operating surface after first boot

Current coverage:
- `unison-platform/docs/deployment/ubuntu-native.md`
- `unison-platform/qa/test_native_install_acceptance.py`
- `unison-platform/installer/unisonctl.sh doctor`
- `unison-platform/installer/unisonctl.sh health`

Current status:
- `partial`

What is validated now:
- local Ubuntu runtime bring-up and deterministic service convergence
- golden-path service validation from a live stack

Remaining gap:
- fresh-machine install acceptance still needs repeated validation from a clean Ubuntu host, not only an already prepared developer machine

### Journey 2: First-Run Onboarding

Acceptance requirement:
- microphone, speakers, local model, wakeword posture, and first-admin setup converge without developer-only ambiguity

Current coverage:
- `unison-platform/scripts/validate-golden-path.sh`
- `unison-platform/qa/test_native_install_acceptance.py`
- `unison-experience-renderer` onboarding endpoints

Current status:
- `advanced`

What is validated now:
- `/bootstrap/status`
- `/startup/status`
- `/onboarding-status`
- onboarding profile persistence
- `ready_to_finish: true`

Remaining gap:
- browser-mediated microphone/speaker checks still need a documented manual acceptance pass on clean hardware

### Journey 3: Presence and First Interaction

Acceptance requirement:
- first-run experience feels renderer-led, calm, and not like a service console

Current coverage:
- renderer endpoint readiness
- startup convergence checks

Current status:
- `partial`

What is validated now:
- renderer is the primary runtime surface
- orchestrator startup no longer stalls on stale renderer readiness

Remaining gap:
- doctrine-aligned visual/interaction fidelity is still mostly manual review, not testable acceptance

### Journey 4: Personal Briefing

Acceptance requirement:
- local briefing works end to end through orchestrator, inference, and renderer

Current coverage:
- `unison-platform/qa/test_native_install_acceptance.py`
- authenticated orchestrator `POST /ingest` briefing flow
- renderer experience evidence via `/experiences`

Current status:
- `advanced`

What is validated now:
- authenticated briefing request through orchestrator
- briefing cards returned from the live API
- renderer receives briefing experiences with `origin_intent=dashboard.refresh`

Remaining gap:
- dashboard persistence/readback through `unison-context` still needs hardening as a separate reliability item

### Journey 5: System Help and Diagnostics

Acceptance requirement:
- person can ask for local diagnostics and receive bounded, reliable output

Current coverage:
- `unisonctl doctor`
- `unisonctl health`
- service health/readiness endpoints

Current status:
- `partial`

Remaining gap:
- no end-to-end natural-language diagnostics flow acceptance yet

### Journey 6: One Real Connector Outcome

Acceptance requirement:
- Gmail onboarding, summarize, and draft flow works with explicit setup and bounded failure handling

Current coverage:
- none at Milestone 1 acceptance level

Current status:
- `gap`

Remaining gap:
- Gmail connector onboarding and summarize/draft acceptance is not yet represented in platform or workspace acceptance assets

### Journey 7: One Real Legacy Workflow

Acceptance requirement:
- bounded VDI document retrieval/download works and stores artifacts safely

Current coverage:
- `unison-platform/qa/test_native_install_acceptance.py`
- live `agent-vdi` download API contract check
- artifact ID return path from `agent-vdi`
- stored artifact retrieval from `unison-storage`
- renderer-visible actuation outcome for the VDI download path

Current status:
- `partial`

Remaining gap:
- allowlisted-domain policy is not yet exercised in live Milestone 1 acceptance
- the current acceptance exercises the service-level VDI path directly rather than the full orchestrator-driven legacy workflow

### Journey 8: Reboot, Update, Recover

Evidence boundary note:
- this journey depends heavily on platform-owned tooling and is not fully evidenced by the current `unison-workspace` snapshot alone

Acceptance requirement:
- reboot returns to service
- update path is explicit and recoverable
- recovery tools work from supported install path

Current coverage:
- `unisonctl` operational commands
- native-install acceptance shape checks
- `unison-platform/scripts/validate-recovery-path.sh`
- post-restart briefing and VDI acceptance when Milestone 1 test credentials are supplied
- live updates policy/plan/apply/status acceptance when the `updates` profile is enabled
- updates check/plan are now driven by a generated platform release manifest in the local-source path
- updates apply/rollback now persist a concrete release-history ledger with prior-target metadata
- updates apply/status now return a concrete no-op compose execution plan derived from pinned image metadata
- updates apply/rollback now emit persisted staged override artifacts for the target and inverse rollback plan
- platform tooling can now install an emitted apply artifact as a next-boot staged compose override
- platform tooling can finalize a staged boot and feed the applied target back into `unison-updates` as last-known-good
- platform now includes a scripted validator for the full stage -> finalize -> last-known-good lifecycle

Current status:
- `partial`

Remaining gap:
- full reboot persistence is still not exercised explicitly
- real package/image promotion and rollback are not yet exercised end to end
- `unison-updates` still remains optional behind a compose profile in the platform stack

## Release Gate Matrix

Interpretation note:
- gate status values below describe the intended Milestone 1 program state across workspace plus platform evidence
- they should not be read as claims that the current `unison-workspace` checkout independently proves each gate end to end

### Gate A: Installability

Status:
- `advanced`

Evidence:
- canonical Ubuntu native install path documented
- local-source bring-up path added with `make up-local`
- golden-path validation added with `make validate-golden`

Remaining gap:
- repeated clean-host install verification

### Gate B: Core Reliability

Status:
- `advanced`

Evidence:
- deterministic startup convergence fixed
- live renderer/auth re-checking in orchestrator startup status
- validated `READY_LISTENING` startup state

Remaining gap:
- full reboot persistence still needs repeatable acceptance coverage

### Gate C: Experience Fidelity

Status:
- `partial`

Evidence:
- renderer-led startup/onboarding path is active

Remaining gap:
- calmness/presence quality still lacks objective acceptance criteria beyond endpoint readiness

### Gate D: Safety and Trust

Status:
- `advanced`

Evidence:
- first-admin bootstrap is explicit
- wakeword remains opt-in posture
- auth bootstrap and onboarding are convergent on the live path

Remaining gap:
- connector secret handling and release-manifest hardening still need explicit Milestone 1 acceptance criteria

### Gate E: Capability Utility

Status:
- `gap`

Evidence:
- inference and onboarding are validated

Remaining gap:
- briefing, Gmail, and bounded VDI outcome are not yet covered by acceptance tests

### Gate F: Release Engineering

Status:
- `partial`

Evidence:
- canonical install docs and local validation path exist

Remaining gap:
- versioned artifacts, manifest/checksum publication, and rollback verification remain incomplete

## Next Acceptance Work

Highest-value next additions:

1. Add a real native-install acceptance runbook for clean Ubuntu 24.04 machines:
   install, reboot, validate, recover.
2. Add a bounded acceptance harness for Journey 7:
   allowlisted VDI document retrieval into `unison-storage`.
3. Add Gmail onboarding and summarize/draft acceptance:
   explicit secret/bootstrap handling, failure cases, and draft confirmation.
4. Harden dashboard persistence/readback between orchestrator and context so briefing cards are durably queryable as well as renderer-visible.

## Execution Rule

No new Milestone 1 work should be treated as release-critical unless it maps to one of:

- an uncovered required journey
- a failing release gate
- a reliability problem in the validated Ubuntu native golden path
