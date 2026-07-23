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

## Remaining Phase 9.1 work

The release process must connect real promoted image digests to SBOMs,
provenance, and signature verification. Runtime
fault injection can be exercised in CI where representative; physical results
remain in the hardware ledger.
