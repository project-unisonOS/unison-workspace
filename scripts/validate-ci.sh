#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

PROJECT_NAME="${COMPOSE_PROJECT_NAME:-unison-devstack}"
COMPOSE_FILE="unison-devstack/docker-compose.yml"
PORTS_FILE="unison-devstack/docker-compose.ports.yml"
LOCALHOST_FILE="unison-devstack/docker-compose.localhost.yml"

compose_files=(-f "$COMPOSE_FILE" -f "$PORTS_FILE")
if [[ "${UNISON_RENDERER_LOCALHOST:-0}" == "1" ]]; then
  compose_files+=(-f "$LOCALHOST_FILE")
fi

services=(
  postgres redis neo4j jaeger
  policy storage context intent-graph context-graph inference
  experience-renderer auth consent capability comms
  network-vpn agent-vdi actuation orchestrator
  io-speech io-vision io-core
)

echo "[ci] bringing up minimal validation stack"
docker compose -p "$PROJECT_NAME" "${compose_files[@]}" up -d --remove-orphans --wait --wait-timeout 300 "${services[@]}"

echo "[ci][1/4] Devstack smoke"
./scripts/smoke.sh

echo "[ci][2/4] Multimodal validation"
python3 unison-devstack/scripts/test_multimodal.py

echo "[ci][3/4] Renderer-led golden-path validation"
python3 unison-devstack/scripts/validate_golden_path.py

echo "[ci][4/4] Journey 6 fake-mail validation"
python3 unison-devstack/scripts/validate_journey6_fake_mail.py

echo "CI-friendly validation sequence completed."
