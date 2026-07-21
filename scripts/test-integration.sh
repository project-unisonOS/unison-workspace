#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "[integration] validating the current Compose integration profile"
docker compose \
  -f "${ROOT_DIR}/unison-devstack/docker-compose.yml" \
  -f "${ROOT_DIR}/unison-devstack/docker-compose.ports.yml" \
  config --quiet
echo "[integration] run ./scripts/validate-ci.sh to start services and execute integration journeys."
