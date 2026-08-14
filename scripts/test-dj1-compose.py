#!/usr/bin/env python3
"""Exercise DJ-1 across real containers, including renderer loss and replay."""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
COMPOSE = ["docker", "compose", "-f", str(ROOT / "compose.dj1.yml")]
BASE = "http://127.0.0.1:18080"
AUTH_BASE = "http://127.0.0.1:18088"


def compose(*args: str) -> None:
    subprocess.run([*COMPOSE, *args], cwd=ROOT, check=True)


def request(path: str, payload: dict | None = None, *, token: str | None = None) -> dict:
    body = None if payload is None else json.dumps(payload).encode()
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(BASE + path, data=body, headers=headers, method="GET" if body is None else "POST")
    with urlopen(req, timeout=20) as response:  # nosec B310 - fixed loopback acceptance endpoint
        return json.load(response)


def auth_request(path: str, payload: dict, *, bootstrap: bool = False, form: bool = False) -> dict:
    headers = {"Content-Type": "application/x-www-form-urlencoded" if form else "application/json"}
    if bootstrap:
        headers["X-Unison-Bootstrap-Token"] = "dj1-bootstrap-token"
    body = urlencode(payload).encode() if form else json.dumps(payload).encode()
    req = Request(AUTH_BASE + path, data=body, headers=headers, method="POST")
    with urlopen(req, timeout=20) as response:  # nosec B310 - fixed loopback acceptance endpoint
        return json.load(response)


def expect_status(status: int, action) -> None:
    try:
        action()
    except HTTPError as exc:
        assert exc.code == status, f"expected HTTP {status}, received {exc.code}"
    else:
        raise AssertionError(f"expected HTTP {status}")


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
        identity = auth_request("/bootstrap/admin", {
            "username": "dj1-operator",
            "display_name": "DJ-1 Operator",
            "household_name": "DJ-1 Household",
            "password": "DJ1-Integration-Only-7!",
            "confirmed": True,
        }, bootstrap=True)
        issued = auth_request("/token", {
            "username": "dj1-operator",
            "password": "DJ1-Integration-Only-7!",
            "grant_type": "password",
        }, form=True)
        token = issued["access_token"]
        fixture["person_id"] = identity["person_id"]
        fixture["assistant_instance_id"] = identity["assistant_instance_id"]
        fixture["household_id"] = identity["household_id"]

        expect_status(401, lambda: request("/v1/incidents/simulations/water-leak", fixture))
        forged = json.loads(json.dumps(fixture))
        forged["person_id"] = "person-forged"
        expect_status(403, lambda: request("/v1/incidents/simulations/water-leak", forged, token=token))

        normal = request("/v1/incidents/simulations/water-leak", fixture, token=token)
        assert normal["renderer_delivered"] is True
        assert normal["evidence_class"] == "simulation"

        compose("stop", "renderer")
        degraded = json.loads(json.dumps(fixture))
        degraded["observation"]["observation_id"] = "observation-water-2"
        degraded["observation"]["source_sequence"] = 3
        partial = request("/v1/incidents/simulations/water-leak", degraded, token=token)
        assert partial["renderer_delivered"] is False
        assert partial["incident"]["state"] == "action-needed"

        compose("start", "renderer")
        wait_ready("http://127.0.0.1:18092/health")
        replay = request("/v1/incidents/delivery/retry", {}, token=token)
        assert replay == {"delivered": 1, "remaining": 0, "evidence_class": "simulation"}

        compose("stop", "auth")
        unavailable = json.loads(json.dumps(fixture))
        unavailable["observation"]["observation_id"] = "observation-auth-outage"
        unavailable["observation"]["source_sequence"] = 4
        expect_status(403, lambda: request("/v1/incidents/simulations/water-leak", unavailable, token=token))
        print(json.dumps({"principal": identity, "normal": normal, "renderer_loss": partial, "replay": replay}, indent=2))
        print("DJ-1 authenticated container acceptance passed; simulation evidence only.")
    finally:
        if "--keep" not in sys.argv:
            compose("down", "--volumes", "--remove-orphans")


if __name__ == "__main__":
    main()
