# Phase 5 acceptance evidence

Status: In review

Prepared: 2026-07-21

Gate owner: human architecture/security review

Gate decision: Pending

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

`scripts/test-phase5.sh` passes 30 focused contract, pairing, two-person isolation, stolen-subject, replay, duplicate, delayed, non-private, rate-limit, outage/reconnect, draft/confirmation, revocation, orchestration, accessibility, documentation, gitlink, and topology checks. `docker compose config --quiet` resolves the credential-free platform profile.

Focused component results:

| Component | Result |
| --- | --- |
| `unison-common` full suite | 285 passed, 1 skipped |
| `unison-auth` full suite | 38 passed |
| `unison-comms` full suite with explicit test bypass | 28 passed |
| Orchestrator Phase 5 ingress | 3 passed |
| Renderer full suite | 33 passed |
| Integrated Phase 5 gate | 30 passed |

No fake-provider test contains `api.telegram.org` or a real credential. Stored SQLite token values are asserted not to contain plaintext token material, and a second person cannot create or confirm a draft through the first person's provider account.

## Network and exposure evidence

The reference adapter uses only HTTPS POST to Telegram `getUpdates` and `sendMessage`. The worker process has no FastAPI/ASGI listener. Compose gives comms an internal `expose: 8080` entry for the authenticated renderer but no host `ports` entry; the worker has neither. Static topology assertions and resolved Compose configuration pass. A fresh-clone host-port scan is part of the final publication evidence.

## Published review candidates

- Common contracts: [unison-common#6](https://github.com/project-unisonOS/unison-common/pull/6)
- Pairing authority: [unison-auth#11](https://github.com/project-unisonOS/unison-auth/pull/11)
- Telegram gateway: [unison-comms#2](https://github.com/project-unisonOS/unison-comms/pull/2)
- Channel ingress policy: [unison-orchestrator#20](https://github.com/project-unisonOS/unison-orchestrator/pull/20)
- Accessible remote-assistant flow: [unison-experience-renderer#6](https://github.com/project-unisonOS/unison-experience-renderer/pull/6)
- Private channel topology: [unison-platform#8](https://github.com/project-unisonOS/unison-platform/pull/8)

Workspace and public-site candidates, hosted Actions links, immutable commit list, browser accessibility, and recursive fresh-clone results will be added before the final gate is presented.

## Residual risks and limitations

- Telegram remains able to process message content and metadata; UnisonOS cannot provide provider blindness or E2EE to the node through Bot API traffic.
- Timing and message-size metadata are not padded. This is disclosed residual risk T-17.
- Telegram availability and policy changes are outside appliance control. Safe degraded behavior is implemented, not provider independence.
- The fake-provider proof avoids real personal data and does not claim production load, provider SLA, Telegram policy certification, or a supported release.
- Host-root compromise, hardware-backed key sealing, provider-blind backup, and replacement-device restore remain outside Phase 5. Phase 6 is not started.
- SMS, WhatsApp, voice calls, Telegram groups, media/attachments, and additional adapters are not authorized by this gate.

## Gate recommendation

Approve Phase 5 only after the named candidates are pinned in the workspace, component/workspace/site Actions pass, recursive fresh-clone validation passes, and browser accessibility/network exposure evidence is recorded. Approval would mark Phase 5 **Complete** and keep Phase 6 **Not started**.
