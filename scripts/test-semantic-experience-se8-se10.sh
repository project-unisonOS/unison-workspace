#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
export PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export OTEL_ENABLED=false OTEL_SDK_DISABLED=true UNISON_DISABLE_OTEL_EXPORTER=true

export PYTHONPATH="${ROOT_DIR}/unison-common/src"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_model_runtime_contracts.py"

export PYTHONPATH="${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-inference/src:${ROOT_DIR}/unison-orchestrator/src"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-inference/tests/test_governed_models_se8_se10.py" \
  "${ROOT_DIR}/tests/semantic/test_se8_se10_qualification.py"

echo "[PASS] SE8-SE10 signed registry, deterministic routing, proposal reconciliation, and simulated qualification passed."
