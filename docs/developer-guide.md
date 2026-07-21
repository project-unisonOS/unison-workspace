Developer Guide (Meta Repo)
==========================

Audience: new contributors who want a single-clone path to the full Unison stack.

Prerequisites
-------------
- Ubuntu/WSL2 or Linux with Docker Engine + Docker Compose v2
- Git with SSH access to `project-unisonos`
- Python 3.12 (the deterministic Phase 0 development profile)

Getting the Workspace
---------------------
1) Clone and init submodules:
   ```bash
   git clone git@github.com:project-unisonos/unison-workspace.git
   cd unison-workspace
   git submodule update --init --recursive
   ```
2) (Optional) Pull latest on all submodules:
   ```bash
   ./scripts/sync.sh
   ```
3) Bootstrap and validate the pinned environment:
   ```bash
   ./scripts/bootstrap-dev.sh
   ./scripts/validate-phase0.sh
   ./scripts/test-unit.sh
   ./scripts/test-boundaries.sh
   ```

On Windows, PowerShell is a thin WSL2 wrapper over those same commands:

```powershell
.\scripts\unison.ps1 bootstrap
.\scripts\unison.ps1 validate-phase0
.\scripts\unison.ps1 test-unit
```

There is no separate Windows implementation path. The historical installers in
`unison-devstack/install.sh` and `unison-devstack/install.ps1` describe an older
prototype topology and are not supported UnisonOS appliance installers.

The standardized test entrypoints are `test-unit.sh`, `test-boundaries.sh`,
`test-integration.sh`, and `test-e2e.sh`. Phase 0 executes unit and static boundary
planning checks. Integration and end-to-end wrappers retain the existing Docker
journeys and require their documented service prerequisites.

Running Devstack + Experience Renderer
--------------------------------------
1) Ensure Docker is running.
2) Review workspace completeness before first bring-up:
   - this workspace includes the submodules listed in `.gitmodules`
   - `unison-devstack/docker-compose.yml` also references several services not present as submodules in this checkout
   - a successful bring-up may therefore rely on prebuilt GHCR images, sibling repo checkouts outside this workspace snapshot, or a narrower local profile than the full compose file implies
3) Start services:
   ```bash
   ./scripts/up.sh
   ```
   `./scripts/up.sh` runs a quick host-port preflight to catch port conflicts before Docker Compose starts, and includes `unison-devstack/docker-compose.ports.yml` for host port publishing.
   Optional: publish the renderer on `http://localhost` (port 80) instead of only `:8092`:
   ```bash
   UNISON_RENDERER_LOCALHOST=1 ./scripts/up.sh
   ```
4) Security overlay (segmented networks; no host port publishing):
   ```bash
   ./scripts/up-security.sh
   ./scripts/smoke-security.sh
   ```
   Stop security overlay:
   ```bash
   ./scripts/down-security.sh
   ```
3) Access:
   - Orchestrator: http://localhost:8080/health
   - Experience renderer: http://localhost:8092/health
   - Supporting services: see `unison-devstack/README.md`

Smoke Test
----------
```bash
./scripts/smoke.sh
```
This runs `python3 unison-devstack/scripts/e2e_smoke.py` against the running stack and is the fastest basic verification after `./scripts/up.sh`.

For the full recommended local validation sequence, run:

```bash
./scripts/validate-local.sh
```

For a narrower CI-friendly path that brings up only the services needed for the current green validation sequence, run:

```bash
./scripts/validate-ci.sh
```

Scope note:
- `./scripts/smoke.sh` validates the devstack end-to-end smoke path only
- it should not be treated as proof that voice, vision, or the broader multimodal experience is working end to end
- for multimodal validation, run `python3 unison-devstack/scripts/test_multimodal.py` separately
- for the current renderer-led product-path contract, run `python3 unison-devstack/scripts/validate_golden_path.py`
- for the local no-credential Journey 6 email path, run `python3 unison-devstack/scripts/validate_journey6_fake_mail.py`

Recommended local validation sequence:
1. `./scripts/smoke.sh`
2. `python3 unison-devstack/scripts/test_multimodal.py`
3. `python3 unison-devstack/scripts/validate_golden_path.py`
4. `python3 unison-devstack/scripts/validate_journey6_fake_mail.py`

Or run the wrappers:

```bash
./scripts/validate-local.sh
./scripts/validate-ci.sh
```

See `unison-docs/dev/golden-path-validation.md` for the current golden-path definition.

Repo-local regression anchors for that path now include focused tests in:
- `unison-orchestrator/tests/test_startup_status.py`
- `unison-orchestrator/tests/test_startup_status_ready.py`
- `unison-orchestrator/tests/test_dashboard_refresh.py`
- `unison-orchestrator/tests/test_voice_ingest.py`
- `unison-experience-renderer/tests/test_startup_status_endpoint.py`
- `unison-experience-renderer/tests/test_onboarding_endpoint.py`
- `unison-experience-renderer/tests/test_onboarding_ready.py`
- `unison-context/tests/test_dashboard.py`

For Tranche C Journey 7 work, the workspace now also carries a bounded orchestrator-side `vdi.download` planning and executor contract slice. This is useful regression coverage for the first legacy workflow, but it is still not the same as full Milestone 1 acceptance of the end-to-end orchestrator -> actuation -> VDI -> storage -> renderer path.

For Tranche C Journey 6 work, the broader local repo set now also includes a real bounded Gmail onboarding slice in `unison-comms`, covering readiness/onboarding state, bootstrap-backed local credential storage, verification, reset with bootstrap-store clearing, an OAuth-ready contract surface, draft-first compose behavior, adapter-backed summarize, and provider-aware empty/message shaping. The workspace checkout still carries the orchestrator/docs Gmail draft contract checkpoint around `comms.compose`, which remains useful as an orchestrator-boundary regression anchor. Neither should be read as proof that live Gmail summarize/provider flows are fully validated end to end in this checkout.

The current validated checkpoint also includes a startup-status truth fix in `unison-orchestrator` so `/startup/status` prefers cached `poweron` snapshot truth during focused validation instead of overriding it with live checks when snapshot checks are already present.

Repo Map
--------
See `docs/repo-map.md` for roles, statuses, entry points, and current workspace-boundary caveats.

Working in a Specific Service
-----------------------------
Each submodule is a normal git repo:
```bash
cd unison-orchestrator
git checkout -b feature/xyz
# hack, test, commit, push
```

Updating the Workspace
----------------------
- Pull latest meta + submodules:
  ```bash
  git pull origin main
  git submodule update --remote --merge
  ```
- Or run `./scripts/sync.sh` to pull `main` in every submodule and record the new SHAs.

Troubleshooting
---------------
- Compose errors: `docker compose -f unison-devstack/docker-compose.yml pull --ignore-pull-failures` then re-run `./scripts/up.sh`.
- Stale submodules: `./scripts/sync.sh`.
- Port conflicts: run `./scripts/doctor.sh` first, then adjust published bindings in `unison-devstack/docker-compose.ports.yml` if needed.
- WSL + Docker Desktop: avoid running a second Docker daemon inside Ubuntu. If `./scripts/doctor.sh` warns about `docker.service`, disable it: `sudo systemctl disable --now docker docker.socket containerd`.
- Debug: `./scripts/status.sh`, `./scripts/logs.sh`, `./scripts/doctor.sh`.
