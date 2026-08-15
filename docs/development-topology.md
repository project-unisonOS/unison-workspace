# Development and repository topology

Status: accepted development policy, 2026-08-14.

## Canonical machine roles

| Role | System | Authority |
| --- | --- | --- |
| Control plane | Windows Codex app | Direct work, voice/remote coordination, review; not the canonical Linux runtime |
| Development integration | Ubuntu dev NUC over SSH/Tailscale | Canonical Linux bootstrap, tests, focused Compose profiles, evidence capture |
| Interim deployment lab | Dual-GPU workstation | Deferred until inventoried; later owns inference, power, and thermal evidence |
| Source of truth | GitHub organization | Reviewed code, contracts, task packets, CI, issues, and durable handoff state |

Contributors may use any coding agent. Repository files, not an agent's chat
history, must contain the authority, constraints, commands, and evidence needed
to resume work.

## Supported development profiles

1. `component`: run a repository's unit and contract suite.
2. `dj1`: run `./scripts/test-dj1.sh`, then
   `.venv/bin/python scripts/test-dj1-compose.py` on the NUC.
3. `full-devstack`: exploratory only until every build context is reconciled
   with the workspace layout and every required repository is pinned.
4. `gpu-lab`: deferred until inventory and activation gates in
   `unison-infrastructure/environments/gpu-lab.yaml` are satisfied.

The focused root-level Compose profile is canonical for DJ-1. The historical
`unison-devstack/docker-compose.yml` assumes sibling checkouts through `../../`
paths and references services not consistently pinned in older workspace
snapshots. It is not the default contributor entrypoint.

## Windows and dev NUC workflow

Windows and Codex are the control plane. The dev NUC is the authoritative Linux
build and integration plane. Code remains in a normal Git checkout on the NUC;
Windows does not mount or mirror that checkout as a runtime filesystem.

Configure the control plane once:

```powershell
$env:UNISON_DEV_NUC_HOST = 'dev-nuc'
$env:UNISON_DEV_NUC_WORKSPACE = '/srv/unison/unison-workspace'
```

Then use `scripts/remote-dev.ps1` for bootstrap, validation, unit, boundary, and
status commands. SSH transport may use the local network or Tailscale. Host-key
verification and user authentication remain SSH responsibilities. The wrapper
does not copy secrets, create credentials, or make Windows a deployment host.

Every contributor, including a coding agent, begins with `AGENTS.md`, an active
task packet, and `docs/repo-map.md`. A clean clone must pass
`python scripts/validate-agent-onboarding.py` before it is considered ready.

## Repository direction

- `unison-workspace` is the human and agent front door, pins coordinated
  revisions, and owns cross-repository acceptance and evidence.
- `unison-common` owns versioned wire contracts and compatibility tests.
- A service repository owns its implementation and local tests.
- `unison-infrastructure` owns environment and deployment profiles.
- `unison-hardware` owns hardware requirements, interfaces, BOM records, and
  qualification plans.
- `unison-docs` remains the public documentation site; normative execution
  guidance lives adjacent to the code it governs and is linked from there.

Do not create another repository for a feature until it has an independent
release cadence, authority boundary, security boundary, or substantially
different toolchain. Generated clients, when introduced, are generated from
`unison-common` contracts and published or pinned through a documented release;
hand-edited copies are prohibited.

## Submodule and devstack disposition

The workspace currently pins the repositories required for the supported
component and DJ-1 profiles. Services referenced only by the broad legacy
devstack must either be added deliberately with an owner and required checks,
or moved behind an optional profile. A green focused profile must never be
described as proof that the full historical devstack is deployable.
