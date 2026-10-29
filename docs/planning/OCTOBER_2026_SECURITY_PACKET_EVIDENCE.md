# October 2026 security implementation evidence

Status: draft packets under human review. No operational deployment or private
health-data authorization. Evidence is synthetic software testing.

## Objective and authority

Close authenticated-boundary and private-state gaps, then converge the actual
runtime before a read-only synthetic health journey. No broad rewrite, hardware
purchase, OAuth grant, real records, paid model, purchase or meeting participation.
The original local October plan and unrelated work are preserved.

## Component packets

### Current review checkpoint

No PR is merged at this checkpoint. Merge authorization has been received;
independent exact-head review precedes merging validated related changes.

| Component | Current head | Verified evidence |
| --- | --- | --- |
| Orchestrator PR47 | `923eaeae2c1f7c018ba76cd38e2abe178a85a1e1` | All hosted checks pass; 284 Linux tests. New coverage includes alternate JSON identity hints, disabled legacy ingress, production authenticated cache namespaces and server-owned trace filenames. |
| Storage PR34 | `7343e72078d0f89184e55051653b3d4b64a52f6b` | All hosted checks pass; 48 local and Linux tests. Terminal batch rejection persists after restart; domain records use encrypted transactions; concurrent ingestion/deletion and abrupt process-death rollback covered. |
| Platform PR44 | `caa59f2347de002616d638b5668da2d12e7217d9` | Hosted Linux contract passes. Test-only signed authorization metadata has relative short expiry; expired root and signed-target rejection remain enforced. Workspace pin advanced after this result. |
| Inference PR9 | `dbc372d64eae359acbbc2b4dd9dc5b54388f07f3` | 32 focused local synthetic tests pass. Strict text schema and loopback transport enforced. Runtime artifact/execution binding and caller authority integration remain blockers; keep draft. |

Workspace CI previously failed on expired simulation metadata and an inaccessible
MinIO image. The fixture repair above preserves production expiry enforcement.
The replacement backup CI harness uses the same official MinIO release binary,
verified against its pinned SHA-256, on a loopback-only ephemeral runner. It
retains the existing encrypted backup, verification and restore assertions.
Workspace final-head validation is still pending; no green claim is made yet.

### Earlier packets (historical evidence)

| Packet | Draft PR | Evidence before dependency refresh |
| --- | --- | --- |
| Authenticated input and event scope; fail-closed policy/confirmation; minimized input diagnostics | https://github.com/project-unisonOS/unison-orchestrator/pull/47 | 266 tests passed locally on Windows/Python 3.12 and in hosted Linux CI at `0cf0edc934a22bcfb7e48753e77c2ec61b00bc76`; 23 focused tests include signed synthetic identities and loopback JWKS/session introspection |
| Encrypted atomic source bytes and derivatives | https://github.com/project-unisonOS/unison-storage/pull/34 | 15 focused tests passed locally; hosted Linux suite passed 44 tests at `a7ead47d78bf5daa7453e07b2d38f2d2002d1d86` |

Initial regression runs reproduced eight ingress/boundary failures and three
source-state failures. Existing missing/expired/revoked/wrong-audience/forged
identity denials passed. The source tests include multiple threads/processes,
restart, wrong-key rejection, rollback after extraction failure and deletion.

Workspace boundary fixture commands also passed: household structure, 35 mapped
threats, and DJ-0's 10 contract candidates / 2 journeys / 12 gates. These are
fixture evidence, not proof of complete runtime enforcement.

Security scanners blocked both initial drafts on vulnerable dependency pins.
PyJWT and the compatible OpenTelemetry family have been updated in the drafts;
all security checks remain enabled. Final-head validation is green for orchestrator
`64e5cd1cd931523e120b2a64b3f862c4e4469a62` and storage
`0158beec29e8c69daf3a154284f8aad9c3afbe12`, including functional tests,
image builds and vulnerability checks. They remain unapproved draft PRs;
workspace pins were unchanged at that earlier checkpoint.

Inference draft https://github.com/project-unisonOS/unison-inference/pull/9
requires authenticated `inference.local` scope, a signed registry, trusted hardware
inventory and bounded read-only local text execution. Remote fallback/tools are
unavailable pending separate authority. Eight baseline failures were reproduced;
expanded local tests yielded 51 passes and two existing Windows-only directory
fsync errors. Linux CI passes on `ea9b5c935d4f92ebcf29f07211fd5621ee5d24be`, including the corrected fixture and lifecycle cases. This is a
controlled callback test, not a real model qualification.

## Scope and remaining work

The source format preserves and rejects legacy plaintext indexes pending an
explicit offline migration. Existing installations and operational services were
not touched. Backup compatibility, secure erasure, key custody, other private
stores, complete inference/fallback enforcement and independent review remain
open gates. Neither draft proves an ordinary health assistant or local-model
integration. Original parser/provider fixtures remain unsuitable for real intake.

Next packet: complete independent review and workspace validation, then establish
the reviewed inference caller/runtime contract and authenticated integration
harness. Resolution and incident state still require their own persistence work.
Record acceptance evidence before changing public capability claims. Merge
authorization does not authorize submitting a formal PR approval review.

## Further persistence work

Private-domain transaction validation is now included in the 48-test storage
suite. Other stores, physical power-loss behavior, all correction/recovery races,
and the first synthetic health journey remain outstanding.
