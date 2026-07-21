# Governed context v2

Status: Phase 2 review candidate

Authority: `unison-common/schemas/governed-context.v2.schema.json` and `unison-context /v2`

## Boundary model

A relationship describes how a person understands a contact. It never grants
data access. A context-space membership is the only governed-context authority.
Every assistant receives an independent private space. Shared data requires an
explicit shared space, owner invitation, invitee acceptance, and a deliberate
copy. Removing a member immediately revokes reads and advances the space key
version so a storage/key implementation can rotate cryptographic material.

Search defaults to the caller's private spaces. Prompt construction is stricter:
the caller must name spaces, prove membership, and supply a purpose. Only records
that permit inference and either declare that purpose or are purpose-neutral are
included. Missing, nonexistent, and unauthorized spaces all produce the same
`404 {"detail":"context unavailable"}` response. Ambiguous relationship context
produces `409 {"detail":"context choice required"}` without guessing.

## Restrictive admission example

```json
{
  "space_id": "private-alice",
  "kind": "asserted_fact",
  "content": {"preference": "quiet mornings"},
  "provenance": "conversation:019",
  "governance": {
    "sensitivity": "private",
    "purposes": ["schedule"],
    "audiences": [],
    "allow_inference": true,
    "allow_action": false,
    "allow_disclosure": false,
    "allow_backup": false,
    "allow_sync": false
  }
}
```

Inferred hypotheses must have confidence below 1.0. Ephemeral records require an
expiry and cannot enable backup or sync. Disclosure remains denied in Phase 2;
the complete disclosure evaluator belongs to Phase 3.

## User controls and lifecycle

Inspection returns what is known, provenance, storage space, active members,
revision history, and the available correct/delete/share controls. Corrections
preserve an auditable prior revision. Delete and retention expiry replace both
current content and correction snapshots with empty tombstones. Export walks only
spaces currently authorized to the person. Explicit sharing clones content into
the shared space and records the private source identifier without changing it.

## Legacy migration

`migrate_legacy_private` copies profile, conversation, and dashboard rows into the
owner's private space. A journal makes the operation idempotent. It never infers a
relationship or promotes legacy data to shared storage. Missing legacy tables are
reported as zero records rather than treated as a failure.

## Accessible operation

The renderer provides native labels, fieldsets, buttons, confirmation checkboxes,
share preview, cancellation, and a live semantic status region. Space creation,
correction, deletion, sharing, charter/goal/commitment management, and privacy
inspection do not depend on drag, color, vision, speech, or precise pointer input.
