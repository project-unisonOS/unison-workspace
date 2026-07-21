#!/usr/bin/env python3
"""Fail if Phase 1 product profiles regress to broad reusable secrets."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEV_SECURITY = ROOT / "unison-devstack" / "docker-compose.security.yml"
PLATFORM = ROOT.parent / "unison-platform"
NATIVE = PLATFORM / "compose" / "compose.yaml"
INSTALLER = PLATFORM / "scripts" / "native" / "ubuntu_install.sh"


def require(text: str, markers: tuple[str, ...], label: str, failures: list[str]) -> None:
    for marker in markers:
        if marker not in text:
            failures.append(f"{label}: missing {marker}")


def main() -> int:
    failures: list[str] = []
    dev = DEV_SECURITY.read_text(encoding="utf-8")
    require(
        dev,
        (
            'UNISON_ALLOW_HS256_SERVICE_TOKENS: "false"',
            "UNISON_AUTH_BOOTSTRAP_TOKEN_FILE: /run/secrets/unison_bootstrap_token",
            "COMMS_ROOT_KEY_FILE: /run/secrets/unison_comms_root",
            "UNISON_CONTEXT_PROFILE_KEY_FILE: /run/secrets/unison_context_root",
            "STORAGE_OBJECT_ENC_KEY_FILE: /run/secrets/unison_storage_root",
            "UNISON_CAPABILITY_AUTH_MODE: unison_jwt",
            'UNISON_REQUIRE_CONSENT: "true"',
        ),
        "hardened dev profile",
        failures,
    )
    if NATIVE.exists() and INSTALLER.exists():
        native = NATIVE.read_text(encoding="utf-8")
        installer = INSTALLER.read_text(encoding="utf-8")
        require(
            native,
            (
                "UNISON_AUTH_BOOTSTRAP_TOKEN_FILE: /run/secrets/unison_bootstrap_token",
                "UNISON_CONTEXT_PROFILE_KEY_FILE: /run/secrets/unison_context_root",
                "STORAGE_OBJECT_ENC_KEY_FILE: /run/secrets/unison_storage_root",
                "UNISON_AUTH_IDENTITY_DATABASE_PATH: /keys/identity.db",
                'UNISON_REQUIRE_CONSENT: "true"',
                "unison-consent:${UNISON_IMAGE_TAG:-latest}",
            ),
            "native appliance profile",
            failures,
        )
        for forbidden in ("UNISON_JWT_SECRET=$(", "UNISON_CONSENT_SECRET=$("):
            if forbidden in installer:
                failures.append(f"native installer: forbidden broad secret generator {forbidden}")
        for template in (PLATFORM / ".env.example", PLATFORM / ".env.template"):
            template_text = template.read_text(encoding="utf-8")
            for forbidden in ("UNISON_JWT_SECRET=", "JWT_SECRET_KEY=", "JWT_ALGORITHM=HS256"):
                if forbidden in template_text:
                    failures.append(f"{template.name}: forbidden product secret setting {forbidden}")
    else:
        print("[note] optional sibling unison-platform absent; native profile validation not run")

    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}", file=sys.stderr)
        return 1
    print("[PASS] Phase 1 product profiles use scoped secret files and signed principal auth.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
