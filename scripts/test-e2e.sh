#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "[e2e] using the established local validation sequence"
exec "${ROOT_DIR}/scripts/validate-local.sh"
