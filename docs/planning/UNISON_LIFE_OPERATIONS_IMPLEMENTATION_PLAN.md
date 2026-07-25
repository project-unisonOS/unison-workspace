<!-- markdownlint-configure-file {"MD024": {"siblings_only": true}} -->

# Unison life operations and conversational data onboarding implementation plan

Status: active Phase 11 execution plan; LO-0 through LO-6 software gates and LO-7 synthetic gate implemented

Date: 2026-07-25

Depends on:

- [Private life operations capability architecture](UNISON_PRIVATE_LIFE_OPERATIONS_ARCHITECTURE.md)
- Phase 1 principal binding and personal namespaces
- Phase 2 governed memory and context spaces
- Phase 3 capability, action, disclosure, and confirmation policy
- Phase 5 Channel Gateway
- Phase 6 provider-blind backup and restore
- Phase 8 capability supply-chain contracts
- Phase 10 adaptive maintenance

## Objective

Make it easy for a person to give Unison enough trustworthy context to become
useful without requiring technical setup, indiscriminate data access, or a
large up-front configuration exercise.

Deliver one shared ingestion and conversational onboarding platform, then use
it to implement:

1. private household operations;
2. a health timeline and visit-preparation experience; and
3. a read-only personal and family financial-attention experience.

## Experience principles

- **Conversation first, controls always available:** a person can say what they
  want to connect or drag something into the conversation. Structured privacy,
  destination, correction, and deletion controls remain directly accessible.
- **Progressive value:** one document or one account produces a useful result.
  Unison does not require a complete life import before helping.
- **Progressive profiling:** ask only questions needed for the current goal.
  Learn additional preferences when they become relevant.
- **Preview before admission:** show what Unison recognized, where it will live,
  who can access it, and what it will be used for before durable storage.
- **Source before inference:** preserve the original source and provenance.
  Derived facts never silently replace it.
- **Person before household:** new information is private to the importing
  person unless that person explicitly chooses a shared space.
- **Local first:** OCR, classification, extraction, deduplication, and
  summarization run locally when the appliance can support them.
- **Read-only first:** initial provider connections request the minimum
  read-only scopes.
- **Reversible onboarding:** disconnect, stop sync, correct, reclassify, export,
  and delete are normal flows.
- **No dark patterns:** declining a connection does not block unrelated
  features.

## Low-friction seeding mechanisms

### Conversational attachment

The person drops a file or image into the conversation or says:

- "Add this receipt to the dishwasher."
- "These are my latest lab results."
- "Keep this insurance policy private."
- "Use these statements to help me understand our monthly obligations."

Unison responds with a compact intake preview, not an opaque success message.

Initial formats:

- PDF;
- JPEG, PNG, and HEIF images;
- plain text and Markdown;
- CSV and JSON exports;
- common office documents;
- email message files; and
- ZIP archives after safe inventory review.

### Camera and scan capture

A phone or browser surface supports:

- one-tap photo capture;
- multi-page document scan;
- automatic edge and orientation correction;
- local OCR;
- barcode, QR code, model number, and serial-number recognition; and
- immediate destination and privacy confirmation.

The initial upload stays quarantined until malware, type, size, and archive
checks pass.

### Account connection

The conversational flow explains what access will be requested and why:

> "I can connect read-only access to your checking account to build a cash-flow
> forecast. I will not be able to transfer money. You can disconnect it and
> delete imported history at any time."

Preferred mechanism order:

1. OAuth 2.0 Authorization Code with PKCE and provider API;
2. SMART on FHIR for health systems;
3. provider-supported export import;
4. trusted MCP server through the Capability Host;
5. bounded browser export assistance; and
6. manual upload.

Unison never asks a person to paste a bank or health-portal password into chat.
Tokens are stored in the per-person credential namespace, never in a skill,
prompt, memory record, or MCP configuration visible to another principal.

### Guided export import

When no API is available, Unison explains how to export data from the provider,
waits for the file, identifies the export version, and imports it. A governed
skill may guide navigation, but it cannot read unrelated pages or submit a
provider action.

### Forward or share to Unison

Later channel integrations can support:

- share-sheet delivery from a phone;
- forwarding a receipt or statement through a bound private channel;
- saving from a browser extension; and
- adding files to an explicitly configured local intake folder.

Each item retains the authenticated sender or device, original timestamp,
channel assurance, and disclosure history.

### Existing local collections

A person can select a bounded local folder such as:

- `Household manuals`;
- `Health records`;
- `Tax 2026`; or
- `Receipts to review`.

The default is one-time import. Continuous watching is a separate revocable
grant with visible scope, schedule, and last-sync status. Hidden whole-home
directory crawling is prohibited.

### Conversational interview

Some important information has no source document. Unison can ask a short,
goal-specific interview:

- "Which home systems would be hardest to recover during an emergency?"
- "Which accounts pay your recurring household bills?"
- "Which medications should appear in your appointment brief?"

Answers are self-reports, labeled accordingly. Unison shows the resulting
record and asks for correction rather than treating model interpretation as
fact.

## Universal intake pipeline

```text
Authenticated source
        |
        v
Encrypted quarantine
        |
        +--> type, size, archive, and malware checks
        |
        v
Local OCR and structural extraction
        |
        v
Document and domain classification
        |
        v
Duplicate and prior-version detection
        |
        v
Proposed records, relationships, and destination space
        |
        v
Conversational preview and correction
        |
        v
Policy and consent decision
        |
        v
Immutable source admission plus versioned derived records
        |
        v
Index, timeline, commitments, and recommendations
        |
        v
Receipt, sync state, retention, and deletion controls
```

### Quarantine

Quarantine records:

- source principal and channel;
- byte length and cryptographic hash;
- claimed and detected media type;
- original name after path sanitization;
- scan results;
- archive inventory;
- processing policy; and
- expiration if admission is not completed.

No quarantined content enters retrieval, model context, skills, MCP, or shared
spaces.

### Extraction

Extraction produces:

- immutable source text with page or image coordinates;
- structured fields with confidence;
- table structures;
- dates, amounts, organizations, people, products, accounts, medications, and
  identifiers;
- candidate relationships;
- explicit redactions; and
- parser and model provenance.

Every extracted value points back to the exact source region.

### Classification and routing

The classifier proposes, but does not silently decide:

- domain;
- record type;
- person or household destination;
- sensitivity;
- retention;
- likely duplicates or superseded versions; and
- suggested next action.

Low-confidence, cross-person, or unexpectedly sensitive routing always asks.

### Admission

Admission creates:

1. an immutable encrypted source object;
2. a source record with provenance;
3. versioned derived domain records;
4. event and relationship edges;
5. search and retrieval entries scoped to the principal and context space; and
6. an understandable receipt.

Corrections create a new derived version and preserve the distinction between
source content and the person's correction.

## Account connection flow

```text
Person states a goal
        |
        v
Unison recommends a provider connection or export
        |
        v
Scope and privacy preview
        |
        v
Step-up authentication when required
        |
        v
Provider authorization with PKCE
        |
        v
Token sealed in per-person credential store
        |
        v
Initial bounded read-only sync
        |
        v
Record and field preview
        |
        v
Person confirms destination and retention
        |
        v
Incremental sync with cursor, receipt, and health status
```

Connection records include provider, principal, granted scopes, issue and
expiry times, last successful sync, cursor, imported record types, revocation
state, and deletion behavior. Provider credentials are referenced by opaque
handle.

## Conversational onboarding pattern

The dialogue uses six repeatable moves:

1. **Goal:** "What would you like help keeping track of?"
2. **Smallest useful input:** offer one account, one document, one photo, or a
   brief interview.
3. **Trust preview:** explain access, destination, retention, processing, and
   actions that remain impossible.
4. **Import preview:** show recognized facts, uncertainty, duplicates, and
   proposed relationships.
5. **First value:** immediately produce an inventory entry, timeline, attention
   item, or brief.
6. **Optional next step:** offer the next highest-value source without blocking
   use.

The conversation never becomes the sole way to understand or reverse setup.
The surface also provides Connections, Imports, Sources, Privacy, and Delete or
Disconnect views.

## Shared implementation architecture

### Canonical services and modules

- **Intake Gateway:** authenticated upload and import sessions, quarantine, and
  safe byte handling.
- **Extraction Worker:** local OCR, layout, table, metadata, and field
  extraction.
- **Admission Coordinator:** preview, correction, policy, source preservation,
  and governed-memory admission.
- **Connection Broker:** OAuth or SMART authorization, token handles, sync
  cursors, refresh, revocation, and provider health.
- **Domain Registry:** versioned record schemas, classifiers, validators,
  relationship rules, and retention defaults.
- **Life Operations Engine:** timelines, obligations, forecasts, attention
  rules, briefs, and cross-domain planning.
- **Unison Surface:** conversational setup plus explicit connection, import,
  source, privacy, correction, and deletion views.

These may begin as modules behind existing process boundaries. No new
independent service is created until isolation, scaling, or privilege requires
it.

### Capability package contract

Each package declares:

- resource and record types;
- accepted source formats;
- provider adapters and MCP mappings;
- extraction and normalization version;
- sensitivity and retention defaults;
- allowed destinations;
- read, interpret, prepare, execute, and prohibited actions;
- disclosure and confirmation rules;
- verification and recovery procedures;
- accessible experiences; and
- synthetic fixtures and adversarial tests.

### Tool routing

- stable APIs use typed native adapters;
- trusted third-party tools may arrive through MCP but are rewrapped as
  canonical actions;
- skills guide provider-specific procedures without credentials or authority;
- browser or computer use is an isolated export and navigation fallback;
- local models handle sensitive OCR, classification, extraction, and routine
  reasoning;
- remote models receive only an approved minimized projection; and
- every external action passes the existing Capability Host and policy flow.

## Phased delivery

### LO-0: Decisions, schemas, threats, and synthetic corpus

Status: **Complete in software on 2026-07-25.** Canonical contracts, prohibited
action policy, synthetic canary corpus, threat map, and executable contract
tests are recorded in
[PHASE11_LO0_LO2_EVIDENCE.md](PHASE11_LO0_LO2_EVIDENCE.md).

Deliver:

- approve the life operations architecture and onboarding privacy model;
- add canonical `SourceObject`, `ImportSession`, `ExtractedField`,
  `DerivedRecord`, `Connection`, `SyncReceipt`, `DomainPackage`,
  `AttentionItem`, and `Brief` contracts;
- define source versus inference correction semantics;
- define health and finance prohibited-action policies;
- map upload, parser, OCR, prompt-injection, cross-person, credential,
  malicious-document, archive, browser, MCP, and provider threats;
- build synthetic household, health, and finance documents with privacy
  canaries; and
- establish document-parser and OCR benchmark fixtures.

Gate:

- all records bind to an authenticated principal and destination space;
- a derived value can be traced to a source region and processing version;
- malicious files and document instructions cannot enter model or execution
  authority;
- health and finance unsafe actions fail closed; and
- no real personal data is used in tests.

### LO-1: Universal intake and source library

Status: **Complete in software on 2026-07-25.** The authenticated storage
boundary implements encrypted quarantine, deterministic local extraction,
injected local OCR, metadata, CSV table and barcode extraction, type and archive
checks, deduplication, versioning, correction, admission, rollback, export,
reclassification, and deletion. The renderer supplies file, camera, preview,
and private admission controls.

Deliver:

- authenticated drag-and-drop and file-picker intake;
- camera and multi-page scan capture;
- encrypted quarantine;
- media, size, archive, and malware checks;
- local OCR, layout, table, metadata, and barcode extraction;
- duplicate and prior-version detection;
- conversational import preview and correction;
- private-by-default admission;
- source library with provenance, versions, export, reclassify, and delete; and
- accessible progress and recovery for large or interrupted imports.

Gate:

- supported formats produce deterministic source and derived records;
- personal-content canaries remain in the correct namespace;
- files cannot escape quarantine through type confusion, archive traversal,
  parser failure, or document prompt injection;
- every admitted fact cites its source;
- interruption resumes or rolls back without partial memory admission; and
- deletion removes source and derived indexes according to recorded retention.

### LO-2: Connection Broker and conversational setup

Status: **Complete for the initial sandbox and local contract scope on
2026-07-25.** The catalog includes generic OAuth PKCE, SMART FHIR, financial
sandbox, selected local folder, and bounded MCP profiles. Opaque per-person
handles, cursors, receipts, deduplication, isolation, disconnect, revocation,
and accessible progressive setup are implemented. Production provider
certification remains later adapter work and is not implied by this gate.

Deliver:

- provider-connection catalog with plain-language scope manifests;
- OAuth Authorization Code with PKCE;
- SMART on FHIR authorization profile;
- per-person token handles and refresh;
- one-time export-import guides;
- bounded MCP connection registration;
- local folder one-time import;
- optional folder-watch grants;
- share-sheet and bound-channel intake contract;
- incremental sync cursors, receipts, health, disconnect, and delete;
- progressive conversational onboarding; and
- explicit Connections and Imports settings.

Initial adapters:

- one generic OAuth fixture;
- one SMART FHIR sandbox;
- one financial sandbox or standards-based test provider;
- local folder and manual export import.

Gate:

- the requested scope is minimal and read-only;
- no secret enters a prompt, skill, memory, log, or MCP-visible configuration;
- one person's token cannot sync into another person's space;
- revocation stops refresh and incremental sync;
- disconnect and delete semantics are understandable and tested;
- provider outage and expired consent recover without duplicate admission; and
- a person can complete setup by keyboard, screen reader, speech, or touch.

### LO-3: Private household operations

Status: **Complete in software on 2026-07-25.** Canonical household records,
exact-identifier reconciliation, deadline and exact-recall attention, cited
repair and procedure briefs, read-only Matter and energy record types,
private-by-default storage, explicit sharing, draft-only external work, and
physical-actuation denial are implemented and tested.

Deliver:

- household item, product, property, warranty, receipt, manual, service event,
  renewal, return window, recall, subscription, and procedure records;
- receipt, manual, invoice, label, and product-photo extraction;
- product and serial/model reconciliation;
- warranty, renewal, return, and maintenance attention rules;
- exact-product recall and security-notice matching;
- repair brief and household procedure experiences;
- optional Matter read-only inventory and energy records; and
- owner-confirmed sharing into a household space.

First-value journeys:

- photograph a product label and attach its receipt;
- upload a manual and ask how to perform a safe maintenance task;
- identify an upcoming return or warranty deadline;
- prepare a repair brief; and
- find the correct shutoff or recovery procedure.

Gate:

- one document or photo creates a useful inventory entry;
- product matching discloses uncertainty;
- private purchases do not enter a shared inventory automatically;
- a recall matches an exact owned product rather than popularity;
- external scheduling or purchases remain draft-first; and
- no physical actuation occurs.

### LO-4: Health timeline and visit preparation

Status: **Complete in software and sandbox scope on 2026-07-25.** Dedicated
health spaces, FHIR normalization, source reconciliation, deterministic urgent
guidance, user-selected descriptive trends, cited timelines and visit briefs,
selective emergency presentation, and diagnosis, treatment-change, emergency
dismissal, and cross-person denials are implemented. Live clinical-provider
certification remains outside this software gate.

Deliver:

- dedicated encrypted health space and retention controls;
- FHIR resource normalization;
- SMART patient authorization and sandbox sync;
- C-CDA, PDF, image, CSV, and wearable export intake;
- medication, condition, allergy, immunization, lab, observation, procedure,
  encounter, instruction, referral, and follow-up records;
- source reconciliation and contradiction review;
- user-selected trend rules;
- cited health timeline and "what changed" experience;
- visit brief and provider-message draft; and
- selective emergency-information presentation.

Gate:

- every clinical and self-reported claim preserves provenance;
- inferred conditions cannot become confirmed diagnoses;
- medication changes, diagnosis, and emergency dismissal are prohibited;
- health information cannot cross person or household spaces implicitly;
- urgent fixtures invoke deterministic safety guidance;
- a visit brief cites exact source records and includes uncertainty; and
- deleting or disconnecting a source has clear effects on retained history.

### LO-5: Personal and family financial attention

Status: **Complete in software and sandbox scope on 2026-07-25.** Dedicated
financial spaces, observed and inferred separation, statement reconciliation,
exception rules, local range forecasts, explicit household contributions,
cited weekly briefs, non-executable drafts, and consequential financial-action
denials are implemented. Live financial-provider certification remains outside
this software gate.

Deliver:

- dedicated financial space and account-sharing model;
- provider sandbox and CSV, OFX, QFX, statement, bill, receipt, tax form, and
  insurance-document intake;
- account, balance, transaction, merchant, obligation, recurring event, asset,
  liability, reimbursement, refund, subscription, and goal records;
- observed versus inferred category separation;
- recurring obligation, duplicate charge, price increase, missed refund, and
  subscription attention rules;
- local cash-flow forecasts with ranges and confidence;
- private and explicitly shared household views;
- cited weekly financial-attention brief; and
- dispute, reimbursement, and cancellation drafts.

Gate:

- initial connections and imports are read-only;
- no autonomous money movement, investment, credit, filing, or account closure
  exists;
- amounts reconcile to source statements within defined tolerances;
- inferred categories and forecasts are visibly distinguishable;
- one person's private account does not appear in household totals without
  explicit contribution rules;
- a weekly brief prioritizes exceptions instead of producing notification
  noise; and
- credentials, full account identifiers, and document canaries do not leak.

### LO-6: Cross-domain life operations

Status: **Complete in software on 2026-07-25.** Person-approved, purpose-bound,
field-minimized links, benefits and claim packets, care and continuity record
types, transition templates, credential and expiration records, removable
links, independent-source preservation, and explainable unified attention are
implemented.

Deliver:

- user-approved links between household, health, finance, calendar, task, and
  communication records;
- benefits and claims packet preparation;
- care-coordination commitments;
- life-transition plan templates;
- credential and expiration tracking;
- insurance-claim timelines;
- continuity and emergency-plan drafts; and
- a unified, privacy-scoped attention inbox.

Gate:

- cross-domain links are purpose-bound and explainable;
- joining two private domains never widens disclosure by inference;
- attention ranking reflects the person's goals, deadlines, risk, and burden;
- every recommended external action shows affected domains and recipients; and
- removing a cross-domain link does not destroy its independent sources.

### LO-7: Calibration and value pilot

Status: **Software and synthetic gate complete on 2026-07-25; human gate
pending.** The opt-in enforcement, metric contract, targets, synthetic
household baseline, deletion and boundary tests, accessible experience, safety
reviews, and operational runbooks are implemented. A real opt-in pilot and
explicit human package/provider support decisions cannot be replaced by CI and
remain required before Phase 11 can close.

Deliver:

- opt-in pilot using household operations first, then health and finance
  read-only cohorts;
- measure time to first value, setup completion, correction rate, extraction
  precision, useful-attention precision, brief usefulness, notification burden,
  privacy comprehension, deletion success, and time returned;
- accessibility, health-safety, financial-safety, privacy, security, and
  provider-governance review;
- support, recovery, parser-update, connector-revocation, and incident
  runbooks; and
- explicit human decisions for supported packages and providers.

Gate:

- a person reaches useful output from one source in a short guided session;
- no cross-person disclosure, unauthorized provider access, unsafe medical or
  financial action, or uncontained document instruction occurs;
- correction and deletion work across source and derived records;
- supported extraction and attention precision meet approved targets; and
- the pilot demonstrates meaningful time or attention returned.

## Cross-cutting security and privacy requirements

- All intake is authenticated and principal-bound before bytes are accepted.
- Quarantine has no retrieval, skill, MCP, tool, or execution authority.
- Original source bytes are immutable; corrections version derived records.
- Document text is untrusted data, never instruction authority.
- Provider scopes are allowlisted and recorded.
- OAuth state, PKCE, redirect URI, nonce, token audience, and issuer checks fail
  closed.
- Tokens remain opaque outside the credential broker.
- Browser exports use isolated profiles and stop before submissions.
- MCP servers cannot select a principal, destination space, retention, or
  action authority.
- Health and finance processing defaults to local inference.
- Remote disclosure is field-minimized, purpose-bound, visible, and optional.
- Household administrators cannot inspect another person's private imports,
  connection metadata, or processing results.
- Backups preserve source, derived record, credential, and namespace
  separation.
- Parser, OCR, classifier, and model versions are recorded for reproducibility
  and correction.

## Accessibility requirements

- Upload, scan, connect, preview, correct, and delete work without drag and
  drop.
- Camera capture has manual alternatives and clear image-quality feedback.
- OCR uncertainty is available nonvisually.
- Tables have navigable semantic alternatives.
- Progress never relies on animation or color.
- Long imports may be paused and resumed.
- Conversational questions are also represented as explicit form controls.
- Speech interaction never speaks full sensitive values by default.
- Every consent and disclosure preview is concise, expandable, and
  screen-reader navigable.

## Success measures

- time from first interaction to first useful result;
- percentage of sources admitted without correction;
- correction rate by field and parser;
- provider-connection completion and revocation success;
- duplicate and prior-version precision;
- attention-item acceptance and dismissal;
- brief usefulness;
- notification burden;
- time returned;
- percentage of processing performed locally;
- number and volume of optional remote disclosures;
- deletion and export completion;
- cross-person isolation failures;
- unsafe health or finance recommendations;
- credential, source, or personal-content leakage; and
- support burden per active domain package.

## Recommended delivery order

Begin with LO-0 through LO-2 as one shared foundation. Then implement LO-3
household operations because it gives broad, safe, visible value and supplies
the source, extraction, correction, and attention patterns required by health
and finance.

Proceed to LO-4 health with read-only records and visit preparation, then LO-5
finance with read-only attention and forecasting. Do not begin money movement,
medical treatment execution, or broad cross-domain automation during this
phase.
