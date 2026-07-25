# Phase 11 LO-0 through LO-2 acceptance evidence

Status: software gates passed 2026-07-25

## Accepted boundary

AD-050 is accepted for the shared private life operations foundation. Health
and finance begin read-only. Diagnosis, prescribing, treatment changes, money
movement, securities trading, credit opening, beneficiary changes, and tax
filing fail closed.

## Implementation inventory

| Slice | Repository | Evidence |
| --- | --- | --- |
| LO-0 | `unison-common` | Ten canonical contracts, region provenance, correction semantics, prohibited-action policy, household, health, and finance synthetic canaries. |
| LO-1 | `unison-storage` | Encrypted quarantine and source library with safe paths, size and media allowlists, signature checks, archive limits, traversal denial, malicious-document flags, local extraction and OCR adapter, metadata, tables, barcodes, deduplication, versions, correction, admission, export, reclassification, rollback, and deletion. |
| LO-1 | `unison-experience-renderer` | Authenticated file picker, multi-file camera capture, conversational preview, safety flags, private admission, source count, status announcements, and keyboard focus handoff. |
| LO-2 | `unison-storage` | Read-only provider catalog, OAuth Authorization Code PKCE state, SMART FHIR and finance sandbox profiles, opaque token handles, bounded local and MCP grants, sync cursors and receipts, idempotent item import, cross-person isolation, disconnect, and revocation. |
| LO-2 | `unison-experience-renderer` | Plain-language scope preview, progressive connection setup, Connections and Imports review, keyboard, touch, speech-compatible semantics, and polite live status. |

## Threat and control map

| Threat | Control and executable evidence |
| --- | --- |
| Unauthenticated or cross-person import | Principal middleware and person plus space binding; negative export, sync, and disconnect tests. |
| Path and archive escape | Basename normalization, identifier validation, absolute path and parent traversal rejection, member and expansion limits. |
| Media type confusion | Explicit media allowlist, filename agreement, and PDF, PNG, JPEG, and ZIP signature checks. |
| Parser or OCR failure | Quarantine remains non-authoritative; deterministic metadata survives; admission creates no executable authority. |
| Document prompt injection | All source content is labeled untrusted; instruction and credential-exfiltration patterns produce review flags and no grants. |
| Malware | Signature policy blocks admission and fails closed. A production scanner can replace the deterministic fixture scanner behind the same gate. |
| Credential disclosure | The browser never accepts a provider credential. Storage returns only `vault://` or bounded-resource handles. Secrets do not enter prompts, skills, memory, logs, or MCP configuration. |
| OAuth interception or replay | Authorization Code PKCE S256, random state, ten-minute expiry, and one-time state consumption. |
| MCP scope expansion | Registration accepts only `mcp-resource://` bounded grants and read-only resource scope. |
| Provider replay or outage | Per-connection item deduplication, cursor receipts, stable connection state, and no import on inactive or revoked connections. |
| Unsafe health or finance action | Canonical prohibited-action policy rejects consequential action classes. |

## Synthetic and parser corpus

`unison-common/tests/fixtures/life_operations` contains synthetic household,
health, and finance documents. Each has a unique privacy canary and no real
personal information. The household fixture also contains a document prompt
injection. Storage tests add safe and hostile archives, image/OCR, CSV table,
barcode, malware, interruption, duplicate sync, revocation, and cross-person
fixtures.

## Scope truth

The software gate covers the initial local and sandbox adapter contract. It
does not claim production OAuth client registration, live SMART endpoint
certification, live financial-provider certification, production malware-engine
integration, or OCR quality on physical camera hardware. Those require adapter
and hardware evidence before a supported release.
