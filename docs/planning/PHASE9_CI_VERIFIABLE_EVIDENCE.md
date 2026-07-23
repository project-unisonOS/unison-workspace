# Phase 9 environment-independent evidence

Status: In progress

## Deterministic runtime contract

Platform commit `58e04a71afb6f3aa3e35b42e9bbb89e2e011aa71` adds the
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

## Remaining Phase 9.1 work

The release process must generate real image digests, source/schema/config/model
versions, licenses, SBOMs, provenance, and signature verification. Runtime
fault injection can be exercised in CI where representative; physical results
remain in the hardware ledger.
