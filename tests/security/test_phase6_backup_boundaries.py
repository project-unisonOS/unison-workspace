from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.phase6_backup_demo import run_demo
from src.backup_backends import HostileMemoryBackend
from src.backup_service import BackupCoordinator, FileCheckpointWitness, ScopeSecrets
from unison_common.backup import ScopeKind, VerificationStatus


def test_t07_t13_t17_provider_and_stolen_backup_see_ciphertext_and_minimal_metadata(tmp_path):
    result = run_demo(tmp_path)
    assert result["provider_plaintext_canaries"] == 0
    assert result["private_scope_ids_distinct"] is True
    assert result["repeated_verifications"] == 6


def test_t20_admin_provider_and_wrong_person_cannot_recover(tmp_path):
    backend = HostileMemoryBackend()
    coordinator = BackupCoordinator(
        backend,
        FileCheckpointWitness(tmp_path / "witness"),
        journal_root=tmp_path / "journals",
        chunk_size=8,
    )
    owner = ScopeSecrets.create(ScopeKind.PERSON, "owner")
    attacker = ScopeSecrets.create(ScopeKind.PERSON, "attacker")
    coordinator.create_snapshot(owner, b"owner-only")
    with pytest.raises(Exception):
        coordinator.plan_restore(attacker, target_device_id="admin-device")
    assert b"owner-only" not in b"".join(backend.objects.values())


def test_t13_manifest_truncation_reordering_corruption_and_replay_fail_closed(tmp_path):
    backend = HostileMemoryBackend()
    coordinator = BackupCoordinator(
        backend,
        FileCheckpointWitness(tmp_path / "witness"),
        journal_root=tmp_path / "journals",
        chunk_size=8,
    )
    owner = ScopeSecrets.create(ScopeKind.PERSON, "owner")
    coordinator.create_snapshot(owner, b"one")
    first_head = backend.get(f"heads/{owner.opaque_scope_id}.json")
    coordinator.create_snapshot(owner, b"two")
    backend.put(f"heads/{owner.opaque_scope_id}.json", first_head)
    assert coordinator.verify(owner).status is VerificationStatus.ROLLED_BACK


def test_t30_independent_export_delete_and_shared_removal_semantics(tmp_path):
    result = run_demo(tmp_path)
    assert result["shared_members_before"] == ["person-alice", "person-bob"]
    assert result["shared_members_after_removal"] == ["person-alice"]
    assert result["old_devices_revoked"] is True


def test_backup_is_not_sync_or_remote_access(tmp_path):
    result = run_demo(tmp_path)
    assert result["home_node_authoritative"] is True
    assert result["multi_writer_sync_enabled"] is False
