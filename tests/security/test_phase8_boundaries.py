from pathlib import Path


ROOT = Path(__file__).parents[2]


def test_supported_expansion_has_contract_security_and_recovery_paths():
    common = (ROOT / "unison-common/schemas/ecosystem-expansion.v1.schema.json").read_text()
    capability = (ROOT / "unison-capability/src/ecosystem.py").read_text()
    renderer = (ROOT / "unison-experience-renderer/src/web/modalityNegotiation.js").read_text()
    speech = (ROOT / "unison-io-speech/src/message_schema.py").read_text()
    inference = (ROOT / "unison-inference/src/routing.py").read_text()
    assert "preserves_actions" in common
    for marker in ("verify_manifest_signature", "permission_diff", "RevocationRegistry", "require_compatibility"):
        assert marker in capability
    assert "semanticActionsPreserved" in renderer
    assert "captions" in speech and "cancel_tts" in speech
    for marker in ("cost_ceiling", "max_risk", "max_disclosure", "offline"):
        assert marker in inference


def test_experimental_and_deferred_boundaries_are_explicit():
    evidence = (ROOT / "docs/planning/PHASE8_EXPANSION_8_1_EVIDENCE.md").read_text()
    assert "Braille" in evidence and "experimental" in evidence
    assert "disabled-user research" in evidence
    for deferred in ("BCI", "robotics", "spatial", "autonomous financial"):
        assert deferred in evidence
