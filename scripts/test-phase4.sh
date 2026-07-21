#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
export PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYTHONPATH="${ROOT_DIR}:${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-auth/src:${ROOT_DIR}/unison-context/src:${ROOT_DIR}/unison-orchestrator/src:${ROOT_DIR}/unison-experience-renderer/src"
export OTEL_ENABLED=false OTEL_SDK_DISABLED=true UNISON_DISABLE_OTEL_EXPORTER=true
export UNISON_PRINCIPAL_BINDING_TEST_BYPASS=true

"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_household.py" \
  "${ROOT_DIR}/unison-auth/tests/test_identity_store.py" \
  "${ROOT_DIR}/unison-context/tests/test_governed_repository.py" \
  "${ROOT_DIR}/unison-orchestrator/tests/test_household_resources.py" \
  "${ROOT_DIR}/unison-experience-renderer/tests/test_phase4_household_accessibility.py" \
  "${ROOT_DIR}/tests/security/test_phase4_household_proof.py"
"${PYTHON_BIN}" "${ROOT_DIR}/scripts/run-phase4-household-proof.py"

echo "[PASS] Phase 4 two-assistant household proof passed."

