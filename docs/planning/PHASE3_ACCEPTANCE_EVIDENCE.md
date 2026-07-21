# Phase 3 acceptance evidence

Status: In review

Prepared: 2026-07-21

Gate owner: human architecture/security review

Gate decision: Pending

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

## Published evidence to capture

- Component and workspace commit identifiers and draft pull requests.
- Green component/workspace GitHub Actions URLs.
- Recursive fresh-clone `validate-phase0.sh`, `test-phase1.sh`, `test-phase2.sh`,
  and `test-phase3.sh` output.
- Browser/axe result for the semantic trust decision review.

## Gate boundary

Phase 3 remains **In review** until publication, Actions, fresh-clone, and the
final human gate are complete. Phase 4 is **Not started** and is not authorized.
