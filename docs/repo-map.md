Unison Repo Map (Meta Snapshot)
===============================

| Repo | Role | Status | Entry Points / Notes |
| --- | --- | --- | --- |
| unison-orchestrator | Request router and policy-aware orchestration | Core | `src/server.py`, health `:8080`; tests `pytest` |
| unison-context | Context service (kv + profiles) | Core | `src/server.py`; tests `pytest` |
| unison-context-graph | Graph API over context/intent | Core | `src/main.py` (FastAPI); tests `pytest` |
| unison-intent-graph | Intent graph service | Core | `src/main.py`; tests `pytest` |
| unison-auth | Auth service (tokens/session) | Core | `src/auth_service.py`; tests `pytest` |
| unison-consent | Consent enforcement | Core | `src/main.py`; tests `pytest` |
| unison-policy | Policy evaluation | Core | `src/server.py`; tests `pytest` |
| unison-inference | Inference gateway | Core | `src/server.py`; tests `pytest` |
| unison-io-core | IO core adapter | Core | `src/server.py`; tests `pytest` |
| unison-io-speech | Speech IO adapter | Core | `src/server.py`; tests `pytest` |
| unison-io-vision | Vision IO adapter | Core | `src/server.py`; tests `pytest` |
| unison-storage | Storage adapter | Core | `src/server.py`; tests `pytest` |
| unison-experience-renderer | Experience/API renderer | Core | `src/main.py`; tests `pytest`/FastAPI |
| unison-agent-vdi | Agent UI shell | Core | `src/main.py`; tests `pytest` |
| unison-devstack | Compose + tooling for full stack | Core tooling | `docker-compose.yml`, scripts in `scripts/` |
| unison-common | Shared Python package | Core lib | Built as wheel `ghcr.io/project-unisonos/unison-common-wheel` |
| unison-docs | Canonical documentation | Core docs | See `unison-docs/dev` and `unison-docs/experience` |
| unison-payments | Payments capability (modular) | Optional | `src/` services; tests `pytest` |
| unison-shell | CLI helper / runtime shell | Optional | `README`, scripts; tests per repo |

Notes
-----
- Image tag `1.0` (and `latest`) for all services and the shared wheel are published to `ghcr.io/project-unisonos`.
- Devstack compose is consumed via `./scripts/up.sh` in this meta repo (delegates to `unison-devstack/docker-compose.yml`).
