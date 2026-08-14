# Unison resolution and skill evolution

Status: **Accepted product and architecture direction; implementation planning open**  
Accepted: 2026-08-14  
Related decision: `AD-056` in
[UNISON_ARCHITECTURE_DECISIONS.md](UNISON_ARCHITECTURE_DECISIONS.md)

## Purpose

Unison prefers deterministic execution where it improves safety, authority,
consistency, cost, latency, inspectability, and recovery. That preference must
not make the system feel like a menu of preprogrammed commands. People should
be able to express unfamiliar goals naturally in any supported modality and
receive a serious attempt at resolution.

The system is therefore open-world in problem solving and closed-world in
authority:

> Unison may reason, research, compose, experiment, and propose broadly. It may
> read, disclose, persist, or act only through explicit governed authority.

## Experience promise

Unison should:

- focus on the person's intended outcome rather than require a known command;
- accept natural, incomplete, or unfamiliar requests in any supported input
  modality;
- use available context to reduce unnecessary questioning without guessing
  identity, permission, recipients, or consequential facts;
- try more than one safe route when the obvious route is unavailable;
- explain uncertainty and constraints without presenting a generic refusal as
  the first response;
- provide useful partial progress, research, a plan, a draft, a simulation, or
  a human handoff when direct completion is unavailable;
- preserve semantic continuity while changing algorithms, tools, models, or
  modalities; and
- learn structurally from repeated work without silently converting personal
  behavior into authority or globally shared training data.

Natural interaction does not mean hiding important boundaries. Exact
recipients, disclosures, costs, risks, uncertainty, confirmation, cancellation,
and recovery remain visible when material.

## Resolution ladder

For each bounded outcome or subproblem, Unison should consider the following
routes. The ladder is a planning model, not a requirement to execute every step
serially.

1. **Known deterministic route:** use a tested algorithm, workflow, skill,
   capability, database query, calculation, or device procedure.
2. **Deterministic composition:** compose existing typed tools and skills into a
   new plan while preserving their authority and contracts.
3. **Retrieval and adaptation:** retrieve reviewed local sources, prior
   person-approved artifacts, or model-independent templates and adapt them to
   the current context.
4. **Bounded local inference:** use an eligible local model to interpret,
   synthesize, translate, plan, or propose a semantic result.
5. **Governed external research or inference:** when policy permits, use
   minimized, purpose-bound queries and reviewed providers; preserve disclosure
   and residual metadata records.
6. **Clarification:** ask the smallest question that can materially change the
   safe route. Do not force the person to translate a natural goal into system
   jargon.
7. **Experiment or simulation:** test a proposed route in a sandbox, dry run,
   synthetic environment, or read-only preview before asking for authority.
8. **Useful partial outcome:** provide verified facts, options, a draft,
   checklist, source packet, blocked-step explanation, or preparation for a
   qualified person.
9. **Safe handoff:** identify what a human or external professional needs, make
   the handoff accessible, and retain an inspectable continuation state.

The planner can move between routes as evidence changes. A failed tool call
does not authorize a broader disclosure or action. A model's confidence does
not replace missing authority, facts, equipment, or professional qualification.

## Resolution attempt contract

Every nontrivial attempt should be representable without storing private
content in operational telemetry:

- stable attempt and outcome identifiers;
- authenticated person and assistant, held in the private audit domain;
- purpose, risk, and requested result class;
- authorized context-space and data-domain handles;
- routes considered and deterministic rejection reasons;
- tools, skills, algorithms, sources, and model versions used;
- disclosures and external providers;
- assumptions, uncertainties, and clarification decisions;
- progress, partial artifacts, blocked steps, and recovery state;
- exact actions proposed or executed and their receipts;
- person correction, usefulness, and completion signal; and
- a content-free structural fingerprint eligible for repeat-pattern analysis.

Operational summaries exposed to administrators must not reveal the person's
request, sources, domain, or inferred interests merely because a resolution
attempt occurred.

## Persistence without fabrication

“Try to resolve” means exhaust safe, relevant routes in proportion to the value
and urgency of the request. It does not mean:

- invent facts, sources, capabilities, completion, or confidence;
- bypass privacy, policy, confirmation, safety, or professional boundaries;
- repeatedly ask the same question or retry a failing provider without a
  bounded strategy;
- consume unbounded compute, energy, money, attention, or time;
- make an unsafe physical or external action because no deterministic workflow
  exists; or
- conceal that a partial result, simulation, or model proposal is not a
  completed real-world outcome.

Each attempt should have time, cost, resource, disclosure, and retry budgets.
When a budget or authority boundary stops progress, Unison explains the most
useful next route and preserves resumable state.

## From repeated request to deterministic capability

Repeated novel work should create a *determinization candidate*, not silently
create executable authority. Candidate generation can occur when:

- the same person repeats structurally similar work;
- several consenting people encounter the same pattern;
- a model repeatedly composes the same tools or transformations;
- corrections reveal a stable rule;
- a task has high latency, cost, energy, or disclosure burden that a local
  deterministic path could reduce; or
- repeated failure or recovery indicates a missing capability.

Structural similarity should prefer content-free features such as tool graph,
contract types, error class, required fields, modality transitions, risk class,
and outcome shape. Personal content, health conditions, financial behavior,
relationships, and private interests must not enter organization-wide pattern
analysis without explicit research or contribution consent.

## Skill incubation lifecycle

1. **Observe:** record a private resolution receipt and content-free structural
   fingerprint.
2. **Detect:** identify a repeated pattern within the authorized scope and
   explain why it may benefit from a reusable path.
3. **Propose:** create a non-executable candidate containing inputs, outputs,
   dependencies, authority, failure modes, privacy, accessibility, and expected
   benefit.
4. **Generalize:** remove person-specific content and separate invariant steps
   from parameters and optional model contributions.
5. **Specify:** select the appropriate form—algorithm, query, rule, workflow,
   tool wrapper, skill, adapter, cache, fixture, or knowledge pack.
6. **Test:** replay synthetic and explicitly approved cases, including negative,
   adversarial, cross-person, offline, degraded, accessibility, cancellation,
   and recovery paths.
7. **Review:** require the relevant code, domain, privacy, security,
   accessibility, and safety owners. High-risk domains require qualified human
   review.
8. **Sign and package:** bind implementation, manifest, permissions, data,
   devices, egress, resource limits, compatibility, provenance, and revocation.
9. **Shadow and canary:** compare against prior routes without silently changing
   authority or durable person state.
10. **Promote or reject:** promote only with measurable improvement and no
    boundary regression; retain rollback.
11. **Monitor and evolve:** observe content-free health, correction, fallback,
    and outcome signals; revise, revoke, or retire as conditions change.

Person-local automations may have a lighter publication process but still need
inspectable inputs, authority, cancellation, and deletion. They remain private
and do not become globally installed skills by default.

## Deterministic and non-deterministic composition

A promoted route need not eliminate models. The stable deterministic envelope
can define:

- authorized inputs and retrieval;
- tool and skill graph;
- exact computations and invariants;
- bounded locations where model inference is useful;
- proposal schemas and reconciliation;
- stop, clarification, confirmation, and recovery rules;
- semantic output requirements; and
- evaluation and rollback.

This produces consistent work without pretending that language, perception,
research, or open-ended reasoning can always be reduced to fixed code.

## Multimodal naturalness

The resolution ladder operates on semantic outcomes, not UI commands. Every
supported modality should allow a person to:

- state a novel goal;
- understand what Unison thinks the outcome is;
- answer necessary clarification;
- inspect progress, uncertainty, sources, and choices;
- approve, cancel, correct, redirect, or resume;
- receive useful partial results; and
- understand the final outcome or remaining block.

One modality may require a different conversational rhythm, information
granularity, spatial description, navigation model, or confirmation mechanism.
Naturalness means native expression with equivalent authority and meaning, not
word-for-word translation of a visual interface.

## Measures

The program should measure:

- safe resolution rate for known and novel requests;
- useful partial-outcome rate;
- unsupported/generic-refusal rate;
- clarification count and whether each question changed the route;
- person correction, redirection, cancellation, and resumption success;
- source/provenance coverage and unsupported-claim rate;
- deterministic route coverage and fallback success;
- time, cost, energy, disclosure, and model-call burden per outcome;
- repeated-pattern detection precision;
- candidate-to-promoted-skill rate and measured benefit;
- regressions, boundary incidents, unsafe actions, and rollback; and
- semantic equivalence and naturalness across modalities through representative
  participatory research.

Optimization must not reward confident completion, engagement, or low refusal
at the expense of truth, privacy, safety, or person control.

## Initial implementation implications

- extend the accepted task/workflow record with resolution routes, assumptions,
  budgets, partial outcomes, and structural fingerprints;
- define `resolution-attempt.v1` and `determinization-candidate.v1` as the next
  contract candidates;
- keep private resolution receipts separate from content-free operational
  pattern signals;
- add bounded novel-request and repeated-pattern fixtures to DJ-1/DJ-2;
- make deterministic no-model paths a minimum, not the maximum behavior of the
  reference demonstrations;
- allow optional local-model interpretation and composition after deterministic
  safety/authority gates pass;
- preserve unresolved goals and partial artifacts for later continuation; and
- route generalizable candidates into the existing signed capability, model,
  update, and adaptive-maintenance lifecycles rather than self-modifying live
  production code.

