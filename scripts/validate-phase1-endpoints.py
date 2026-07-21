#!/usr/bin/env python3
"""Inventory every FastAPI endpoint and verify Phase 1 binding coverage."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "phase1-endpoints.v1.json"
HTTP_METHODS = {"get", "post", "put", "patch", "delete"}
FORBIDDEN_DEFAULTS = ("local-user", "local-person")


def route_decorators(path: Path):
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for decorator in node.decorator_list:
            if not isinstance(decorator, ast.Call) or not isinstance(decorator.func, ast.Attribute):
                continue
            if decorator.func.attr not in HTTP_METHODS or not decorator.args:
                continue
            value = decorator.args[0]
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                yield decorator.func.attr.upper(), value.value, node.name, path


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    report = {"schema_version": 1, "services": [], "totals": {"public": 0, "protected": 0}}
    failures: list[str] = []
    for service in manifest["services"]:
        guard = (ROOT / service["guard_file"]).resolve()
        if not guard.exists():
            if service.get("optional_sibling"):
                report["services"].append({"service": service["service"], "status": "optional-sibling-absent", "public": 0, "protected": 0})
                continue
            failures.append(f"{service['service']}: guard file missing: {guard}")
            continue
        if service["guard_marker"] not in guard.read_text(encoding="utf-8"):
            failures.append(f"{service['service']}: guard marker missing")

        public = set(service.get("public_paths", []))
        prefixes = tuple(service.get("public_prefixes", []))
        routes = []
        source_files: list[Path] = []
        for root_value in service["roots"]:
            source = (ROOT / root_value).resolve()
            if not source.exists():
                if service.get("optional_sibling"):
                    continue
                failures.append(f"{service['service']}: source missing: {source}")
                continue
            source_files.extend(sorted(source.rglob("*.py")) if source.is_dir() else [source])
        for source in source_files:
            text = source.read_text(encoding="utf-8")
            if service["service"] not in {"auth"}:
                for forbidden in FORBIDDEN_DEFAULTS:
                    if re.search(rf"[\"']{re.escape(forbidden)}[\"']", text):
                        failures.append(f"{service['service']}: forbidden identity default {forbidden} in {source}")
            routes.extend(route_decorators(source))

        public_count = sum(1 for _, path, _, _ in routes if path in public or any(path.startswith(prefix) for prefix in prefixes))
        protected_count = len(routes) - public_count
        if protected_count == 0 and service["service"] not in {"capability"}:
            failures.append(f"{service['service']}: no protected endpoint was inventoried")
        report["services"].append({
            "service": service["service"],
            "status": "covered",
            "public": public_count,
            "protected": protected_count,
            "routes": len(routes),
        })
        report["totals"]["public"] += public_count
        report["totals"]["protected"] += protected_count

    print(json.dumps(report, indent=2, sort_keys=True))
    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}", file=sys.stderr)
        return 1
    print("[PASS] Every inventoried protected service has trusted principal enforcement.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
