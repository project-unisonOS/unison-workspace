# Phase 6 cryptographic review

Status: implementation review candidate
Review date: 2026-07-22
Profile: `unison-backup-v1`

This is a focused architecture and implementation review against the approved
Phase 6 decisions and published standards. It is not a claim of independent
third-party certification or a production TPM assessment.

## Approved construction

| Purpose | Construction | Boundary |
| --- | --- | --- |
| Chunk confidentiality and integrity | Fresh 256-bit DEK, AES-256-GCM, 96-bit random nonce | One chunk in one opaque person/space scope |
| Data-key wrapping | AES-256-GCM under current scope epoch key with scope/object AAD | One person or shared-space epoch |
| Domain separation and opaque identifiers | HKDF-SHA-256 and HMAC-SHA-256 | Separate scope and chunk-index purposes |
| Manifest confidentiality | AES-256-GCM under scope epoch key | Exact manifest sequence/scope/epoch AAD |
| Manifest authenticity | Ed25519 over exact deterministic stored envelope bytes | Trusted signer fingerprint in independent checkpoint |
| Recovery capsule | Argon2id (64 MiB, three iterations, parallelism one) then AES-256-GCM | One independently enrolled adult |
| Freshness | Signed hash-linked sequence plus independent checkpoint and retention floor | Provider cannot replace trusted local anchor |

References:

- [NIST SP 800-38D, GCM](https://csrc.nist.gov/pubs/sp/800/38/d/final)
- [NIST FIPS 186-5, EdDSA](https://csrc.nist.gov/pubs/fips/186-5/final)
- [NIST SP 800-56C Rev. 2, extraction and expansion KDFs](https://csrc.nist.gov/pubs/sp/800/56/c/r2/final)
- [RFC 9106, Argon2](https://www.rfc-editor.org/rfc/rfc9106)

## Review findings

1. Encryption and recovery execute locally; backend classes accept bytes and
   opaque names only.
2. Chunk data keys and GCM nonces come from the operating-system cryptographic
   random source. Keys are never reused intentionally.
3. AAD binds format, opaque scope, object/manifest identity, sequence, and epoch.
4. Deterministic chunk identifiers are keyed per stable opaque scope. They
   expose equality only within that scope, enabling incremental reuse without
   cross-person deduplication.
5. A supplied public key is not trusted merely because it accompanies a
   manifest. Verification compares it with the independently held trusted key.
6. The signed digest and independent checkpoint detect provider forgery,
   rollback, and forks. Full retained-lineage verification detects truncation
   and reordering. The checkpoint records an authorized retention floor.
7. Replacement recovery uses an enrolled Ed25519 recovery key; auth stores only
   its public key, encrypted-capsule digest, and checkpoint.
8. Recovery code entry is local and non-voice. Remote-channel and voice
   enrollment are rejected.
9. Shared membership removal rotates the random space key and future wraps
   include current members only.
10. Verification authenticates and hashes every retained chunk before restore;
    activation is atomic and interruption/cancellation preserves current data.

## Misuse and residual analysis

- **Nonce collision:** random 96-bit GCM nonces have a negligible but non-zero
  collision probability. Keys rotate by scope epoch; verification fails closed.
- **Provider denial:** a provider can omit or withhold bytes. The protocol
  detects but cannot prevent denial of service.
- **Metadata:** opaque object equality, sizes, timing, volume, account, and
  bucket remain visible. Padding/traffic shaping are deferred.
- **Recovery loss:** losing the recovery kit and every trusted checkpoint device
  makes recovery impossible. No administrator/provider override exists.
- **Historical shared keys:** a removed member may retain data/keys previously
  authorized. Rotation protects future state only.
- **Deletion:** local cryptographic erasure and provider disappearance checks
  cannot prove provider physical erasure.
- **Memory and host compromise:** an unlocked running node holds keys in memory.
  Full-disk protection and future validated TPM protection remain necessary.
- **Software fallback:** Phase 6 does not claim production hardware-backed key
  protection.

## Review conclusion

The v1 construction is suitable for the bounded Phase 6 engineering gate when
the independent checkpoint is present and the documented residual limits remain
visible. Production release still requires hardware validation, provider terms
review, operational key handling, and preferably an independent external
cryptographic assessment.
