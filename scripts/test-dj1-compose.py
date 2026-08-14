#!/usr/bin/env python3
"""Exercise DJ-1 across real containers, including renderer loss and replay."""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
COMPOSE = ["docker", "compose", "-f", str(ROOT / "compose.dj1.yml")]
BASE = "http://127.0.0.1:18080"


def compose(*args: str) -> None:
    subprocess.run([*COMPOSE, *args], cwd=ROOT, check=True)


def request(path: str, payload: dict | None = None) -> dict:
    body = None if payload is None else json.dumps(payload).encode()
    req = Request(BASE + path, data=body, headers={"Content-Type": "application/json"}, method="GET" if body is None else "POST")
    with urlopen(req, timeout=20) as response:  # nosec B310 - fixed loopback acceptance endpoint
        return json.load(response)


def wait_ready(url: str = BASE + "/health") -> None:
    for _ in range(60):
        try:
            with urlopen(url, timeout=5):  # nosec B310 - fixed loopback acceptance endpoint
                pass
            return
        except (URLError, TimeoutError, ConnectionError, OSError):
            time.sleep(1)
    raise RuntimeError("orchestrator did not become healthy")


def main() -> None:
    fixture = json.loads((ROOT / "tests/fixtures/dj1/water-leak-simulation.json").read_text())
    compose("down", "--volumes", "--remove-orphans")
    try:
        compose("up", "--detach", "--build")
        wait_ready()
        normal = request("/v1/incidents/simulations/water-leak", fixture)
        assert normal["renderer_delivered"] is True
        assert normal["evidence_class"] == "simulation"

        compose("stop", "renderer")
        degraded = json.loads(json.dumps(fixture))
        degraded["observation"]["observation_id"] = "observation-water-2"
        degraded["observation"]["source_sequence"] = 2
        partial = request("/v1/incidents/simulations/water-leak", degraded)
        assert partial["renderer_delivered"] is False
        assert partial["incident"]["state"] == "action-needed"

        compose("start", "renderer")
        wait_ready("http://127.0.0.1:18092/health")
        replay = request("/v1/incidents/delivery/retry", {})
        assert replay == {"delivered": 1, "remaining": 0, "evidence_class": "simulation"}
        print(json.dumps({"normal": normal, "renderer_loss": partial, "replay": replay}, indent=2))
        print("DJ-1 container acceptance passed; simulation evidence only.")
    finally:
        if "--keep" not in sys.argv:
            compose("down", "--volumes", "--remove-orphans")


if __name__ == "__main__":
    main()
