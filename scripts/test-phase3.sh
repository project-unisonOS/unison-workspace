#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-policy/src:${ROOT_DIR}/unison-capability/src:${ROOT_DIR}/unison-inference/src:${ROOT_DIR}/unison-consent/src:${ROOT_DIR}/unison-experience-renderer/src"
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export OTEL_ENABLED=false OTEL_SDK_DISABLED=true UNISON_DISABLE_OTEL_EXPORTER=true
export UNISON_PRINCIPAL_BINDING_TEST_BYPASS=true

"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_trust_governance.py" \
  "${ROOT_DIR}/unison-policy/tests/test_trust_service.py" \
  "${ROOT_DIR}/unison-consent/tests/test_phase3_migration.py" \
  "${ROOT_DIR}/unison-capability/tests/test_phase3_governance.py" \
  "${ROOT_DIR}/unison-inference/tests/test_phase3_disclosure.py" \
  "${ROOT_DIR}/unison-experience-renderer/tests/test_phase3_trust_accessibility.py" \
  "${ROOT_DIR}/tests/security/test_phase3_boundaries.py"

echo "[PASS] Phase 3 trust, disclosure, capability, adversarial, and accessibility suite passed."
