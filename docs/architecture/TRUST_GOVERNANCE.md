# Trust governance boundary

Status: Phase 3 review candidate

The Personal Data and Trust Store owns the versioned Trust API. Policy rules,
consent grants, disclosure decisions, minimization, delegated authority,
confirmation, owner-readable audit, and task credential brokerage converge at
this boundary. Legacy consent JWTs remain compatibility evidence, not authority.

Every decision binds a verified principal and assistant to an explicit purpose,
audience, context space, assurance level, data classes, action, channel, and
recipients. Missing or unknown values deny. Outcomes are allow, deny, redact,
minimize, ask, or step-up. High-risk and external actions remain drafts until an
exact, short-lived confirmation is consumed once. Sensitive action without
strong assurance steps up before confirmation.

The inference broker prefers local execution. A remote call requires a positive
disclosure decision and receives only named fields; credentials and undeclared
attachments are removed. Email, websites, documents, tool results, and model
outputs are content with provenance and taint, never sources of authority.

The Capability Host accepts only `unison.capability-governance.v1` manifests by
default. Actions, data reads/writes, recipient classes, execution location,
risk, reversibility, cost, confirmation, accessibility, audit, retention,
egress, files, devices, timeout, resources, signature, and revocation identity
are mandatory. Runtime authority is grant-bound, expiring, and nonce protected.
Broad filesystem or network grants are invalid. A test-only compatibility flag
exists for historical fixture coverage and is off by default.

Secrets are encrypted locally and represented outside the broker by opaque
identifiers. The broker checks principal and capability at injection time and
hands plaintext directly to the transport consumer; planners, models, decision
records, and audit views never receive it.
