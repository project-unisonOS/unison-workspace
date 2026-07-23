#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "[FAIL] Development environment missing. Run ./scripts/bootstrap-dev.sh" >&2
  exit 1
fi
"$PYTHON_BIN" "${ROOT_DIR}/scripts/validate-phase9-scope.py"
echo "[PASS] Phase 9.0 scope gate passed."
