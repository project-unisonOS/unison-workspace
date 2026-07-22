from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_phase5_components_are_pinned_workspace_submodules():
    modules = (ROOT / ".gitmodules").read_text(encoding="utf-8")
    assert 'path = unison-comms' in modules
    assert 'path = unison-platform' in modules
    assert (ROOT / "unison-comms" / "src" / "channel_gateway.py").is_file()
    assert (ROOT / "unison-platform" / "docs" / "TELEGRAM_CHANNEL.md").is_file()


def _service_block(compose: str, name: str, next_name: str) -> str:
    return compose.split(f"  {name}:\n", 1)[1].split(f"  {next_name}:\n", 1)[0]


def test_channel_services_have_no_host_port_and_use_secret_files():
    compose = (ROOT / "unison-platform" / "compose" / "compose.yaml").read_text(encoding="utf-8")
    comms = _service_block(compose, "comms", "telegram-channel-worker")
    worker = _service_block(compose, "telegram-channel-worker", "agent-vdi")
    assert "ports:" not in comms
    assert "ports:" not in worker
    assert 'expose:\n      - "8080"' in comms
    assert "CHANNEL_GATEWAY_ROOT_KEY_FILE" in comms and "AUTH_CHANNEL_WORKLOAD_SECRET_FILE" in comms
    assert "run_telegram_worker.py" in worker
    assert "api.telegram.org" in (ROOT / "unison-platform" / "docs" / "TELEGRAM_CHANNEL.md").read_text(encoding="utf-8")


def test_provider_disclosure_and_fake_conformance_are_credential_free():
    guide = (ROOT / "unison-comms" / "docs" / "telegram-channel.md").read_text(encoding="utf-8")
    test_source = (ROOT / "unison-comms" / "tests" / "test_channel_gateway.py").read_text(encoding="utf-8")
    assert "low-assurance" in guide
    assert "not end-to-end encrypted" in guide
    assert "up to 24 hours" in guide
    assert "FakeTelegramProvider" in test_source
    assert "api.telegram.org" not in test_source
    assert "real credential" in guide
