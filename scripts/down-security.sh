#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

PROJECT_NAME="${COMPOSE_PROJECT_NAME:-unison-devstack}"
BASE_FILE="unison-devstack/docker-compose.yml"
SEC_FILE="unison-devstack/docker-compose.security.yml"

docker compose -p "$PROJECT_NAME" -f "$BASE_FILE" -f "$SEC_FILE" down --remove-orphans "$@"

