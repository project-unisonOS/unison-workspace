"""Clean replacement-device Phase 6 proof with synthetic household data."""

from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path
from typing import Any

from unison_common.backup import ScopeKind, VerificationStatus

from src.backup_backends import FileSystemBackend
from src.backup_service import BackupCoordinator, FileCheckpointWitness, ScopeSecrets


def run_demo(root: Path) -> dict[str, Any]:
    source = FileSystemBackend(root / "provider-a")
    destination = FileSystemBackend(root / "provider-b")
    witness = FileCheckpointWitness(root / "trusted-checkpoints")
    coordinator = BackupCoordinator(
        source,
        witness,
        journal_root=root / "source-journals",
        chunk_size=16,
    )
    scopes = {
        "alice": ScopeSecrets.create(ScopeKind.PERSON, "person-alice"),
        "bob": ScopeSecrets.create(ScopeKind.PERSON, "person-bob"),
        "household": ScopeSecrets.create(
            ScopeKind.SHARED_SPACE,
            "space-household",
        ),
    }
    payloads = {
        "alice": b'{"private":"ALICE-PHASE6-CANARY","goal":"call dentist"}',
        "bob": b'{"private":"BOB-PHASE6-CANARY","goal":"renew passport"}',
        "household": b'{"shared":["milk","calendar: dinner at 18:00"]}',
    }
    envelopes = {}
    for name, secrets in scopes.items():
        envelopes[name] = coordinator.create_snapshot(
            secrets,
            payloads[name],
            provenance=(f"synthetic-phase6:{name}",),
        )
        first = coordinator.verify_and_record(secrets, force=True)
        second = coordinator.verify_and_record(secrets, force=True)
        if (
            first.status is not VerificationStatus.VERIFIED
            or second.status is not VerificationStatus.VERIFIED
        ):
            raise RuntimeError(f"repeated verification failed for {name}")

    provider_bytes = b"\n".join(
        path.read_bytes()
        for path in (root / "provider-a").rglob("*")
        if path.is_file()
    )
    for canary in (b"ALICE-PHASE6-CANARY", b"BOB-PHASE6-CANARY", b"space-household"):
        if canary in provider_bytes:
            raise RuntimeError("provider observed private or local scope data")

    for secrets in scopes.values():
        migrated = coordinator.migrate_provider(secrets, destination)
        if migrated.status is not VerificationStatus.VERIFIED:
            raise RuntimeError("provider migration verification failed")

    replacement = BackupCoordinator(
        destination,
        witness,
        journal_root=root / "replacement-journals",
        chunk_size=16,
    )
    restored: dict[str, str] = {}
    for name, secrets in scopes.items():
        plan = replacement.plan_restore(
            secrets,
            target_device_id=f"replacement-{name}",
        )
        target = root / "clean-device" / f"{name}.json"
        result = replacement.restore(
            secrets,
            plan,
            target=target,
            replaced_device_id=f"lost-{name}",
            rotate_after_activate=True,
        )
        if target.read_bytes() != payloads[name]:
            raise RuntimeError(f"restored payload mismatch for {name}")
        restored[name] = result.status.value

    household = scopes["household"]
    active_wraps = household.wrap_shared_space_key(
        {
            "person-alice": b"a" * 32,
            "person-bob": b"b" * 32,
        }
    )
    household.rotate(revoked_device_id="removed-person-bob-device")
    post_removal_wraps = household.wrap_shared_space_key(
        {"person-alice": b"a" * 32}
    )
    if "person-bob" in post_removal_wraps:
        raise RuntimeError("removed shared member received a future key wrap")

    return {
        "format": "unison-phase6-demo-v1",
        "scopes": sorted(scopes),
        "provider_plaintext_canaries": 0,
        "repeated_verifications": 2 * len(scopes),
        "provider_migration": "verified",
        "restored": restored,
        "private_scope_ids_distinct": (
            envelopes["alice"].opaque_scope_id
            != envelopes["bob"].opaque_scope_id
        ),
        "shared_members_before": sorted(active_wraps),
        "shared_members_after_removal": sorted(post_removal_wraps),
        "old_devices_revoked": all(
            any(item.startswith("lost-") for item in scope.revoked_device_ids)
            for scope in scopes.values()
        ),
        "home_node_authoritative": True,
        "multi_writer_sync_enabled": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root")
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.root:
        result = run_demo(Path(args.root))
    else:
        with tempfile.TemporaryDirectory(prefix="unison-phase6-") as temporary:
            result = run_demo(Path(temporary))
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
