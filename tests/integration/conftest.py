"""Explicit component roots for isolated cross-component tests."""
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
ORCHESTRATOR = Path(os.getenv("UNISON_TEST_ORCHESTRATOR_ROOT", str(ROOT / "unison-orchestrator"))).resolve()
STORAGE = Path(os.getenv("UNISON_TEST_STORAGE_ROOT", str(ROOT / "unison-storage"))).resolve()
COMMON = Path(os.getenv("UNISON_TEST_COMMON_ROOT", str(ROOT / "unison-common"))).resolve()
for path in (COMMON / "src", STORAGE / "src", ORCHESTRATOR / "src", ORCHESTRATOR / "tests"):
    sys.path.insert(0, str(path))
