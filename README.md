Unison Workspace Meta Repo
==========================

## Role in UnisonOS
This repository is the “front door” for developers. Clone once, pull submodules, and you have the full Unison workspace: services, devstack, shared libraries, docs, and optional payments.

Quickstart
----------
- Clone: `git clone git@github.com:project-unisonos/unison-workspace.git && cd unison-workspace`
- Pull submodules: `git submodule update --init --recursive`
- Review current workspace scope and prerequisites in `docs/developer-guide.md` before first bring-up
- Start devstack: `./scripts/up.sh`
- Stop devstack: `./scripts/down.sh`
- Smoke test: `./scripts/smoke.sh`
- Full local validation sequence: `./scripts/validate-local.sh`
- CI-friendly validation sequence: `./scripts/validate-ci.sh`
- Security overlay: `./scripts/up-security.sh` then `./scripts/smoke-security.sh`
- Secrets: use `.env.example` as a template only. Source real secrets from Vault/Secret Manager (or Doppler/1Password CLI) into your shell; never commit `.env` files.

Important current limitation:
- `./scripts/up.sh` delegates to `unison-devstack`, which references additional repos and images outside this submodule set. In practice, a successful full-stack bring-up may require either prebuilt images for those services or sibling checkouts beyond what `.gitmodules` provides today.

What’s Inside (Submodules)
--------------------------
Included directly in this workspace snapshot:
- Core services: `unison-orchestrator`, `unison-context`, `unison-context-graph`, `unison-intent-graph`, `unison-auth`, `unison-consent`, `unison-policy`, `unison-inference`
- IO services: `unison-io-core`, `unison-io-speech`, `unison-io-vision`, `unison-storage`
- Experience: `unison-experience-renderer`, `unison-agent-vdi`
- Shared & tooling: `unison-common`, `unison-devstack`, `unison-docs`
- Optional: `unison-payments`

Not included as submodules in this workspace snapshot, but still referenced by some docs and devstack paths:
- `unison-actuation`
- `unison-capabilities` (local checkout path for the capability resolver service repo)
- `unison-comms`
- `unison-io-bci`
- `unison-network-vpn`
- `unison-platform`
- `unison-skill-register`

Treat this repository as the main developer front door for the repos above, not yet as a complete single-clone source checkout for every repo mentioned across the broader UnisonOS platform docs.

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
- Milestone 1 acceptance matrix: `docs/milestone-1-acceptance-matrix.md`
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
- Manual compose: published dev host ports live in `unison-devstack/docker-compose.ports.yml` (use `docker compose -f unison-devstack/docker-compose.yml -f unison-devstack/docker-compose.ports.yml up -d`); security overlay uses `-f unison-devstack/docker-compose.security.yml` without the ports overlay.
- If bring-up fails on port allocation, run `./scripts/doctor.sh` first. It checks the overlay port set that `./scripts/up.sh` actually uses.

## Tests
- From `unison-devstack`: `python scripts/e2e_smoke.py`, `python scripts/test_multimodal.py`, `python scripts/validate_golden_path.py`, and `python scripts/validate_journey6_fake_mail.py` (requires Docker running).
- `./scripts/smoke.sh` runs the devstack end-to-end smoke only. It does not, by itself, validate full multimodal behavior or the renderer-led golden path.
- `./scripts/validate-local.sh` runs the recommended local validation sequence in one command.
- `./scripts/validate-ci.sh` brings up the minimum stack needed for the current green validation sequence, intentionally skipping optional services like `io-bci`.
- Recommended local validation sequence:
  1. `./scripts/smoke.sh`
  2. `python3 unison-devstack/scripts/test_multimodal.py`
  3. `python3 unison-devstack/scripts/validate_golden_path.py`
  4. `python3 unison-devstack/scripts/validate_journey6_fake_mail.py`
- See `unison-docs/dev/golden-path-validation.md` for the current renderer-led golden-path contract.

## Links
- Platform roadmap: `unison-docs/roadmap/deployment-platform-roadmap.md`
- Release/branching policy: `unison-docs/dev/release-and-branching.md`
