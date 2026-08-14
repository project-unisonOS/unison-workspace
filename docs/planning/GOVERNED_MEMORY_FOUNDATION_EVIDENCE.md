# Governed memory foundation evidence

Status: accepted foundation evidence

Date: 2026-08-14

Evidence class: unit and focused service integration with synthetic data

## Revisions

| Repository | Revision | Review |
| --- | --- | --- |
| `unison-common` | `65e517a` | merged `project-unisonOS/unison-common#26` |
| `unison-context` | `878b37c` | merged `project-unisonOS/unison-context#26` |
| `unison-workspace` | pending | pending |

## Results

| Boundary | Result |
| --- | --- |
| Common governed-memory/context contract and schema tests | 12 passed locally |
| Context repository and API tests | 16 passed on `dev-nuc` |
| Health versus financial domain filtering | passed with synthetic records |
| Missing explicit space/domain/purpose | rejected by the retrieval contract |
| Remote model disclosure | denied by default in the context packet |
| Correction invalidation | active derived view invalidated with receipt |
| Membership revocation/key-version advance | space derived views invalidated with receipts |
| Existing governed-context API compatibility | focused API suite passed |
| Common hosted tests, contracts, lint, security, and package build | passed |
| Context hosted tests, image builds, Python security, and container supply chain | passed |

The context security gates initially identified fixed vulnerability
`CVE-2026-69247` in `cryptography 49.0.0`. The runtime pin was upgraded to
`50.0.0`; both filesystem and container scans then passed.

The broad legacy context suite reported 14 authentication failures because those
tests call protected routes without enabling the repository's established test
principal bypass. The focused governed API run used that explicit test-only
bypass and passed. This is not production authentication evidence; authenticated
cross-container principal propagation was established separately by DJ-1.

## Claims not established

- physical separation or hardware-backed custody of domain keys;
- production vector database behavior or embedding quality;
- automatic derived-view rebuild, dual-index migration, or restore;
- safe automatic activation of a usage-proposed taxonomy domain;
- use with real health, financial, legal, or household personal data.
