# Phase 7 acceptance evidence

Status: **In review**
Evidence date: 2026-07-23
Phase 8: **Not started**

## Bounded product claim

Phase 7 implements seven governed workflow families: calendar coordination;
email triage, summary, and draft; reminder and commitment review; household
coordination; relationship-aware contact recall; document/web research; and
travel planning. It does not claim generalized autonomy, automatic sending,
booking, purchasing, or financial execution.

## Implementation inventory

| Repository | Candidate |
| --- | --- |
| `unison-common` | `88bf3aefcd7bdf12496d99d50c41d04e9fdd09fd`, merged PRs #11/#12: workflow plans, approvals, failure/recovery, outcome evidence, metrics, record/replay, and byte-identical canonical/packaged schema |
| `unison-orchestrator` | `16d5b491b2cb57df167c5d75f92863c5ca679bb0`, merged PR #25: seven-workflow engine, fake providers, exact approval, minimization, idempotency, cancellation, compensation, retry, and provider replacement |
| `unison-experience-renderer` | `bcff72d9241a96272a97fd4969e603ec08c3bdec`, merged PR #9: semantic plan, approval, execution, outcome, cancellation, error, retry, and replacement controls |
| `unison-docs` | `80fd683d21bcf3503b11c2e891212b74222b682a`, merged PR #2: exact supported-workflow and synthetic record/replay documentation |
| Public site | `7315ceeecd18077a0e16c9407ce4fe2b8a3eef61`, merged PR #11: public workflow boundary, recovery, evidence, and limitation guidance |
| `unison-workspace` | This review candidate: decisions AD-035 through AD-040, threat reassessment, fixtures, aggregate gate, CI integration, and closeout evidence |

## Acceptance matrix

| Requirement | Evidence |
| --- | --- |
| Scheduling/calendar coordination | Fake calendar proposal/create journey with exact recipient approval |
| Email triage, summary, draft | Tainted synthetic email, minimization, wrong-recipient denial, draft-first action |
| Reminders/tasks/follow-up/commitments | Commitment-bound task journey and completion metrics |
| Household coordination | Explicit shared-space journey with private-space regression |
| Relationship-aware contact recall | Local contact provider and authorized-context check |
| Document/web research | Tainted instructions remain data; approved excerpt/query only |
| Travel planning | Minimized constraints, timeout retry, and provider replacement |
| Inspectable/cancellable/recoverable | Plan, exact approval, idempotency, retry, cancellation, compensation, receipts |
| Person-aligned outcomes | Local time-return, task, commitment, interruption, recovery, call, disclosure, incident metrics |
| No engagement/provider bias | Prohibited ranking-signal matrix fails closed |
| Accessible completion | Semantic primary, approval, error, cancel, retry, replacement, and outcome paths plus browser axe |

## Executed local evidence

- Full component regressions: `unison-common` 296 passed/1 skipped;
  `unison-orchestrator` 225 passed/2 skipped; renderer 40 passed.
- Aggregate Phase 7 proof: 28 passed. Seven journeys completed, 81 estimated
  minutes returned, seven administrative tasks and commitments completed,
  seven interruptions avoided, one safe recovery, zero duplicate actions,
  zero engagement signals, and zero boundary incidents.
- Disclosure audit: seven external calls disclosed 15 allowlisted fields;
  adversarial instruction/sponsorship fields were absent from provider payloads.
- Renderer Chromium/Playwright/axe: zero WCAG A/AA violations, 51 semantic
  controls, keyboard focus, reduced-motion, and forced-color behavior passed.
- Public site strict clean build passed.
- All candidate worktrees pass `git diff --check`.

## Hosted and publication evidence

- Component PRs #11, #25, #9, #2, and public-site PR #11 are merged.
- Common tests/contracts/lint/security/package jobs passed in run
  `30023654019`; orchestrator tests/security/container jobs passed in run
  `30023932896`; renderer and public-site build/accessibility checks passed.
- Workspace hosted CI/security, post-merge site deployment, recursive
  fresh-clone validation, and the exact final workspace commit remain the
  named closeout checks before the status changes from In review to Complete.

## Residual limits

- Mandatory acceptance uses deterministic synthetic fake providers with no
  personal data or credentials. No production provider is enabled or claimed;
  any future live adapter requires synthetic-account acceptance against the
  same exact-action, minimization, idempotency, cancellation, and recovery
  contract.
- External communication remains draft/proposal first.
- No automatic booking, purchasing, payments, or high-impact actuation.
- Time returned is an estimate unless the person chooses to confirm it locally.
- Website/document summaries are not a substitute for professional advice.
- Provider denial and stale upstream information remain possible and visible.
