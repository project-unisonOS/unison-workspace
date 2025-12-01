#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/.."

git submodule update --init --recursive

docker compose -f unison-devstack/docker-compose.yml up -d "$@"

echo "Devstack started. Health checks: see unison-devstack README."
