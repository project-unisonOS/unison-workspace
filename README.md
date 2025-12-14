Unison Workspace Meta Repo
==========================

## Role in UnisonOS
This repository is the “front door” for developers. Clone once, pull submodules, and you have the full Unison workspace: services, devstack, shared libraries, docs, and optional payments.

Quickstart
----------
- Clone: `git clone git@github.com:project-unisonos/unison-workspace.git && cd unison-workspace`
- Pull submodules: `git submodule update --init --recursive`
- Start devstack: `./scripts/up.sh`
- Stop devstack: `./scripts/down.sh`
- Smoke test: `./scripts/smoke.sh`
- Security overlay: `./scripts/up-security.sh` then `./scripts/smoke-security.sh`
- Secrets: use `.env.example` as a template only. Source real secrets from Vault/Secret Manager (or Doppler/1Password CLI) into your shell; never commit `.env` files.

What’s Inside (Submodules)
--------------------------
- Core services: `unison-orchestrator`, `unison-context`, `unison-context-graph`, `unison-intent-graph`, `unison-auth`, `unison-consent`, `unison-policy`, `unison-inference`
- IO services: `unison-io-core`, `unison-io-speech`, `unison-io-vision`, `unison-storage`
- Experience: `unison-experience-renderer`, `unison-agent-vdi`
- Shared & tooling: `unison-common`, `unison-devstack`, `unison-docs`
- Optional: `unison-payments`

Dev Flow Highlights
-------------------
- `./scripts/bootstrap.sh` – ensure submodules are initialized and dependencies are ready.
- `./scripts/sync.sh` – pull latest `main` on every submodule.
- `./scripts/up.sh` – run devstack via the devstack compose file.
- `./scripts/smoke.sh` – run the devstack E2E smoke.

Docs
----
- Developer guide: `docs/developer-guide.md`
- Repo map: `docs/repo-map.md`
- Full documentation set lives in `unison-docs` (also a submodule).
- Public docs: https://project-unisonos.github.io
- Repo roles: `unison-docs/dev/unison-repo-roles.md`

Troubleshooting
---------------
- If services fail to start, try `docker compose -f unison-devstack/docker-compose.yml pull --ignore-pull-failures` then rerun `./scripts/up.sh`.
- If submodules drift, run `./scripts/sync.sh` to re-pin to the latest `main`.
- If startup feels “stuck”, run `./scripts/doctor.sh` to catch port conflicts and compose misconfig fast.
- WSL + Docker Desktop: don’t also run a separate Docker daemon inside Ubuntu (it can “steal” host ports). If `./scripts/doctor.sh` warns about `docker.service`, disable it: `sudo systemctl disable --now docker docker.socket containerd`.
- Optional knobs: `UNISON_SYNC_SUBMODULES=1 ./scripts/up.sh`, `UNISON_SKIP_PORT_PREFLIGHT=1 ./scripts/up.sh`.
- Manual compose: dev ports live in `unison-devstack/docker-compose.ports.yml` (use `docker compose -f unison-devstack/docker-compose.yml -f unison-devstack/docker-compose.ports.yml up -d`); security overlay uses `-f unison-devstack/docker-compose.security.yml` without the ports overlay.

## Tests
- From `unison-devstack`: `python scripts/e2e_smoke.py` and `python scripts/test_multimodal.py` (requires Docker running).

## Links
- Platform roadmap: `unison-docs/roadmap/deployment-platform-roadmap.md`
- Release/branching policy: `unison-docs/dev/release-and-branching.md`
