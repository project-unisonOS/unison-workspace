"""Actual authenticated ASGI routes + encrypted storage; controlled policy.

No operational runtime, wearable, model or real records. This is explicitly
in-process integration with a loopback JWKS/introspection service.
"""
import base64
import importlib.util
import json
from pathlib import Path

import httpx
import pytest
from cryptography.fernet import Fernet
from fastapi.testclient import TestClient

from conftest import STORAGE
from test_authenticated_input_boundary import boundary, input_body  # noqa: F401
from test_synthetic_wellness import fixture_observations, DAY, ControlledPolicy
from orchestrator.wellness import SyntheticWellnessJourney
from orchestrator.wellness_storage import DomainObservationReader


@pytest.fixture
def storage_api(boundary, monkeypatch, tmp_path):
    monkeypatch.setenv("ENVIRONMENT", "test")
    monkeypatch.setenv("STORAGE_OBJECT_ENC_KEY", Fernet.generate_key().decode())
    monkeypatch.setenv("UNISON_LIFE_OPERATIONS_ROOT", str(tmp_path / "sources"))
    monkeypatch.setenv("UNISON_LIFE_DOMAINS_ROOT", str(tmp_path / "domains"))
    monkeypatch.setenv("UNISON_INCIDENTS_ROOT", str(tmp_path / "incidents"))
    monkeypatch.setenv("UNISON_STORAGE_DB", str(tmp_path / "ordinary.db"))
    spec = importlib.util.spec_from_file_location("synthetic_storage_api", STORAGE / "src" / "server.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with TestClient(module.app) as client:
        yield module, client


def test_authenticated_brief_from_encrypted_sources_restart_delete_and_revoke(boundary, storage_api, tmp_path):
    ingress, headers, revoked, _ = boundary
    storage, vault = storage_api
    read_scopes = ["wellness.read", "wellness.present", "storage.health.read"]
    authority = headers(aud=["orchestrator", "storage"], scopes=read_scopes)
    bob = headers("bob", aud=["orchestrator", "storage"], scopes=read_scopes)
    ingest_scopes = ["storage.import.start", "storage.import.upload", "storage.import.admit",
                     "storage.domain.create", "storage.sources.read", "storage.sources.delete"]
    ingest = headers(aud=["storage"], scopes=ingest_scopes, jti="ingest-alice")
    bob_sources = headers("bob", aud=["storage"], scopes=["storage.sources.read", "storage.sources.delete"])
    fixtures = fixture_observations()
    source_ids = {}
    for metric in ("sleep_duration", "steps"):
        batch = [item for item in fixtures if item["metric"] == metric]
        raw = json.dumps({"synthetic": True, "observations": batch}).encode()
        started = vault.post("/v1/imports", json={}, headers=ingest)
        assert started.status_code == 200
        session = started.json()["session_id"]
        source = vault.post(f"/v1/imports/{session}/sources", headers=ingest, json={
            "filename": metric + ".json", "media_type": "application/json",
            "content_b64": base64.b64encode(raw).decode()})
        assert source.status_code == 200
        source_id = source.json()["source_id"]
        source_ids[metric] = source_id
        assert vault.post(f"/v1/imports/{session}/admit", json={}, headers=ingest).status_code == 200
        # Manually associated facts, not extraction or verified source-byte
        # provenance. Storage validates reference ownership/admission, not that
        # these manually supplied facts were extracted from the original bytes.
        for item in batch:
            item["source_record_id"] = source_id
            created = vault.post("/v1/domain/records", headers=ingest, json={
                "domain": "health", "record_type": "wearable-observation", "facts": item,
                "source_ids": [source_id]})
            assert created.status_code == 200
    # Exercise implemented routes with positive controls. No HTTP export route
    # exists; a 404 on a guessed export URL proves nothing about isolation.
    owner_sources = vault.get("/v1/sources", headers=ingest)
    assert owner_sources.status_code == 200
    assert {item["source_id"] for item in owner_sources.json()["sources"]} == set(source_ids.values())
    other_sources = vault.get("/v1/sources", headers=bob_sources)
    assert other_sources.status_code == 200 and other_sources.json()["sources"] == []
    assert vault.delete(f"/v1/sources/{source_ids['sleep_duration']}", headers=bob_sources).status_code == 404
    assert vault.get("/v1/sources", headers=ingest).json() == owner_sources.json()
    assert vault.post("/v1/imports", headers=authority, json={}).status_code == 403
    assert vault.post("/v1/domain/records", headers=authority, json={}).status_code == 403
    assert vault.delete(f"/v1/sources/{source_ids['sleep_duration']}", headers=authority).status_code == 403
    assert vault.get("/v1/domain/records?domain=health", headers=ingest).status_code == 403

    reads = []
    def storage_transport(request):
        reads.append(request.url.path)
        response = vault.request(request.method, request.url.raw_path.decode(), headers=dict(request.headers))
        return httpx.Response(response.status_code, content=response.content, headers=dict(response.headers))
    policy = ControlledPolicy()
    reader = DomainObservationReader("http://127.0.0.1:19080", transport=httpx.MockTransport(storage_transport))
    ingress.app.state.synthetic_wellness_journey = SyntheticWellnessJourney(reader=reader, policy=policy)
    body = {**input_body(), "payload": {"intent": "wellness.daily", "source_day": DAY.isoformat()}}
    response = ingress.post("/input", json=body, headers=authority)
    assert response.status_code == 200, response.text
    brief = response.json()["brief"]
    assert [entry["status"] for entry in brief["entries"]] == ["changed", "unchanged"]
    assert brief["entries"][0]["source_ids"] == [source_ids["sleep_duration"]] * 4
    assert policy.calls == [("wellness.read", "alice"), ("wellness.present", "alice")]
    assert len(reads) == 1

    # Reopen the real encrypted stores, not an in-memory substitute.
    storage._DOMAIN_STORE = None
    storage._SOURCE_LIBRARY = None
    assert ingress.post("/input", json=body, headers=authority).json()["brief"] == brief
    other = ingress.post("/input", json=body, headers=bob)
    assert other.status_code == 200
    assert other.json()["brief"]["retained_observations"] == 0
    assert all(item["status"] == "unknown" for item in other.json()["brief"]["entries"])
    for path in (tmp_path / "sources").rglob("*"):
        if path.is_file():
            assert b"synthetic-ring" not in path.read_bytes()
    for path in (tmp_path / "domains").rglob("*"):
        if path.is_file():
            assert b"synthetic-ring" not in path.read_bytes()

    # This verifies ordinary cascade behavior, not cross-database crash atomicity.
    assert vault.delete(f"/v1/sources/{source_ids['sleep_duration']}", headers=ingest).status_code == 200
    after_delete = ingress.post("/input", json=body, headers=authority).json()["brief"]
    assert [item["status"] for item in after_delete["entries"]] == ["unknown", "unchanged"]
    prior_reads = len(reads)
    policy.denied = "wellness.read"
    assert ingress.post("/input", json=body, headers=authority).status_code == 403
    assert len(reads) == prior_reads
    policy.denied = None
    revoked.add("session-alice")
    assert ingress.post("/input", json=body, headers=authority).status_code == 403
    assert vault.get("/v1/domain/records?domain=health", headers=authority).status_code == 403
    assert vault.get("/v1/sources", headers=authority).status_code == 403
    assert len(reads) == prior_reads
