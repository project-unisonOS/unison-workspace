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

Updates commit `ee02705357308354f4ba81ab2eaeb7cf720baa1a` emits a
versioned verified-target receipt only after those checks pass. The receipt
retains the original signed channel metadata and binds root/channel versions,
target and release versions, exact artifact bytes, hardware, restart, and
checkpoint requirements.

Platform commit `5db92993f8c99fe463f8fd825140472d6c5a0ea6` adds the
privileged activation transaction. It independently verifies the receipt's
Ed25519 threshold against a separately pinned update root, verifies the signed
release bundle, checks capacity, creates and verifies a personal-data and
receipt checkpoint, stages the complete target without changing the current
release, atomically activates it, and promotes only after bounded health checks.

CI simulations cover successful `N-1 -> N`, failed `N -> N+1`, health retries,
migration failure, explicit owner rollback, download/staging/post-activation
interruption, safe resume, disk-full refusal and retry, restored-device state,
authorization mismatch, signed-metadata tamper, and expired update roots.
Automatic rollback restores the previous release, installation receipt, and
checkpointed data. These are filesystem simulations, not promoted production
images, physical reboot, or hardware rollback evidence; HW-008 and HW-009
remain pending.

## Hardened public preview distribution

Platform commit `2749aba37e54f328cf1105523c13cc893e7a2ed6` produced
the public `v0.6.0-preview.1` prerelease. The release contains a signed x86-64
bundle, all 13 digest-pinned runtime images, checksums, source correspondence,
an SPDX inventory, provenance, support status, vulnerability evidence,
Ed25519 signatures, and Sigstore evidence.

Release run `30131075439` built and pushed ten project images, signed and
scanned them, assembled and signed the release, then downloaded the public
assets again. The public verification job checked the published bytes and
signatures, completed an installer transaction, and rejected incomplete and
tampered mirrors. The release gate rejects fixable critical vulnerabilities;
the preview publishes remaining no-fix findings and is explicitly marked
unsupported.

The release and its direct bundle, checksum, checksum-signature, verification
key, manifest, support, and vulnerability URLs returned HTTP 200 during the
publication audit. The public GitHub Pages release, installation, status,
lifecycle, and roadmap guidance was refreshed in
`project-unisonos.github.io` commit
`f55560eaa54464dbc9294a80b76eba871db85df3`. Superseded WSL2, VM, split ISO,
and `v0.5.0-alpha.1` pointers are now archived rather than presented as current
downloads.

This closes the environment-independent public-distribution slice of Phase
9.5. It does not satisfy physical install, reboot, update, rollback, firmware,
audio, thermal, or power evidence. Those results remain pending in the
hardware ledger, and the preview is not a supported release.
