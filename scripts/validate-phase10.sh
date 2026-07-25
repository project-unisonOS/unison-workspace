#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "[FAIL] Development environment missing. Run ./scripts/bootstrap-dev.sh" >&2
  exit 1
fi

PYTHONPATH="${ROOT_DIR}/unison-common/src" \
  "$PYTHON_BIN" -m pytest \
  "${ROOT_DIR}/unison-common/tests/test_adaptive_maintenance_schema.py" -q

python3 "${ROOT_DIR}/unison-platform/scripts/test_adaptive_maintenance.py"

PYTHONPATH="${ROOT_DIR}/unison-experience-renderer/src:${ROOT_DIR}/unison-common/src" \
  "$PYTHON_BIN" -m pytest \
  "${ROOT_DIR}/unison-experience-renderer/tests/test_phase10_system_wellbeing.py" -q

echo "[PASS] Phase 10 AM-0 through AM-3 adaptive maintenance gates passed."
