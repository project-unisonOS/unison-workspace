#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONPATH="$root/unison-common/src:$root/unison-storage:$root/unison-orchestrator/src:$root/unison-experience-renderer/src"
export UNISON_PRINCIPAL_BINDING_TEST_BYPASS=true
export DISABLE_AUTH_FOR_TESTS=true
export OTEL_SDK_DISABLED=true

python "$root/scripts/validate-dj0-fixtures.py"
python -m pytest -q \
  "$root/unison-common/tests/test_shared_incident_contracts.py" \
  "$root/unison-storage/tests/test_incident_repository.py" \
  "$root/unison-storage/tests/test_incident_api.py" \
  "$root/unison-orchestrator/tests/test_shared_incident.py" \
  "$root/unison-orchestrator/tests/test_incident_workflow.py" \
  "$root/unison-orchestrator/tests/test_incident_api.py" \
  "$root/unison-orchestrator/tests/test_household_resources.py" \
  "$root/unison-experience-renderer/tests/test_incident_expressions.py" \
  "$root/unison-experience-renderer/tests/test_incident_event_stream.py"

printf 'DJ-1 simulation acceptance passed; no physical-device or participatory claim is made.\n'
