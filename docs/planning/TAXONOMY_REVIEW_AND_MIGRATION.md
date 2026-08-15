# Taxonomy review and migration

Status: implemented software foundation  
Date: 2026-08-14

## Outcome

Turn usage-driven taxonomy proposals into understandable, reversible decisions
without allowing a model or a single approval click to reclassify personal
records. This slice implements three linked but separate ceremonies:

1. a natural, modality-neutral proposal preview;
2. a mandatory full-boundary control review for security domains; and
3. an expiring, exact migration preview followed by explicit confirmation and
   a 30-day rollback window.

## Person-facing proposal

The preview explains why Unison is asking now, what approving the category
would change, what it would not change, and the approve/defer/decline choices.
It explicitly states that declining does not reduce Unison's ability to help
and that activation moves no existing records. The contract contains semantic
text and structured lists so conversation, Braille, switch/AAC, and visual
composers independently express equivalent meaning without relying on color or
layout. Conversation and Braille are native Unison experiences; neither may
consume a visual layout, DOM focus feed, ARIA representation, screenshot, or
screen-reader output. Legacy web compatibility is not acceptance evidence for
blind or visually impaired use of Unison.

## Security-domain review

A security domain cannot activate until the recorded review covers:

- a separate logical key boundary;
- retention behavior;
- sharing behavior; and
- disclosure behavior.

Any omitted control fails closed. The person must still explicitly approve the
proposal after the control review. `unison-policy` issues an Ed25519-signed,
short-lived authorization bound to the person, proposal, policy version, and
complete review. Context verifies the configured public key and rejects locally
asserted or expired reviews.

## Migration and rollback

Activation changes vocabulary only. A later migration preview selects only
records owned by the person and matching explicit source domains. The preview
contains record IDs and revisions, never record content, expires after 15
minutes, and has a deterministic digest. Execution requires confirmation of
that exact digest and fails if any selected record revision changed.

Execution records prior governance, increments record revisions, invalidates
derived views, and issues a receipt. Security-domain migration adds the new
domain, encrypts selected content under the new key-domain handle, and removes
its plaintext database representation. Rollback restores prior governance and
re-encrypts content under its former key-domain handle,
increments revisions again, invalidates derived views, and issues a separate
receipt. The rollback window is 30 days.

## Evidence boundary

Tests use synthetic records and prove contract validation, natural preview
content, security-review gating, exact confirmation, classification/key-domain
change, rollback, and person isolation. They do not prove TPM/HSM key custody,
representative Braille hardware, participatory accessibility, or the security
of a deployed policy-service channel.
