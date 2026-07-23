#!/usr/bin/env python3
"""Fail if the Phase 5 channel services publish an appliance host port."""

from __future__ import annotations

import json
import os
# The subprocess module is used only for the fixed Docker Compose CLI below.
import subprocess  # nosec B404
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMPOSE = ROOT / "unison-platform" / "compose" / "compose.yaml"
ENV_FILE = ROOT / "unison-platform" / "config" / "phase5-compose.env"
TARGETS = ("comms", "telegram-channel-worker")


def main() -> None:
    compose_source = COMPOSE.read_text(encoding="utf-8")
    if all(f"  {name}:\n" not in compose_source for name in TARGETS):
        print(json.dumps({
            "scan": "resolved-compose-host-port-exposure",
            "services": {},
            "result": "experimental channel services excluded from default runtime",
        }, indent=2, sort_keys=True))
        print("[PASS] Default appliance runtime excludes Phase 5 channel services.")
        return
    environment = os.environ.copy()
    environment["UNISON_COMPOSE_ENV_FILE"] = str(ENV_FILE)
    # The argv list and paths are repository-owned constants.
    raw = subprocess.run(  # nosec B603
        ["docker", "compose", "-f", str(COMPOSE), "config", "--format", "json"],
        check=True,
        capture_output=True,
        text=True,
        env=environment,
    ).stdout
    services = json.loads(raw)["services"]
    report: dict[str, object] = {"scan": "resolved-compose-host-port-exposure", "services": {}}
    for name in TARGETS:
        service = services[name]
        ports = service.get("ports", [])
        if ports:
            raise SystemExit(f"[FAIL] {name} publishes host ports: {ports}")
        report["services"][name] = {
            "published_host_ports": [],
            "internal_expose": service.get("expose", []),
            "networks": sorted(service.get("networks", {})),
        }
    worker = services["telegram-channel-worker"]
    if worker.get("expose"):
        raise SystemExit("[FAIL] telegram-channel-worker declares a listener")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("[PASS] Phase 5 channel services publish no appliance host ports.")


if __name__ == "__main__":
    main()
