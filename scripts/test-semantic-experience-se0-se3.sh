#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
export PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export OTEL_ENABLED=false OTEL_SDK_DISABLED=true UNISON_DISABLE_OTEL_EXPORTER=true

export PYTHONPATH="${ROOT_DIR}/unison-common/src"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider   "${ROOT_DIR}/tests/semantic/test_se0_semantic_baseline.py"   "${ROOT_DIR}/unison-common/tests/test_semantic_experience_contracts.py"

export PYTHONPATH="${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-context/src"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider   "${ROOT_DIR}/unison-context/tests/test_interaction_profiles.py"

export PYTHONPATH="${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-orchestrator/src"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider   "${ROOT_DIR}/unison-orchestrator/tests/test_semantic_rom_builder.py"
"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider   "${ROOT_DIR}/unison-orchestrator/tests/test_dev_thin_slice_renderer_emit.py"

node "${ROOT_DIR}/unison-experience-renderer/scripts/test_semantic_composers.mjs"

echo "[PASS] Semantic experience SE0-SE3 contracts, profile boundary, orchestration, and native composers passed."

