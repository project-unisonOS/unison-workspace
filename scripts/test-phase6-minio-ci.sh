#!/usr/bin/env bash
set -euo pipefail

# Same upstream release as the development Compose profile. Its public image is
# no longer pullable; verify the official binary's immutable digest before use.
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEST_ROOT="$(mktemp -d "${RUNNER_TEMP:?CI runner temporary directory required}/unison-phase6.XXXXXX")"
MINIO_PID=""
cleanup() {
  if [[ -n "$MINIO_PID" ]]; then
    kill "$MINIO_PID" 2>/dev/null || true
    wait "$MINIO_PID" 2>/dev/null || true
  fi
  cat "$TEST_ROOT/minio.log" 2>/dev/null || true
  rm -rf -- "$TEST_ROOT"
}
trap cleanup EXIT

curl --fail --location --retry 3 \
  'https://github.com/minio/minio/releases/download/RELEASE.2025-07-23T15-54-02Z/minio.linux-amd64.RELEASE.2025-07-23T15-54-02Z' \
  --output "$TEST_ROOT/minio"
printf '%s  %s\n' 'eef6581f6509f43ece007a6f2eb4c5e3ce41498c8956e919a7ac7b4b170fa431' "$TEST_ROOT/minio" | sha256sum --check --strict
chmod 700 "$TEST_ROOT/minio"
MINIO_ROOT_USER=phase6-test-access MINIO_ROOT_PASSWORD=phase6-test-secret-only \
  "$TEST_ROOT/minio" server "$TEST_ROOT/data" --address 127.0.0.1:19000 --console-address 127.0.0.1:19001 \
  >"$TEST_ROOT/minio.log" 2>&1 &
MINIO_PID=$!
for attempt in $(seq 1 30); do
  kill -0 "$MINIO_PID"
  if curl --fail --silent http://127.0.0.1:19000/minio/health/ready >/dev/null; then
    PYTHONPATH="${ROOT_DIR}/unison-common/src:${ROOT_DIR}/unison-storage" \
      "${UNISON_DEV_VENV:-${ROOT_DIR}/.venv}/bin/python" "${ROOT_DIR}/scripts/test-phase6-minio.py"
    exit 0
  fi
  sleep 1
done
echo '[FAIL] Pinned MinIO did not become ready' >&2
exit 1
