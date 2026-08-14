#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${UNISON_DEV_VENV:-${root}/.venv}/bin/python"
if [[ ! -x "$python_bin" ]]; then
  echo "[FAIL] Development environment missing. Run ./scripts/bootstrap-dev.sh" >&2
  exit 1
fi
export UNISON_PRINCIPAL_BINDING_TEST_BYPASS=true
export DISABLE_AUTH_FOR_TESTS=true
export OTEL_SDK_DISABLED=true

"$python_bin" "$root/scripts/validate-dj0-fixtures.py"
PYTHONPATH="$root/unison-common/src" "$python_bin" -m pytest -q "$root/unison-common/tests/test_shared_incident_contracts.py"
PYTHONPATH="$root/unison-common/src:$root/unison-storage/src" "$python_bin" -m pytest -q \
  "$root/unison-storage/tests/test_incident_repository.py" \
  "$root/unison-storage/tests/test_incident_api.py"
PYTHONPATH="$root/unison-common/src:$root/unison-orchestrator/src" "$python_bin" -m pytest -q \
  "$root/unison-orchestrator/tests/test_shared_incident.py" \
  "$root/unison-orchestrator/tests/test_incident_workflow.py" \
  "$root/unison-orchestrator/tests/test_incident_api.py" \
  "$root/unison-orchestrator/tests/test_household_resources.py"
PYTHONPATH="$root/unison-common/src:$root/unison-experience-renderer/src" "$python_bin" -m pytest -q \
  "$root/unison-experience-renderer/tests/test_incident_expressions.py" \
  "$root/unison-experience-renderer/tests/test_incident_event_stream.py"

printf 'DJ-1 simulation acceptance passed; no physical-device or participatory claim is made.\n'
