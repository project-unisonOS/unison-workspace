# Semantic experience and adaptive I/O design

Status: **Accepted design direction; implementation pending**  
Last updated: 2026-07-25

## Purpose

This document preserves the intended Unison experience for people whose input
and output needs differ from conventional visual computing. It is also the
source material for future GitHub Pages messaging after the implementation and
acceptance evidence support those claims.

Unison should understand the outcome, information, relationships, choices, and
risks in an experience before deciding how to express it. A screen, spoken
conversation, Braille display, sign-language avatar, haptic cue, or combination
of those outputs is one expression of that meaning.

For a person who prefers conversation because visual content is difficult or
impossible to use, Unison should generate a native conversational experience.
It should not create a visual interface and then depend on a screen reader to
recite it. When Unison must operate an existing website or application, it
should recover the meaning and available actions from that experience and
recompose them conversationally.

Screen-reader compatibility remains a useful fallback for legacy web content,
developer tools, and recovery paths. It is not the defining accessibility model
for the Unison operating surface.

## Assessment of the current implementation

The architecture is directionally aligned:

- the renderer is described as a translation surface between intent and
  perception;
- the response path uses a model-independent response object;
- visual, audio, and haptic adapters are separated;
- person-specific preferences, local speech input/output, interruption,
  captions, Braille, vision, and other modality projects exist;
- the authoritative plan requires one semantic outcome adapted to the current
  channel and modality.

The implementation does not yet satisfy the intended experience:

- `ResponseObjectModel` is centered on text and cards and cannot fully express
  relationships, actions, consequences, uncertainty, or modality-equivalent
  interaction;
- renderer directives expose visual density, verbosity, pacing, motion, and a
  small `renderer`/`voice`/`both` choice;
- output selection is often derived from the input channel instead of the
  person's needs, available devices, environment, privacy, and content;
- the browser renderer applies a visual scene first, while its audio adapter
  primarily emits cues or plays audio prepared elsewhere;
- the current voice loop speaks a best-effort summary of a response rather than
  composing an independently navigable conversational experience;
- Braille planning still relies on renderer focus text in places;
- some tests treat `screen_reader_support` as the accessibility outcome.

The existing components are useful building blocks. The missing architectural
center is a rich semantic experience model, a person-aware modality planner,
and native modality composers that preserve meaning and control.

## Experience promise

Unison generates one coherent experience around your intent, needs,
preferences, environment, and available devices. You can understand the same
outcome, inspect important detail, act, confirm, cancel, recover, and change
modality without losing context.

This promise has five consequences:

1. Meaning is authoritative; presentation is derived.
2. Input and output modalities are selected independently.
3. Accessibility needs are durable context rather than optional display
   settings.
4. Each modality receives a native composition, not a transcription of another
   modality.
5. Equivalent understanding and control are testable release requirements.

## Target architecture

```text
Intent, capability result, or external experience
                        |
                        v
             Semantic Experience Model
                        |
                        v
Person interaction profile + device capabilities + situational context
                        |
                        v
             Experience and modality planner
                        |
          +-------------+-------------+
          |             |             |
          v             v             v
 Conversational      Visual        Tactile/sign/
   composer          composer       other composer
          |             |             |
          +-------------+-------------+
                        |
                        v
       Equivalent action, confirmation, interruption,
                    recovery, and audit
```

### Semantic Experience Model

The Semantic Experience Model, or SEM, is the canonical output contract between
orchestration and experience composition. It represents:

- purpose, outcome, and current state;
- entities, values, relationships, hierarchy, sequence, and spatial meaning;
- changes, trends, comparisons, exceptions, uncertainty, and provenance;
- available actions, parameters, consequences, reversibility, and risk;
- required confirmation, cancellation, recovery, and follow-up;
- urgency, attention requirements, privacy, and disclosure state;
- exact content that must be preserved and content that may be summarized;
- stable semantic identifiers for conversational reference and modality
  switching;
- alternate representations supplied by a capability when domain knowledge can
  improve the experience.

The model does not prescribe windows, controls, speech strings, Braille cells,
or visual layouts. Those are composer outputs.

### Personal interaction profile

The profile records durable needs and preferences while supporting reversible,
situational changes. It can include:

- preferred, available, constrained, and unavailable input/output forms;
- conversational detail, pacing, interruption, and turn-taking preferences;
- preferred treatment of lists, tables, charts, images, maps, and spatial
  relationships;
- hearing, vision, motor, language, literacy, and cognitive needs that the
  person chooses to share;
- confirmation, notification, and attention preferences;
- device associations and trusted assistive hardware;
- learned preferences with provenance, confidence, expiry, and an understandable
  explanation;
- temporary states such as driving, a quiet room, shared surroundings, fatigue,
  or unavailable devices.

The profile is private person-owned context. Unison should discover and refine
it conversationally, apply changes gradually, and make every learned adaptation
inspectable and reversible.

### Experience and modality planner

The planner selects an expression plan using:

- the person's interaction profile;
- current device and adapter capabilities;
- situational and environmental context;
- information structure and cognitive load;
- urgency, risk, privacy, and channel assurance;
- latency, resource, and offline constraints;
- the person's explicit choice for the current interaction.

Input modality never dictates output modality by itself. A keyboard request can
receive a spoken response. A voice request can produce a visual or tactile
comparison when appropriate. The planner can select multiple mutually coherent
outputs and identify which one carries each part of the meaning.

### Native conversational composer

The conversational composer turns SEM into dialogue rather than spoken UI. It
supports:

- progressive summaries and optional detail;
- conversational exploration of entities, groups, comparisons, and trends;
- meaningful descriptions of images and spatial relationships;
- stable references such as “the second option” across turns;
- interruption, resumption, repetition, and pacing control;
- concise state-change and progress announcements;
- spoken choices, parameters, confirmations, cancellations, and recovery;
- explicit uncertainty, provenance, privacy, and risk when relevant.

Conversation state points to semantic identifiers in the SEM. It does not depend
on visual focus order or control labels.

### Other native composers

Visual, Braille, sign, haptic, switch/AAC, and future composers consume the same
SEM and expression plan. Each composer uses the strengths of its modality while
preserving the required meaning and actions. A Braille composer, for example,
can prioritize structured tactile reading and navigation without mirroring a
visual focus feed.

### Translation of existing visual experiences

When Unison operates a website, document, desktop application, or remote visual
environment, an Experience Interpreter builds SEM from the best available
sources in this order:

1. domain API or structured application data;
2. document semantics and accessibility tree;
3. application state exposed by an integration or computer-use harness;
4. vision understanding of pixels, charts, images, and layout;
5. carefully bounded model inference, labelled with confidence and provenance.

The interpreter reconciles sources, detects changes, preserves action targets,
and identifies ambiguity before consequential action. The person engages with
the recovered meaning through their preferred modalities. Raw control labels or
screen coordinates remain implementation details unless the person asks for
them.

Example:

> Your electricity bill is $18 higher than last month, mostly because weekday
> heating use increased. It is due Friday. Would you like the daily comparison,
> the full bill, or help changing the thermostat schedule?

This is a conversational expression of the bill's meaning and available next
steps. It is not a screen read aloud.

## Modality equivalence contract

Every supported expression must preserve the required semantic and operational
properties for the current experience:

- **Comprehension**: the person can understand the outcome and its significance.
- **Inspection**: important detail, uncertainty, provenance, and relationships
  remain available.
- **Agency**: every offered action can be selected, parameterized, confirmed,
  cancelled, and reversed or recovered where applicable.
- **Safety**: risk, recipient, disclosure, and irreversible consequences remain
  understandable before action.
- **Continuity**: modality changes retain semantic focus, conversation state,
  pending actions, and audit context.
- **Privacy**: adding a modality does not silently expand collection,
  disclosure, retention, or bystander exposure.
- **Failure recovery**: loss of a device or modality produces an understandable
  fallback or a clear explanation of what cannot safely continue.

Equivalence does not require identical wording, ordering, density, or sensory
presentation. It requires equivalent meaning and control.

## Security and privacy boundaries

- Interaction profiles are private governed context and use the person's key
  and retention domain.
- Needs are disclosed to capabilities only when required for the selected
  expression and allowed by policy.
- Cameras, microphones, assistive devices, environmental sensing, and remote
  models remain capability- and consent-governed.
- Legacy-experience interpretation treats page text, accessibility metadata,
  images, and model output as untrusted content without authority.
- Semantic actions bind to authenticated capability targets and are revalidated
  immediately before consequential execution.
- Bystander, shared-room, and sensitive-content rules can suppress or redirect
  spoken and visible output.
- Adaptations learned by inference carry provenance, confidence, expiry, and a
  reversible approval state.

## Public messaging guardrail

Until acceptance evidence exists, public pages should distinguish the intended
experience from current engineering support. They should not characterize
screen-reader compatibility as the Unison accessibility vision or imply that
native conversational translation of visual experiences is complete.

After implementation, Pages content can draw from these approved themes:

- Unison understands the meaning of an experience before deciding how to
  present it.
- Your needs, preferences, surroundings, and available devices shape the
  experience automatically.
- Conversation, visual presentation, Braille, sign, touch, and future forms are
  native expressions of the same outcome.
- Unison can translate compatible websites, applications, documents, and visual
  information into an experience you can understand and control
  conversationally.
- You can move between modalities without losing context, agency, or safety.

Claims must be narrowed to the slices with published acceptance evidence.

