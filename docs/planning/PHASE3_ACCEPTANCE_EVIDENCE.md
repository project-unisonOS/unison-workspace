# Phase 3 acceptance evidence

Status: Complete

Prepared: 2026-07-21

Gate owner: human architecture/security review

Gate decision: Approved 2026-07-21

## Acceptance mapping

- Unknown principal, assistant, purpose, audience, space, assurance, data class,
  action, or channel authority fails closed through the canonical Trust API.
- Disclosure outcomes cover allow, deny, redact, minimize, ask, and step-up;
  decisions are versioned, durable, owner-readable, and consequence-aware.
- External/high-risk work is draft-first and exact-request confirmation is
  expiring, cancellable, and one-use. Sensitive work requires stronger assurance.
- Remote inference requires an allowing decision, enforces a local-first choice,
  removes undisclosed fields and secrets, and preserves taint/provenance.
- The credential broker encrypts task secrets and injects them only after
  principal/capability binding without planner, model, decision, or audit exposure.
- Capability manifests declare the full Phase 3 authority/resource surface;
  incomplete, legacy, broad, expired, replayed, overreaching, and revoked cases deny.
- Text, speech guidance, keyboard focus, screen-reader semantics, reduced motion,
  simplified language, cancellation, denial, and confirmation expose equivalent meaning.

## Local evidence

`scripts/test-phase3.sh` runs 34 focused contract, policy, migration, capability,
inference, adversarial, disclosure-canary, confirmation, credential, and
accessibility checks from the workspace layout. Component regression results:

- unison-common: 278 passed, 1 skipped.
- unison-policy: 77 passed under the documented principal-binding test profile.
- unison-consent: 14 passed.
- unison-capabilities: 24 passed.
- unison-experience-renderer: 29 passed.
- unison-inference: the 3 Phase 3 disclosure checks pass; its enumerated
  pre-existing model-default/provider-availability/test-isolation failures remain tracked debt.

The expanded workspace unit gate also passes: common 278/1 skipped, auth 35,
consent 14, context 29, storage 3, policy 77, renderer 29, capability 24,
payments 3, and orchestrator 206. Phase 0 static validation and the complete
Phase 1 and Phase 2 boundary gates pass unchanged.

The synthetic disclosure case requested six fields, disclosed three, and emitted
no attachment/secret canary: disclosure ratio 0.50. Adversarial email, website,
document, tool, and model-output cases all denied action authority.

## Published evidence

The ordered Phase 3 review candidate is published in these draft pull requests:

- shared CI `da3cdc8f4b9a4bd6a77b9d3f17a0f80376b9a662`:
  [project-unisonOS/.github#2](https://github.com/project-unisonOS/.github/pull/2)
- common contracts `571d5d521d6e534157e856f330371e0030379b07`:
  [unison-common#4](https://github.com/project-unisonOS/unison-common/pull/4)
- Trust API and policy `21d4355a4acd890e5a340ec54660fb8890184178`:
  [unison-policy#12](https://github.com/project-unisonOS/unison-policy/pull/12)
- consent migration `52cceed31710de12ebd74b3c09aec3fd99793464`:
  [unison-consent#3](https://github.com/project-unisonOS/unison-consent/pull/3)
- governed capability runtime `02c140835f7c0f9bce4de000474ca37d0c749fd0`:
  [unison-capabilities#2](https://github.com/project-unisonOS/unison-capabilities/pull/2)
- disclosure-controlled inference `f2751216eb1b04578048a612e4c6d14eb297e25e`:
  [unison-inference#2](https://github.com/project-unisonOS/unison-inference/pull/2)
- accessible decision renderer `831b35a8ad6cde8a0c1b413fd58d6d1b349ebec0`:
  [unison-experience-renderer#4](https://github.com/project-unisonOS/unison-experience-renderer/pull/4)
- public trust documentation `9df6bab266e3331644c45eaa91cb6a7f63c0a3c6`:
  [project-unisonos.github.io#4](https://github.com/project-unisonOS/project-unisonos.github.io/pull/4)
- integrated workspace candidate `8fc570d89f978685fb027d08b47c44670dffb230`:
  [unison-workspace#4](https://github.com/project-unisonOS/unison-workspace/pull/4)

GitHub-hosted evidence is green for repositories that define workflows:

- [common contracts, lint, Python 3.12/3.13, security, and build](https://github.com/project-unisonOS/unison-common/actions/runs/29868640796)
- [policy tests](https://github.com/project-unisonOS/unison-policy/actions/runs/29869302019)
  and [container build](https://github.com/project-unisonOS/unison-policy/actions/runs/29869301854)
- [renderer tests](https://github.com/project-unisonOS/unison-experience-renderer/actions/runs/29868490464)
- [site build and accessibility](https://github.com/project-unisonOS/project-unisonos.github.io/actions/runs/29868496284)
- [workspace static, unit, PowerShell, and security gates](https://github.com/project-unisonOS/unison-workspace/actions/runs/29869312053)

Consent, capabilities, and inference do not currently define repository-owned
Actions workflows. Their component suites run locally and are pinned and rerun by
the workspace Phase 3 and expanded unit gates; this absence is reported rather
than represented as hosted evidence.

Post-gate note: the separately authorized stabilization sprint added
repository-owned security workflows to all three repositories and repaired the
enumerated inference regressions. Its immutable results are recorded in
`PHASE3_STABILIZATION_EVIDENCE.md`; the paragraph above remains the historical
state at the Phase 3 gate.

## Fresh-clone evidence

A new recursive clone of workspace commit
`8fc570d89f978685fb027d08b47c44670dffb230` initialized all 19 submodules,
including capability `02c1408`, common `571d5d5`, consent `52cceed`, inference
`f275121`, policy `21d4355`, and renderer `831b35a`. From only that clone:

- `scripts/bootstrap-dev.sh`: passed with the locked Python 3.12 environment.
- `scripts/validate-phase0.sh`: passed; 35 topology records, 7 canonical schemas,
  and 30 threat mappings validated. The two documented legacy schema-drift
  warnings remained unchanged.
- `scripts/test-phase1.sh`: passed; 40 trusted-principal tests plus the static
  authentication and product-profile boundaries.
- `scripts/test-phase2.sh`: passed; 26 governed-context tests and the relationship
  integration check.
- `scripts/test-phase3.sh`: passed; 34 trust, disclosure, capability, adversarial,
  confirmation, credential, and accessibility tests.

The published site also passed strict MkDocs rendering. Browser/axe validation
checked 1,851 internal links and reported zero accessibility violations on every
page, including the semantic trust-decision review.

## Final gate decision

The final Phase 3 gate was approved on 2026-07-21 after publication, green
component and workspace Actions, recursive fresh-clone validation, and
accessibility review. Phase 3 is **Complete**. Phase 4 is **Not started** and is
not authorized. The enumerated debt is assigned to the separately authorized
post-Phase 3 stabilization sprint.
