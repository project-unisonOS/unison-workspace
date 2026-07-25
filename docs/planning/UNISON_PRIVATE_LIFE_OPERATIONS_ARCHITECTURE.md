<!-- markdownlint-configure-file {"MD024": {"siblings_only": true}} -->

# Unison private life operations capability architecture

Status: proposed product and technical architecture

Date: 2026-07-25

## Product position

Unison should become a private life operations system, not merely an assistant
that drafts messages and books appointments.

Most agent products focus on tasks that are easy to demonstrate. Unison can
differentiate by maintaining long-running, sensitive, cross-domain
understanding of a person or household while keeping every action governed,
attributable, recoverable, and private.

## Coherent capability model

Every capability follows the same technical flow:

```text
Signals and records
        |
        v
Domain adapters and normalized records
        |
        v
Private event and relationship graph
        |
        v
Local interpretation and planning
        |
        v
Policy, identity, consent, and disclosure gate
        |
        v
Execution router
        |
        v
Provider tool, MCP server, browser, or local operation
        |
        v
Verification, receipt, recovery, and memory update
```

This prevents each feature from becoming an application with different
security, data, and interaction rules.

## Implementation mechanisms

| Mechanism | Best use | Authority |
| --- | --- | --- |
| Native local operation | Local files, models, reminders, calculations, and records | Exact typed operation |
| Direct provider tool or API | Stable transactional APIs such as calendar, banking, or health records | Provider-specific typed operation |
| MCP | Standardized discovery of resources and tools from trusted providers | Always mediated by Unison policy |
| Governed skill | Versioned procedure for accomplishing a goal | Planning knowledge only, never authority |
| Browser or computer use | Sites without suitable APIs | Sandboxed fallback with visual verification |
| Local model | Sensitive interpretation, classification, extraction, and planning | No independent execution authority |
| Remote model | Optional complex reasoning when approved | Explicit disclosure and minimized context |
| Human handoff | Medical, legal, financial, physical, or ambiguous decisions | The person or qualified professional decides |

MCP is a transport and capability-description mechanism, not a trust boundary.
Every MCP tool is converted into a canonical Unison action and passes
principal, context, disclosure, confirmation, budget, audit, and recovery
checks.

A skill describes how to complete something. It never contains credentials or
silently gains authority to execute its procedure.

Computer use is the lowest-preference execution mechanism because it is brittle
and difficult to verify. When required, Unison:

1. runs it in a constrained browser profile;
2. shares only the minimum required information;
3. identifies the expected result before acting;
4. stops at payment, submission, signature, consent, or irreversible
   boundaries;
5. captures a redacted before-and-after receipt; and
6. verifies the result from a second signal such as a confirmation message or
   provider API.

## Capability domains

### Personal health steward

This is a longitudinal organizer, not an autonomous diagnostician.

Useful experiences include:

- build a private health timeline from clinical records, lab results,
  medications, immunizations, wearable data, symptoms, and personal notes;
- prepare visit briefs covering changes, unresolved questions, medication
  effects, and records to bring;
- reconcile medication lists across providers and identify conflicts for human
  review;
- track treatment instructions, referrals, follow-ups, screenings, and
  preventive-care schedules;
- detect meaningful changes in user-selected sleep, mobility, resting heart
  rate, weight, pain, and other indicators;
- explain lab trends in plain language while distinguishing education from
  medical advice;
- prepare insurance appeals and organize supporting records;
- maintain selectively disclosed emergency information; and
- coordinate care without exposing one family member's private health details
  to another.

FHIR is the canonical clinical interchange model and SMART authorization is
preferred where providers support it. SMART defines an OAuth-based pattern for
patient-authorized access to FHIR systems:
[HL7 SMART App Launch](https://hl7.org/fhir/smart-app-launch/1.0.0/).

Raw clinical records live in a dedicated encrypted health space. Derived events
identify provenance as clinical record, device measurement, self-report,
caregiver report, or model inference. An inferred condition never becomes an
established fact without confirmation. Provider messages, appointment changes,
record disclosure, and medication-related actions require explicit approval.
Urgent patterns use predefined safety rules rather than open-ended model
judgment.

A differentiated experience is: "What changed since my last appointment?"
Unison reconciles the person's lived experience with fragmented provider
records and cites every input.

### Personal and family financial operations

The opportunity is reducing the administrative burden and uncertainty
surrounding household money, not merely categorizing past transactions.

Useful experiences include:

- maintain a private cash-flow forecast;
- track bills, annual expenses, renewals, subscriptions, taxes, tuition,
  insurance, and household commitments;
- reconcile transactions with receipts, warranties, reimbursements, and shared
  obligations;
- detect duplicate charges, price increases, missed refunds, expiring
  promotional rates, and unused subscriptions;
- prepare a concise weekly financial-attention brief;
- model moving, job, caregiving, school, and equipment decisions;
- maintain separate personal, shared household, child, business, and
  caregiving financial spaces;
- track family loans without granting household-wide financial visibility;
- assemble tax-document packages and identify missing forms;
- prepare disputes, chargebacks, insurance, reimbursement, and benefits claims;
  and
- track goals using ranges and uncertainty instead of false precision.

Provider APIs or established financial-data intermediaries are preferred over
credential sharing and screen scraping. Accounts, balances, transactions,
obligations, recurring events, assets, and documents normalize into a local
ledger. Observed facts remain separate from inferred categories and forecasts.
Categorization and forecasting run locally by default.

The initial posture is read-only. Transfers, payments, investment changes, and
account closure begin as drafts. New payees, money movement, credit
applications, tax filing, and investment transactions require step-up
confirmation and independent provider verification.

Financial-data access must not depend on one regulation or provider. The US
regulatory timetable remains changeable:
[CFPB personal financial data rights](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/personal-financial-data-rights/).

### Benefits and entitlement navigator

Unison can:

- track employer, government, health, education, disability, veteran,
  caregiver, utility, and local-assistance eligibility;
- maintain renewal dates, evidence requirements, and relevant life changes;
- prepare application packets without submitting them automatically;
- compare explanations of benefits with provider bills;
- track claims, denials, appeals, deadlines, and correspondence;
- identify approved reimbursements or credits that were not received; and
- explain which facts caused an eligibility recommendation.

This combines governed jurisdiction-specific skills, official data sources,
document extraction, browser fallback, and human confirmation. Legal
conclusions are informational and clearly labeled.

### Household administrative memory

Useful experiences include:

- inventory appliances, devices, vehicles, warranties, serial numbers, service
  records, manuals, and replacement parts;
- associate purchases with receipts, payment methods, return windows, and
  protection plans;
- track maintenance intervals and predict upcoming work;
- prepare a repair brief before contacting a provider;
- detect recalls and security notices matching exact owned products;
- keep household procedures such as water shutoff, breaker mapping, network
  recovery, pet care, emergency contacts, and evacuation needs;
- manage moving, renovation, rental, or home-sale projects; and
- track utility use, tariff changes, leaks, abnormal consumption, and
  efficiency opportunities.

Matter is a useful local interoperability layer for compatible home devices,
including energy and water management. Unison retains a provider-independent
device model above it:
[Matter energy-management capabilities](https://csa-iot.org/newsroom/matter-1-3-specification-released/).

### Care coordination

Useful experiences include:

- coordinate meals, transportation, medications, appointments, visits, and
  household help;
- reveal only the task information each caregiver needs;
- track commitments and completion;
- detect caregiver overload and uncovered responsibilities;
- maintain contingency plans when a primary caregiver is unavailable;
- generate privacy-minimized shift-change briefs; and
- support aging parents, children, disability care, post-operative recovery,
  and pets through the same task architecture with different policies.

This builds directly on Unison's principal and context-space model. Family
membership never implies universal access.

### Personal records and credential wallet

Unison indexes:

- identity documents;
- licenses and certifications;
- education and employment records;
- insurance policies;
- property documents;
- medical directives;
- powers of attorney;
- memberships;
- pet records;
- travel documents; and
- selectively shareable proofs.

It tracks issuance, expiration, renewal, revocation, and disclosure. W3C
Verifiable Credentials are an interoperable representation for issuer-signed
claims, but Unison still applies its own issuer-trust policy:
[W3C Verifiable Credentials Data Model 2.0](https://www.w3.org/TR/vc-data-model/).

### Insurance and claims advocate

Unison can:

- maintain policy summaries and renewal comparisons;
- document property condition before a loss;
- assemble incident timelines;
- connect estimates, invoices, photos, correspondence, and payments;
- compare provider bills, insurer explanations, and benefits;
- track deadlines and unanswered correspondence;
- draft appeals and complaints; and
- calculate unresolved amounts without claiming a legal conclusion.

### Personal security and identity defense

Unison can:

- track accounts, recovery methods, passkeys, trusted devices, and breach
  exposure;
- detect risky recovery dependencies;
- identify reused contact information and abandoned accounts;
- prepare recovery before a device is lost;
- track data-broker removal and opt-out requests;
- monitor suspicious mail, login alerts, credit changes, and impersonation
  signals;
- coordinate fraud recovery without exposing every credential to one service;
  and
- maintain continuity procedures for a person's temporary unavailability.

Unison integrates with credential managers without becoming a plaintext
password database.

### Life transition coordinator

Major transitions are multi-month, multi-domain projects:

- moving;
- changing jobs;
- having or adopting a child;
- starting school;
- retirement;
- separation or divorce;
- disability;
- caregiving;
- bereavement;
- immigration;
- deployment; and
- disaster recovery.

Unison builds dependency-aware plans spanning documents, benefits, finances,
appointments, household responsibilities, communications, and deadlines.
Every affected person retains independent privacy and approval.

### Digital estate and continuity

Unison can:

- inventory important accounts and digital assets;
- record transfer, memorialization, archival, and deletion preferences;
- prepare emergency-access packages without releasing them prematurely;
- track executors, delegates, conditions, and expiring documents;
- produce continuity briefs during hospitalization or unavailability; and
- verify that instructions remain current.

This requires conditional disclosure, multiple-party approval, tamper-evident
records, and designs that cannot trigger from one missed interaction.

### Learning and personal development

Unison can:

- maintain a durable skills graph based on goals and demonstrated work;
- detect knowledge decay and schedule refreshers;
- turn real projects into learning plans;
- preserve citations and distinguish learned facts from generated
  explanations;
- track certifications and continuing education;
- build private portfolios and evidence of competence; and
- help family members teach one another without combining private profiles.

### Relationship and community stewardship

Unison can:

- remember commitments, important dates, preferences, and unresolved
  follow-ups;
- suggest reconnecting according to the person's goals rather than engagement
  optimization;
- track mutual aid, volunteering, donations, and community responsibilities;
- prepare context before reconnecting after a long absence; and
- avoid manipulative relationship scoring.

Intimate inferences never enter shared spaces without explicit confirmation.

## Standard domain package

Every domain is implemented with the same internal boundaries:

```text
Domain package
|-- canonical records
|-- provider adapters
|-- MCP mappings
|-- governed skills
|-- policy and disclosure rules
|-- recommendation rules
|-- typed actions
|-- verification rules
|-- recovery procedures
|-- accessible experiences
`-- tests and fixtures
```

Example health operations:

```text
Resources:
  health.timeline.read
  health.medication-list.read
  health.record-source.read

Recommendations:
  health.follow-up.recommend
  health.record-conflict.recommend

Draft actions:
  health.visit-brief.prepare
  health.provider-message.draft

Confirmed actions:
  health.provider-message.send
  health.appointment.reschedule

Prohibited autonomous actions:
  health.medication.change
  health.diagnosis.assert
  health.emergency.dismiss
```

Finance, household, care, records, and every later package use the same shape.

## Shared action-risk model

1. **Observe:** read and organize private information.
2. **Interpret:** produce local summaries, forecasts, anomaly explanations, or
   recommendations.
3. **Prepare:** draft a form, message, plan, claim, payment, or provider
   operation.
4. **Confirm and execute:** perform an exact action after the correct person
   reviews its material effects.
5. **Bounded maintain:** repeat a narrow reversible action under a revocable
   grant.

Medical treatment changes, legal signatures, financial transfers, identity
issuance, physical-access changes, and destructive record operations never
enter the fifth class.

## Prioritized verticals

### Private household operations

Inventory, warranties, renewals, maintenance, recalls, receipts, return
windows, subscriptions, and critical household procedures provide broad value
with relatively low action risk.

### Health timeline and visit preparation

Import records and wearable summaries, reconcile sources, track follow-ups, and
generate a cited visit brief. Do not diagnose or execute treatment changes.

### Family financial attention brief

Provide read-only account and document intake, recurring-obligation detection,
cash-flow forecasting, missed-refund and price-increase detection, and a concise
weekly exception report. Do not move money autonomously.

Together these demonstrate the differentiator: Unison understands the ongoing
operation of your life, quietly finds what deserves attention, and helps
resolve it without monetizing or broadly exposing the underlying data.
