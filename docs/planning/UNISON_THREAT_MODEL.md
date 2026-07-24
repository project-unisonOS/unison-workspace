# Unison Threat Model

Status: authoritative living threat model; Phase 5 bounded controls in review
Last updated: 2026-07-21

## Security objective

Unison must remain a private, inspectable, person-aligned assistant even when several assistants share one appliance and when external models, channels, backup providers, websites, and capabilities are used. The system must make unauthorized use, inference, disclosure, commercialization, or recovery of personal context difficult by design.

No phase is complete until its applicable threats have executable controls and negative tests. Documentation, policy statements, and encrypted transport alone are not sufficient evidence.

## Protected assets

- Person, assistant, household, device, and channel identities.
- Private and shared context, memory, relationships, goals, commitments, charter, preferences, and inferred attributes.
- Credentials, tokens, encryption keys, recovery material, capability grants, and standing permissions.
- Messages, documents, media, model prompts/results, browser state, and task artifacts.
- Audit records, disclosure decisions, provenance, and deletion/export state.
- Availability and integrity of the appliance, models, updates, backups, and recovery process.
- The person's time, attention, reputation, finances, relationships, and ability to cancel or correct actions.

## Principals and adversaries

- The primary person served by an assistant.
- Other household members, including curious or malicious members.
- Household/device administrators who are operationally privileged but not automatically authorized for private data.
- Trusted local services and optional modality adapters.
- Capability packages, connectors, websites, documents, email senders, channel providers, remote models, and backup providers.
- External attackers, thieves, supply-chain attackers, compromised maintainers, and malicious insiders at providers.
- Accidental misuse, ambiguous context, model hallucination, and operator error.

## Trust boundaries

1. Physical appliance and host operating system.
2. Personal Data and Trust Store, including keys and policy decisions.
3. Each `AssistantInstance` and per-person data domain.
4. Each explicit shared `ContextSpace` and its membership/key domain.
5. Unison Core planning and context-use boundary.
6. Capability Host and each individual sandbox.
7. Inference boundary, separated into local and remote providers.
8. Channel Gateway and each provider/relay.
9. Unison Surface and local/remote client session.
10. Backup backend and recovery ceremony.
11. Update, build, artifact, dependency, and GitHub supply chain.

## Core invariants

- Identity authority is server-derived from verified credentials; request identifiers are only hints.
- A process or household administrator does not gain plaintext private data solely through administrative status.
- Private-to-shared promotion is explicit, attributable, reversible where possible, and auditable.
- Unknown authority, scope, purpose, audience, data class, or channel assurance denies.
- Capabilities and models receive only task-minimum data and credentials.
- External results do not enter durable memory without provenance and admission policy.
- Security decisions fail closed when dependencies are unavailable, except where a documented availability policy explicitly selects a safe degraded mode.
- Logs and telemetry do not become a shadow copy of private context.
- Backup providers cannot decrypt content.
- Recovery cannot silently bypass per-person isolation.
- Cancellation and revocation propagate to queued or continuing work.

## Threat register

| ID | Threat | Current exposure observed | Required controls | Phase and boundary evidence |
| --- | --- | --- | --- | --- |
| T-01 | Malicious or overprivileged household administrator | Household administration exposes minimized membership metadata and removal revokes authority without transferring private resources; host-root physical access remains a platform-hardening concern | Separate admin/data authority, per-person keys, minimal metadata, eviction without decryption, auditable admin operations | P4 candidate: minimized listing, no private reads, removal, session revocation, and key rotation pass |
| T-02 | Household member accesses another member's context | Private/shared membership checks bind governed queries and the Phase 4 cross-surface matrix returns non-oracular denial | Principal-bound queries, row/space authorization, independent keys and indexes | P4 candidate: 13/13 surface denials plus search/export/audit canaries pass |
| T-03 | Caller-supplied identity spoofing | Signed context and middleware now reject mismatched person/user/assistant/household/channel hints | Signed principal context, server-side assistant binding, reject mismatches | P1 accepted evidence: forged-hint matrix and endpoint inventory pass |
| T-04 | Compromised remote channel | Telegram is an untrusted low-assurance relay; private-chat binding and per-person credentials now bound its authority | Pairing, channel identity, assurance, least authority, revocation, step-up authentication | P5 candidate: stolen subject/token, wrong person, revocation, and sensitive-task tests deny |
| T-05 | SIM swapping | SMS is not implemented; Telegram identity reassignment is modeled as the analogous low-assurance risk | Treat remote identifiers as low assurance, prohibit recovery/sensitive changes, require stronger factor | P5 candidate: simulated reassignment cannot bind or access protected data |
| T-06 | Voice impersonation | Voice routes lack production speaker authentication | Voice is intent input, not sufficient identity for high risk; step-up and anti-replay | P5/P8: recorded voice cannot authorize protected action |
| T-07 | Stolen appliance | Phase 6 candidate adds provider-blind per-scope backup, recovery proof, replacement-device revocation, and key rotation; full-disk and TPM production validation remain | Full-disk protection guidance, hardware-backed/per-person keys, lockout, remote token revocation, encrypted backups | P6 candidate: provider/stolen-copy plaintext canaries absent; clean restore revokes old devices and rotates backup authority |
| T-08 | Compromised connector/integration | Task credentials are encrypted and injected only to the exact principal/capability consumer; opaque identifiers reach planners | Per-person credential broker, scoped tokens, purpose/data grants, egress allowlists | P3 candidate: wrong principal/capability and audit-secret canaries deny; P7 connector proof remains |
| T-09 | Prompt injection through email | Email is explicitly tainted as untrusted content and cannot supply action authority | Treat content as untrusted data, instruction/data separation, capability confirmation, provenance | P3 candidate: email corpus cannot change policy or invoke send |
| T-10 | Prompt injection through websites/documents/tools | Web, document, tool, and model output share the same provenance/taint denial path | Sandboxing, content labels, taint/provenance, no secret exposure, constrained tool plans | P3 candidate: all four corpora deny high-risk action authority; P7 browser isolation remains |
| T-11 | Malicious capability package | Versioned manifests declare data, recipients, location, risk, cost, reversibility, audit, retention, egress, files, devices, resources, signature, and revocation | Signed package, provenance, explicit data/recipient declarations, sandbox, egress/file/device controls, revocation | P3 candidate: incomplete, broad, expired, replayed, overreaching, and revoked authority denies |
| T-12 | Overbroad model disclosure | Remote inference requires an allowing disclosure decision and removes undisclosed fields and secrets | Disclosure decision, local alternative check, minimization/redaction, provider terms profile, audit | P3 candidate: disclosure canary absent and synthetic field ratio is at most 0.5 |
| T-13 | Backup-provider compromise | Phase 6 candidate uses local envelope encryption, signed encrypted manifests, independent checkpoints, hostile-provider harness, and provider migration | Client encryption, signed manifests, minimal metadata, independent keys, backend portability | P6 candidate: tamper, rollback, fork, truncation, reorder, replay, missing object, corruption, and wrong-key cases fail closed |
| T-14 | Cloud-model retention or training | Provider abstraction exists without enforceable retention profile | Provider policy metadata, user selection, data minimization, no authoritative memory, contractual review | P3/P7: routing honors provider/data-class restrictions |
| T-15 | Secrets leakage | Credential plaintext is encrypted at rest, never returned by the API, and injected only inside an execution consumer | Secret broker, no plaintext env in product, redaction, rotation, scanning, scoped injection | P3 candidate: planner/audit canaries remain absent; hardware rotation remains |
| T-16 | Insecure logs and traces | Trust audit records outcome, reason, consequence, and owner-readable explanation without request content or secrets | Data-class-aware structured logging, payload references, per-person audit access, retention/deletion | P3 candidate: accessible audit and secret canary pass |
| T-17 | Metadata leakage | Telegram and backup providers receive separately documented residual metadata; backup names use keyed opaque person/space identifiers | Minimize identifiers, pad/batch where justified, document residual metadata, separate operational metrics | P6 candidate: provider view contains no local scope names or plaintext; opaque identifiers, size, timing, request volume, account, and bucket remain documented |
| T-18 | Accidental shared-space promotion | Sharing requires a shared target, write membership, accessible preview, and creates a provenance-linked copy | Explicit copy/share action, preview, provenance, policy check, undo/tombstone | P4 candidate: preview and explicit household-artifact flows preserve private source boundaries |
| T-19 | Cross-person inference leakage | Prompt construction requires authorized spaces; household coordination reports zero private sources | Per-principal retrieval/index/cache keys, prompt construction tests, memory isolation, no shared hidden state | P4 candidate: inference refuses retrieval/guessing and shared output contains no private canary |
| T-20 | Unauthorized recovery | Phase 6 candidate enrolls independent recovery public keys, local non-voice ceremony, current checkpoint proof, and replacement-device revocation | Recovery ceremony, independent keys, delay/notification, revocation, no provider-held keys | P6 candidate: wrong person/admin/provider, remote/voice enrollment, wrong signature, replayed challenge, and rollback restore deny |
| T-21 | Supply-chain compromise | Phase 9 locks one artifact owner, deterministic digest manifest, signed bundle/bootstrap verification, installation receipts, threshold-signed updates, pinned release inputs, signed/scanned images, SBOM/provenance, and public-download verification; physical promotion evidence remains open | Pinned actions/digests, dependency locks, SBOM, signed provenance, image verification, reproducible builds | P9 bundle/update transactions reject substitution and restore last known good; P9.5 public preview assets and malicious/partial mirror rejection pass |
| T-22 | Fail-open authorization dependency | Incomplete/unknown trust dimensions, missing remote decisions, unavailable grants, and legacy capability authority deny | Fail-closed sensitive operations, safe degraded read-only modes, dependency health gates | P3 candidate: unknown-dimension and missing-dependency matrices pass |
| T-23 | Replay/idempotency attack | Confirmations, capability authority, provider update IDs, event hashes, nonces, cursor persistence, and replay windows reject reuse | Nonces, timestamps, idempotency store, provider event IDs, replay window | P5 candidate: duplicate, replay, out-of-order cursor, delayed event, outage, and reconnect tests pass |
| T-24 | Confused deputy between services | Capability grants intersect principal, assistant, capability, action, purpose, audience, data, space, and recipient | Workload identity plus end-user delegation chain and audience restriction | P3 candidate: grant-boundary overreach denies |
| T-25 | Shared infrastructure side channel | Principal namespaces and a fair scheduler impose queue, concurrency, CPU, and memory budgets; production timing characterization remains | Namespace isolation, cache partitioning, resource quotas, constant/error-safe responses where needed | P4 candidate: concurrent fairness/quota/restart checks and content-free resource snapshots pass |
| T-26 | Destructive or irreversible action | High-risk or external action is draft/preview first and requires exact, expiring confirmation; sensitive action steps up | Risk/reversibility metadata, dry run, confirmation, undo/compensation, bounded authority | P3 candidate: send/step-up/cancel/replay tests pass; domain undo remains P7 |
| T-27 | Coercive or manipulative optimization | Unknown purposes, including engagement optimization, deny and are owner-explainable | Personal charter, ranking constraints, no sponsored/engagement signals, inspectable rationale | P3 candidate: unknown-purpose matrix denies; P7 workflow ranking review remains |
| T-28 | Accessibility failure causes unsafe consent | Semantic decision, household, remote-channel, backup, and replacement-restore controls expose disclosure, verification, cancellation, denial, revocation, and recovery without color-only meaning | Semantic parity, unambiguous recipient/data/action, cancellation and recovery in every modality | P6 candidate: labelled keyboard-native controls, live status, secret cleanup, dry run, cancellation, reduced-motion/forced-color behavior, and real-browser axe checks pass |
| T-29 | Denial leaks protected existence | Cross-person and nonexistent-resource probes return the same message and operational/audit output excludes protected values | Non-oracular denial responses and privacy-preserving audit details | P4 candidate: 13/13 uniform denial surfaces and audit canaries pass; timing certification remains out of scope |
| T-30 | Deletion/export incompleteness | Phase 6 candidate adds per-scope encrypted export, retention compaction floor, signed tombstone contract, provider deletion, and local key destruction | Data inventory, tombstones, backup retention semantics, per-person export manifest | P6 candidate: deleting one person leaves another verifiable; encrypted export has no plaintext; provider physical-erasure limitation is explicit |

## Phase 7 workflow reassessment

The bounded assistant-workflow implementation adds the following candidate
evidence without expanding the authority established in Phases 1–6:

| Threats | Phase 7 control and evidence |
| --- | --- |
| T-08, T-12, T-14, T-17 | Each external step declares its provider and disclosed fields; the engine emits only an allowlisted payload, records disclosure counts, and supports provider replacement. Fake-provider recordings contain synthetic data and explicitly prohibit personal data. |
| T-09, T-10 | Email, document, web, and provider content remains tainted data. Adversarial `instructions` and `sponsored` fields are removed before provider execution and cannot alter authority. |
| T-19, T-24 | Plans require an allowed context-space subset and allowed recipient subset before any provider call. Cross-person approval, private-space substitution, and wrong-recipient tests fail closed. |
| T-22, T-23 | Provider errors and timeouts produce an inspectable recoverable state. Stable step idempotency prevents duplicate external actions across retry and provider recovery. |
| T-26 | External calendar, mail, and shared-household actions require exact person-bound approval. Every workflow is cancellable and completed reversible actions expose compensation. |
| T-27 | Advertising, engagement, sponsored, and provider-lock-in ranking signals are rejected. Outcome metrics measure administrative work, commitments, interruptions avoided, recovery, disclosure, and estimated time returned. |
| T-28 | Plan, approval, running, success, failure, retry, provider replacement, cancellation, and compensation states have labelled keyboard controls, semantic live status, and non-color-only text equivalents. |

Phase 7 does not claim that an arbitrary provider is trustworthy, that a
provider physically deletes data, or that a model may independently broaden a
plan. Provider production enablement remains contingent on a separately
reviewed adapter, synthetic-account acceptance, scoped credentials, and the
same exact-action boundary tests.

## Phase 8 expansion 8.1 reassessment

| Threats | Expansion 8.1 control and evidence |
| --- | --- |
| T-06, T-26 | Speech is intent input only. Voice/control barge-in stops output and resumes listening; protected actions still require the accepted non-voice/step-up decision path. |
| T-11, T-21 | Canonical Ed25519 verification rejects tampering and unknown publishers. Permission additions require explicit review; incompatible and revoked packages deny. |
| T-12, T-14, T-22 | Model candidates must simultaneously satisfy location, disclosure, cost, risk, and availability. Offline and no-candidate cases fail closed. |
| T-28 | One semantic outcome preserves confirm, cancel, retry, recover, and dismiss actions through caption/visual fallback. High contrast, reduced motion, simplified language, keyboard, screen-reader semantics, and live captions are explicit. |

The expansion does not certify specialized assistive hardware without
representative disabled-user research, nor does it authorize BCI, robotics,
spatial control, or autonomous financial action.

## Cryptographic target model

The exact algorithms and hardware integrations require a dedicated design review, but the architecture requires:

- device identity distinct from person identity;
- per-person master-key hierarchy;
- separate keys for shared spaces;
- envelope encryption so data keys rotate without rewriting every backup object;
- authenticated encryption with stable version metadata;
- signed audit/backup/update manifests;
- revocation and key rotation when a device, channel, capability, or member is removed;
- no silent plaintext fallback in product profiles;
- recovery keys unavailable to storage, channel, model, and backup providers.

The Phase 6 software profile (AES-256-GCM, HKDF-SHA-256, Ed25519, and Argon2id),
recovery ceremony, shared rotation, retention/deletion semantics, and backend
contract were approved on 2026-07-22. TPM production integration, social
recovery, and provider physical-erasure guarantees remain unclaimed and require
separate review.

## Data classification and disclosure

Every durable record and outbound request must identify:

- owner and governing context space;
- provenance/source;
- sensitivity and data classes;
- permitted purposes and audiences;
- inference, action, disclosure, backup, and sync permissions;
- retention/deletion state;
- confidence when inferred;
- the decision and minimization applied before external disclosure.

Classification defaults to the most restrictive plausible state when metadata is missing.

## Audit and inspectability

The audit log must capture who requested what, which assistant/space was active, the purpose, context sources, capability/model/channel recipients, policy/disclosure outcome, confirmation, minimized fields, execution result, and recovery/cancellation state.

Audit views must:

- avoid storing secret values or unnecessary content;
- be accessible to the data owner;
- prevent other household members and ordinary administrators from browsing private events;
- support export, retention, and deletion rules without enabling history rewriting;
- provide human-readable explanations and structured machine evidence.

## Security verification layers

1. Schema/property tests for identifiers, claims, spaces, purposes, data classes, and decisions.
2. Unit tests for pure policy/disclosure and key-selection logic.
3. API boundary tests using forged/mismatched principals.
4. Cross-person and cross-space integration tests with canary records.
5. Capability sandbox escape/overreach tests.
6. Adversarial content tests for email, web, documents, and model outputs.
7. Channel replay, reassignment, revocation, and step-up tests.
8. Backup corruption, provider compromise, and unauthorized restore tests.
9. Supply-chain verification and update rollback tests.
10. Accessible confirmation, denial, cancellation, and recovery tests.

## Residual-risk reporting

Every phase gate must record accepted residual risks, owner, rationale, expiration/review date, and compensating controls. “Local-first,” “encrypted,” “private,” or “AI safety” are not acceptable substitutes for a described control and evidence.
