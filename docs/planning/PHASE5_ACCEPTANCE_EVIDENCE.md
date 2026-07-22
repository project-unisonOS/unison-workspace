# Phase 5 acceptance evidence

Status: Complete

Prepared: 2026-07-21

Gate owner: human architecture/security review

Gate decision: Approved 2026-07-21

## Bounded acceptance claim

The review candidate lets two independent synthetic adults reach their own assistant through Telegram Bot API private-chat long polling without exposing an inbound appliance listener. Telegram remains an explicitly disclosed, low-assurance third-party relay. The proof does not authorize sensitive, recovery, ambiguous, or consequential actions remotely, and it uses no real Telegram credential.

## Approved provider decision

The human owner approved Telegram Bot API long polling as the first reference provider under private-chat-only, per-person credential, low-assurance, disclosure, and local step-up constraints. The review used Telegram's official Bot API, bot-platform, and privacy documentation. Telegram processes bot content and metadata; bot traffic is not end-to-end encrypted to the node; bots cannot initiate a chat; and pending Bot API updates may remain for up to 24 hours.

The provider review and enable/revoke/recover runbook are in `unison-comms/docs/telegram-channel.md`. The authoritative data-flow and storage boundary are in `docs/architecture/CHANNEL_GATEWAY.md`.

## Implemented evidence

- Common contracts define normalized envelopes, capability/assurance profiles, provider privacy, pairing/binding, nonce, delivery, step-up, and accessible semantic outcomes.
- Auth migration v2 owns high-assurance one-use pairing, hashed external subjects, assistant binding, non-oracular lookup, reassignment defense, and account/binding revocation.
- Comms preserves the Gmail adapter and its per-person encrypted/reset behavior while adding encrypted per-person Telegram credentials, an outbound-only long-poll adapter, cursor/idempotency/replay/rate controls, content-free audit, degraded reconnect, and draft-first delivery.
- Auth/comms internal binding uses short-lived workload tokens restricted to audience `auth` and scope `channel:bind`; person tokens do not authorize the worker.
- Orchestration accepts only person-bound low-assurance envelopes, never grants external action authority, and converts sensitive/recovery requests into trusted-local-device step-up.
- The semantic renderer provides labelled disclosure, credential, pairing, connection, revocation, cancellation, denial, and recovery controls with live status and password-field cleanup.
- Platform Compose keeps comms and the worker on the private network with no host port. One worker discovers multiple isolated provider accounts and needs outbound HTTPS only.

## Local conformance and regression evidence

`scripts/test-phase5.sh` passes 31 focused contract, pairing, real auth/gateway composition, two-person isolation, stolen-subject, replay, duplicate, delayed, non-private, rate-limit, outage/reconnect, draft/confirmation, revocation, orchestration, accessibility, documentation, gitlink, and topology checks. The gate also runs the credential-free resolved-Compose exposure scan.

Focused component results:

| Component | Result |
| --- | --- |
| `unison-common` full suite | 285 passed, 1 skipped |
| `unison-auth` full suite | 38 passed |
| `unison-comms` full suite with explicit test bypass | 28 passed |
| Orchestrator Phase 5 ingress | 3 passed |
| Renderer full suite | 33 passed |
| Integrated Phase 5 gate | 31 passed |

No fake-provider test contains `api.telegram.org` or a real credential. Stored SQLite token values are asserted not to contain plaintext token material, and a second person cannot create or confirm a draft through the first person's provider account.

## Network and exposure evidence

The reference adapter uses only HTTPS POST to Telegram `getUpdates` and `sendMessage`. The worker process has no FastAPI/ASGI listener. Compose gives comms an internal `expose: 8080` entry for the authenticated renderer but no host `ports` entry; the worker has neither. `scripts/scan-phase5-network.py` parses the fully resolved Compose model and reports zero published host ports for both services, internal exposure only for comms, and no worker listener. The scan passes from the isolated recursive clone at `c2ef7935c5f5e3f816158517284eeeece19f929b`.

## Published review candidates

- Common contracts: [unison-common#6](https://github.com/project-unisonOS/unison-common/pull/6)
- Pairing authority: [unison-auth#11](https://github.com/project-unisonOS/unison-auth/pull/11)
- Telegram gateway: [unison-comms#2](https://github.com/project-unisonOS/unison-comms/pull/2)
- Runtime dependency compatibility: [unison-capabilities#3](https://github.com/project-unisonOS/unison-capabilities/pull/3)
- Channel ingress policy: [unison-orchestrator#20](https://github.com/project-unisonOS/unison-orchestrator/pull/20)
- Accessible remote-assistant flow: [unison-experience-renderer#6](https://github.com/project-unisonOS/unison-experience-renderer/pull/6)
- Private channel topology: [unison-platform#8](https://github.com/project-unisonOS/unison-platform/pull/8)
- Pinned integration and evidence: [unison-workspace#6](https://github.com/project-unisonOS/unison-workspace/pull/6)
- Public plan/status update: [project-unisonos.github.io#6](https://github.com/project-unisonOS/project-unisonos.github.io/pull/6)

All candidates remain draft and unmerged pending the human gate.

## Immutable review-candidate commits

| Repository | Commit |
| --- | --- |
| `unison-common` | `eef1a7353b2c795233daf0db6079b867ff2d98ba` |
| `unison-auth` | `0e2cadb1ae9945a57cf538ebf46beeb0fd576d42` |
| `unison-comms` | `34f60636bb5453b3e9fe44191c34fffaa176c778` |
| `unison-capabilities` | `e472a305e4c81b57a890ca7a332f7a69d05b87ec` |
| `unison-orchestrator` | `9835162665b3ab6d17a445416569b8acfe982c8b` |
| `unison-experience-renderer` | `967062b0d86541b1840071d1e41d02ac10a68b77` |
| `unison-platform` | `3f855843796a2159726d5ae07acdf0f65490a74a` |
| `unison-workspace` validated implementation/evidence head | `7eb3f1c24f68d4d02e86f85f8fc7d83b0a1c2013` |
| `project-unisonos.github.io` | `7717b5adf980b3953c4d27b03ce3194b71ec3538` |

The workspace gitlinks pin every Phase 5 component commit. The capability compatibility commit removes a top-level module name that shadowed Python's standard-library `secrets` module under the security-fixed Starlette runtime; it changes no authorization behavior.

## Hosted Actions and accessibility evidence

- Common contracts: [run 29881633391](https://github.com/project-unisonOS/unison-common/actions/runs/29881633391) passed Python 3.12/3.13 tests, contracts, lint, security, and package build.
- Communications: [run 29883163014](https://github.com/project-unisonOS/unison-comms/actions/runs/29883163014) passed 28 tests, Bandit, strict Trivy filesystem and image scans, container build, and SBOM generation.
- Capability compatibility: [run 29883646742](https://github.com/project-unisonOS/unison-capabilities/actions/runs/29883646742) passed its repository security, lint, and test gate.
- Orchestrator: [run 29881720677](https://github.com/project-unisonOS/unison-orchestrator/actions/runs/29881720677) and its companion test/build runs passed.
- Renderer: [run 29882496916](https://github.com/project-unisonOS/unison-experience-renderer/actions/runs/29882496916) passed the full 33-test suite.
- Public site: [run 29882409330](https://github.com/project-unisonOS/project-unisonos.github.io/actions/runs/29882409330) passed strict MkDocs build and browser accessibility. The audit covered 44 substantive pages and 1,937 internal links, including the remote-assistant page, with zero WCAG A/AA violations.
- Workspace: [run 29884040060](https://github.com/project-unisonOS/unison-workspace/actions/runs/29884040060) passed deterministic bootstrap, Phase 0, the full component regression, Phases 1–5, PowerShell parsing, security tests, Bandit, Semgrep, Trivy filesystem scanning, and SBOM generation.

`unison-auth` and `unison-platform` do not own repository-level required Actions on these candidates. Their full local suites and behavior are exercised through the pinned isolated workspace gate; this absence is visible rather than represented as a hosted pass.

## Recursive fresh-clone evidence

An isolated `/tmp` checkout recursively cloned all 21 submodules and bootstrapped a new Python 3.12 environment from `requirements-dev.lock`. At workspace commit `1b07a3a0642ea6280bf6ba5d2737e4d29446dc0a`, Phase 0 validation and all prior gates passed: Phase 1 (43), Phase 2 (29 plus 1 authority test), Phase 3 (34), Phase 4 (52 plus the two-assistant proof), and Phase 5 (31). The complete component regression then passed: common 285/1 skipped, auth 38, consent 14, context 31, storage 3, policy 77, comms 28, renderer 33, capability 24, inference 9, payments 3, and orchestrator 212.

The same isolated checkout was fast-forwarded to `c2ef7935c5f5e3f816158517284eeeece19f929b`; submodule status was clean, the 31-check Phase 5 gate passed again, and the new resolved network exposure scan reported no published appliance host port.

## Residual risks and limitations

- Telegram remains able to process message content and metadata; UnisonOS cannot provide provider blindness or E2EE to the node through Bot API traffic.
- Timing and message-size metadata are not padded. This is disclosed residual risk T-17.
- Telegram availability and policy changes are outside appliance control. Safe degraded behavior is implemented, not provider independence.
- The fake-provider proof avoids real personal data and does not claim production load, provider SLA, Telegram policy certification, or a supported release.
- Host-root compromise, hardware-backed key sealing, provider-blind backup, and replacement-device restore remain outside Phase 5. Phase 6 is not started.
- SMS, WhatsApp, voice calls, Telegram groups, media/attachments, and additional adapters are not authorized by this gate.

## Final gate decision

The final Phase 5 gate was approved on 2026-07-21 after the named candidates were pinned and the component, workspace, and site Actions; isolated recursive fresh-clone regression; browser accessibility; and network exposure evidence passed. Phase 5 is **Complete**. Phase 6 remains **Not started** and requires separate authorization.
