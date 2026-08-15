# Resolution pilot and modality roadmap

Status: pilot tooling implemented; real opt-in execution pending

Date: 2026-08-15

## Program objective

Prove that Unison can attempt unfamiliar requests naturally, identify genuinely
repeatable structures without capturing private content, and offer a clear
person-controlled path toward deterministic capability. No pilot candidate is
authorized to execute or become a shared skill.

## Slice 1: real opt-in unfamiliar-request pilot

The pilot uses ordinary requests that are not selected to match an existing
workflow. Participation is explicit and revocable. Each attempt retains its
private request and artifacts in the person's governed context. The evaluation
stream contains only `resolution-pilot-signal.v1` measurements.

Measure outcome, usefulness, elapsed time, interaction turns, clarifications,
corrections, generic refusal, trust and privacy comprehension, candidate
suggestion frequency, and candidate relevance. Do not export prompts, answers,
domain labels, sources, health or financial attributes, or inferred interests.

The initial decision gate requires human review of candidate precision, generic
refusal rate, boundary incidents, participant comments held in private research
records, and whether suggestions feel useful rather than intrusive. Shared
promotion remains prohibited.

## Slice 2: candidate review experience

When a repeatable pattern is detected, Unison explains why it noticed the
pattern, the outcome that could become repeatable, required data and authority,
and whether it would remain person-local or enter a separately governed
contribution process. The person can accept, modify, defer, or reject.

Conversation, Braille, and visual expressions consume the same semantic review
payload but compose it independently. Acceptance advances only the reviewed
candidate lifecycle. It does not grant executable authority.

## Slice 3: personal development topology proof

Windows and Codex remain the control plane. The Ubuntu dev NUC is the canonical
Python 3.12 Linux build and integration host. `scripts/remote-dev.ps1` supports
connectivity inspection, clean recursive clone, bootstrap, validation, unit and
boundary tests, doctor, and status operations over SSH or Tailscale.

The proof record must include host and Python versions, exact Git revisions,
submodule status, commands, results, recovery actions, and confirmation that no
credential or private network address entered the repository.

The initial 2026-08-15 connection attempt to the configured `dev-nuc` SSH alias
timed out in batch mode before returning host information. No remote state was
changed. The inventory-bound proof therefore remains pending network or SSH
availability and must not be represented as complete.

## Common modality integration point

All modality projects integrate at the Semantic Experience Model and expression
plan boundary. A signed `modality-adapter.v1` manifest declares input and output
direction, supported SEM and expression versions, capability identifiers,
permissions, device classes, fallbacks, package digest, and signer.

An adapter may implement conversation, visual presentation, Braille, sign
language, haptics, switch or AAC input, BCI, or a future modality. It cannot
become an authority for identity, consent, policy, disclosure, or action. It
returns typed observations or native expressions with provenance. The planner
owns selection and fallback, while semantic equivalence tests ensure that a new
adapter preserves comprehension, agency, safety, continuity, privacy, and
recovery.

Sign and BCI development require separate repositories or clearly owned
components, threat models, simulated fixtures, and acceptance evidence. Camera,
neural-signal, biometric, or medical-adjacent data requires explicit capability
and consent review. No future adapter needs to imitate a visual screen.

## Remaining tracked slices

1. Threat-model open-world resolution, candidate poisoning, authority growth,
   private fingerprint leakage, package compromise, revocation, and rollback.
2. Prepare and approve participatory conversational and Braille research,
   including representative devices, consent, equivalent-outcome measures,
   interruption, recovery, privacy, and prompt fatigue.
3. After the interim workstation arrives, inventory it and run the deferred GPU,
   model, concurrency, rebuild, restore, power, thermal, acoustic, and resilience
   qualification groups.
4. Define sign-language adapter research with Deaf contributors before choosing
   capture, recognition, or expression technology.
5. Keep BCI exploratory until input semantics, consent, error handling,
   neurological-data governance, device trust, and safety boundaries receive
   qualified review.

## Evidence and claim boundaries

Contract tests and synthetic expressions are software evidence. The remote
workflow is integration evidence only after an inventory-bound NUC run. Real
pilot outcomes are pilot evidence, not production readiness. Modality support
requires representative-device and participatory evidence before public claims.
