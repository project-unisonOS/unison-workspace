#!/usr/bin/env python3
"""Validate the model-independent DJ-0 fixture and gate package."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "dj0" / "dj0-fixtures.v1.json"
GATES_PATH = ROOT / "tests" / "fixtures" / "dj0" / "dj0-gates.v1.json"


class FixtureError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FixtureError(message)


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    require(isinstance(value, dict), f"{path.name} must contain one JSON object")
    return value


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def validate_contracts(package: dict[str, Any]) -> set[str]:
    contracts = package.get("contracts", [])
    require(len(contracts) == 10, "DJ-0 must declare exactly ten contract candidates")
    names = [item.get("name") for item in contracts]
    require(len(names) == len(set(names)), "contract candidate names must be unique")
    for contract in contracts:
        require(contract.get("schema_version") == "contract-candidate.v1", "invalid contract candidate version")
        require(contract.get("proposed_owner"), f"{contract.get('name')} has no proposed owner")
        fields = contract.get("required_fields", [])
        require(fields and len(fields) == len(set(fields)), f"{contract.get('name')} fields must be unique")
    return set(names)


def validate_water(water: dict[str, Any]) -> None:
    require(water.get("execution_mode") == "fully-local-simulation", "water journey must remain a simulation")
    require(water.get("external_network_required") is False, "water journey must not require external network")
    require(water.get("physical_actuation_allowed") is False, "water journey must prohibit physical actuation")
    people = water.get("people", [])
    ids = {person.get("person_id") for person in people}
    require(ids == {"person-alex", "person-jordan"}, "water fixture must contain only Alex and Jordan")
    shared = water.get("shared_space", {})
    require(set(shared.get("members", [])) == ids, "incident membership must match fixture people")
    require("private-health" in shared.get("prohibited_data_classes", []), "health data must be excluded")
    require("private-finance" in shared.get("prohibited_data_classes", []), "finance data must be excluded")

    observations = water.get("sensor", {}).get("observations", [])
    sequences = [item.get("source_sequence") for item in observations]
    require(sequences == sorted(sequences), "sensor observations must be ordered")
    require(len(sequences) == len(set(sequences)), "sensor source sequences must be unique")
    for observation in observations:
        require(0 <= observation.get("confidence", -1) <= 1, "sensor confidence must be between zero and one")
        require(parse_time(observation["observed_at"]) <= parse_time(observation["received_at"]), "sensor receipt predates observation")
        require(parse_time(observation["received_at"]) <= parse_time(observation["fresh_until"]), "sensor observation is stale on receipt")

    pack = water.get("knowledge_pack", {})
    require(pack.get("signature_state") == "fixture-only", "DJ-0 knowledge pack must not claim a release signature")
    require("not-for-real-use" in pack.get("authority", ""), "fixture authority must deny real-world use")
    require(pack.get("stop_rules"), "offline pack requires stop rules")
    require(pack.get("procedures"), "offline pack requires a procedure")

    expression_modalities = {item.get("modality") for item in water.get("expected_expressions", [])}
    require(expression_modalities == {"braille", "visual"}, "water fixture requires Braille and visual expectations")
    cases = {item.get("case_id") for item in water.get("test_cases", [])}
    required_cases = {
        "water-primary-offline",
        "water-no-model",
        "water-electrical-stop",
        "water-duplicate-event",
        "water-braille-unavailable",
        "water-unauthorized-person",
    }
    require(required_cases.issubset(cases), "water fixture is missing required failure cases")


def validate_health_finance(journey: dict[str, Any]) -> None:
    require(journey.get("execution_mode") == "fully-local-synthetic", "health/finance journey must remain synthetic")
    require(journey.get("external_network_required") is False, "health/finance journey must not require external network")
    require(journey.get("person", {}).get("person_id") == "person-morgan", "health/finance fixture must use Morgan")

    sources = journey.get("sources", [])
    source_ids = [item.get("source_id") for item in sources]
    require(len(source_ids) == len(set(source_ids)), "source identifiers must be unique")
    domains = {item.get("domain") for item in sources}
    require({"health", "insurance", "finance", "schedule-transport"}.issubset(domains), "required source domains are missing")

    view = journey.get("cross_domain_view", {})
    require(view.get("person_id") == "person-morgan", "cross-domain view owner mismatch")
    require(parse_time(view["created_at"]) < parse_time(view["expires_at"]), "cross-domain view must expire")
    require(view.get("output_policy") == "private-derived-artifacts-only", "cross-domain output must remain private")
    require(set(view.get("source_revisions", {})) == set(source_ids), "view must pin every source revision")
    selected = {field for fields in view.get("selected_fields", {}).values() for field in fields}
    excluded = set(view.get("excluded_fields", []))
    require(selected.isdisjoint(excluded), "selected and excluded fields overlap")
    require({"account_numbers", "merchant_history", "unrelated_transactions"}.issubset(excluded), "financial minimization fields are missing")

    evidence_states = {item.get("state") for item in journey.get("expected_evidence", [])}
    require({"stale", "unconfirmed", "missing"}.issubset(evidence_states), "uncertain insurance evidence states are incomplete")
    for scenario in journey.get("expected_cost_scenarios", []):
        require(scenario.get("not_a_guarantee") is True, "cost scenarios must deny guarantee")
        require(scenario.get("amount_low") <= scenario.get("amount_high"), "cost scenario range is inverted")
        require(scenario.get("calculation_rule") and scenario.get("source_ids"), "cost scenario lacks reproducible inputs")

    for artifact in journey.get("expected_artifacts", []):
        require(artifact.get("person_id") == "person-morgan", "artifact owner mismatch")
        require(artifact.get("disclosure_state") == "private-not-sent", "DJ-0 artifacts must remain unsent")
        require(artifact.get("recompute_on_change") is True, "derived artifact must invalidate on change")
        require(artifact.get("view_id") == view.get("view_id"), "artifact must identify its temporary view")

    modalities = {item.get("modality") for item in journey.get("expected_expressions", [])}
    require(modalities == {"conversation", "visual"}, "health/finance fixture requires conversation and visual expectations")
    cases = {item.get("case_id") for item in journey.get("test_cases", [])}
    required_cases = {
        "health-finance-primary-local",
        "health-finance-no-finance",
        "health-finance-no-model",
        "health-finance-urgent-language",
        "health-finance-correction",
        "health-finance-outsider",
    }
    require(required_cases.issubset(cases), "health/finance fixture is missing required failure cases")


def validate_gates(gates: dict[str, Any], journey_ids: set[str]) -> None:
    require(gates.get("schema_version") == "dj0-gate-matrix.v1", "invalid DJ-0 gate matrix version")
    require(gates.get("truth_label") == "simulation", "gate matrix must remain simulation")
    require(gates.get("contains_real_personal_data") is False, "gate matrix cannot contain real personal data")
    items = gates.get("gates", [])
    gate_ids = [item.get("gate_id") for item in items]
    require(len(items) >= 12 and len(gate_ids) == len(set(gate_ids)), "DJ-0 requires twelve unique gates")
    categories = {item.get("category") for item in items}
    require({"privacy", "accessibility", "safety", "resilience", "integrity", "correctness", "data-lifecycle", "authority", "evidence"}.issubset(categories), "gate categories are incomplete")
    for gate in items:
        require(set(gate.get("journeys", [])).issubset(journey_ids), f"{gate.get('gate_id')} references unknown journey")
        require(gate.get("negative_cases"), f"{gate.get('gate_id')} lacks negative cases")
        require(gate.get("required_evidence"), f"{gate.get('gate_id')} lacks evidence requirements")
    prohibited = set(gates.get("prohibited_actions", []))
    require({"physical-actuation", "diagnose", "move-money", "widen-disclosure"}.issubset(prohibited), "prohibited-action set is incomplete")


def main() -> None:
    package = load(FIXTURE_PATH)
    gates = load(GATES_PATH)
    require(package.get("schema_version") == "dj0-fixture-package.v1", "invalid DJ-0 fixture version")
    require(package.get("truth_label") == "simulation", "fixture package must remain simulation")
    require(package.get("contains_real_personal_data") is False, "fixtures cannot contain real personal data")
    require(package.get("requires_model") is False, "DJ-0 fixtures must be model-independent")
    validate_contracts(package)
    journeys = package.get("journeys", {})
    require(set(journeys) == {"water_leak", "health_finance"}, "fixture package must contain exactly two journeys")
    validate_water(journeys["water_leak"])
    validate_health_finance(journeys["health_finance"])
    journey_ids = {journey["journey_id"] for journey in journeys.values()}
    validate_gates(gates, journey_ids)
    print("DJ-0 fixture validation passed: 10 contract candidates, 2 journeys, 12 gates")


if __name__ == "__main__":
    main()
