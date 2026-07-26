#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
export PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export OTEL_ENABLED=false OTEL_SDK_DISABLED=true UNISON_DISABLE_OTEL_EXPORTER=true

export PYTHONPATH="${ROOT_DIR}/unison-common/src"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_model_lifecycle_contracts.py"

export PYTHONPATH="${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-inference/src"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-inference/tests/test_model_lifecycle_se11_se12.py" \
  "${ROOT_DIR}/tests/semantic/test_se11_se12_qualification.py"

echo "[PASS] SE11-SE12 evaluation, canary, rollback, invariance, and truthful simulated qualification passed."
