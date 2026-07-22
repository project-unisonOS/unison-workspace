#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
export PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYTHONPATH="${ROOT_DIR}:${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-auth/src:${ROOT_DIR}/unison-comms/src:${ROOT_DIR}/unison-orchestrator/src:${ROOT_DIR}/unison-experience-renderer/src"
export OTEL_ENABLED=false OTEL_SDK_DISABLED=true UNISON_DISABLE_OTEL_EXPORTER=true
export DISABLE_AUTH_FOR_TESTS=true UNISON_PRINCIPAL_BINDING_TEST_BYPASS=true

"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_channel.py" \
  "${ROOT_DIR}/unison-auth/tests/test_identity_store.py" \
  "${ROOT_DIR}/unison-comms/tests/test_channel_gateway.py" \
  "${ROOT_DIR}/unison-orchestrator/tests/test_phase5_channel_ingress.py" \
  "${ROOT_DIR}/unison-experience-renderer/tests/test_phase5_channel_accessibility.py" \
  "${ROOT_DIR}/tests/security/test_phase5_channel_gateway.py"

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/scan-phase5-network.py"

echo "[PASS] Phase 5 Channel Gateway and remote-text proof passed."
