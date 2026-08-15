# Agent-first contributor model

Status: accepted operating guidance  
Audience: human contributors and coding agents acting on their behalf

## Purpose

Most Unison contributors are expected to work through Codex, Claude, or another
coding agent. Project structure must therefore be machine-navigable without
becoming opaque to people. The same concise Markdown, versioned contracts,
commands, and evidence should serve both audiences.

## Development topology

| Plane | Role | Current policy |
| --- | --- | --- |
| Windows and Codex | Human/agent control plane, review, planning, lightweight edits | Not the canonical Linux runtime or secrets authority |
| Ubuntu `dev-nuc` | Stable Linux build, component integration, clean-worktree validation | Available now through local network and Tailscale SSH |
| Interim GPU workstation | Persistent inference deployment, concurrency, energy, thermal, and recovery qualification | Deferred until the machine is installed and inventoried |
| GitHub | Canonical source, review, hosted CI, security scanning, durable coordination | Hosted results never imply physical or participatory evidence |

The workspace is the developer front door and release/integration manifest.
Component repositories own runtime code and canonical contracts. The NUC must
remain usable without the GPU host, and the GPU host must not become the only
machine capable of building Unison.

## Repository direction

Retain component repositories where they express real security, ownership, or
release boundaries. Reduce contributor discovery cost through the workspace,
shared workflows, and explicit maps rather than immediately collapsing code.

Planned first-class repositories:

- `unison-infrastructure`: named environment profiles, Compose and deployment
  definitions, provisioning, observability, lab inventory, and reproducible
  validation;
- `unison-hardware`: system requirements, stable interfaces, BOM schema,
  candidate components, power/thermal budgets, schematics, PCB/mechanical
  sources, enclosure work, and qualification plans;
- organization `.github`: shared contribution policy, templates, labels,
  ownership, reusable CI, RFCs, and security reporting.

Do not split early hardware concepts into many repositories. Split a design
only after it has an independent owner, lifecycle, release artifact, or safety
review boundary.

## Machine-readable contribution packet

Every non-trivial task should make these fields discoverable in Markdown or a
small adjacent YAML/JSON file:

- objective and explicit non-goals;
- authoritative documents and contract versions;
- repositories and immutable starting commits;
- allowed systems and authority limits;
- environment profile and exact entrypoint;
- ordered implementation checkpoints;
- required tests and evidence class;
- privacy, security, accessibility, and physical-safety constraints;
- branch, commit, and PR state;
- recovery instructions and next action.

An agent should not need to infer authority from chat history, duplicate a
contract in another repository, or guess which test proves completion.

## Documentation design rules

- Put a one-sentence purpose and authority boundary near the top.
- Prefer stable headings, tables, explicit paths, exact commands, and versioned
  identifiers over narrative-only guidance.
- State what is implemented, simulated, proposed, deferred, and prohibited.
- Link to one canonical source instead of copying normative rules.
- Keep setup commands non-interactive where possible and document prerequisites.
- Provide a narrow focused test and a workspace acceptance command.
- Include recovery behavior for unavailable services, models, modalities, and
  remote machines.
- Use plain language, semantic structure, and non-visual-only cues so guidance
  remains accessible to assistive technology.

## Current order of operations

1. Use Windows and Codex as the control plane and the dev NUC as the canonical
   Linux build and integration host.
2. Implement resolution attempts and reviewed determinization candidates.
3. Maintain versioned hardware requirements, interfaces, BOM records, and
   qualification plans without premature component lock-in.
4. Inventory and qualify the GPU workstation when it becomes available.
5. Begin later demonstration journeys only from reviewed contracts and task
   packets.

Foundation revisions created on 2026-08-14:

- `project-unisonOS/unison-infrastructure@3e31498`, including schema validation CI;
- `project-unisonOS/unison-hardware@7df94ed`, including registry/BOM validation CI;
- `project-unisonOS/.github#5` merged the shared agent-ready issue and pull
  request templates.
