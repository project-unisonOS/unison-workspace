#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
export PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYTHONPATH="${ROOT_DIR}:${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-storage:${ROOT_DIR}/unison-auth:${ROOT_DIR}/unison-experience-renderer/src"
export OTEL_ENABLED=false OTEL_SDK_DISABLED=true UNISON_DISABLE_OTEL_EXPORTER=true
export DISABLE_AUTH_FOR_TESTS=true UNISON_PRINCIPAL_BINDING_TEST_BYPASS=true

"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_backup.py" \
  "${ROOT_DIR}/unison-storage/tests/test_phase6_backup.py" \
  "${ROOT_DIR}/unison-auth/tests/test_phase6_recovery.py" \
  "${ROOT_DIR}/unison-experience-renderer/tests/test_phase6_backup_accessibility.py" \
  "${ROOT_DIR}/tests/security/test_phase6_backup_boundaries.py"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/validate-phase6-schema.py"
"${PYTHON_BIN}" "${ROOT_DIR}/tools/phase6_backup_demo.py"

echo "[PASS] Phase 6 provider-blind backup and replacement restore proof passed."
