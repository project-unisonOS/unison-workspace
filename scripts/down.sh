#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

PROJECT_NAME="${COMPOSE_PROJECT_NAME:-unison-devstack}"
COMPOSE_FILE="unison-devstack/docker-compose.yml"
PORTS_FILE="unison-devstack/docker-compose.ports.yml"

docker compose -p "$PROJECT_NAME" -f "$COMPOSE_FILE" -f "$PORTS_FILE" down --remove-orphans "$@"
