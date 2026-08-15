# NUC workspace convergence plan

Status: convergence execution in progress

Date: 2026-08-15

## Objective

Converge the dev NUC on one canonical Unison workspace without losing useful
work, importing obsolete configuration, or overwriting unrelated local changes.

## Audited workspaces

| Workspace | Revision | State | Disposition |
| --- | --- | --- | --- |
| `/home/darryl-adams/project-unisonOS/unison-workspace` | `b2652dc` | Parent is 160 commits behind current `main`; three dirty submodules | Preserve until the dispositions below are complete, then retire |
| `/home/darryl-adams/project-unisonOS/validation/unison-workspace-2251305` | `eb21f83` after validation update | Clean, recursive, bootstrapped, and validated over LAN SSH | Promote to the canonical NUC workspace after old-workspace retirement |

The old parent repository has no direct file changes and no commits ahead of
current `main`. Its feature-branch commits in the three dirty submodules are all
ancestors of current component `main` and do not need separate merging.

## Change inventory and disposition

### `unison-orchestrator`

State: 44 commits behind current component `main`, with uncommitted changes to
`src/server.py` and `tests/test_capabilities_flow.py`.

Disposition: **reimplement and merge on current `main`**.

The patch moves `publish_capabilities_to_context` before its first call, removes
a duplicate definition, and replaces a test that can silently skip with a
deterministic fake capability manifest. Current `main` still calls the function
before definition inside a broad exception handler, which can set capabilities
to unavailable during startup. The intent remains valid, but the old patch must
not be applied blindly across 44 newer commits.

Required proof:

- focused capability publication test does not skip;
- import and startup retain a nonempty eligible capability manifest;
- failed context publication remains nonfatal and observable;
- orchestrator unit, security, and workspace integration checks pass.

### `unison-devstack/.env.security`

State: one uncommitted deletion of the `OPENAI_API_KEY` placeholder.

Disposition: **discard**.

The deletion is not a secret recovery or functional implementation. Removing
only the OpenAI placeholder while retaining other provider placeholders is not
a coherent provider-policy change. Provider eligibility, local-first routing,
and secret injection should be changed through reviewed configuration and
documentation rather than a local example-file deletion.

### `unison-inference/.env.example`

State: one uncommitted deletion of the empty `OPENAI_API_KEY` example entry.

Disposition: **discard**.

The same reasoning applies. External providers remain governed optional routes,
and deleting one empty example variable does not disable or secure the route.

### `unison-devstack/docker-compose.resource-limits.yml`

State: untracked Compose overlay assigning most services 512 MiB, Neo4j 1 GiB,
swap limits, and no automatic restart.

Disposition: **retain as design input, then reimplement in the owned environment
profile if measurements justify it**.

The overlay is not ready to merge. It predates the current `io-bci` service,
applies one memory budget to unlike workloads, has no measured NUC baseline,
and belongs with the declarative dev NUC environment profile rather than as an
untracked broad-devstack override. Preserve its intent in the follow-up task:
protect host responsiveness, avoid automatic full-stack restart, and define
per-service memory, swap, health, and degradation behavior using measured load.

## Ordered convergence

1. Export a manifest of the old parent revision, submodule revisions, branches,
   status, and checksums for the five changed or untracked files.
2. Save the orchestrator patch and resource-overlay source in a temporary,
   access-controlled NUC archive outside the canonical workspace. Do not archive
   credentials or environment values.
3. Reimplement the orchestrator fix from current component `main`, add the
   deterministic regression test, pass hosted CI, and merge it.
4. Open a separate measured dev NUC resource-budget task. Do not merge the old
   overlay as production or supported configuration.
5. Confirm the validated workspace is clean, current, recursively synchronized,
   bootstrapped, and passes focused plus Phase 0 checks at the final revisions.
6. Move the old workspace to a revision-named quarantine directory. Do not
   delete it during the move step.
7. Move the validated workspace to
   `/home/darryl-adams/project-unisonOS/unison-workspace`, update the Windows
   remote-development workspace setting, and rerun LAN SSH status, bootstrap,
   focused tests, and Phase 0 validation.
8. Retain the quarantined workspace for a short review window. Delete it only
   after explicit approval and checksum comparison confirms every disposition.

## Completion gate

Convergence is complete when one canonical NUC workspace tracks workspace
`main`, every submodule matches its pinned revision, Git status is clean, the
Windows wrapper uses `dev-nuc-lan`, bootstrap and Phase 0 validation pass, the
orchestrator fix is merged, the resource-budget concept has a tracked owner, and
the quarantined workspace has an explicit retain or delete decision.

No existing workspace, branch, file, or archive is deleted by this plan.

## Execution record

The credential-free archive was created at
`/home/darryl-adams/project-unisonOS/workspace-convergence-archive/b2652dc-20260815`.
It contains the orchestrator working patch, resource-overlay source, and a
checksum and revision manifest. Environment values were not archived. The
orchestrator fix was reimplemented against current `main` with a deterministic
regression test. The measured resource follow-up is tracked by
`DEV-NUC-RESOURCE-BUDGET.task.json`; the old overlay itself will not be merged.
