# Governed context and memory: next slice

Status: first foundation slice implemented

Date: 2026-08-14

## Outcome

Turn the existing governed-context v2 authority model into the durable memory
path used by orchestration and model routing. The slice must preserve local-first
operation, person-level privacy inside a household, explicit shared spaces, and
model replaceability. A vector index is a derived retrieval aid, never the
authoritative record or an authorization boundary.

## Existing foundations to reuse

- Auth-issued principal, person, assistant, household, membership, key,
  credential, data, cache, and index namespaces.
- Governed context v2 spaces, memberships, provenance, correction, deletion,
  expiry, export, and explicit copy-to-share semantics.
- Trust-governance decisions over purpose, audience, space, assurance, data
  class, action, channel, and disclosure.
- Storage encryption/key-broker boundaries and local/off-prem backup policy
  concepts already recorded in the system architecture.

## First implementation boundary

1. Define versioned memory-record and retrieval-request contracts with
   principal/space binding, data class, source provenance, asserted/inferred
   status, confidence, purpose, retention, correction lineage, and algorithm
   provenance.
2. Admit records only after authenticated principal binding and policy checks.
   Health and finance remain in separate governed spaces and key domains;
   household membership alone grants no access.
3. Keep authoritative records in relational/object storage. Treat embeddings,
   summaries, caches, and graph edges as disposable derived views tied to source
   revision and index namespace.
4. Retrieve in two stages: deterministic authorization/filtering first, then
   semantic ranking inside the authorized candidate set. Never search a global
   vector collection and filter afterward.
5. Propagate correction, deletion, membership revocation, retention expiry, and
   key rotation into derived-view invalidation with receipts and replayable jobs.
6. Build context packets with an explicit token budget, purpose, citations,
   uncertainty, disclosure decision, and local/remote routing limit.
7. Prove cross-person/domain denial, stale-index exclusion, restart recovery,
   embedding replacement, export, deletion, and backup policy.

## Repository ownership

| Repository | Responsibility |
| --- | --- |
| `unison-common` | memory, retrieval, provenance, and invalidation contracts |
| `unison-context` | spaces, membership, admission, lifecycle, and retrieval policy |
| `unison-storage` | encrypted records, objects, derived-view metadata, backup hooks |
| `unison-context-graph` | rebuildable non-authoritative relationship/index projection |
| `unison-orchestrator` | purpose-bound context packet assembly and deterministic-first routing |
| `unison-inference` | governed embedding/model selection without data authority |
| `unison-workspace` | fixtures, cross-service gates, evidence, and task packet |

## Decisions required before code

- Canonical data-class taxonomy and which classes require distinct encryption
  keys versus distinct logical spaces.
- Retention defaults and whether a person can make them more restrictive.
- Embedding migration strategy: dual index, rebuild-and-swap, or both.
- Backup envelope/key ownership and the minimum viable restore ceremony.
- Which cross-domain joins require fresh consent or explicit confirmation.

The first proof uses synthetic household, health, and financial records and may
claim integration evidence only. It cannot establish clinical efficacy,
financial suitability, production security, or physical appliance readiness.

## Implemented foundation

The first review slice defines `unison.memory.v1` with an open-vocabulary domain
identifier rather than a closed enum. Domain definitions record whether they
originated with the system, a person, observed usage, or a software update. This
allows candidates such as `legal` to be proposed without a contract release;
activation, migration, key separation, and retention remain governed decisions.

Context retrieval now checks authenticated space access and domain constraints
before ranking. It returns a purpose-bound, token-bounded packet with citations
and remote use denied by default. Embeddings, summaries, caches, and graph edges
are revision-bound derived views. Correction, deletion, retention expiry, and
membership revocation invalidate affected views and create durable receipts.

Usage-driven taxonomy proposals are now implemented as a separate governed
slice documented in `USAGE_DRIVEN_TAXONOMY.md`. They require repeated evidence
and explicit person approval; automatic activation and record migration remain
prohibited. Durable rebuild jobs and the dual-index rebuild-and-swap strategy
are now implemented, and mounted-file custody plus replacement-restore
operations are defined in `REBUILD_KEY_CUSTODY_AND_CONTRIBUTOR_EVIDENCE.md`.
Physical key custody, storage-tier movement, measured large-index rebuilds, and
witnessed appliance restore remain explicit follow-on work rather than being
inferred from passing unit/integration tests.
