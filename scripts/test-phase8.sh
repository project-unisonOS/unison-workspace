#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
export PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYTHONPATH="${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-capability/src:${ROOT_DIR}/unison-inference/src:${ROOT_DIR}/unison-io-speech:${ROOT_DIR}/unison-experience-renderer/src"
export OTEL_ENABLED=false OTEL_SDK_DISABLED=true UNISON_DISABLE_OTEL_EXPORTER=true

"${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_ecosystem_expansion_schema.py" \
  "${ROOT_DIR}/unison-capability/tests/test_phase8_ecosystem.py" \
  "${ROOT_DIR}/unison-inference/tests/test_phase8_routing.py" \
  "${ROOT_DIR}/unison-io-speech/tests/test_phase8_voice_parity.py" \
  "${ROOT_DIR}/unison-experience-renderer/tests/test_phase8_modalities.py" \
  "${ROOT_DIR}/tests/security/test_phase8_boundaries.py"

echo "[PASS] Phase 8 expansion 8.1 contracts, accessibility, routing, and supply-chain controls passed."

"${ROOT_DIR}/scripts/test-semantic-experience-se0-se3.sh"
"${ROOT_DIR}/scripts/test-semantic-experience-se4-se7.sh"
"${ROOT_DIR}/scripts/test-semantic-experience-se8-se10.sh"
