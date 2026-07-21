from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
AUTH_SOURCE = ROOT / "unison-auth" / "src"
SUBMODULES_AVAILABLE = AUTH_SOURCE.is_dir()
if SUBMODULES_AVAILABLE:
    sys.path.insert(0, str(AUTH_SOURCE))
    from identity_store import IdentityStore  # noqa: E402
    from unison_common.principal import (  # noqa: E402
        partition_key,
        principal_context_from_claims,
        redact_principal_for_log,
    )


RESOURCE_TYPES = ("read", "write", "search", "cache", "replay", "object", "vault", "audit")


def _identity(store: IdentityStore, name: str, household=None):
    if household is None:
        return store.bootstrap_first_person(
            confirmed=True,
            login_handle=f"{name}-login",
            display_name=name.title(),
            household_name="Boundary household",
            password_hash=f"hash-{name}",
        )
    token, _ = store.create_invitation(
        invited_by_person_id=household["person_id"],
        household_id=household["household_id"],
    )
    return store.accept_invitation(
        invitation_token=token,
        login_handle=f"{name}-login",
        display_name=name.title(),
        password_hash=f"hash-{name}",
    )


def _context(identity, token_id):
    now = int(time.time())
    return principal_context_from_claims(
        {
            "sub": identity["principal_id"],
            "principal_id": identity["principal_id"],
            "principal_kind": "person",
            "person_id": identity["person_id"],
            "assistant_instance_id": identity["assistant_instance_id"],
            "household_id": identity["household_id"],
            "membership_id": identity["membership_id"],
            "roles": identity["roles"],
            "aud": ["orchestrator", "context", "storage"],
            "auth_method": "passkey",
            "assurance": "high",
            "session_id": f"session-{token_id}",
            "key_handle": identity["key_handle"],
            "credential_namespace": identity["credential_namespace"],
            "data_namespace": identity["data_namespace"],
            "cache_namespace": identity["cache_namespace"],
            "index_namespace": identity["index_namespace"],
            "jti": token_id,
            "iat": now - 1,
            "exp": now + 300,
        }
    )


@pytest.mark.skipif(
    not SUBMODULES_AVAILABLE,
    reason="cross-repository Phase 1 boundary evidence requires initialized submodules",
)
def test_two_adults_share_household_but_not_any_private_resource(tmp_path):
    store = IdentityStore(str(tmp_path / "identity.db"))
    alice = _identity(store, "alice")
    bob = _identity(store, "bob", alice)
    alice_context = _context(alice, "alice-token")
    bob_context = _context(bob, "bob-token")
    assert alice_context.household_id == bob_context.household_id

    resources = {}
    for resource in RESOURCE_TYPES:
        key = partition_key(alice_context, resource, "private-canary")
        resources[key] = f"alice-{resource}-canary"
        bob_key = partition_key(bob_context, resource, "private-canary")
        assert bob_key != key
        assert bob_key not in resources
        assert all(not candidate.startswith(bob_context.data_namespace) for candidate in resources)


@pytest.mark.skipif(
    not SUBMODULES_AVAILABLE,
    reason="cross-repository Phase 1 boundary evidence requires initialized submodules",
)
def test_key_credential_namespace_and_logs_do_not_cross_principals(tmp_path):
    store = IdentityStore(str(tmp_path / "identity.db"))
    alice = _identity(store, "alice")
    bob = _identity(store, "bob", alice)
    assert alice["key_handle"] != bob["key_handle"]
    assert alice["credential_namespace"] != bob["credential_namespace"]
    assert alice["cache_namespace"] != bob["cache_namespace"]
    assert alice["index_namespace"] != bob["index_namespace"]

    logged = json.dumps(redact_principal_for_log(_context(alice, "alice-token")), sort_keys=True)
    for canary in (
        alice["key_handle"],
        alice["credential_namespace"],
        alice["data_namespace"],
        alice["cache_namespace"],
        alice["index_namespace"],
        "alice-password-canary",
    ):
        assert canary not in logged
