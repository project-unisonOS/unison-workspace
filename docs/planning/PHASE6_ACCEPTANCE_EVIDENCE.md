# Phase 6 acceptance evidence

Status: **In review**
Evidence date: 2026-07-23
Phase 7: **Not started**

## Scope

Phase 6 implements the approved provider-blind backup v1 profile and a bounded
replacement-device restore. The home node remains authoritative; backup is not
synchronization or remote access.

Approved decisions AD-026 through AD-034 cover the cryptographic profile,
person-controlled recovery, independent checkpoint, shared-space epochs,
retention/deletion, backend contract, replacement activation, accessibility,
and single-writer boundary.

## Implementation inventory

| Repository | Candidate |
| --- | --- |
| `unison-common` | `8b82c2fe26b31aa4b368eb150654e0dd3561fa58`, draft PR #10: canonical schema/models, AES-GCM envelope encryption, HKDF/HMAC domain separation, Ed25519 manifest signing, Argon2id recovery capsule, checkpoint verification |
| `unison-storage` | `9fb770faeca085433e266bd12907d1b278a270f5`, draft PR #15: filesystem/hostile/S3 backends; incremental snapshots; lineage; scheduled verification; retention; export/deletion; provider migration; resumable restore; rotation |
| `unison-auth` | `02c0e26bec35a3dc4797de7a8da726ee70d271a7`, draft PR #20: schema v3 recovery enrollment, expiring challenge, signed replacement proof, checkpoint rollback defense, device revocation and rotation requirements |
| `unison-experience-renderer` | `c8a86d1caafd86b065b13771ea53fb784deccc22`, draft PR #8: semantic backup status, recovery-key safety, dry run, activation, cancellation/resumption, provider/admin disclosure |
| `unison-docs` | `6d410f3cc2cffb4b663137cdf5aebc798632cdfd`, draft PR #1: format, backend contract, metadata, recovery ceremony, provider migration and disaster runbooks |
| `unison-workspace` | Decisions, threat model, hostile-provider tests, MinIO profile, clean-device proof and evidence |
| Public site | `a65c6912253d90c2f9eaaa3c9ffb67f69319b872`, draft PR #9: truthful Phase 6 review-candidate status, recovery boundary and residual limits |

## Acceptance matrix

| Requirement | Evidence |
| --- | --- |
| Provider sees ciphertext only | Provider-view canaries and opaque-namespace tests |
| Wrong person/admin/provider cannot decrypt | Independent-key and recovery-proof negative tests |
| Tamper/rollback/truncation/reorder/missing/corruption/replay | Hostile backend and anchored-lineage tests |
| Interrupted backup/restore resumes safely | Idempotent chunk reuse and restore-journal tests |
| Independent deletion/export/shared removal | Per-scope export/deletion and epoch-wrap tests |
| Repeated verification | Scheduled verification records plus repeated clean proof |
| Provider portability | Filesystem-to-filesystem and S3-compatible migration tests |
| Clean replacement restore | Two private scopes and one shared scope restored on an empty target |
| Accessible recovery | Static semantic tests plus real-browser axe/keyboard run |
| Threat controls | T-07, T-13, T-17, T-20, T-21, and T-30 report |

## Executed local evidence

- Component regressions: `unison-common` 291 passed/1 skipped;
  `unison-storage` 13 passed; `unison-auth` 43 passed;
  `unison-experience-renderer` 37 passed.
- Aggregate Phase 6 proof: 30 passed, canonical/package schema parity passed,
  six repeated verifications, three-scope clean replacement restore, provider
  migration, revocation, and shared-member rotation passed.
- Renderer Chromium/Playwright/axe: zero WCAG A/AA violations, 41 semantic
  controls, keyboard focus, reduced-motion and forced-colors checks passed.
- Public site strict clean build passed; 1,949 internal links resolved and the
  full Chromium/axe page audit reported zero violations, including the new
  backup/recovery page.
- All candidate worktrees pass `git diff --check`.

## Evidence pending publication

Hosted component/workspace Actions, hosted MinIO validation, fresh recursive
clone, ordered merge, final public-site deployment, final workspace commit/PR
reference, and the human gate decision remain to be recorded.

## Residual limits

- No production TPM or secure-element claim.
- No provider physical-erasure guarantee.
- No recovery when both the person's recovery kit and all trusted recovery
  devices are lost.
- No retroactive revocation of historical shared keys already possessed.
- No padding or traffic-shaping guarantee for residual size/timing metadata.
- No multi-writer synchronization.
- No external independent cryptographic certification.

## Gate rule

Phase 6 is not Complete until component and workspace changes are published,
hosted checks and fresh-clone evidence pass, the final evidence values replace
the pending section, and the human final gate is explicitly approved. Phase 7
remains Not started.
