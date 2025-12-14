#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

PROJECT_NAME="${COMPOSE_PROJECT_NAME:-unison-devstack}"
COMPOSE_FILE="unison-devstack/docker-compose.yml"
PORTS_FILE="unison-devstack/docker-compose.ports.yml"

echo "[doctor] docker: $(docker --version 2>/dev/null || echo 'missing')"
echo "[doctor] compose: $(docker compose version 2>/dev/null || echo 'missing')"
echo "[doctor] engine: $(docker info --format '{{.Name}} ({{.OperatingSystem}})' 2>/dev/null || echo 'unknown')"

if ! docker info >/dev/null 2>&1; then
  echo "[doctor] FAIL: Docker daemon not reachable" >&2
  exit 1
fi

if command -v systemctl >/dev/null 2>&1; then
  if systemctl is-active docker.service >/dev/null 2>&1; then
    if docker info --format '{{.OperatingSystem}}' 2>/dev/null | grep -qi 'docker desktop'; then
      echo "[doctor] WARN: local docker.service is active inside this WSL distro" >&2
      echo "[doctor]       if you're using Docker Desktop, disable it to avoid port conflicts:" >&2
      echo "[doctor]       sudo systemctl disable --now docker docker.socket containerd" >&2
    fi
  fi
fi

echo "[doctor] compose config: ok"
docker compose -p "$PROJECT_NAME" -f "$COMPOSE_FILE" -f "$PORTS_FILE" config >/dev/null

if command -v ss >/dev/null 2>&1; then
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
    echo "[doctor] WARN: host ports already in use: ${in_use[*]}" >&2
    echo "[doctor]       if this isn't the devstack, bring-up will fail; stop conflicts or change ports." >&2
    if ps -eo pid,comm,args 2>/dev/null | grep -q '[d]ocker-proxy'; then
      echo "[doctor]       docker-proxy listeners (likely from another daemon):" >&2
      ps -eo pid,comm,args 2>/dev/null | grep -E '[d]ocker-proxy' | head -n 12 >&2 || true
    fi
  else
    echo "[doctor] ports: ok"
  fi
fi

echo "[doctor] current stack:"
docker compose -p "$PROJECT_NAME" -f "$COMPOSE_FILE" -f "$PORTS_FILE" ps
