# Usage-driven taxonomy evolution

Status: implemented foundation  
Date: 2026-08-14

## Decision

Unison may recognize that a person's repeated usage would benefit from a new
tag, subdomain, or security domain and ask the person about it. Recognition is
advisory: inference can propose vocabulary, but it cannot silently create a
permanent domain, change an encryption boundary, or migrate records.

The interaction should be natural and sparse: “You have several legal-related
items. Would you like Legal to become its own protected area?” The proposal
must explain why it appeared, what would change, and what would not change.

## Lifecycle

1. Observe content-free signals such as repeated requests, classification
   corrections, distinct audiences, or policy/retention/sharing friction.
2. Require at least three matching signals across at least two days.
3. Propose one of three levels: a lightweight tag, a subdomain under an existing
   domain, or a security domain with a separate policy/key boundary.
4. Show evidence count, rationale, benefits, and migration scope. Do not expose
   raw request or memory content in the signal or proposal record.
5. Require explicit person confirmation for activation. Decline suppresses the
   candidate for 90 days; defer suppresses it for 30 days.
6. Activate the vocabulary only. Record migration remains a separate,
   receipt-bearing operation and starts in `not-started` state.

Novel requests still use governed inference immediately. Taxonomy evolution is
an optimization path for repeated patterns, not a capability gate.

## Authority and isolation

- Taxonomies, evidence, proposals, decisions, and active domains are scoped to
  one person, including within a household.
- A model can recommend a level but cannot make policy, identity, consent,
  retention, disclosure, or key-boundary decisions.
- Security-domain proposals use the same explicit approval rule as other
  levels and must never be inferred from diagnosis, wealth, disability, or
  another sensitive personal attribute.
- Software updates may ship suggested definitions, but adoption remains a
  visible governed decision.

## Implemented surface

- `unison.memory.v1` contracts for usage signals, proposals, decisions, and
  activation receipts.
- SQLite/Postgres-compatible persistent tables in `unison-context`.
- API routes under `/v2/taxonomy` for signals, evaluation, proposal review,
  decisions, and active-domain listing.
- Unit/integration evidence covers the `legal` example, thresholds, explicit
  approval, cooldown, no automatic migration, and cross-person isolation.

## Follow-on implementation

The user-facing proposal preview, migration preview and rollback workflow, and
security-domain control review are implemented in
`TAXONOMY_REVIEW_AND_MIGRATION.md`. Configurable thresholds learned from
prompt-fatigue metrics, separately authenticated policy issuance, physical
key-broker re-encryption, and participatory accessibility evidence remain open.
