# GitHub contribution governance

Status: active, 2026-08-14.

The `platform` and `security-leads` organization teams exist and own the paths
declared in `CODEOWNERS`. The initial maintainer belongs to both teams; add
contributors with the least organization and repository role required.

Main-branch protection is active for `unison-workspace`, `unison-common`,
`unison-storage`, `unison-orchestrator`, `unison-experience-renderer`,
`unison-infrastructure`, `unison-hardware`, and the organization `.github`
repository. The common controls are:

- changes through pull requests;
- one approving review and CODEOWNER review;
- stale review dismissal and resolved conversations;
- force-push and branch-deletion prevention;
- administrators may perform an explicit emergency bypass;
- repository-specific CI checks are required where stable checks exist.

Required checks:

| Repository | Checks |
| --- | --- |
| workspace | Phase 0, Phase 6 S3, PowerShell parsing, Python security |
| storage | image build, Python security, container supply chain |
| orchestrator | build, image build, tests, Python security, container supply chain |
| experience renderer | tests |
| infrastructure | environment profiles |
| hardware | hardware data |

`unison-common` and `.github` currently require review but have no stable status
context configured. Adding a stable CI workflow to each is a governance backlog
item; do not invent a required context before GitHub has observed it.

Emergency bypasses must be intentional, named in the merge record, followed by
the normal validation, and documented if they affect released artifacts or
authority boundaries.
