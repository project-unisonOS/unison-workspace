# Phase 3 migration and rollback

Existing consent scopes and capability manifests are inventoried but do not gain
authority by translation. A legacy consent record is importable only when its
principal, assistant, capability, actions, purposes, audiences, data classes,
spaces, and recipients are explicit. Otherwise it is retained read-only and
disabled. Unversioned capability manifests are disabled by default.

Migration creates `unison.trust.v1` grants and
`unison.capability-governance.v1` manifests alongside the read-only originals.
Operators validate synthetic decisions before enabling a migrated capability.
Rollback revokes the imported grant and manifest revision, clears outstanding
confirmations/nonces, and returns to the disabled read-only legacy record. It
never re-enables implicit legacy scope semantics.
