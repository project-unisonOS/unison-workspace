Developer Guide (Meta Repo)
==========================

Audience: new contributors who want a single-clone path to the full Unison stack.

Prerequisites
-------------
- Ubuntu/WSL2 or Linux with Docker Engine + Docker Compose v2
- Git with SSH access to `project-unisonos`
- Python 3.10+ (for smoke scripts)

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

Running Devstack + Experience Renderer
--------------------------------------
1) Ensure Docker is running.
2) Start services:
   ```bash
   ./scripts/up.sh
   ```
3) Access:
   - Orchestrator: http://localhost:8090/health
   - Experience renderer: http://localhost:8092
   - Supporting services: see `unison-devstack/README.md`

Smoke Test
----------
```bash
./scripts/smoke.sh
```
This runs `python3 unison-devstack/scripts/e2e_smoke.py` against the running stack.

Repo Map
--------
See `docs/repo-map.md` for roles, statuses, and entry points.

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
- Port conflicts: adjust bindings in `unison-devstack/docker-compose.yml`.
