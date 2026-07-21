#!/usr/bin/env python3
"""Validate canonical JSON schemas and explicitly account for legacy drift."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "schemas.v1.json"


def fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    raise SystemExit(1)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON at {path.relative_to(ROOT)}: {exc}")


def main() -> None:
    data = load_json(MANIFEST)
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        fail("schema manifest schema_version must be 1")
    authority = data.get("authority")
    if authority != "unison-common/schemas":
        fail("schema authority must be unison-common/schemas")
    names: set[str] = set()
    canonical_paths: set[str] = set()
    warnings = 0
    for schema in data.get("schemas", []):
        name = schema.get("name")
        canonical = schema.get("canonical")
        if not name or name in names or not canonical or canonical in canonical_paths:
            fail("schema names and canonical paths must be present and unique")
        names.add(name)
        canonical_paths.add(canonical)
        if not canonical.startswith(f"{authority}/"):
            fail(f"canonical schema is outside authority: {canonical}")
        canonical_path = ROOT / canonical
        load_json(canonical_path)
        for legacy in schema.get("legacy_copies", []):
            legacy_path = ROOT / legacy["path"]
            load_json(legacy_path)
            differs = digest(canonical_path) != digest(legacy_path)
            if differs and legacy.get("status") != "migration-required":
                fail(f"undeclared schema drift: {legacy['path']}")
            if differs:
                warnings += 1
                print(f"[WARN] tracked legacy drift: {legacy['path']}")
    disk = {str(path.relative_to(ROOT)).replace('\\', '/') for path in (ROOT / authority).glob("*.json")}
    undeclared = sorted(disk - canonical_paths)
    if undeclared:
        fail(f"canonical schemas missing from manifest: {', '.join(undeclared)}")
    print(f"[PASS] {len(names)} canonical schemas validated; {warnings} tracked migration item(s).")


if __name__ == "__main__":
    main()
