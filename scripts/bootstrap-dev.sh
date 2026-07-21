#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}"
PYTHON_BIN="${UNISON_PYTHON:-python3}"

if [[ "$(uname -s)" != "Linux" ]]; then
  echo "[FAIL] Run the authoritative bootstrap in Linux or WSL2." >&2
  exit 1
fi

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "[FAIL] Python command not found: $PYTHON_BIN" >&2
  exit 1
fi

python_version="$($PYTHON_BIN -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
if [[ "$python_version" != "3.12" ]]; then
  echo "[FAIL] Python 3.12 is required for the Phase 0 profile; found $python_version." >&2
  exit 1
fi

required_submodules=(
  unison-common unison-auth unison-consent unison-context unison-policy
  unison-storage unison-orchestrator unison-experience-renderer
)
for repo in "${required_submodules[@]}"; do
  if [[ ! -d "${ROOT_DIR}/${repo}" ]]; then
    echo "[FAIL] Missing required submodule: $repo" >&2
    echo "       Run: git submodule update --init --recursive" >&2
    exit 1
  fi
done

echo "[bootstrap] creating/updating ${VENV_DIR}"
"$PYTHON_BIN" -m venv "$VENV_DIR"
"${VENV_DIR}/bin/python" -m pip install --upgrade \
  pip==26.1.2 setuptools==83.0.0 wheel==0.47.0
"${VENV_DIR}/bin/python" -m pip install --requirement "${ROOT_DIR}/requirements-dev.lock"
site_packages="$("${VENV_DIR}/bin/python" -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"
printf '%s\n' "${ROOT_DIR}/unison-common/src" > "${site_packages}/unison-common-workspace.pth"

"${VENV_DIR}/bin/python" "${ROOT_DIR}/scripts/validate-dev-environment.py"

echo "[PASS] Phase 0 development environment is ready."
echo "       Run: ./scripts/test-unit.sh"
echo "       Run: ./scripts/validate-phase0.sh"
