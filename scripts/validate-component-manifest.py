#!/usr/bin/env python3
"""Validate the Phase 0 component inventory and topology mapping."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "components.v1.json"
ALLOWED_CHECKOUTS = {"root", "submodule", "sibling"}
ALLOWED_DISPOSITIONS = {"retain", "consolidate", "replace", "defer", "archive"}
ALLOWED_MATURITY = {"implemented", "experimental", "scaffold", "research", "legacy"}
REQUIRED = {"id", "repository", "checkout", "current_role", "target_boundary", "disposition", "default_appliance", "maturity"}


def fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        fail("component manifest schema_version must be 1")
    if not data.get("default_code_owner") or not data.get("data_authority_policy"):
        fail("component manifest must define code and data authority ownership")
    components = data.get("components")
    if not isinstance(components, list) or not components:
        fail("component manifest must contain components")
    ids: set[str] = set()
    repositories: set[str] = set()
    for index, component in enumerate(components):
        missing = REQUIRED - component.keys()
        if missing:
            fail(f"component {index} missing: {', '.join(sorted(missing))}")
        if component["id"] in ids or component["repository"] in repositories:
            fail(f"duplicate component id or repository: {component['id']}")
        ids.add(component["id"])
        repositories.add(component["repository"])
        if component["checkout"] not in ALLOWED_CHECKOUTS:
            fail(f"invalid checkout for {component['id']}")
        if component["disposition"] not in ALLOWED_DISPOSITIONS:
            fail(f"invalid disposition for {component['id']}")
        if component["maturity"] not in ALLOWED_MATURITY:
            fail(f"invalid maturity for {component['id']}")
        if not isinstance(component["default_appliance"], bool):
            fail(f"default_appliance must be boolean for {component['id']}")
        path = ROOT if component["checkout"] == "root" else ROOT / component["repository"]
        if component["checkout"] == "sibling":
            path = ROOT.parent / component["repository"]
        if not path.is_dir():
            fail(f"declared checkout is absent: {component['repository']}")
    for profile in data.get("runtime_profiles", []):
        compose_files = [ROOT / item for item in profile.get("compose_files", [])]
        if any(not path.is_file() for path in compose_files):
            print(f"[NOTE] runtime profile unavailable in this checkout: {profile['name']}")
            continue
        command = ["docker", "compose"]
        for path in compose_files:
            command.extend(["-f", str(path)])
        command.extend(["config", "--services"])
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        services = [line for line in result.stdout.splitlines() if line]
        if len(services) != profile.get("service_count"):
            fail(f"runtime profile service drift for {profile['name']}: expected {profile.get('service_count')}, found {len(services)}")
    print(f"[PASS] {len(components)} component records map to the approved topology.")


if __name__ == "__main__":
    main()
