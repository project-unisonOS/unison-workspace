#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

PROJECT_NAME="${COMPOSE_PROJECT_NAME:-unison-devstack}"
COMPOSE_FILE="unison-devstack/docker-compose.yml"
PORTS_FILE="unison-devstack/docker-compose.ports.yml"
LOCALHOST_FILE="unison-devstack/docker-compose.localhost.yml"

compose_files=(-f "$COMPOSE_FILE" -f "$PORTS_FILE")
if [[ "${UNISON_RENDERER_LOCALHOST:-0}" == "1" ]]; then
  compose_files+=(-f "$LOCALHOST_FILE")
fi

docker compose -p "$PROJECT_NAME" "${compose_files[@]}" logs "$@"
