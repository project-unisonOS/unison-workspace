#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

# Prefer Buildx Bake for better build performance when available.
# Override with `COMPOSE_BAKE=false` if needed.
export COMPOSE_BAKE="${COMPOSE_BAKE:-true}"

PROJECT_NAME="${COMPOSE_PROJECT_NAME:-unison-devstack}"
COMPOSE_FILE="unison-devstack/docker-compose.yml"
PORTS_FILE="unison-devstack/docker-compose.ports.yml"

if [[ "${UNISON_SYNC_SUBMODULES:-0}" == "1" ]]; then
  git submodule update --init --recursive
fi

existing_containers="$(docker compose -p "$PROJECT_NAME" -f "$COMPOSE_FILE" -f "$PORTS_FILE" ps -q 2>/dev/null || true)"
if [[ "${UNISON_SKIP_PORT_PREFLIGHT:-0}" != "1" ]] && [[ -z "${existing_containers}" ]] && command -v ss >/dev/null 2>&1; then
  required_ports=(
    5432 6379 7072
    7474 7687
    8080 8081 8082 8083 8084 8085 8086 8087 8088 8089
    8091 8092 8093 8094 8095 8096 8097
    14250 16686 4317 4318
  )
  in_use=()
  for port in "${required_ports[@]}"; do
    if ss -ltnH "sport = :$port" 2>/dev/null | grep -q .; then
      in_use+=("$port")
    fi
  done
  if ((${#in_use[@]})); then
    echo "Port preflight failed; these host ports are already in use: ${in_use[*]}" >&2
    echo "Stop the conflicting process(es) or change published ports in unison-devstack/docker-compose.ports.yml." >&2
    if command -v systemctl >/dev/null 2>&1 && systemctl is-active docker.service >/dev/null 2>&1; then
      if docker info --format '{{.OperatingSystem}}' 2>/dev/null | grep -qi 'docker desktop'; then
        echo "" >&2
        echo "WSL note: your Ubuntu distro has its own Docker daemon running (systemd docker.service)." >&2
        echo "If you're using Docker Desktop, disable the local daemon to avoid \"port already allocated\" conflicts:" >&2
        echo "  sudo systemctl disable --now docker docker.socket containerd" >&2
      fi
    fi
    if ps -eo pid,comm,args 2>/dev/null | grep -q '[d]ocker-proxy'; then
      echo "" >&2
      echo "Port holders (if docker-proxy):" >&2
      ps -eo pid,comm,args 2>/dev/null | grep -E '[d]ocker-proxy' | head -n 12 >&2 || true
    fi
    echo "" >&2
    echo "To bypass the preflight (not recommended): UNISON_SKIP_PORT_PREFLIGHT=1 ./scripts/up.sh" >&2
    exit 1
  fi
fi

needs_build_common=0
for arg in "$@"; do
  if [[ "$arg" == "--build" ]]; then
    needs_build_common=1
    break
  fi
done
if [[ "$needs_build_common" == "1" ]]; then
  docker compose -p "$PROJECT_NAME" -f "$COMPOSE_FILE" -f "$PORTS_FILE" --profile build-common build unison-common-wheel
fi

docker compose -p "$PROJECT_NAME" -f "$COMPOSE_FILE" -f "$PORTS_FILE" up -d --remove-orphans --wait --wait-timeout 300 "$@"

echo "Devstack started. Health checks: see unison-devstack README."
