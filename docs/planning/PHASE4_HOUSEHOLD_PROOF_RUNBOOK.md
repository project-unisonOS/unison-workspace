# Phase 4 synthetic household proof runbook

This runbook uses generated identities and canaries only. Never substitute real
credentials or household content. The supported proof host is Ubuntu 24.04
x86_64 or WSL2 Ubuntu 24.04 with Python 3.12.

## Reproduce the proof

From a recursive `unison-workspace` checkout:

```bash
./scripts/bootstrap-dev.sh
./scripts/test-phase4.sh
```

The command runs the component household contracts and 50 integrated checks,
then prints one JSON result. A passing report has two assistants, two shared
artifacts, 13 negative surfaces, zero private sources read for coordination,
no private canary values, and `phase5_started: false`.

Validate the bounded deployment overlay from the sibling `unison-platform`
checkout after creating a synthetic `.env` from `.env.example`:

```bash
docker compose -f compose/compose.yaml -f compose/household-proof.yaml config --quiet
```

Do not use `up` with production credentials for this proof. If a local synthetic
stack is started, stop it without deleting evidence volumes with:

```bash
docker compose -f compose/compose.yaml -f compose/household-proof.yaml down
```

## Expected recovery and denial behavior

- A cross-person or nonexistent resource returns the same `resource unavailable`
  response.
- An invalid shared-artifact update changes no state.
- Restart reconstructs durable private/shared state and requeues only opaque work.
- Removing a member revokes identity and shared-space access and advances the
  shared-space key version.
- Audit and resource status never include task content or another person's canary.

See `TWO_ASSISTANT_HOUSEHOLD_PROOF.md` for the diagram and text equivalent.
