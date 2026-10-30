# October 2026 security implementation evidence

## Synthetic browser workflow evidence

Starting revisions: storage `d860878e0d9987e2b266d45a96bf981141ae9f35`, workspace
`fccbeb20410a5fd54cbbadc321b822ba6df025c7`; renderer from its current main.
The backend reuses the export parser, prospectively binds selected file hash/size,
and checks a separately retained authority ledger for all workflow actions.

Local evidence: full storage run 109 passed before two final added cases; final
focused workflow suite 16 passed (including concurrent restore/revoke and corrupt
ledger). Renderer local suite exposed Windows POSIX-mode/encoding assumptions and
one fixture wording issue; wording corrected, Linux exact-head suite required.
Real browser test passes: 320/1280 widths, normal/forced colors, keyboard, source
links, unknown wording, 200% text and 24 axe audit states. Eight termination/restore
cycles replace actual encrypted SQLite data bytes while retaining authority.
Initial contrast and enlarged-text wrapping failures were corrected without disabling
checks. Screenshots were visually inspected. Upstream renderer/storage transport is
in-process; browser HTTP and signed identity checks are real test services.

No personal records, model invocation, live integration, host security change or
operational deployment occurred. All new candidates must remain draft pending review.


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

### Validated browser milestone component pins

Storage draft #38 `8c2e2186d12e7d007d75c8c7a511ae90c45bd3ef`: all hosted checks
pass, including 111 tests in run 41081214797. Renderer draft #25
`71b05af3b817fabf8728a1551fc386321e5af64b`: Linux tests and existing Phase 1/2
accessibility pass in run 41081283720. Renderer starting main was
`65fcd0ac3973bcbdbf152170854b5403fa236723`.
The local new browser acceptance passes 24 audited states across normal/forced
colors and 320/1280 widths, keyboard operation, 200% text and source links.
The combined workspace now runs that acceptance with locked Playwright dependencies
and saves synthetic screenshots/results as a CI artifact. Combined result pending.
All PRs remain drafts; no public or operational deployment occurred.

Review correction: renderer 378beebfed3f23d60f59e089db080fb8612ccbe8 disables conflicting controls during requests and announces busy state, rejects stale visibility-invalidated responses, and clarifies that 24-hour access expiry does not delete retained content/backups. Node delayed-request regressions cover consent/import, brief, clear, terminal actions and restore. The original enabled Clear control failed the new regression before the fix. Existing authority-ledger rollback limitations remain unchanged. Updated combined validation pending.

## October 30 source/delegation candidate

Objective: prove source-neutral intake boundaries with synthetic statement and
unfamiliar-document adapters, plus a bounded provider-neutral delegation/repair
and multimodal intent contract. This is not real-data enrollment or a production
runtime. No OAuth grant, vault access, model run, transaction or external account
was created. Source, identity and semantic-experience roadmap entries are reconciled
in the existing implementation plan.

Starting revisions: storage main `3c96ae4062f95aca1f4e5742ebd447f0ff44f46f`,
orchestrator main `3a9f15655864cc2e8284f1e3dd58be74040fed3b`, workspace main
`61da02a2ef704445bbc9d8b3aefdcdc46823ee21`.

Candidates: storage #39 `43d2d40238cbf7cc9df8506f4ce06662ecc72892` and
orchestrator #51 `e118068f00c156415a8ffe4bd9734659d7c06e31`. Both are draft,
unmerged. The existing renderer pin is unchanged. Library contracts are
`SourceAdapter` / `source-evidence.v1`, `CredentialUseAdapter`,
`synthetic-delegation.v1`, and `intent-experience.v1`.

Local Windows control-plane evidence: 28 source/refactored health lifecycle tests
passed before the final protocol-only refinement; 12 source tests passed on the
final storage candidate. 19 delegation unit/simulation tests passed on its final
candidate. New cross-component acceptance passes with actual encrypted SQLite
state reopened after restart, five tasks/one repair, paused/revoked exclusions,
source-linked facts and deletion/old-data restore denial. Run with explicit
UNISON_TEST_STORAGE_ROOT, UNISON_TEST_ORCHESTRATOR_ROOT and UNISON_TEST_COMMON_ROOT:
`python -m pytest tests/integration/test_source_delegation.py -q`.

New source formats and delegation engine have no production HTTP ingress. Person
contexts in the new integration are synthetic validated contract fixtures, not a
new end-to-end OAuth/authentication proof. Existing authenticated health tests
continue to exercise the refactored lifecycle. Static semantic HTML and spoken
text are representations; no real ASR/TTS or participant/device accessibility
qualification is claimed. Three mechanism labels use one mock adapter protocol,
not three real integrations. Provider unknown/absent outcomes remain pending;
there is no automatic retry that could duplicate an in-flight effect.

Remaining gates: secured broker/process isolation, real provider and supported
nonvisual challenge integrations, full external-effect reconciliation, production
principal binding, ledger/key recovery and rollback resistance, adapter package
qualification, migrations and participant testing. Recovery in this packet uses
current retained authority; physical deletion and outside copies remain outside
its proof. No new candidate may merge or publicly deploy before independent
exact-head review and authorization. Hosted CI and independent review pending.

## Review correction and connected intent candidate

This supersedes the prior orchestration candidate. Four regression cases
reproduced missing unique grant/duration binding, missing exact task binding and
an advertised but unimplemented Repair response. Corrected orchestrator #51 is
`3e4dba62d9d8d223fcdb3c7fa8b74eed2a6a2360`; new renderer #26 is
`6ed92219106ea0ee9c18ac4e8ed7f9ee5a961103`. Storage #39 is unchanged.

The v2 grant/confirmation state includes unique grant/task identity, person,
meaningful scope, duration/expiry and approval deadlines. The old unmerged v1
state is rejected rather than silently migrated. Repair requests and subsequent
simulated verification now follow the actual presented-choice path with current
resource/challenge bindings. Plain-language permission summaries show scope and
expiry without exposing opaque internal IDs as the person's workflow.

The optional renderer now connects visual choices and typed screenless commands
to trusted mock state transitions. It requires an authenticated person and
explicit fixture coordinator injection; it is default-disabled. Separate mock
OAuth access/refresh leases, non-refreshable session expiry and locked/expiring
vault-use approval have distinct state behavior. Existing valid delegation is
reused without requesting new authority for each task.

Local final focused evidence: 29 delegation tests; two renderer bridge tests;
source/delegation encrypted integration passes; existing health and connected
intent browser journeys pass together (2 tests, 92.14 seconds). The new journey
uses signed fixture identities and actual renderer HTTP/controls, exercises
visual and typed screenless modes at 320/1280 widths, forced colors, 200% text,
reload/mode persistence, busy controls, authorization negatives and unsupported
nonvisual verification. Four sampled visual fallback states have zero axe
violations; this is not participant or real speech qualification. Screenshots
and results are retained by the existing browser artifact step.

No ASR/TTS, live credentials/providers, actual MFA/device verification, real data,
operational runtime or public deployment. New candidates remain draft and
unmerged pending exact-head CI and independent review. Hosted results for prior
heads do not validate this correction.

Two further mock-isolation regressions reproduced cross-connection renewal of
OAuth/vault-use leases. The final mock adapters isolate refresh lease deadlines
per handle and invalidate old vault leases on unlock before fresh approval.
Both regressions pass; focused delegation suite now has 29 passing tests.
