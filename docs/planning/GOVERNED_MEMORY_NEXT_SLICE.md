# Governed context and memory: next slice

Status: proposed implementation slice

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
