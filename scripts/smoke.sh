#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

SMOKE_SCRIPT="unison-devstack/scripts/e2e_smoke.py"
COMPOSE_FILE="unison-devstack/docker-compose.yml"
PORTS_FILE="unison-devstack/docker-compose.ports.yml"
PROJECT_NAME="${COMPOSE_PROJECT_NAME:-unison-devstack}"
SMOKE_IMAGE="${UNISON_SMOKE_IMAGE:-unison-devstack-smoke:local}"

supports_proposed_action() {
  python3 - <<'PY'
import json, sys
try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(1)
skills = data.get("skills") or []
sys.exit(0 if "proposed_action" in skills else 1)
PY
}

# Fast path: run directly on host if localhost actually points at the devstack orchestrator.
if command -v curl >/dev/null 2>&1 && command -v python3 >/dev/null 2>&1; then
  if curl -fsS "http://localhost:8080/introspect" | supports_proposed_action; then
    echo "=== E2E smoke: host mode ==="
    python3 "$SMOKE_SCRIPT"
    exit 0
  fi
fi

# Fallback: run inside the compose network (reliable on WSL/Docker Desktop where localhost forwarding can be surprising).
echo "=== E2E smoke: docker network mode ==="
ORCH_CID="$(docker compose -p "$PROJECT_NAME" -f "$COMPOSE_FILE" -f "$PORTS_FILE" ps -q orchestrator)"
if [[ -z "${ORCH_CID}" ]]; then
  echo "[FAIL] orchestrator container not running (start with ./scripts/up.sh)" >&2
  exit 1
fi
NET="$(docker inspect -f '{{range $k, $v := .NetworkSettings.Networks}}{{$k}}{{end}}' "$ORCH_CID")"
if [[ -z "${NET}" ]]; then
  echo "[FAIL] could not determine compose network for orchestrator" >&2
  exit 1
fi

if ! docker image inspect "$SMOKE_IMAGE" >/dev/null 2>&1; then
  docker build -t "$SMOKE_IMAGE" -f "unison-devstack/Dockerfile.smoke" "unison-devstack"
fi

docker run --rm \
  --network "$NET" \
  -v "$PWD/unison-devstack/scripts:/scripts:ro" \
  -e UNISON_ORCH_URL="http://orchestrator:8080" \
  -e UNISON_CONTEXT_URL="http://context:8081" \
  -e UNISON_IOCORE_URL="http://io-core:8085" \
  -e UNISON_POLICY_URL="http://policy:8083" \
  -e UNISON_ACTUATION_URL="http://actuation:8086" \
  "$SMOKE_IMAGE" \
  python /scripts/e2e_smoke.py
