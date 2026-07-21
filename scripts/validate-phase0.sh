#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}"
PYTHON_BIN="${VENV_DIR}/bin/python"

if [[ ! -x "$PYTHON_BIN" ]]; then
  echo "[FAIL] Development environment missing. Run ./scripts/bootstrap-dev.sh" >&2
  exit 1
fi

echo "[phase0][1/7] development environment"
"$PYTHON_BIN" "${ROOT_DIR}/scripts/validate-dev-environment.py"

echo "[phase0][2/7] component manifest"
"$PYTHON_BIN" "${ROOT_DIR}/scripts/validate-component-manifest.py"

echo "[phase0][3/7] schema authority and JSON schemas"
"$PYTHON_BIN" "${ROOT_DIR}/scripts/validate-schema-manifest.py"

echo "[phase0][4/7] synthetic household fixtures"
"$PYTHON_BIN" "${ROOT_DIR}/scripts/validate-household-fixtures.py"

echo "[phase0][5/7] threat-to-test coverage"
"$PYTHON_BIN" "${ROOT_DIR}/scripts/validate-threat-map.py"

echo "[phase0][6/7] Compose configurations"
docker compose \
  -f "${ROOT_DIR}/unison-devstack/docker-compose.yml" \
  -f "${ROOT_DIR}/unison-devstack/docker-compose.ports.yml" \
  config --quiet

platform_dir="${ROOT_DIR}/../unison-platform"
if [[ -f "${platform_dir}/compose/compose.native.yaml" ]]; then
  docker compose -f "${platform_dir}/compose/compose.native.yaml" config --quiet
else
  echo "[phase0] NOTE: sibling unison-platform not present; native profile check skipped."
fi

echo "[phase0][7/7] shell syntax"
for script in "${ROOT_DIR}"/scripts/*.sh; do
  bash -n "$script"
done

echo "[PASS] Static Phase 0 validation passed."
