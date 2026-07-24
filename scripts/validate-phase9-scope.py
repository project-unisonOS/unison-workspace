#!/usr/bin/env python3
"""Validate the locked Phase 9 lifecycle and artifact authority."""

import json
import subprocess  # nosec B404
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"[FAIL] {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    data = json.loads((ROOT / "manifests/appliance-lifecycle.v1.json").read_text())
    if data.get("schema_version") != 1 or data.get("status") != "phase9-scope-locked":
        fail("lifecycle contract must be locked v1")
    expected = {
        "artifact": "signed-native-installation-bundle",
        "operating_system": "Ubuntu 24.04 LTS",
        "architecture": "x86_64",
        "boot": "UEFI",
    }
    for key, value in expected.items():
        if data.get("supported_target", {}).get(key) != value:
            fail(f"supported target {key} must be {value}")
    if data["runtime_profile"].get("mutable_tags_allowed") is not False:
        fail("supported runtime must prohibit mutable tags")
    entrypoint = ROOT / data["runtime_profile"].get("compose_entrypoint", "")
    if entrypoint.name != "compose.supported.yaml" or not entrypoint.is_file():
        fail("supported runtime must use the constrained Compose entrypoint")
    subprocess.run(  # nosec B603
        [str(ROOT / "unison-platform/scripts/validate-supported-runtime.py")],
        check=True,
    )
    subprocess.run(  # nosec B603
        [str(ROOT / "unison-platform/scripts/test_supported_manifest.py")],
        check=True,
    )
    for test in (
        "test_installer_preflight.py",
        "test_installer_transactions.py",
        "test_supported_bundle.py",
    ):
        subprocess.run(  # nosec B603
            [str(ROOT / "unison-platform/scripts" / test)],
            check=True,
        )
    subprocess.run(  # nosec B603
        [
            sys.executable,
            str(ROOT / "unison-updates/scripts/test_trusted_metadata.py"),
        ],
        check=True,
    )
    if data["product_profile"].get("default_telemetry") != "off":
        fail("telemetry must default off")
    if data["update_authority"].get("metadata_framework") != "TUF":
        fail("TUF must own update metadata")
    if data["update_authority"].get("irreversible_stable_migrations") is not False:
        fail("stable releases must prohibit irreversible migrations")
    modules = (ROOT / ".gitmodules").read_text()
    for repository in ("unison-platform", "unison-updates"):
        if f"path = {repository}" not in modules:
            fail(f"{repository} must be a submodule")
        result = subprocess.run(  # nosec B603
            ["git", "-C", str(ROOT / repository), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True
        )
        if len(result.stdout.strip()) != 40:
            fail(f"{repository} must resolve to an immutable commit")
    print("[PASS] Phase 9 lifecycle authority and supported target are locked.")


if __name__ == "__main__":
    main()
