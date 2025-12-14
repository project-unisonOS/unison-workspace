#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

PROJECT_NAME="${COMPOSE_PROJECT_NAME:-unison-devstack}"
BASE_FILE="unison-devstack/docker-compose.yml"
SEC_FILE="unison-devstack/docker-compose.security.yml"

docker compose -p "$PROJECT_NAME" -f "$BASE_FILE" -f "$SEC_FILE" up -d --remove-orphans --wait --wait-timeout 300 "$@"

echo "Devstack (security overlay) started. Use ./scripts/smoke-security.sh to validate."
