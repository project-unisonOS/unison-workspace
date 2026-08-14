# Agent contribution guide

Unison is a privacy-first household intelligence platform. Treat repository
contracts, authority boundaries, and evidence labels as product behavior.

## Start here

1. Read `docs/agent-contributor-model.md`.
2. Read `docs/repo-map.md` and the target component README.
3. Read the applicable planning journey and contract before changing code.
4. Run the narrowest relevant test, then the workspace boundary test.

## Non-negotiable rules

- Preserve unrelated and uncommitted contributor work. Use clean worktrees for
  remote or concurrent work.
- Never commit secrets, tokens, personal data, raw household media, or machine-
  specific credentials.
- Do not let a model, renderer, adapter, or tool become an authority for
  identity, consent, policy, incident state, or physical actuation.
- Label evidence as unit, simulation, hosted CI, physical hardware, or
  participatory. Never upgrade a claim beyond the evidence collected.
- Prefer versioned contracts and deterministic routes; retain a governed,
  bounded inference route for novel requests.
- Update the owning component first and the workspace gitlink only after the
  component commit is pushed and validated.

## Durable handoff

For long-running work, record objective, non-goals, starting revisions,
environment, checks, commits, PRs, unresolved risks, and next action in a
versioned planning or evidence document. Chat history is not project state.
