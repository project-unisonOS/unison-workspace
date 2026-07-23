# UnisonOS appliance support contract

Status: Phase 9 scope lock, not a supported-release announcement

## Supported-release target

The first support candidate is a signed native installation bundle for Ubuntu
24.04 LTS on x86_64 UEFI hardware. WSL2, virtual-machine images, the evaluator
bare-metal ISO, and arm64 remain evaluation-only. Publication of this contract
does not promote an artifact; promotion requires every Phase 9 gate.

`unison-platform` owns installation, runtime, diagnostics, recovery, removal,
artifact assembly, and release publication. `unison-updates` owns signed
channel metadata, update selection, staging, verification, and update state.
`unison-workspace` pins both and owns the cross-repository gate and evidence.

## Product and lifecycle policy

The supported profile covers the bounded Phase 7 journeys and the Phase 8.1
slice where selected hardware supports them. Experimental adapters are never
silently included in the support claim.

- Stable releases are planned monthly, with emergency security releases.
- Current stable and immediately previous stable receive update support.
- Application restarts use an owner-configurable maintenance window and are not
  unattended by default.
- Ubuntu security updates may download unattended; activation follows the
  owner's restart policy and update health gate.
- Product telemetry is off by default. Remote reliability reporting is
  explicit opt-in, privacy-minimized, inspectable, and revocable.

## Severity and response targets

| Severity | Meaning | Initial response | Release expectation |
| --- | --- | --- | --- |
| Critical | Active compromise, update-trust failure, cross-person disclosure, or unrecoverable data-loss risk | 24 hours | Withdraw/revoke and safely issue an emergency fix |
| High | Exploitable boundary failure or widespread install/update/integrity failure | 2 business days | Emergency or next stable release |
| Medium | Material supported-journey failure with a safe workaround | 5 business days | Next stable release |
| Low | Cosmetic, documentation, or limited-impact defect | 10 business days | Maintenance backlog |

These are engineering response targets, not a paid availability SLA.

## Hardware support tiers

- **Reference:** a named system on which the complete release gate is repeated.
- **Compatible:** meets the enforced profile and passes the compatibility suite.
- **Community-tested:** useful evidence without the maintained support gate.
- **Unsupported:** known incompatible or outside the declared target.

The matrix and installer probe become authoritative in Phase 9.4. Until then no
physical system is represented as supported.
