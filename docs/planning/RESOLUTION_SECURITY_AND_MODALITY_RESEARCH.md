# Resolution security and modality research preparation

Status: software security gates and research protocol prepared; real pilot and
participatory execution pending

Date: 2026-08-15

## Resolution threat model

The open-world resolver may propose broadly but gains no authority from model
output, retrieved text, tool output, repetition, or participant approval of a
candidate concept. Identity, context access, disclosure, package installation,
and consequential action remain governed by their existing authorities.

| Threat | Required control | Executable evidence |
| --- | --- | --- |
| Private prompt or answer enters pilot telemetry | Strict content-free contract and unknown-field rejection | Forbidden `prompt` fixture fails closed |
| Cross-person pilot observation or summary | Authenticated participant binding and person-filtered storage | Repository cross-person denial test |
| Candidate poisoning with unrelated attempts | Every evidence attempt belongs to the actor and matches one fingerprint | Mixed-fingerprint denial test |
| Candidate creation from one event or duplicated identifiers | At least two distinct evidence attempts | Contract negative test |
| Candidate silently becomes executable | Sequential review, signing, canary, promotion, and rollback gates | Existing skipped-transition denial test |
| Malformed or substituted package identity | SHA-256 digest validation and named reviewers | Contract validation and transition tests |
| Prompt injection expands tool or disclosure authority | Resolver output remains a typed proposal; tools revalidate authority | Existing bounded-resolution and policy boundary suites |
| Aggregated metrics conceal harm | Boundary incidents are recorded and counted, never hardcoded | Pilot summary incident-count test |
| Revoked adapter or candidate continues operating | Signed package registry, revocation, planner eligibility, and rollback | Required before shared promotion |

No organization-wide fingerprint aggregation, shared promotion, or autonomous
skill installation is authorized by this slice. Those require privacy review,
minimum cohort protections, poisoning analysis, revocation drills, and a named
human promotion decision.

## Real pilot protocol

Participation must be explicit, scoped, revocable, and understandable in the
participant's native modality. Start with person-local use. Do not preselect
requests to make the resolver appear successful. Private requests, outputs,
comments, and artifacts remain in the person's governed research record.

The content-free signal records outcome, usefulness, elapsed time, interaction
turns, clarifications, corrections, generic refusal, candidate suggestion and
relevance, trust, privacy comprehension, and boundary incidents. Reviewers stop
the pilot immediately for cross-person disclosure, unauthorized external
action, concealed uncertainty, or unsafe advice.

No candidate advances beyond `proposed` during the initial pilot. Human review
determines whether suggestion precision, usefulness, prompt burden, and trust
justify a later canary design.

## Participatory conversational and Braille protocol

Recruit conversational and Braille participants through accessible materials
and compensate expertise. Participants choose input and output forms, recording
permissions, retention, and withdrawal. Use representative devices when making
device claims.

Test novel requests, candidate explanation, accept, modify, defer and reject,
interruption, correction, modality switching, privacy-sensitive output,
uncertainty, partial outcomes, cancellation, and recovery. Measure equivalent
understanding and control, time and effort, clarification quality, prompt
fatigue, trust, privacy comprehension, and recovery success.

Conversation and Braille are independent native compositions. Neither is a
translation of a visual screen. A result passes only if participants can reach
equivalent meaning, agency, safety, continuity, privacy, and recovery.

## Sign-language research preparation

Deaf contributors and sign-language researchers must shape the task model
before technology selection. Research must distinguish sign recognition, sign
generation, Deaf conversational norms, facial and spatial grammar, regional
language variation, interpreter involvement, and failure recovery. Camera data
is sensitive capability input and cannot be retained or reused by default.

A sign adapter integrates through `modality-adapter.v1` and SEM. It does not
consume a visual layout and cannot infer consent or identity from signing.

## BCI research boundary

BCI remains exploratory. Before implementation, qualified reviewers must define
signal meaning, calibration, false activation handling, intentional control,
fatigue, device trust, raw signal retention, inferred neurological attributes,
emergency stopping, and medical-adjacent claim boundaries.

A BCI adapter may emit typed input observations through the common adapter
contract. It cannot directly authorize actions, and model confidence cannot
replace explicit confirmation. Raw neural signals and derived features require
separate governed data classes, retention, deletion, export, and research
consent decisions.

## Exit gates

- Real pilot execution produces content-free aggregate evidence and private
  participant records without boundary incidents.
- Participatory plans receive accessibility, privacy, and research review.
- Shared promotion remains disabled until revocation and rollback are tested.
- Sign and BCI projects remain unclaimed until their own participatory, device,
  security, and safety evidence passes.
