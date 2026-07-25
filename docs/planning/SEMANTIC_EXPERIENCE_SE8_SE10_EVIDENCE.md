# Semantic experience SE8 through SE10 acceptance evidence

Status: **Software and simulated qualification scope complete; hardware model qualification deferred**

Acceptance date: 2026-07-25

## Accepted scope

- SE8 defines bounded interpretation, extraction, vision, semantic construction,
  synthesis, and conversation tasks.
- Signed immutable per-version manifests carry artifact, provenance, runtime,
  task, modality, language, structured-output, hardware, privacy, license,
  quality, latency, risk, support, limitation, and rollback metadata.
- Installed and remote inventories record availability separately from
  eligibility. Artifact digests are checked for installed candidates.
- Forged signatures, immutable-version drift, tampered artifacts, unknown task
  claims, and incompatible candidates fail closed.
- SE9 evaluates privacy, disclosure, retention, risk, task, modality, language,
  context, structured output, offline state, hardware, latency, cost, license,
  artifact integrity, and support before ranking.
- Ranking is inspectable and person-aligned. Popularity, sponsorship, provider
  preference, engagement, and affiliate value are prohibited inputs.
- Each bounded operation receives its own route decision with rejected reasons,
  eligible candidates, rank inputs, exact version, minimized disclosure, and
  deterministic fallback.
- SE10 accepts only typed, provenance-bearing, explicitly untrusted model
  proposals. Deterministic source versions, facts, recipients, action IDs,
  confirmation/recovery requirements, and semantic equivalence remain platform
  authority.
- Exact facts are restored from deterministic sources. High and critical risk
  content uses deterministic language.

## Accepted component commits

| Repository | Commit | Scope |
| --- | --- | --- |
| unison-common | 1e593c8280045e2dcf80413b84b3b47c5e2119ae | Task, manifest, route-decision, and untrusted-proposal contracts |
| unison-inference | 0f5bab77313de8ea976898cc5bcbf931a3f13ec8 | Signed registry, eligibility, ranking, request integration, and semantic validation |

## Automated results

| Gate | Result |
| --- | --- |
| Model runtime contracts | Passed |
| Forgery, registry drift, and artifact integrity | Passed |
| Eligibility and per-operation routing | Passed |
| Offline, hardware, disclosure, cost, license, and support denials | Passed |
| Prohibited commercial ranking signals | Passed |
| Incomplete, hallucinated, stale, recipient-changing, and recovery-free proposals | Passed |
| All six approved task classes | Passed in synthetic qualification |
| Conversation, visual, and Braille semantic equivalence | Passed in simulation |

## Deferred qualification

- Manifest hardware requirements and measured results currently contain
  synthetic or developer-host evidence only.
- Appliance CPU, GPU, RAM, thermals, energy, contention, and latency validation
  remains in SE-HW-07.
- Representative vision hardware remains in SE-HW-04 and SE-HW-05.
- No model/version is promoted to supported status by this slice.
- Model canary, promotion, health monitoring, and rollback execution begin in
  SE11.

## Public claims

No GitHub Pages claim changes are authorized by this slice. Public messaging
can be revised after SE11 and SE12 connect model lifecycle evidence to supported
hardware and release compatibility.
