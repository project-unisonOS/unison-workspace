# Phase 9 environment-independent evidence

Status: In progress

## Deterministic runtime contract

Platform commit `7284acef48d520a9225953bdc329ca077e5b6c0f` adds the
Phase 9 supported Compose entrypoint. Its static gate establishes:

- exactly 13 required services;
- a required digest reference for every service image;
- no mutable tag selector in the supported override;
- removal of developer host ports from internal services; and
- exactly two host-facing surfaces, both bound to loopback.

Platform PR 16 passed its supported-runtime contract and actionlint jobs. This
is source and CI evidence only. It does not satisfy cold-start, reboot,
pressure, fault-recovery, or physical installation checks HW-001 through
HW-007.

Platform PR 17 adds a deterministic supported-release manifest. Two builds
from identical source and inputs are byte-identical. The publish path rejects
missing, mutable, and example zero digests, and records source, Compose,
service images, host packages/resources, schema/configuration/backup/model
versions, model-profile hash, and declared licenses. The dependency-free
negative and reproducibility tests run from both platform and workspace CI.

Platform PRs 18 and 19 add environment-independent installer evidence. The
preflight accepts the exact target profile and blocks nine incompatible
OS/architecture/resource/firmware/runtime cases. The transaction primitive
stages versioned bundles, atomically activates them, retains last known good
through injected interruptions, supports idempotent reinstall and repair, and
requires an exact destruction phrase before factory reset. Ordinary uninstall
preserves the separate personal-data directory. These temporary-filesystem
tests do not satisfy physical checks HW-005 through HW-007.

Platform PR 20, merged as
`86a53cb9f455a6d203e71849164892881c99966d`, connects those primitives
through a deterministic signed release bundle and bootstrap boundary. The
bundle contains the supported manifest, Compose contract, immutable image
environment, host requirements, license inventory, and model profile under a
canonical Ed25519-signed index. Bootstrap verification runs before privilege
elevation and binds confirmation to the exact bundle index, trusted public key,
installation prefix, and personal-data path.

Hosted and workspace acceptance build byte-identical bundles, reject content
corruption, invalid signatures, missing and extra files, a substituted trust
root, and service/image reassignment, then exercise refusal before exact plan
acceptance, transactional install, an installation receipt, idempotent
reinstall, and data-preserving uninstall. The receipt reconciles the installed
tree with the bundle index, release manifest, source commit, and immutable
image inventory. This is CI/simulation evidence only: it does not publish real
release images or satisfy HW-005, HW-006, or HW-015.

## Signed update-channel trust

Updates commit `a48a49b0a7bdd7ff9cd347f1d9c66910074423d3` adds
canonical Ed25519 threshold verification for root and channel metadata. The
client requires unexpired, monotonically advancing metadata and target
versions, exact channel and Ubuntu x86_64 binding, and matching artifact length
and SHA-256 before staging. Root rotation advances exactly one version and
requires thresholds from both the trusted and proposed roots.

Hosted and workspace simulations reject replay/freeze, expiration, wrong
channel, corrupt artifact, incompatible hardware, target rollback, signed
payload tampering, and invalid root-version jumps. A valid dual-authority key
rotation succeeds. These metadata tests do not satisfy real promoted update,
interruption, reboot, or rollback checks HW-008 and HW-009.

## Remaining Phase 9.1 work

The release process must connect real promoted image digests to SBOMs,
provenance, and public-download verification. Runtime
fault injection can be exercised in CI where representative; physical results
remain in the hardware ledger.
