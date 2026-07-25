#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
export PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export OTEL_ENABLED=false OTEL_SDK_DISABLED=true UNISON_DISABLE_OTEL_EXPORTER=true

export PYTHONPATH="${ROOT_DIR}/unison-common/src"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_semantic_runtime_contracts.py"

export PYTHONPATH="${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-orchestrator/src"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-orchestrator/tests/test_semantic_runtime_se4_se6.py" \
  "${ROOT_DIR}/tests/semantic/test_se4_se7_qualification.py"

export PYTHONPATH="${ROOT_DIR}/unison-capability/src"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-capability/tests/test_semantic_targets.py"

node "${ROOT_DIR}/unison-experience-renderer/scripts/test_semantic_composers.mjs"
echo "[PASS] SE4-SE7 software planning, continuity, equivalence, interpretation, authority, and simulated qualification passed."
