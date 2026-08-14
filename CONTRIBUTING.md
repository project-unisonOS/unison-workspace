# Contributing

Follow the org-wide guidelines in `.github/CONTRIBUTING.md`.

- Keep secrets out of the repo; never commit `.env` or tokens.
- Run lint/tests before PRs; add abuse-case tests when touching auth/policy flows.
- Seek at least one review; security-sensitive changes should involve `@project-unisonOS/security-leads`.

## Agent-led contributions

Start with `AGENTS.md`. Work from an issue or a validated packet in `tasks/`
that states authority, allowed changes, non-goals, validation, evidence class,
rollback, and handoff. Chat history and agent memory are not project records.

Every PR must identify affected contracts and authority boundaries, include
exact validation commands and results, distinguish simulation from physical or
participatory evidence, and update durable handoff state. Follow
`docs/contract-versioning-policy.md` for cross-service changes.

One approving review is required. Request security review for authentication,
authorization, consent, encryption, personal-data boundaries, network exposure,
incident response, update trust, or physical actuation. Request accessibility
review when interaction semantics or modality projections change.
