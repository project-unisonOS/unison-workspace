import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [
    str(ROOT / "unison-comms" / "src"),
    str(ROOT / "unison-auth" / "src"),
    str(ROOT / "unison-common" / "src"),
]

from channel_gateway import ChannelGateway, FakeTelegramProvider  # noqa: E402
from identity_store import IdentityStore  # noqa: E402


def test_phase5_components_are_pinned_workspace_submodules():
    modules = (ROOT / ".gitmodules").read_text(encoding="utf-8")
    assert 'path = unison-comms' in modules
    assert 'path = unison-platform' in modules
    assert (ROOT / "unison-comms" / "src" / "channel_gateway.py").is_file()
    assert (ROOT / "unison-platform" / "compose" / "compose.native.yaml").is_file()
    assert (ROOT / "docs" / "architecture" / "CHANNEL_GATEWAY.md").is_file()


def _service_block(compose: str, name: str, next_name: str) -> str:
    return compose.split(f"  {name}:\n", 1)[1].split(f"  {next_name}:\n", 1)[0]


def test_channel_services_have_no_host_port_and_use_secret_files():
    compose = (ROOT / "unison-platform" / "compose" / "compose.yaml").read_text(encoding="utf-8")
    if "  comms:\n" not in compose and "  telegram-channel-worker:\n" not in compose:
        # The later native baseline excludes experimental remote channels from
        # its default runtime instead of exposing them with product services.
        return
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


def test_real_auth_binding_authority_composes_with_gateway(tmp_path):
    now = 1_800_000_000.0
    identity = IdentityStore(str(tmp_path / "identity.db"))
    person = identity.bootstrap_first_person(
        confirmed=True, login_handle="alex", display_name="Alex", household_name="Home", password_hash="hash"
    )
    provider = FakeTelegramProvider()
    gateway = ChannelGateway(
        str(tmp_path / "channels.db"), "workspace-integration-root-key-material", identity,
        lambda _token: provider, now=lambda: now,
    )
    account = "bot-alex"
    gateway.register_telegram_account(
        person_id=person["person_id"], provider_account_id=account, token="synthetic-not-real", bot_id="bot-1"
    )
    code, _ = identity.create_channel_pairing(
        person_id=person["person_id"], provider="telegram", provider_account_id=account,
        local_assurance="passkey",
    )
    provider.updates = [{
        "update_id": 1,
        "message": {"date": int(now), "text": f"/pair {code}", "from": {"id": 101}, "chat": {"id": 101, "type": "private"}},
    }]
    assert gateway.poll(account)[0].status == "paired"
    provider.updates = [{
        "update_id": 2,
        "message": {"date": int(now), "text": "summarize my day", "from": {"id": 101}, "chat": {"id": 101, "type": "private"}},
    }]
    accepted = gateway.poll(account)[0]
    assert accepted.status == "accepted"
    assert accepted.envelope.bound_person_id == person["person_id"]
    assert accepted.envelope.bound_assistant_instance_id == person["assistant_instance_id"]
