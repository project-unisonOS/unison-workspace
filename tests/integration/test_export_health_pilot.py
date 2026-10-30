"""Synthetic source bytes -> extraction -> brief with durable policy, no model.

Real ASGI routes and encrypted SQLite; HTTP transport is in-process and identity
uses loopback JWKS/introspection. This is not a deployed multi-process pilot.
"""
import base64
import json
import time

import httpx
from test_authenticated_input_boundary import boundary, input_body  # noqa: F401
from test_wellness_storage_journey import storage_api  # noqa: F401
from test_synthetic_wellness import fixture_observations, DAY
from orchestrator.wellness import SyntheticWellnessJourney
from orchestrator.wellness_storage import ExportPilotReader


def test_export_to_brief_with_independent_consent(boundary, storage_api, monkeypatch):
    ingress, headers, _, _ = boundary
    storage, vault = storage_api
    monkeypatch.setenv("UNISON_SYNTHETIC_HEALTH_PILOT", "true")
    control = headers(aud=["storage"], scopes=["storage.import.start", "storage.import.upload",
                      "storage.import.admit", "storage.health.consent", "storage.health.extract", "storage.sources.delete"])
    reader = headers(aud=["storage", "orchestrator"], scopes=["wellness.read", "wellness.present", "storage.health.pilot.read"])
    fields = {"upstream_id", "source", "device", "method", "metric", "kind", "value", "unit", "source_day",
              "original_timezone", "measured_start", "measured_end", "quality", "missing_reason", "revision"}
    sources = []
    for metric in ("sleep_duration", "steps"):
        rows = [{k: v for k, v in row.items() if k in fields} for row in fixture_observations() if row["metric"] == metric]
        payload = {"schema_version": "synthetic-health-export.v1", "synthetic": True, "observations": rows}
        session = vault.post("/v1/imports", headers=control, json={}).json()["session_id"]
        source = vault.post(f"/v1/imports/{session}/sources", headers=control, json={
            "filename": metric+".json", "media_type": "application/json",
            "content_b64": base64.b64encode(json.dumps(payload).encode()).decode()}).json()["source_id"]
        assert vault.post(f"/v1/imports/{session}/admit", headers=control, json={}).status_code == 200
        sources.append(source)
    grant = vault.post("/v1/health-pilot/consents", headers=control, json={"source_ids": sources,
                       "purpose": "wellness.summary", "confirmed": True, "expires_at": time.time()+3600}).json()["grant_id"]
    for source in sources:
        response = vault.post(f"/v1/health-pilot/sources/{source}/extract", headers=control, json={"grant_id": grant})
        assert response.status_code == 200, response.text
    assert storage._domain_store().records("alice") == []  # No manually posted facts.
    calls, revoke_after_read = [], [False]
    def transport(request):
        calls.append(request.url.path)
        response = vault.request(request.method, request.url.raw_path.decode(), headers=dict(request.headers), content=request.content)
        if revoke_after_read[0] and request.url.path.endswith("/records"):
            assert vault.delete(f"/v1/health-pilot/consents/{grant}", headers=control).status_code == 200
        return httpx.Response(response.status_code, content=response.content, headers=dict(response.headers))
    adapter = ExportPilotReader("http://127.0.0.1:19080", grant, transport=httpx.MockTransport(transport))
    ingress.app.state.synthetic_wellness_journey = SyntheticWellnessJourney(reader=adapter, policy=adapter)
    body = {**input_body(), "payload": {"intent": "wellness.daily", "source_day": DAY.isoformat()}}
    response = ingress.post("/input", headers=reader, json=body)
    assert response.status_code == 200, response.text
    brief = response.json()["brief"]
    assert [row["status"] for row in brief["entries"]] == ["changed", "unchanged"]
    assert calls == ["/v1/health-pilot/authorize", "/v1/health-pilot/records", "/v1/health-pilot/authorize"]
    storage._SOURCE_LIBRARY = None
    assert ingress.post("/input", headers=reader, json=body).json()["brief"] == brief
    bob = headers("bob", aud=["storage", "orchestrator"], scopes=["wellness.read", "wellness.present", "storage.health.pilot.read"])
    assert ingress.post("/input", headers=bob, json=body).status_code == 403
    revoke_after_read[0] = True
    denied = ingress.post("/input", headers=reader, json=body)
    assert denied.status_code == 403 and "brief" not in denied.json()
    storage._SOURCE_LIBRARY = None
    assert ingress.post("/input", headers=reader, json=body).status_code == 403
