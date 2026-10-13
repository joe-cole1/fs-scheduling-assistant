# Build and publish the operator downloads

Operators use the root README's **latest release** links, download a named ZIP and open START HERE.docx. This page is for repository maintainers. GitHub Actions builds and publishes the files; nothing runs on a squadron computer or inside GenAI.mil.

## Publish a release

The normal release path is a single manual GitHub Actions workflow. **Do not manually create a tag or click Publish release first.**

1. **Prepare the source change in a PR.** Update `packaging/update-note.md`, CHANGELOG.md and `packaging/version.txt`. The version file is the intended stable release identity. If a persistent installed artifact changes, also update `packaging/persistent-artifacts.json` and append the required migration record.
2. **Review and merge.** The PR runs **Validate operator packages** and **Validate GitHub workflows** when applicable. Package validation checks persistent-state declarations, builds both ZIPs twice, byte-compares them, checks package integrity, the task-file contract and source coverage, and runs the regression tests, including contract coverage. Visual Word review and GenAI.mil/operational validation remain separate when applicable.
3. **Open Actions → Publish release → Run workflow.** Leave the workflow branch on the repository default branch (`main`). Normally leave **Version** blank; the workflow uses the stable version already committed in `packaging/version.txt`. If you enter Version as an extra confirmation, it must exactly match the source version.
4. **Let the workflow own the transaction.** It validates the source-controlled version, current default-branch commit and release slot, builds and checks the packages twice, runs regression tests, generates the release notes, creates or resumes a matching **draft** release, uploads every release asset with bounded transient-failure retries, verifies existing/uploaded bytes, writes the final notes, and only then publishes the draft.
5. **Confirm the workflow is green before distribution.** The published release should already contain `Panton_Scheduling_Assistant.zip`, `Update.zip`, `manifest.json`, `SHA256SUMS.txt`, generated release notes and download links. GitHub's automatic Source code archives are not the operator kit.

With immutable releases enabled, publication is intentionally the **last** mutation. Users should never see a newly published release waiting for its operator ZIPs to appear.

## Source-controlled version selection

`packaging/version.txt` is the release identity prepared and reviewed with the source change. A blank Version field means **use that source version**. An entered Version is only an additional confirmation and must exactly match `packaging/version.txt`; it is not an override.

This prevents a workflow run from silently assigning a package number that disagrees with the source, update note or change log. Intentional patch, minor or major changes are made by changing `packaging/version.txt` in the reviewed PR. Stable semantic versions are required; prerelease suffixes are rejected by the normal publish workflow.

All publish runs share one concurrency group so release transactions cannot race each other.

## Failure and retry behavior

The workflow is designed to fail safely:

- **Before draft creation:** no release is published. Fix the cause and rerun. A blank Version field continues to resolve to the same source-controlled version until the source changes.
- **Transient or ambiguous asset upload failure:** HTTP 429/5xx and network failures receive bounded retries. Before another upload POST, the workflow re-reads the draft. If GitHub actually saved the expected asset, its bytes are verified and the workflow continues without uploading a duplicate. If GitHub left an incomplete expected asset such as a `starter` placeholder, that incomplete asset is deleted before retry. Differing completed assets are never overwritten.
- **After draft creation but before publication:** the matching release remains a mutable draft. Rerun from the same source version. The workflow removes only incomplete expected upload placeholders, verifies completed draft asset bytes and uploads only missing files.
- **Different draft bytes, unexpected assets, changed source, or changed tag target:** the workflow stops rather than overwrite or reinterpret the draft.
- **Already-published release:** the workflow refuses to repair, replace or mutate it. Published immutable releases and tags are never moved. Use a new source version.

Do not manually publish an in-progress draft while the workflow is incomplete. If a draft represents an abandoned source/version, inspect and delete that draft manually; a different source-controlled version does not reuse it.

The failed `v0.5.2` publish-then-build run is the historical example of why this workflow is draft-first: GitHub made the release immutable immediately, while the assets had not yet been attached.

## Release notes

Release notes are generated before publication. The workflow composes:

- **What changed** from the released commit's `packaging/update-note.md`;
- **What you need to do** from the standard install/update procedure plus any migration introduced in that version;
- **Validation and known limitations** from the checks that actually passed in the release workflow, while explicitly separating Word/model/operational validation;
- **Changes and contributors** from GitHub's generated release notes; and
- a generated **Downloads / Build verification** block with asset links, source commit and SHA-256 checksums.

See `packaging/release-notes-template.md` for the maintained structure. No manual release-note drafting is required in the normal path. Keep `packaging/update-note.md` accurate and user-facing, and avoid hard-coding a package number into prose when the generated release metadata already provides it.

## Release version and source authority

The source tree is authoritative for both release contents and release identity. The workflow reads the stable version from `packaging/version.txt` on the exact default-branch commit being released. An explicit workflow Version must match that value or publication stops before release creation/modification.

The exact default-branch commit validated at workflow start is the release source. The workflow refuses to run from another selected workflow ref. Before publication it creates/resumes only a draft tied to that exact source commit and source version. It never moves an existing tag.

This preserves source integrity with zero routine version entry:

- `packaging/version.txt` must contain a valid stable semantic version;
- an explicitly entered Version must match it exactly;
- the workflow must be run from the default branch;
- the current source commit must satisfy its reproducibility/dependency contract;
- a same-version published release is a hard stop;
- a same-version draft is resumable only under the documented safe-retry rules;
- an existing tag without the matching draft is a hard stop; and
- all assets are byte-verified before publication.

## Reproducible package format

`packaging/reproducibility.json` defines package format 1. It pins:

- CPython `3.12.14`;
- the SHA-256 of `packaging/requirements.txt`;
- stored ZIP members (`archive_mode: stored`) for generated DOCX containers and outer operator ZIPs; and
- a deterministic metadata sentinel of **1980-01-01 00:00:00 UTC**.

The 1980 value is intentionally not a release/build/install date. Operators identify an installed kit by the "Kit version" line in each task file and the package number in Word document headers.

Both PR validation and release publication build the packages twice and compare the generated ZIPs/manifest byte-for-byte. The package checker also validates ZIP/DOCX structure, metadata, the task-file contract, source coverage, operator jargon, update contents and update/rollback preservation.

`v0.4.1` remains the documented legacy dependency exception. Later releases use the reproducibility contract present in the exact source commit being released.

## Workflow validation

Two read-only PR/main checks cover different risks:

- **Validate GitHub workflows** runs checksum-pinned actionlint when workflow definitions change.
- **Validate operator packages** runs for package/release-workflow-affecting sources. It validates persistent-state declarations, builds both operator downloads twice, byte-compares them, checks package integrity and source coverage, and runs the package/release regression tests. It does not publish anything.

A green hosted gate verifies repository/build behavior, not native Word rendering, GenAI.mil instruction-following or operational readiness.

## Persistent installed-state migrations

`packaging/persistent-artifacts.json` declares what survives a routine update:
- the Pantons profile and the Squadron Rules frame (together they make Squadron Rules.docx)
- the input checklist
- the weekly folder layout

Source-backed entries store their current Git blob fingerprint. Artifacts that are no longer installed stay registered with `retired_in`, so migration history remains valid.

A persistent installed-state change requires an explicit package-version change and an append-only migration declaration. When an unsuperseded migration exists, `Update.zip` carries **READ ME - Squadron Rules changes.docx**. It holds the instructions plus reference-only copies for human review and merge, and never replaces Squadron Rules or weekly work automatically.

## Installed layout, updates and rollback

| Folder or file | Contents | Update/rollback behavior |
| --- | --- | --- |
| START HERE.docx | One page: the 4 moves, which task file for which day, update steps | Replaced by an update or a prior-release rollback |
| TASK FILES | 8 self-contained task files | Deleted, then replaced from the update; contains no human work |
| Squadron Rules.docx | Human-maintained Pantons rules, reference index and DO-approved lessons | Never in an update; preserved and never automatically rolled back |
| WEEKS/_COPY ME - New week | INPUT CHECKLIST.docx, empty Inputs and Schedules | Preserved; the checklist is a registered persistent artifact |
| WEEKS/Week of date | Inputs, Schedules and saved WEEK FILEs | Never included in an update or rollback |
| READ ME - Squadron Rules changes.docx (when present) | Migration instructions and reference copies | Read, act on what applies, then delete |

For rollback, download the exact prior release's `Update.zip`, delete TASK FILES, and copy that update in. Squadron Rules, weekly folders, WEEK FILEs, approvals and completed actuals are untouched.

## Sources and local build

- `kit/core.md`: shared instructions in every task file.
- `kit/tasks/`: one step-by-step script per task.
- `kit/week-file.md`: the WEEK FILE format.
- `kit/start-here.md`, `kit/input-checklist.md`: operator Word documents.
- `kit/squadron-rules.md` + `../local-profiles/pantons.md`: Squadron Rules.docx.
- `version.txt`: reviewed stable release/package identity used by the publish workflow.
- `update-note.md`: release/change summary used for release notes.
- `release-notes-template.md`: explanation of the generated release-note structure.
- `persistent-artifacts.json`: persistent-state fingerprints, weekly-folder layout and migration history.
- `reproducibility.json` / `requirements.txt`: package runtime/dependency contract.
- `../scripts/build_packages.py` and `check_packages.py`: deterministic generation and package checks. Each task file is assembled as: the no-delegation guard, a header, `core.md`, the task script, `week-file.md` and the end marker. Each must stay plain ASCII and within the size budget.
- `../scripts/prepare_release.py`: reads and validates the source version and any explicit confirmation, checks the default-branch source, and checks the resumable release slot. It publishes nothing.
- `../scripts/release_packages.py`: generates release notes, creates or resumes the draft, safely retries and reconciles asset uploads, verifies assets and performs the final publication.

From the repository root, use CPython 3.12.14:

```sh
python -m pip install -r packaging/requirements.txt
python scripts/check_persistent_migrations.py
python scripts/build_packages.py --output /path/to/temporary/package-output
python scripts/check_packages.py /path/to/temporary/package-output
python -m unittest discover -s tests -v
```

The temporary output has a `build` folder and `downloads` with both ZIPs and the manifest. Keep generated files out of Git. Render START HERE (one page), the input checklist and Squadron Rules for visual review when they change.

A new non-negotiable rule needs a phrase in `tests/test_contract_coverage.py`, so the compressed task files are proven to carry it. Native Word and GenAI.mil behavior need separate validation; build success is not proof of operational readiness.

Migration history stays append-only. An appended consolidated migration may name earlier IDs in `supersedes` only if it covers all their artifacts.

GitHub Releases retain past versions and source tags. There are no current-tree archive folders or committed ZIP copies. For a fork, update the repository URLs in the root README before distribution.
