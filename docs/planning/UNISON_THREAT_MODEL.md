# Unison Threat Model

Status: authoritative living threat model; Phase 3 controls evidenced
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
| T-01 | Malicious or overprivileged household administrator | Phase 1 separates household administration from person data/key handles; host-root physical access remains a platform-hardening concern | Separate admin/data authority, per-person keys, minimal metadata, eviction without decryption, auditable admin operations | P1 accepted evidence: admin has no private-read/key-export role; P4 proof remains |
| T-02 | Household member accesses another member's context | Phase 2 private/shared membership checks bind every governed query and return non-oracular denial | Principal-bound queries, row/space authorization, independent keys and indexes | P2 candidate: private memory/summary/index/search/prompt/export canaries remain isolated |
| T-03 | Caller-supplied identity spoofing | Signed context and middleware now reject mismatched person/user/assistant/household/channel hints | Signed principal context, server-side assistant binding, reject mismatches | P1 accepted evidence: forged-hint matrix and endpoint inventory pass |
| T-04 | Compromised remote channel | No normalized assurance/binding system | Pairing, channel identity, assurance, least authority, revocation, step-up authentication | P5: stolen token/channel cannot perform sensitive task |
| T-05 | SIM swapping | SMS not implemented; future risk | Treat SMS as low assurance, prohibit recovery/sensitive changes, require stronger factor | P5: simulated reassignment cannot access protected data |
| T-06 | Voice impersonation | Voice routes lack production speaker authentication | Voice is intent input, not sufficient identity for high risk; step-up and anti-replay | P5/P8: recorded voice cannot authorize protected action |
| T-07 | Stolen appliance | Phase 1 provides per-person key handles, lock and revocation; disk encryption, TPM binding, remote revocation transport, and backup remain | Full-disk protection guidance, hardware-backed/per-person keys, lockout, remote token revocation, encrypted backups | P1 accepted evidence: lock/revocation and encrypted local migration; P6 offline/backup proof remains |
| T-08 | Compromised connector/integration | Task credentials are encrypted and injected only to the exact principal/capability consumer; opaque identifiers reach planners | Per-person credential broker, scoped tokens, purpose/data grants, egress allowlists | P3 candidate: wrong principal/capability and audit-secret canaries deny; P7 connector proof remains |
| T-09 | Prompt injection through email | Email is explicitly tainted as untrusted content and cannot supply action authority | Treat content as untrusted data, instruction/data separation, capability confirmation, provenance | P3 candidate: email corpus cannot change policy or invoke send |
| T-10 | Prompt injection through websites/documents/tools | Web, document, tool, and model output share the same provenance/taint denial path | Sandboxing, content labels, taint/provenance, no secret exposure, constrained tool plans | P3 candidate: all four corpora deny high-risk action authority; P7 browser isolation remains |
| T-11 | Malicious capability package | Versioned manifests declare data, recipients, location, risk, cost, reversibility, audit, retention, egress, files, devices, resources, signature, and revocation | Signed package, provenance, explicit data/recipient declarations, sandbox, egress/file/device controls, revocation | P3 candidate: incomplete, broad, expired, replayed, overreaching, and revoked authority denies |
| T-12 | Overbroad model disclosure | Remote inference requires an allowing disclosure decision and removes undisclosed fields and secrets | Disclosure decision, local alternative check, minimization/redaction, provider terms profile, audit | P3 candidate: disclosure canary absent and synthetic field ratio is at most 0.5 |
| T-13 | Backup-provider compromise | Conventional S3 examples; no E2EE protocol | Client encryption, signed manifests, minimal metadata, independent keys, backend portability | P6: hostile backend cannot decrypt or forge accepted snapshot |
| T-14 | Cloud-model retention or training | Provider abstraction exists without enforceable retention profile | Provider policy metadata, user selection, data minimization, no authoritative memory, contractual review | P3/P7: routing honors provider/data-class restrictions |
| T-15 | Secrets leakage | Credential plaintext is encrypted at rest, never returned by the API, and injected only inside an execution consumer | Secret broker, no plaintext env in product, redaction, rotation, scanning, scoped injection | P3 candidate: planner/audit canaries remain absent; hardware rotation remains |
| T-16 | Insecure logs and traces | Trust audit records outcome, reason, consequence, and owner-readable explanation without request content or secrets | Data-class-aware structured logging, payload references, per-person audit access, retention/deletion | P3 candidate: accessible audit and secret canary pass |
| T-17 | Metadata leakage | Disclosure minimization bounds fields; residual provider timing/size metadata remains | Minimize identifiers, pad/batch where justified, document residual metadata, separate operational metrics | P3 candidate: field minimization metric; P5/P6 transport metadata work remains |
| T-18 | Accidental shared-space promotion | Sharing requires a shared target, write membership, confirmation-oriented UX, and creates a provenance-linked copy | Explicit copy/share action, preview, provenance, policy check, undo/tombstone | P2 candidate: source classification/space remain unchanged and clone is audited |
| T-19 | Cross-person inference leakage | Prompt construction requires explicit authorized spaces and purpose-compatible inference records | Per-principal retrieval/index/cache keys, prompt construction tests, memory isolation, no shared hidden state | P2 candidate: memory/summary/index canaries never enter another person's search, prompt, or export |
| T-20 | Unauthorized recovery | No per-person recovery design | Recovery ceremony, independent keys, delay/notification, revocation, no provider-held keys | P6: attacker/admin cannot restore another person |
| T-21 | Supply-chain compromise | Mixed CI, tag-pinned actions, downloaded cosign binary without checksum in release workflow | Pinned actions/digests, dependency locks, SBOM, signed provenance, image verification, reproducible builds | P0/P6/P8: verify signatures/SBOM/provenance before install/update |
| T-22 | Fail-open authorization dependency | Incomplete/unknown trust dimensions, missing remote decisions, unavailable grants, and legacy capability authority deny | Fail-closed sensitive operations, safe degraded read-only modes, dependency health gates | P3 candidate: unknown-dimension and missing-dependency matrices pass |
| T-23 | Replay/idempotency attack | Confirmations and capability authority use request binding, expiry, one-use state, and nonce replay guards | Nonces, timestamps, idempotency store, provider event IDs, replay window | P3 candidate: replay/expiry/cancellation tests pass; P5 channel replay remains |
| T-24 | Confused deputy between services | Capability grants intersect principal, assistant, capability, action, purpose, audience, data, space, and recipient | Workload identity plus end-user delegation chain and audience restriction | P3 candidate: grant-boundary overreach denies |
| T-25 | Shared infrastructure side channel | Trust audit and credentials are principal-bound; resource ceilings are mandatory manifest fields | Namespace isolation, cache partitioning, resource quotas, constant/error-safe responses where needed | P3 candidate: resource declaration and owner audit pass; P4 timing proof remains |
| T-26 | Destructive or irreversible action | High-risk or external action is draft/preview first and requires exact, expiring confirmation; sensitive action steps up | Risk/reversibility metadata, dry run, confirmation, undo/compensation, bounded authority | P3 candidate: send/step-up/cancel/replay tests pass; domain undo remains P7 |
| T-27 | Coercive or manipulative optimization | Unknown purposes, including engagement optimization, deny and are owner-explainable | Personal charter, ranking constraints, no sponsored/engagement signals, inspectable rationale | P3 candidate: unknown-purpose matrix denies; P7 workflow ranking review remains |
| T-28 | Accessibility failure causes unsafe consent | Semantic review exposes action, recipients, data, purpose, consequence, reversibility, cost, and equivalent options | Semantic parity, unambiguous recipient/data/action, cancellation and recovery in every modality | P3 candidate: text/speech/keyboard/screen-reader/reduced-motion assertions pass |
| T-29 | Denial leaks protected existence | Trust denials describe missing authority dimensions without revealing protected resource existence | Non-oracular denial responses and privacy-preserving audit details | P3 candidate: uniform authority denial and minimal audit pass; P4 timing proof remains |
| T-30 | Deletion/export incompleteness | Governed current/history content is redacted on delete/expiry and per-person export traverses authorized spaces | Data inventory, tombstones, backup retention semantics, per-person export manifest | P2 candidate: retention/deletion/export reconciliation passes; provider-blind backup semantics remain P6 |

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

Algorithm selection, TPM integration, passkey support, recovery shares, and secure deletion guarantees are pending human/security review. Until decided, planned cryptography must not be labeled implemented.

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
