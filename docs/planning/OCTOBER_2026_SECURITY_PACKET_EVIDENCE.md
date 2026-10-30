# October 2026 security implementation evidence

## October 30 export-first prerequisite candidate

Starting from merged storage #36/workspace #59, this packet adds separate synthetic
consent/extraction routes and an owner-scoped deletion recovery outbox. Source-to-fact
provenance now comes from stored JSON bytes in the new pilot path; the old manually
associated fixture path remains explicitly separate. No real export compatibility
or deployed independent policy-service claim is made.

Local storage: 95 tests passed, including 20 new authenticated pilot cases. Coverage
includes expiry, revocation, wrong policy/purpose/person/scope, source/receipt damage,
malformed export, restart, concurrent extract/delete and interruption before/after
domain commit. Local new workspace integration passed with actual ASGI storage and
ingress, loopback identity, real durable consent and no manual fact insertion.
The HTTP transport remains in-process; this is software simulation evidence.
Exact component heads, hosted results and review links will be appended after checks.


## Storage authority candidate under review

Storage draft #36 at `13f84799e722c220c54ad5711a35bb9a541f0c7c` passes all hosted
checks and 75 component tests. Eight authenticated baseline failures were
reproduced; 27 new tests cover scopes, source states, identities, revocation,
orphan reads after restart and simultaneous create/delete locking. This workspace
candidate pins that validated component and uses separate read and intake tokens;
combined hosted validation is pending.

Exact operation scopes and owned admitted source references are enforced on the
bounded canonical API. Unmapped legacy workflows deny authenticated callers.
Source locks span domain creation; canonical reads deny invalid references after
a partial deletion. Two-store deletion remains non-atomic. Facts are manually
associated, not verified extractions from source bytes. Consent, independent
policy, derivative/backup recovery and full runtime qualification remain open.

A separately approved disposable CPU model experiment uses fixed official Qwen
and llama.cpp artifacts with strict resource/network limits. Its workflow records
success or failure honestly; no model result is claimed until that run completes.
No operational deployment or live health-account connection is authorized here.
## Objective and authority

Close authenticated-boundary and private-state gaps, then converge the actual
runtime before a read-only synthetic health journey. No broad rewrite, hardware
purchase, OAuth grant, real records, paid model, purchase or meeting participation.
The original local October plan and unrelated work are preserved.

## Component packets

### Current merged foundations and synthetic candidate

Verified merges: platform PR44 `39ff9994e1643d806a450041ae35987be1064b65`,
storage PR34 `4642dd1feec4a7712cecdffda5e761bb06af39cf`, orchestrator PR47
`dc28f170454498e15cb966daa87261e1985cb09a`, workspace PR57
`c212b72d948a017496c4c4bfe7dcedc8096271f0`. Workspace run 40959020046
passed every job, including Phases 0–10 and encrypted MinIO backup/verify/restore.
That earlier run did not adopt the new orchestrator/storage components.

This new candidate pins tested storage `7343e72078d0f89184e55051653b3d4b64a52f6b`
and orchestrator wellness draft `b0ab000bab586476867388418181e87f47a39f98`.
Caller adapter PR48 merged as `8dabe96f16c644475099b2ae1964bde88f3bf2b3`; PR49 targets main.
both component heads pass all hosted checks (300 caller tests; 329 wellness tests). Inference remains unadopted; its
separate draft at `a3c066aef0447f474438ae90d6d14c0289777f3f` passes 70 tests
but still lacks qualified immutable runtime binding.

The local synthetic integration test passes through real storage import,
admission, domain records, canonical authenticated input, encrypted databases,
restart, person isolation, deletion cascade and session revocation. Manually posted synthetic observation fixtures produce changed/unchanged/unknown entries with associated source IDs.
ASGI transports are in-process, JWKS/introspection is loopback, and policy
decisions are controlled fixtures. No real model or wearable runs. Production
does not configure the journey. Combined workspace run 40963268626 passed all jobs at bd59e870b9154736b80440eaf16f47a8515e2f5d with the preceding wellness pin. This revision advances the pin after the multi-metric deduplication regression passed component CI; final combined validation is pending.

Source/domain deletion spans separate commits. The test verifies ordinary
cascade, not crash atomicity or simultaneous ingest/delete/correction. Migration,
backup integration and consent-grant lifecycle remain open. The deterministic
brief does not infer medical significance or actionable treatment opportunities.

### Earlier review checkpoint before merges

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

### Synthetic packet review clarification (October 29)

The harness manually posts observation facts after source admission. Associated
source IDs do not prove derivation from stored source bytes, and storage does not
yet validate source existence/ownership/admission for domain references. Storage
operation-specific write scopes are also outstanding: a read-only brief does not
prove a least-privilege storage bearer. Production remains unconfigured.

The corrected integration assertion uses the implemented GET /v1/sources route:
owner success, empty other-person list, denied other-person deletion and preserved
owner state. No HTTP source export route exists. Direct storage revocation is
checked separately from ingress revocation. Independent policy/consent gates,
source/domain atomicity and real runtime qualification remain open.
### Approved CPU experiment result: not qualified

Run 40974190175 stopped before downloads because no cached Ubuntu image existed.
Run 40974416361 used an ephemeral empty image with no extra external download;
verified the approved Qwen and llama.cpp artifact sizes/SHA-256 and license texts;
and ran dependency/help checks with network disabled, read-only mounts, no
credentials, an unprivileged UID, two CPUs and 4 GiB memory. The inference phase did
not run: the pinned runner does not advertise the harness's --no-conversation
option. No model-quality, latency or runtime-integration success is claimed.

The failed evidence artifact is retained with that run. The workflow is now
manual-only so ordinary PR updates cannot consume another model download. This
does not turn the failed experiment green; another actual-model attempt requires
an explicit run after reviewing the exact CLI contract and transfer budget.
Required storage/workspace validation remains unchanged.
The pinned upstream completion README and argument definitions identify
llama-completion as the non-conversational entrypoint. The harness selection is
corrected, but no second model download or inference run has been performed.
An explicit future run must account for another approximately 1.14 GB transfer;
the preserved failed run does not become successful through this source fix.

### Terminal lifecycle correction and actual CPU smoke result

Independent review identified a source lifecycle replay issue. New authenticated
regressions reproduce it before the fix and cover restart after an interrupted
cascade. The correction makes rejection/rollback terminal, prevents deleted IDs
from regaining admission, and checks source bytes and metadata integrity before
admission and canonical reference use. Valid intact replay remains idempotent.
Two-database deletion is still not atomic; this closes the tested replay path,
not every recovery or derivative-store gate. Revised component validation and
workspace pin are recorded with the correction commit.

The single corrected CPU attempt completed actual generation in run 40976039551,
using the exact previously approved artifacts and limits. Dependencies and CLI
flags were checked before model download; total transfer including licenses was
1,140,027,510 bytes and wall time for the inference command was 8.28 seconds.
The container had no network or credentials, read-only mounts, an unprivileged UID,
two CPU threads and a 4 GiB memory cap. This is one hosted CPU smoke result, not
Ollama binding, deployed policy integration, physical qualification or a benchmark.
The raw completion did not follow the requested READY response format, so prompt
construction and instruction-following remain unqualified. Failure 40974416361 and
success 40976039551 retain separate evidence. Dedicated experiment PR #60 closed
without merging; the reviewed integration branch keeps its manual-only workflow.
### Validated component candidates for this workspace pin

- Storage draft #37: `b352435f0bc24f9494866bc11b77a4277297ca45`; all hosted
  checks pass (security run 40995718560), 95 local component tests pass.
- Orchestrator draft #50: `028ba8ece6926857da74883473621a7e4d335889`;
  hosted run 40996216258 reports 336 passed; security run 40996216745 passes.
- Both old manual-fact and new export-derived local integration tests pass together
  (2 passed). The new path uses real durable consent and byte extraction.
- Initial local orchestrator invocation without legacy fixture switches reported
  328 passes/8 auth-related failures; new authenticated adapter tests passed. A
  later full local retry was stopped after exact-head hosted validation succeeded.
  Legacy CI switches are explicitly cleared by all authenticated boundary tests.
- Public documentation draft #54 at `d0a572d7c4560452842d60a558a32c964cfdacfb`
  passed build/accessibility in run 40996251981; deployment skipped. No public
  release claim changed yet. Workspace combined hosted validation pending.

Readiness: suitable for review as a synthetic prerequisite packet only. Do not
admit real records. Outstanding gates include prospective consent before actual
intake, selected real export adapters, restore-resistant revocation/deletion,
other derivative stores, key/incident operations, physical recovery and accessible
participant evaluation. Inference #9 remains draft; no new model experiment.
