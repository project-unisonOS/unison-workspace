#!/usr/bin/env python3
"""Validate a modality adapter manifest without granting it system authority."""
import json
import re
import sys
from pathlib import Path

REQUIRED = {"schema_version", "adapter_id", "modality", "input_supported",
            "output_supported", "sem_versions", "expression_versions", "capability_ids",
            "package_digest", "signer_id"}
OPTIONAL = {"required_permissions", "device_classes", "fallback_modalities"}
AUTHORITY_FIELDS = {"consent", "consent_grant", "identity", "policy", "authorization",
                    "action_authority", "disclosure_authority"}

def validate(path: Path) -> None:
    value = json.loads(path.read_text(encoding="utf-8"))
    unknown = set(value) - REQUIRED - OPTIONAL
    missing = REQUIRED - set(value)
    if missing or unknown:
        raise ValueError(f"manifest fields invalid; missing={sorted(missing)} unknown={sorted(unknown)}")
    if set(value) & AUTHORITY_FIELDS:
        raise ValueError("modality adapters cannot declare identity, consent, policy, disclosure, or action authority")
    if value["schema_version"] != "modality-adapter.v1":
        raise ValueError("unsupported modality adapter schema")
    if not value["input_supported"] and not value["output_supported"]:
        raise ValueError("adapter must provide input or output")
    if not value["sem_versions"] or not value["expression_versions"]:
        raise ValueError("adapter must declare semantic and expression contracts")
    if not re.fullmatch(r"sha256:[a-f0-9]{64}", value["package_digest"]):
        raise ValueError("package_digest must be a lowercase SHA-256 digest")

if __name__ == "__main__":
    try:
        validate(Path(sys.argv[1]))
    except (IndexError, OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc)) from exc
    print(f"validated modality adapter manifest: {sys.argv[1]}")
