from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "tests/fixtures/semantic-experience/se0-journeys.v1.json"


def test_se0_journeys_are_synthetic_semantic_and_action_complete():
    body = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert body["schema_version"] == "se0-journeys.v1"
    assert body["synthetic_only"] is True
    assert len(body["journeys"]) == 6
    ids = set()
    forbidden = {"click", "button", "screen reader", "screen-reader", "checkbox", "pixel"}
    for journey in body["journeys"]:
        ids.add(journey["journey_id"])
        assert journey["purpose"] and journey["outcome"]
        assert journey["required_meaning"] and journey["exact_content"]
        assert journey["provenance"] and journey["recovery"]
        assert all(action["action_id"] and action["risk"] for action in journey["actions"])
        rendered = json.dumps(journey).lower()
        assert not any(term in rendered for term in forbidden)
    assert len(ids) == 6


def test_semantic_contracts_are_canonical_and_packaged():
    for name in ("semantic-experience.v1.schema.json", "interaction-profile.v1.schema.json"):
        root_schema = ROOT / "unison-common/schemas" / name
        packaged_schema = ROOT / "unison-common/src/unison_common/schemas" / name
        assert root_schema.read_bytes() == packaged_schema.read_bytes()

