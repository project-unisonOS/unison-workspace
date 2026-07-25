# Model runtime v1 migration

Request-selected provider/model fields and unverified candidate lists remain
legacy compatibility inputs. New semantic operations use a bounded
`model-task-requirement`, a signature-verified registry, live hardware and
offline state, and a person-owned routing policy.

Availability discovery only updates inventory. It cannot register a model,
change manifest claims, relax eligibility, or nominate a route.

Model-assisted semantic work returns `model-semantic-proposal.v1`. The proposal
is always untrusted. The platform validates source versions, exact facts,
required meaning, uncertainty, recipients, deterministic action identifiers,
recovery, and provenance before accepting any contribution.

Existing provider adapters remain behind the governed route decision. Direct
provider/model selection can be removed after all callers supply task
requirements and the signed registry is loaded by appliance startup authority.
