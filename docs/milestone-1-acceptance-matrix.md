# Milestone 1 Acceptance Matrix

This document converts `UNISONOS_PRODUCTION_IMPLEMENTATION_PLAN.md` into concrete Milestone 1 acceptance coverage.

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

- `unison-platform/scripts/validate-golden-path.sh`
- `unison-platform/qa/test_smoke.py`
- `unison-platform/qa/test_native_install_acceptance.py`
- `unison-platform/installer/unisonctl.sh` health/doctor checks
- authenticated briefing acceptance through `POST /ingest` with `intent=dashboard.refresh`

Validated current local runtime:

- inference `ready: true` with model `qwen3.5:0.8b`
- auth bootstrap enabled and first admin created
- orchestrator startup converges to `READY_LISTENING`
- renderer onboarding converges to `ready_to_finish: true`

## Journey Matrix

### Journey 1: Install and Boot

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
- `agent-vdi` readiness only

Current status:
- `gap`

Remaining gap:
- no Milestone 1 acceptance test yet exercises the allowlisted VDI download flow end to end

### Journey 8: Reboot, Update, Recover

Acceptance requirement:
- reboot returns to service
- update path is explicit and recoverable
- recovery tools work from supported install path

Current coverage:
- `unisonctl` operational commands
- native-install acceptance shape checks

Current status:
- `partial`

Remaining gap:
- reboot/update/recovery need explicit acceptance scenarios on a real installed stack
- `unison-updates` is still missing and remains optional behind a compose profile

## Release Gate Matrix

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
- reboot and recovery scenarios need repeatable acceptance coverage

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
- versioned artifacts, manifest/checksum publication, rollback verification, and `unison-updates` implementation remain incomplete

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
