# Milestone 1 Doc Audit: Install and Release Surfaces

This audit reviews the current install, download, image, and release-facing documentation across:

- `project-unisonos.github.io`
- `unison-docs`
- `unison-platform` (as the reference implementation source for install/release behavior)
- `unison-workspace` (as the planning and coordination surface)

The purpose is to identify where current docs already align with the Milestone 1 install strategy and where they still overemphasize the older alpha multi-artifact release story.

Related planning artifacts:

- `docs/milestone-1-artifact-install-strategy.md`
- `UNISONOS_PRODUCTION_IMPLEMENTATION_PLAN.md`
- `docs/milestone-1-acceptance-matrix.md`

## 1. Audit Standard

This audit uses the following classification:

- **Aligned**: clearly supports the canonical Milestone 1 install strategy
- **Partially aligned**: contains correct framing, but still gives too much emphasis or ambiguous priority to evaluator artifacts
- **Conflicting**: presents the older multi-artifact evaluator story as the primary or required release/install model

Canonical Milestone 1 standard used for this audit:

- supported install path: Ubuntu 24.04 native on x86_64
- canonical installer: `unison-platform/installer/install-native.sh`
- canonical ops CLI: `unisonctl`
- WSL2, Linux VM, and bare-metal ISO are evaluation-only
- public docs should foreground the supported route first and demote evaluator artifacts accordingly

## 2. Summary Findings

High-level result:

- `unison-platform` is mostly aligned and already provides the strongest installable-product foundation
- `project-unisonos.github.io` is mixed: some pages already reflect the native-first Milestone 1 story, but several developer-facing pages still present WSL/VM/ISO artifacts too prominently
- `unison-docs` still contains explicit alpha-release contracts that treat WSL2, Linux VM, and bare-metal ISO as co-equal or required release outputs

Main conclusion:

The core problem is no longer a lack of install/release direction.
The problem is that multiple documentation layers still reflect different eras of the release strategy.

## 3. Reference Sources Already Supporting the Milestone 1 Direction

These are the clearest current anchor points for the intended installable-product path.

### 3.1 `unison-platform/docs/install.md`

Status:
- **Aligned**

Why:
- explicitly states the supported installation target is Ubuntu 24.04 native on x86_64
- clearly labels WSL2, VM, and bare-metal as evaluation-only channels
- frames the native route as the primary path

Recommended action:
- keep as the canonical top-level install page

### 3.2 `unison-platform/docs/deployment/ubuntu-native.md`

Status:
- **Aligned**

Why:
- defines the canonical Milestone 1 install path
- describes the actual installer behavior
- documents production-safe environment and first-start constraints
- includes first-admin bootstrap and operational validation

Recommended action:
- keep as the canonical supported install guide

### 3.3 `unison-platform/installer/install-native.sh`

Status:
- **Aligned implementation artifact**

Why:
- real installer exists and supports the native-first path

Recommended action:
- use this as the implementation anchor for public install docs

### 3.4 `project-unisonos.github.io/docs/developers/releases.md`

Status:
- **Partially aligned**

Why:
- correctly states that Ubuntu 24.04 native is the supported installation target
- correctly labels WSL2, Linux VM, and bare metal as evaluation channels
- but still gives strong visual and content emphasis to the alpha multi-artifact release set in the release spotlight and expected asset-name sections

Recommended action:
- keep the page, but restructure it so the canonical supported install route is the first and dominant section
- move evaluator asset details into a secondary section
- avoid making the expected WSL/VM/ISO asset set look like the default Milestone 1 product package

## 4. Public Site Pages Requiring Revision

### 4.1 `project-unisonos.github.io/docs/developers/onboarding.md`

Status:
- **Partially aligned**

Current issue:
- page is developer-focused, which is fine, but it still says:
  - platform releases ship evaluator artifacts for WSL2, Linux VM, and bare metal from a single tag
  - one tag means one GitHub Release with multiple artifacts plus checksums/manifest
- that framing is still anchored in the older multi-artifact release narrative

Recommended revision:
- keep WSL2/Linux as developer environment guidance
- revise release-related sections to say:
  - developer onboarding primarily uses the workspace/devstack route
  - supported Milestone 1 install path is Ubuntu native
  - evaluator images may exist from the same release process, but they are not the primary install story

Priority:
- high

### 4.2 `project-unisonos.github.io/docs/developers/images-builds-and-releases.md`

Status:
- **Conflicting**

Current issue:
- page opens by saying UnisonOS ships as images and installers for WSL, VMs, and physical hardware
- image types are presented as peer first-class outputs
- latest images section tells readers GitHub Releases attach WSL, VM, and ISO artifacts
- workflow section emphasizes building those image targets as the release model

Why this conflicts:
- for Milestone 1, the public story should not imply that WSL bundle, Linux VM image, and bare-metal ISO are co-equal with the supported native install route

Recommended revision:
- reframe the page around artifact classes:
  - primary supported route: Ubuntu native installer bundle
  - evaluator image channels: WSL, VM, bare metal
- explicitly state which outputs are supported versus evaluation-only
- make local image-building commands clearly secondary to the canonical install strategy
- separate “release engineering internals” from “what users should install”

Priority:
- very high

### 4.3 `project-unisonos.github.io/docs/developers/hardware.md`

Status:
- **Partially aligned**

Current issue:
- installation options section lists installers and WSL/VM/ISO artifacts together without enough prioritization
- implies multiple artifact types are equally central to hardware deployment

Recommended revision:
- make Ubuntu native installer the first and clearly preferred hardware deployment route
- move WSL out of hardware framing except as an evaluation/developer path
- describe VM/ISO artifacts as secondary evaluation channels

Priority:
- medium

### 4.4 `project-unisonos.github.io/docs/developers/releases.md`

Status:
- **Partially aligned**

Current issue:
- page already contains the right milestone statement, but the release spotlight and asset expectations still center alpha evaluator artifacts

Recommended revision:
- reorder sections:
  1. supported install path
  2. canonical install docs
  3. supported release asset expectations for the primary route
  4. evaluation artifacts, if present
- make the native install route visually dominant

Priority:
- very high

## 5. `unison-docs` Pages Requiring Revision

### 5.1 `unison-docs/dev/releases/evaluate-alpha.md`

Status:
- **Conflicting**

Current issue:
- page is explicitly built around choosing among WSL2, Linux VM, and bare-metal ISO artifacts
- says all artifacts live on the GitHub Release for `v0.5.0-alpha.N`
- presents those artifacts as the main evaluation/download surface

Recommended revision options:

Option A, preferred:
- retain this page as an explicit historical or evaluator-only page
- add strong front-matter language that it describes alpha evaluation artifacts, not the canonical Milestone 1 install path
- add a prominent pointer to the Ubuntu native install docs

Option B:
- replace with a broader “evaluation channels” page that explicitly subordinates these artifacts to the native route

Priority:
- very high

### 5.2 `unison-docs/dev/releases/alpha-0.5.0.md`

Status:
- **Conflicting**

Current issue:
- defines alpha acceptance as requiring install success on all targets: WSL2, Linux VM, bare-metal ISO installer
- defines the alpha GitHub Release artifact set as mandatory WSL, VM, and ISO outputs

Why this matters:
- this is the strongest single remaining artifact-contract document that conflicts with the new Milestone 1 native-first strategy

Recommended revision:
- revise the alpha release contract so it distinguishes:
  - primary supported artifact / install route
  - optional evaluator artifacts
- change “must include all artifacts” language to milestone-appropriate release requirements
- align acceptance gates with the supported install path first

Priority:
- critical

### 5.3 `unison-docs/dev/release-and-branching.md`

Status:
- **Partially aligned**

Current issue:
- says GitHub Releases include images (WSL/VM/ISO) from `images/`
- says release workflow packages WSL/VM/ISO artifacts and attaches them to releases on tags
- does not clearly distinguish supported versus evaluation channels

Recommended revision:
- keep the technical truth that the workflow may package these assets
- add milestone-aware framing:
  - native installer path is primary
  - image outputs are evaluator channels unless explicitly promoted
- align terminology with the Milestone 1 artifact strategy

Priority:
- high

### 5.4 `unison-docs/dev/deployment/install-wsl2.md`

Status:
- **Partially aligned**

Current issue:
- useful as an evaluation doc, but currently reads like a straightforward install target doc

Recommended revision:
- prepend an explicit note that WSL2 is an evaluation-only channel for Milestone 1
- point readers first to Ubuntu native if they want the supported install route

Priority:
- medium

### 5.5 `unison-docs/dev/deployment/install-linux-vm.md`

Status:
- **Partially aligned**

Recommended revision:
- same as WSL2 doc: explicitly label evaluation-only and point to native install first

Priority:
- medium

### 5.6 `unison-docs/dev/deployment/install-bare-metal.md`

Status:
- **Partially aligned**

Recommended revision:
- explicitly label this as evaluation-only for Milestone 1 unless the program decides to promote it later
- point to Ubuntu native as the supported route

Priority:
- medium

## 6. Pages That Are Fine To Leave Mostly Alone

These pages mention WSL2 or artifacts in developer context but are not the main source of release/install ambiguity:

- `project-unisonos.github.io/docs/developers/get-started.md`
- `project-unisonos.github.io/docs/developers/prerequisites.md`
- `project-unisonos.github.io/docs/developers/devstack.md`
- `unison-docs/dev/developer-guide.md`
- `unison-docs/dev/hardware-deployment-guide.md`

These may still deserve wording cleanup later, but they are not the highest-risk sources of install-strategy confusion.

## 7. Recommended Revision Order

### Phase 1: Fix the strategy-defining conflicts

1. `unison-docs/dev/releases/alpha-0.5.0.md`
2. `unison-docs/dev/releases/evaluate-alpha.md`
3. `project-unisonos.github.io/docs/developers/releases.md`
4. `project-unisonos.github.io/docs/developers/images-builds-and-releases.md`
5. `unison-docs/dev/release-and-branching.md`

### Phase 2: Fix evaluator-install page framing

6. `unison-docs/dev/deployment/install-wsl2.md`
7. `unison-docs/dev/deployment/install-linux-vm.md`
8. `unison-docs/dev/deployment/install-bare-metal.md`
9. `project-unisonos.github.io/docs/developers/onboarding.md`
10. `project-unisonos.github.io/docs/developers/hardware.md`

## 8. Recommended Wording Pattern

Use a consistent framing pattern across docs:

### Supported route wording

- "For the current Milestone 1 production-track release, the supported installation target is Ubuntu 24.04 native on x86_64."
- "The canonical install path is the Ubuntu native installer in `unison-platform`."

### Evaluation route wording

- "WSL2, Linux VM, and bare-metal image artifacts remain evaluation-only channels for Milestone 1."
- "These artifacts may be useful for demos, hardware exploration, and developer evaluation, but they are not the canonical supported install path."

### Release-asset wording

- "Release assets may include evaluator images and supporting manifests/checksums, but the supported installation route should be foregrounded first in all install and release documentation."

## 9. Concrete Next Step

The next docs-only implementation pass should:

- update the five highest-priority pages first
- avoid changing technical claims about what the release workflow can build
- change framing, ordering, and labels so the supported install route is unmistakable

## 10. Bottom Line

The installable-product direction is already visible in the repos.

What still needs work is documentation convergence.

The highest-value docs change is not inventing a new strategy.
It is making every install and release surface tell the same story:

- one supported Milestone 1 install route
- several evaluator channels
- one clear user expectation
