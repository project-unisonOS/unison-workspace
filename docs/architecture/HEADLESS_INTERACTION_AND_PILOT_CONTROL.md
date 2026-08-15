# Headless interaction and pilot control

Status: contracts and person-isolated persistence implemented; device and human
pilot evidence pending

Date: 2026-08-15

## Architecture

The headless NUC is a service host, not the interaction device. A local, LAN,
Tailscale, or approved relay client supplies a native input adapter and a native
output adapter. The session stores semantic focus, pending action identifiers,
transport, modality identifiers, expiry, and only a digest of the reconnect
token. It does not store a visual screen representation for later reading.

Reconnect requires the same person, the session identifier, the matching token
digest, an unexpired session, and a nonterminal state. Identity and authorization
continue to come from existing Unison authorities. The headless session does not
create either one.

## Pilot controls

Pilot enrollment references an existing consent grant, declares scopes and a
retention period, and separately enables content-free telemetry. Revocation
turns telemetry off immediately. Deletion removes pilot signals and reviews and
retains only the deleted enrollment state needed to prove that collection is no
longer authorized.

Pilot review is computed from content-free aggregates. Its counts must match the
stored summary. A boundary incident forces a pause or stop decision. Private
participant comments remain in separately governed research records.

## Candidate canary

The initial canary is synthetic. It can run only while the candidate is in the
canary state and its package digest matches the reviewed transition. A rollback
must reference a rollback receipt. This proves software mechanics only and does
not authorize shared promotion or execution on personal data.

## Deferred evidence

Real pilot enrollment, conversational or Braille device sessions, participatory
research, physical resource qualification, and GPU workloads remain deferred
until the owner and required hardware are available.
