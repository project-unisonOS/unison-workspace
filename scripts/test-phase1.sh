#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PYTHON_BIN="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python"
TEST_ROOT="$(mktemp -d)"
trap 'rm -rf -- "$TEST_ROOT"' EXIT

common_env=(
  PYTHONDONTWRITEBYTECODE=1
  PYTHONPATH="${ROOT_DIR}/unison-common/src"
  OTEL_SDK_DISABLED=true
  UNISON_DISABLE_OTEL_EXPORTER=true
  OTEL_TRACES_EXPORTER=none
  UNISON_AUTH_KEYS_DIR="${TEST_ROOT}/auth-keys"
  UNISON_AUTH_IDENTITY_DATABASE_PATH="${TEST_ROOT}/identity.db"
)

"${PYTHON_BIN}" "${ROOT_DIR}/scripts/validate-phase1-endpoints.py"
"${PYTHON_BIN}" "${ROOT_DIR}/scripts/validate-phase1-product-profile.py"

env "${common_env[@]}" "${PYTHON_BIN}" -m pytest -q -p no:cacheprovider \
  "${ROOT_DIR}/unison-common/tests/test_principal.py" \
  "${ROOT_DIR}/unison-common/tests/test_principal_middleware.py" \
  "${ROOT_DIR}/unison-common/tests/test_trust.py" \
  "${ROOT_DIR}/unison-auth/tests/test_identity_store.py" \
  "${ROOT_DIR}/unison-auth/tests/test_phase1_api.py" \
  "${ROOT_DIR}/unison-experience-renderer/tests/test_phase1_enrollment_accessibility.py" \
  "${ROOT_DIR}/tests/security/test_phase1_boundaries.py"

for sibling in unison-comms unison-capability unison-actuation; do
  sibling_root="${ROOT_DIR}/../${sibling}"
  if [[ -d "${sibling_root}/tests" ]]; then
    sibling_env=(UNISON_PRINCIPAL_BINDING_TEST_BYPASS=true)
    if [[ "${sibling}" == "unison-comms" ]]; then
      sibling_env+=(DISABLE_AUTH_FOR_TESTS=true)
    fi
    case "${sibling}" in
      unison-comms) sibling_tests=(tests/test_phase1_partitioning.py tests/test_gmail_contract.py) ;;
      unison-capability) sibling_tests=(tests/test_api_authz.py tests/test_audit_redaction.py) ;;
      unison-actuation) sibling_tests=(tests/test_auth.py) ;;
    esac
    env "${common_env[@]}" \
      PYTHONPATH="${sibling_root}/src:${ROOT_DIR}/unison-common/src" \
      "${sibling_env[@]}" \
      "${PYTHON_BIN}" -m pytest -q -p no:cacheprovider "${sibling_tests[@]/#/${sibling_root}/}"
  fi
done

if rg -n -g '*.py' '"(local-user|local-person)"' \
  "${ROOT_DIR}/unison-orchestrator/src" \
  "${ROOT_DIR}/unison-context/src" \
  "${ROOT_DIR}/unison-storage/src" \
  "${ROOT_DIR}/unison-experience-renderer/src"; then
  echo "[FAIL] caller authority fallback remains in a protected production path" >&2
  exit 1
fi

for sibling_src in "${ROOT_DIR}/../unison-comms/src" "${ROOT_DIR}/../unison-capability/src" "${ROOT_DIR}/../unison-actuation/src"; do
  if [[ -d "${sibling_src}" ]] && rg -n -g '*.py' '"(local-user|local-person)"' "${sibling_src}"; then
    echo "[FAIL] caller authority fallback remains in ${sibling_src}" >&2
    exit 1
  fi
done

echo "[PASS] Phase 1 trusted-principal boundary suite passed."
