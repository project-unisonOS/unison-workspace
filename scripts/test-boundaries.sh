#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "[FAIL] Development environment missing. Run ./scripts/bootstrap-dev.sh" >&2
  exit 1
fi

"$PYTHON_BIN" "${ROOT_DIR}/scripts/validate-household-fixtures.py"
"$PYTHON_BIN" "${ROOT_DIR}/scripts/validate-threat-map.py"
echo "[PASS] Phase 0 boundary fixtures and planned threat coverage passed."
echo "[NOTE] Runtime household boundary enforcement begins only after the Phase 0 gate."
