#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
export PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYTHONPATH="${ROOT_DIR}:${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-orchestrator/src:${ROOT_DIR}/unison-experience-renderer/src"
export OTEL_ENABLED=false OTEL_SDK_DISABLED=true UNISON_DISABLE_OTEL_EXPORTER=true

"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_workflows.py" \
  "${ROOT_DIR}/unison-orchestrator/tests/test_phase7_workflows.py" \
  "${ROOT_DIR}/unison-experience-renderer/tests/test_phase7_workflow_accessibility.py" \
  "${ROOT_DIR}/tests/security/test_phase7_workflow_boundaries.py"

"${PYTHON_BIN}" "${ROOT_DIR}/tools/phase7_workflow_demo.py"

echo "[PASS] Phase 7 bounded assistant workflows and outcome evidence passed."
