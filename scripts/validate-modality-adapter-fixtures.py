#!/usr/bin/env python3
"""Exercise accepted and rejected modality adapter fixtures."""
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
validator = root / "scripts/validate-modality-adapter.py"
valid = root / "tests/fixtures/modality-adapter.valid.json"
forbidden = root / "tests/fixtures/modality-adapter.forbidden.json"
subprocess.run([sys.executable, str(validator), str(valid)], check=True)
denied = subprocess.run([sys.executable, str(validator), str(forbidden)], capture_output=True, text=True)
assert denied.returncode != 0
assert "unknown=['consent']" in denied.stderr
print("validated modality adapter authority boundary")
