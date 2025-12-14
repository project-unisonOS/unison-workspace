#!/usr/bin/env bash
set -euo pipefail

if ! command -v systemctl >/dev/null 2>&1; then
  echo "systemctl not available; nothing to do."
  exit 0
fi

if ! docker info >/dev/null 2>&1; then
  echo "Docker daemon not reachable; start Docker Desktop first." >&2
  exit 1
fi

if ! docker info --format '{{.OperatingSystem}}' 2>/dev/null | grep -qi 'docker desktop'; then
  echo "Docker Desktop not detected; not changing local docker.service." >&2
  exit 1
fi

if ! systemctl is-active docker.service >/dev/null 2>&1; then
  echo "local docker.service is not running; nothing to do."
  exit 0
fi

cat <<'EOF'
Detected Docker Desktop + a second Docker daemon running inside this WSL distro.

This commonly causes devstack bring-up to fail with "port is already allocated".

Run this manually (requires sudo):
  sudo systemctl disable --now docker docker.socket containerd
EOF

