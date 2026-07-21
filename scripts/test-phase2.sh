#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
common_env=(
  PYTHONDONTWRITEBYTECODE=1
  PYTHONPATH="${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-context/src:${ROOT_DIR}/unison-orchestrator/src:${ROOT_DIR}/unison-experience-renderer/src"
  PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
  OTEL_ENABLED=false
  OTEL_SDK_DISABLED=true
  UNISON_DISABLE_OTEL_EXPORTER=true
  UNISON_PRINCIPAL_BINDING_TEST_BYPASS=true
)

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/validate-phase2-fixture.py"

env "${common_env[@]}" "${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_governed_context.py" \
  "${ROOT_DIR}/unison-common/tests/test_governed_context_schema.py" \
  "${ROOT_DIR}/unison-context/tests/test_governed_repository.py" \
  "${ROOT_DIR}/unison-context/tests/test_governed_api.py" \
  "${ROOT_DIR}/unison-orchestrator/tests/test_governed_context_client.py" \
  "${ROOT_DIR}/unison-experience-renderer/tests/test_phase2_context_accessibility.py" \
  "${ROOT_DIR}/tests/security/test_phase2_boundaries.py"

env \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH="${ROOT_DIR}/unison-context-graph/src:${ROOT_DIR}/unison-common/src" \
  PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
  OTEL_ENABLED=false \
  UNISON_DISABLE_OTEL_EXPORTER=true \
  "${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-context-graph/tests/test_phase2_authority.py"

echo "[PASS] Phase 2 governed context and relationship boundary suite passed."
