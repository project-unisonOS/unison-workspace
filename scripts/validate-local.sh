#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[1/4] Devstack smoke"
./scripts/smoke.sh

echo "[2/4] Multimodal validation"
python3 unison-devstack/scripts/test_multimodal.py

echo "[3/4] Renderer-led golden-path validation"
python3 unison-devstack/scripts/validate_golden_path.py

echo "[4/4] Journey 6 fake-mail validation"
python3 unison-devstack/scripts/validate_journey6_fake_mail.py

echo "Local validation sequence completed."
