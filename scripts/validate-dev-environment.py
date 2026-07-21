#!/usr/bin/env python3
"""Validate the deterministic Phase 0 Python development profile."""

from __future__ import annotations

import importlib
import json
import platform
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_IMPORTS = {
    "bcrypt": "bcrypt",
    "cryptography": "cryptography",
    "fastapi": "fastapi",
    "httpx": "httpx",
    "jose": "python-jose",
    "neo4j": "neo4j",
    "passlib": "passlib",
    "pydantic": "pydantic",
    "pytest": "pytest",
    "redis": "redis",
    "schedule": "schedule",
    "sqlalchemy": "SQLAlchemy",
    "unison_common": "unison-common",
    "yaml": "PyYAML",
}


def fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    if sys.version_info[:2] != (3, 12):
        fail(f"Python 3.12 required; found {platform.python_version()}")

    missing = []
    for module, package in REQUIRED_IMPORTS.items():
        try:
            importlib.import_module(module)
        except Exception as exc:  # pragma: no cover - diagnostic path
            missing.append({"module": module, "package": package, "error": str(exc)})

    if missing:
        print(json.dumps({"missing": missing}, indent=2), file=sys.stderr)
        fail("development environment is incomplete")

    expected = [
        ROOT / "requirements-dev.lock",
        ROOT / "manifests" / "components.v1.json",
        ROOT / "manifests" / "schemas.v1.json",
        ROOT / "tests" / "fixtures" / "household" / "two-adults.v1.json",
        ROOT / "tests" / "security" / "phase0-boundary-test-map.json",
    ]
    absent = [str(path.relative_to(ROOT)) for path in expected if not path.is_file()]
    if absent:
        fail(f"missing Phase 0 files: {', '.join(absent)}")

    print(
        json.dumps(
            {
                "status": "ok",
                "python": platform.python_version(),
                "platform": platform.platform(),
                "workspace": str(ROOT),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
