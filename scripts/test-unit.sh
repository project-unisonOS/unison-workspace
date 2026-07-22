#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}"
PYTHON_BIN="${VENV_DIR}/bin/python"

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "[FAIL] Development environment missing. Run ./scripts/bootstrap-dev.sh" >&2
  exit 1
fi

repos=(
  unison-common
  unison-auth
  unison-consent
  unison-context
  unison-storage
  unison-policy
  unison-comms
  unison-experience-renderer
  unison-capability
  unison-inference
  unison-payments
  unison-orchestrator
)

test_root="$(mktemp -d)"
cleanup() {
  rm -rf -- "$test_root"
}
trap cleanup EXIT

failures=()
for repo in "${repos[@]}"; do
  echo "[unit] $repo"
  otel_sdk_disabled=true
  if [[ "$repo" == "unison-common" ]]; then
    # The common suite exercises real in-process span creation and propagation.
    # Export remains disabled below, so this does not send test telemetry.
    otel_sdk_disabled=false
  fi
  if ! (
    cd "${ROOT_DIR}/${repo}"
    env \
      PYTHONDONTWRITEBYTECODE=1 \
      PYTHONPATH="${ROOT_DIR}/${repo}/src:${ROOT_DIR}/unison-common/src${PYTHONPATH:+:${PYTHONPATH}}" \
      OTEL_SDK_DISABLED="$otel_sdk_disabled" \
      UNISON_DISABLE_OTEL_EXPORTER=true \
      OTEL_TRACES_EXPORTER=none \
      OTEL_METRICS_EXPORTER=none \
      OTEL_LOGS_EXPORTER=none \
      UNISON_CONSENT_KEYS_DIR="${test_root}/consent-keys" \
      UNISON_AUTH_KEYS_DIR="${test_root}/auth-keys" \
      UNISON_AUTH_IDENTITY_DATABASE_PATH="${test_root}/${repo}-identity.db" \
      UNISON_PRINCIPAL_BINDING_TEST_BYPASS=true \
      DISABLE_AUTH_FOR_TESTS=true \
      "$PYTHON_BIN" -m pytest tests -q -p no:cacheprovider
  ); then
    failures+=("$repo")
  fi
done

if ((${#failures[@]})); then
  echo "[FAIL] Unit suites failed: ${failures[*]}" >&2
  exit 1
fi

echo "[PASS] Core Phase 0 unit suites passed."
