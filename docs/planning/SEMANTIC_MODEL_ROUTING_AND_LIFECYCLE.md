# Semantic experience model routing and lifecycle

Status: **Current-state assessment and accepted follow-on design; implementation incomplete**  
Last updated: 2026-07-25  
Prerequisite program: [SEMANTIC_EXPERIENCE_IMPLEMENTATION_PLAN.md](SEMANTIC_EXPERIENCE_IMPLEMENTATION_PLAN.md)

## Purpose

This document defines the role of AI models in the semantic experience system,
records what is implemented today, and identifies the model-routing and
model-lifecycle work that follows `SE0` through `SE7`.

Models are bounded reasoning and translation components. They can help Unison
interpret meaning, understand unstructured or visual information, propose a
semantic representation, and compose natural expressions. Deterministic
platform services retain authority over identity, context access, privacy,
policy, disclosure, capability execution, confirmation, durable state,
provenance, audit, and recovery.

The governing rule is:

> A model may propose meaning or expression. The platform decides what data it
> may see, validates what it returns, and controls what can happen.

## Current implementation assessment

### Implemented foundations

The following behavior exists and has relevant automated coverage:

- `unison-inference` provides one broker API over local Ollama, OpenAI, and Azure
  provider adapters.
- Local inference is the default and cloud fallback defaults off.
- Text and attachment-bearing requests select separately configured local text
  and multimodal model identifiers.
- Provider readiness checks detect missing local models or unavailable provider
  credentials before invocation.
- Explicit provider/model and configured fallback fields are accepted.
- A remote provider call requires a recorded local-alternative check and an
  allowing disclosure decision.
- Disclosure enforcement removes credentials and secrets and can remove prompt,
  message, attachment, or tool fields outside the approved disclosed-field set.
- Provider, model, fallback use, event identity, and result metadata are logged.
- Model outputs and external tool content are treated as untrusted content and
  do not authorize actions.
- Local ASR and TTS paths expose engine/profile status, captions, interruption,
  and renderer playback events.
- Model packs have early presence/readiness checks before selected local-model
  execution paths.

These controls are meaningful foundations, especially the remote-disclosure
gate. They do not yet constitute the complete routing and lifecycle design.

### Partially implemented behavior

- **Local versus remote selection:** providers and fallbacks exist, while route
  choice is primarily configuration- or request-driven rather than evaluated
  from a complete task policy.
- **Task specialization:** text versus attachment presence affects the default
  model, but there is no canonical task taxonomy or model capability registry.
- **Hardware awareness:** readiness can confirm that a configured local model is
  present. It does not yet select among candidates using current RAM, processor,
  accelerator, latency, energy, thermals, or concurrent workload.
- **Privacy-aware routing:** remote calls fail without disclosure authority and
  are minimized. Candidate comparison does not yet incorporate the relative
  disclosure burden of every eligible route.
- **Structured output:** some orchestration paths validate phase-specific plans
  and response contracts. Model output is not uniformly constrained and
  validated as Semantic Experience Model proposals.
- **Speech rendering:** local TTS and interruption work, while the current voice
  loop generally speaks a best-effort response summary rather than using a
  native conversational composer.
- **Compatibility:** model configuration and model-pack checks exist, while
  signed per-version compatibility, quality, risk, and hardware manifests do
  not.

### Behavior not yet implemented

- deterministic eligibility across privacy, disclosure, risk, task capability,
  hardware, offline state, latency, cost, license, and support status;
- inspectable ranking among all eligible models for each bounded operation;
- independent routing for intent interpretation, visual understanding,
  semantic construction, conversational composition, and other task classes;
- a signed registry describing model capabilities, limits, provenance,
  compatibility, measured quality, and approved risk classes;
- uniform schema validation, semantic reconciliation, and required-fact checks
  around model-proposed SEM content;
- deterministic ownership of exact facts, recipients, consequences,
  confirmations, action bindings, and recovery content in every expression;
- golden semantic-journey comparison across model versions;
- shadow, canary, promotion, health-gate, and automatic rollback workflows for
  model updates;
- experience-level compatibility guarantees that allow model replacement
  without changing identity, memory, permissions, or interaction-profile state;
- supported-hardware performance and resource qualification per model version.

## Target request flow

```text
Bounded reasoning or composition operation
                    |
                    v
          Typed task requirements
                    |
                    v
       Deterministic eligibility gate
 privacy | disclosure | risk | task | hardware | offline
 latency | cost | license | compatibility | support
                    |
                    v
        Inspectable candidate ranking
                    |
                    v
     Minimized, provenance-bearing request
                    |
                    v
             Selected model
                    |
                    v
       Typed untrusted model proposal
                    |
                    v
 Schema + fact + provenance + policy + action validation
                    |
                    v
 Accepted semantic contribution or explicit fallback
```

Routing occurs per bounded operation. One interaction can use deterministic
code for calculations, a small local model for intent interpretation, a vision
model for a chart, a stronger approved model for synthesis, a conversational
composer for expression, and local TTS for speech.

## Deterministic eligibility

The platform removes every candidate that fails a hard requirement:

- required task, modality, language, context size, and structured-output
  capability;
- local-only, offline, disclosure, sensitivity, recipient, and retention rules;
- approved risk class and deterministic-fallback requirement;
- installed artifact integrity and model/runtime compatibility;
- processor, accelerator, RAM, storage, and architecture compatibility;
- latency and availability requirements;
- cost ceiling and provider-account policy;
- license and support status.

A model cannot nominate itself, relax an eligibility rule, authorize broader
context, or select a remote provider. When no candidate remains, Unison uses a
deterministic fallback, reduces scope, requests a specific permission, or
explains the unavailable capability.

## Candidate ranking

Eligible candidates are ranked through an inspectable policy using task quality,
locality, disclosure burden, measured reliability, latency, current load,
memory, accelerator availability, energy, thermals, cost, and the person's
preferences. A learned predictor may later contribute a quality estimate, but
it cannot replace eligibility or become action authority.

Popularity, sponsorship, provider preference, engagement, and affiliate value
are prohibited ranking inputs.

## Division of responsibility

### Appropriate model contributions

- interpret ambiguous natural language;
- summarize authorized sources;
- describe images, charts, and spatial relationships;
- identify possible relationships, exceptions, and trends;
- propose SEM nodes with confidence and provenance references;
- compose natural conversation and modality-appropriate explanations;
- propose clarifying questions and progressive detail;
- estimate task-specific quality for routing evidence.

### Deterministic platform responsibilities

- authenticate the principal and choose authorized context;
- enforce policy, consent, disclosure, minimization, and retention;
- calculate exact values when deterministic sources are available;
- validate facts against source data and preserve uncertainty;
- assign stable semantic and action identifiers;
- select allowed modalities under hard privacy and safety constraints;
- bind actions to real capability targets;
- present exact recipients, amounts, consequences, and confirmations;
- execute, cancel, compensate, recover, and audit actions;
- admit durable memory and store interaction-profile state;
- enforce semantic-equivalence and model-promotion gates.

Fluent output is never evidence of permission, factual correctness, completed
execution, or safe recovery.

## Interaction with semantic rendering

Capabilities first return typed facts, state, actions, and provenance. A model
may help interpret unstructured portions or propose a richer SEM. The platform
then validates the proposal, reconciles computable claims with source data,
binds actions, and confirms that required privacy, uncertainty, provenance, and
recovery content remains present.

The modality planner creates an expression plan from accepted SEM and the
person's interaction profile. A model may phrase selected conversational or
descriptive portions. Deterministic composers retain exact values, choices,
warnings, confirmations, action identifiers, and recovery instructions.

High-risk experiences can use entirely deterministic language while retaining
the same semantic navigation model.

For an existing website or application, models may interpret pixels, layout,
charts, and ambiguous labels. Structured application data and accessibility
semantics remain preferred sources. The platform reconciles observations,
marks uncertainty, binds semantic actions to authenticated targets, and
revalidates the target immediately before consequential execution.

## Model update and replacement contract

Models are replaceable implementations behind stable contracts. Updating a
model cannot redefine:

- identity, assistant ownership, or context-space membership;
- permissions, consent, disclosure, or action authority;
- semantic schemas or stable action identifiers;
- confirmation and recovery requirements;
- memories, personal directives, or interaction profiles;
- durable session and audit history.

Each model version has a signed manifest containing its source, digest, model
family and version, quantization, runtime, supported tasks and languages,
context/output limits, structured-output support, hardware/resource needs,
execution location, license, provider/privacy constraints, measured latency and
quality, approved risk classes, known limitations, and rollback compatibility.

## Upgrade pipeline

1. Verify artifact signature, digest, source, license, and manifest.
2. Confirm runtime and exact hardware compatibility.
3. Benchmark latency, memory, accelerator, energy, and thermal behavior.
4. Run contract and structured-output validation.
5. Run golden semantic journeys and required-fact comparisons.
6. Run privacy, disclosure, cross-person, and secret-canary tests.
7. Run adversarial-content and prompt-injection tests.
8. Run modality-equivalence and accessible-recovery tests.
9. Evaluate in shadow mode using synthetic or explicitly approved data.
10. Promote to a bounded canary population or task class.
11. Observe content-free health and quality signals.
12. Promote, retain the prior version, or roll back automatically.

Wording may change between model versions. Required meaning, uncertainty,
provenance, available actions, recipients, disclosure boundaries, confirmation,
and recovery cannot.

## Public messaging guardrail

Public content may say that Unison supports local and remote provider adapters,
defaults to local inference, and enforces disclosure decisions before remote
inference. It must describe full task-aware routing, hardware-aware selection,
native semantic composition, and governed model upgrades as planned until the
follow-on slices have accepted evidence.

