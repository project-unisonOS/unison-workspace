#!/usr/bin/env python3
"""Validate the S3-compatible backend against the Phase 6 MinIO profile."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

import boto3

from src.backup_backends import S3Backend
from src.backup_service import BackupCoordinator, FileCheckpointWitness, ScopeSecrets
from unison_common.backup import ScopeKind, VerificationStatus


def main() -> int:
    endpoint = os.getenv("PHASE6_S3_ENDPOINT", "http://127.0.0.1:19000")
    bucket = os.getenv("PHASE6_S3_BUCKET", "unison-phase6")
    client = boto3.client(
        "s3",
        endpoint_url=endpoint,
        region_name="us-east-1",
        aws_access_key_id="phase6-test-access",
        aws_secret_access_key="phase6-test-secret-only",
    )
    try:
        client.create_bucket(Bucket=bucket)
    except client.exceptions.BucketAlreadyOwnedByYou:
        pass
    backend = S3Backend(bucket=bucket, client=client, prefix="phase6")
    with tempfile.TemporaryDirectory(prefix="unison-phase6-minio-") as temporary:
        root = Path(temporary)
        coordinator = BackupCoordinator(
            backend,
            FileCheckpointWitness(root / "witness"),
            journal_root=root / "journals",
            chunk_size=8,
        )
        scope = ScopeSecrets.create(ScopeKind.PERSON, "minio-person")
        canary = b"MINIO-PROVIDER-MUST-NOT-READ"
        coordinator.create_snapshot(scope, canary)
        verification = coordinator.verify(scope)
        if verification.status is not VerificationStatus.VERIFIED:
            raise SystemExit(verification.detail)
        raw = b"".join(backend.get(key) for key in backend.list("objects"))
        raw += b"".join(backend.get(key) for key in backend.list("manifests"))
        if canary in raw or b"minio-person" in raw:
            raise SystemExit("MinIO provider view exposed plaintext")
        plan = coordinator.plan_restore(scope, target_device_id="replacement-minio")
        restored = root / "restored.bin"
        coordinator.restore(scope, plan, target=restored)
        if restored.read_bytes() != canary:
            raise SystemExit("MinIO restore mismatch")
    print("[PASS] S3-compatible MinIO backup, verification, and restore passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
