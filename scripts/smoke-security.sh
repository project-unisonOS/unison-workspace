#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

PROJECT_NAME="${COMPOSE_PROJECT_NAME:-unison-devstack}"
BASE_FILE="unison-devstack/docker-compose.yml"
SEC_FILE="unison-devstack/docker-compose.security.yml"
SMOKE_SCRIPT="unison-devstack/scripts/e2e_smoke.py"
SMOKE_IMAGE="${UNISON_SMOKE_IMAGE:-unison-devstack-smoke:local}"

echo "=== Security smoke: port exposure ==="
check_not_published() {
  local svc="$1"
  local port="$2"
  local out
  out="$(docker compose -p "$PROJECT_NAME" -f "$BASE_FILE" -f "$SEC_FILE" port "$svc" "$port" 2>/dev/null || true)"
  # `docker compose port` prints `:0` when the container port exists but is not published.
  if [[ -n "$out" && "$out" != ":0" ]]; then
    echo "[FAIL] $svc:$port is published to host: $out" >&2
    exit 1
  fi
  echo "[ok] $svc:$port not published"
}

check_not_published postgres 5432
check_not_published redis 6379
check_not_published neo4j 7474
check_not_published neo4j 7687
check_not_published orchestrator 8080
check_not_published experience-renderer 8082
check_not_published storage 8082
check_not_published context 8081
check_not_published policy 8083
check_not_published intent-graph 8080
check_not_published context-graph 8081
check_not_published inference 8087
check_not_published network-vpn 8084
check_not_published network-vpn 8083

echo "=== Security smoke: in-network e2e ==="
ORCH_CID="$(docker compose -p "$PROJECT_NAME" -f "$BASE_FILE" -f "$SEC_FILE" ps -q orchestrator)"
if [[ -z "${ORCH_CID}" ]]; then
  echo "[FAIL] orchestrator container not running (start with ./scripts/up-security.sh)" >&2
  exit 1
fi
NETS="$(docker inspect -f '{{range $k, $v := .NetworkSettings.Networks}}{{println $k}}{{end}}' "$ORCH_CID")"
if [[ -z "${NETS}" ]]; then
  echo "[FAIL] could not determine compose network for orchestrator" >&2
  exit 1
fi
NET="${PROJECT_NAME}_internal"
if ! echo "$NETS" | grep -qx "$NET"; then
  NET="$(echo "$NETS" | head -n 1)"
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
