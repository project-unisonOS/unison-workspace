# Modality adapter developer guide

Status: software contract and synthetic conformance kit implemented

Date: 2026-08-15

## Purpose

A modality adapter converts native human input into typed semantic observations,
or converts a Semantic Experience Model expression plan into native output. It
does not reproduce a visual screen for a person who does not use visual output.
Conversation, Braille, sign language, switch and AAC input, haptics, BCI, and
future modalities use the same integration boundary while remaining native to
their users.

## Stable integration point

Every adapter declares `modality-adapter.v1`, supported SEM and expression
versions, direction, capabilities, device classes, permissions, fallbacks, a
package digest, and signer. Run:

```text
python scripts/validate-modality-adapter.py path/to/manifest.json
```

The synthetic reference fixture is
`tests/fixtures/modality-adapter.valid.json`. The conformance check is:

```text
python scripts/validate-modality-adapter-fixtures.py
```

## Authority boundary

An adapter cannot own identity, consent, policy, disclosure, or action
authority. It requests named capabilities from Unison and returns provenance
with observations or expressions. The orchestration and policy layers decide
whether data may be captured, retained, disclosed, or used for an action.

Raw camera, biometric, neural-signal, or medical-adjacent data remains in its
governed space and is not operational telemetry. New modality repositories need
a threat model, synthetic fixtures, semantic-equivalence checks, native recovery
behavior, and named reviewers before integration.

## Contributor handoff

An agent or human contributor should begin with the valid fixture, replace only
adapter-specific identifiers and capabilities, and add both positive and
authority-boundary tests. Synthetic conformance is not participatory evidence.
Claims about a modality require representative people, native devices, and the
approved research protocol.
