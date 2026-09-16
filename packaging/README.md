# Build and publish the operator downloads

Operators use the root README's **latest release** links, download a named ZIP and open START HERE.docx. This page is for the person maintaining the repository. GitHub Actions builds the files; nothing runs on a squadron computer or inside GenAI.mil.

## Publish a release

1. **Prepare the source change in a PR.** Update `packaging/update-note.md` and CHANGELOG.md for the release contents. `packaging/version.txt` remains useful for local/development builds, but it is **not** release authority. If a persistent installed artifact changes, also update `packaging/persistent-artifacts.json` and its migration record as required by the package checks.
2. **Review before publishing.** The PR runs **Validate operator packages**, which installs the pinned dependencies, validates persistent-state declarations, builds all three ZIPs twice, byte-compares them, checks package integrity/source coverage and runs the regression suite. A green hosted gate does not replace visual review: render/review new or changed Word pages and record actual model/operational validation separately. Merge the reviewed source changes into the default branch. Do not commit generated ZIPs.
3. **On GitHub, open Releases → Draft a new release.** Choose the release tag/version you want, such as `v0.5.2`, on the reviewed default-branch commit. **That release tag is the authoritative package version.** A tag identifies both the source that will be built and the version printed into the generated package. Do not move an old tag to new content.
4. **Write the release notes.** Use [the short template](release-notes-template.md) and keep its exact **What changed**, **What you need to do**, and **Validation and known limitations** headings. Click **Generate release notes** to add merged PRs, contributor credits and the full comparison link below your human summary. Review the result. If those three headings are absent, the release workflow preserves the text but explicitly states that no structured human validation summary was present; generated PR notes are not treated as validation evidence.
5. **Click Publish release.** For normal squadron distribution, publish a full release and mark it Latest. The **Build release downloads** workflow validates the tag/build contract, builds and checks all three ZIPs from that exact tagged commit, injects the release tag's version into the disposable build workspace, uploads the assets plus manifest/checksums, then adds verified download links to the notes. Your written notes are preserved. Publishing alone does not establish that the build succeeded.
6. **Confirm the green workflow result before distribution.** Verify the three named ZIPs appear under Assets and the README downloads work. The automatic **Source code** ZIP/tar.gz is not the operator kit. If the job fails, use the recovery directions below.

The release is visible while the build runs, so its download links may briefly be unavailable. This is the explicitly chosen publish-then-build flow. A draft-build-then-publish flow would be necessary if assets must exist at the instant of publication or if immutable releases are enabled. Do not disable immutability or weaken repository controls to work around a failure. The workflow reports an immutable release with missing assets before attempting an upload.

Publication retains the repository's visibility; it does not make a private repository public. Users still need access or a human-provided copy in an approved shared location. Human review controls releasability, and no actual operational products belong in the repository or release notes.

## Release version authority

For GitHub Releases, the published tag is the single source of truth for package identity. A release tagged `v0.5.2` builds package `0.5.2` even if the tagged source's `packaging/version.txt` contains a different local-build value. The workflow writes the validated tag version only into the temporary `release-source/packaging/version.txt` checkout before running the tagged builder/checker. It does not change the tag, commit, repository branch or published source archive.

This preserves the useful integrity controls without requiring two independent human version selections:

- the tag must be a valid version-shaped tag;
- the release must already exist and refer to that tag;
- the tagged commit must be merged into the default branch;
- all package source other than injected release identity comes from that exact tag;
- the tagged reproducibility/dependency contract must validate;
- existing differing release assets are never overwritten.

## Fill an existing release or recover a failed build

1. Open **Actions → Build release downloads → Run workflow**.
2. Use the default branch for the workflow. Enter the existing published tag and run it.
3. Check the completed run and release Assets.

The selected tag must exist and its commit must be merged into the default branch. **It does not need to match `packaging/version.txt`; the selected release tag supplies the package version.** Both full releases and prereleases can receive assets; GitHub's Latest links select full releases. No draft is published by the workflow. Editing a published release's notes does not rebuild it.

A partial upload can be rerun: existing files are downloaded and compared, missing files are attached, and every expected file is checked again. Different existing bytes stop the run; the workflow does not replace them. For changed source or intentional changes to published content, prepare a new version. Repeated runs replace only the marked generated notes section, retaining all text outside it.

### v0.4.1 legacy recovery

`v0.4.1` predates the tagged reproducibility contract. Its successful hosted asset build used CPython `3.12.14`, the original DEFLATE-based tagged builder, and the dependency versions now frozen in `packaging/legacy/v0.4.1-requirements.txt`. The release controller recognizes **only** exact tag `v0.4.1` as this legacy exception. Existing differing assets are still never overwritten. If a future environment cannot reproduce a missing v0.4.1 asset byte-for-byte, recovery stops rather than mutating the release.

Every later release must contain its own `packaging/requirements.txt` and `packaging/reproducibility.json`. The controller reads and validates those files from the **tagged source**, not current `main`, before building. Unsupported/missing future contracts fail explicitly.

## Reproducible package format

`packaging/reproducibility.json` defines package format 1. It pins:

- CPython `3.12.14`;
- the SHA-256 of the tagged `packaging/requirements.txt`;
- stored ZIP members (`archive_mode: stored`) for generated DOCX containers and outer operator ZIPs;
- a deterministic metadata sentinel of **1980-01-01 00:00:00 UTC**, the earliest portable ZIP timestamp.

The 1980 value is intentionally **not** a release, build, or install date. It prevents a reproducibility timestamp from looking like a real operational freshness signal. Operators identify the installed System by the package number printed in generated document headers. Filesystem/Word dates must not be used to decide which package is newer.

Stored members deliberately avoid dependency on a runner's zlib implementation. **Validate operator packages** builds twice in separate output directories and byte-compares all three ZIPs plus the manifest. The checker also enforces the sentinel on outer ZIP entries, every DOCX member, and Word created/modified core properties. A future package-format change requires an explicit controller/build update; do not silently reinterpret an old contract.

## Workflow validation

Two read-only PR/main checks cover different risks:

- **Validate GitHub workflows** runs checksum-pinned actionlint when workflow definitions change. It validates GitHub Actions expressions/context availability; plain YAML parsing is insufficient.
- **Validate operator packages** runs for package-affecting sources. It validates persistent-state declarations, builds all operator downloads twice under the exact package interpreter, byte-compares them, checks package integrity/ZIP format/metadata/Markdown-to-Word source coverage, and runs the package/release unit tests. It does not publish anything.

Local maintainers can run `actionlint -shellcheck= -pyflakes= .github/workflows/*.yml` before pushing workflow changes. A green hosted package job verifies repository/build behavior, not native Word rendering, GenAI.mil instruction following or operational readiness.

## Persistent installed-state migrations

`packaging/persistent-artifacts.json` is the maintained declaration for files/layout that survive a routine System update: the Pantons local-profile seed, generic local-profile seed, stable-reference/playbook templates and reusable weekly-folder layout. Source-backed entries store their current Git blob fingerprint. The package validation fails if one of those sources changes without updating the declaration.

On a PR, `scripts/check_persistent_migrations.py` compares the declaration with the target branch. Persistent changes remain deliberately explicit because they affect human-maintained installed state. Follow the checker-required migration declaration/version metadata for those changes; this development metadata does not override the eventual GitHub release tag.

Routine releases with no persistent change keep the current non-destructive update behavior. When actionable migration history exists, the update ZIP adds **PERSISTENT MIGRATIONS.docx** and clearly marked reference-only source copies where applicable. Those files stay in the temporary update folder; they are comparison material, not replacements for Local Guidance. The appropriate human decides whether/how to merge a policy or local-content change.

## Installed layout, updates and rollback

| Folder or file | Contents | Update/rollback behavior |
| --- | --- | --- |
| START HERE.docx | Short day/step entry instructions | Replaced by an update or prior-release rollback |
| System | Startup, day-based Instructions, Blank Forms, Reference | Replaced next week; same replaceable surface for rollback |
| Local Guidance | Human-maintained profile, references and playbook | Preserved; never automatically rolled back |
| COPY THIS FOLDER FOR EACH NEW WEEK | Empty Inputs, Schedules, Working Record | Preserved; layout changes require a declared migration |
| Week of date | Weekly sources, schedules and records | Never included in update/rollback |
| PERSISTENT MIGRATIONS.docx (when present) | Explicit persistent-state migration instructions | Read from temporary update; do not install as local policy |

For rollback, operators use **System → Instructions → 13 Update for Next Week.docx** and download the exact prior release's named `Update_Existing_Setup.zip`. They replace only `System` and `START HERE`. No local archive folder is needed because GitHub Releases retain prior named assets and source tags.

Rollback normally happens at the next-week boundary. An urgent current-week rollback must preserve all current schedule versions, decision/waiver records, buy/sell approvals, publication records, completed actuals and handoff state and must record only that the reusable System version changed. An older System package does not revoke or reinterpret human decisions. If a persistent migration was previously human-approved and merged into Local Guidance, reversing that local change requires a separate human decision; System rollback never performs it automatically.

The package checker simulates both update and rollback surfaces and verifies that local guidance/playbook plus weekly schedule/decision bytes survive both operations.

## Sources and local build

- `guides/`: START HERE and the day/step Word guide sources, including Monday inputs, Tuesday start/planning, Wednesday build, Thursday QC/optional DO review/buy-sell, post-buy/sell implementation, Friday publication, execution, handoff, update and setup-check instructions.
- `version.txt`: local/development build version. GitHub release builds override it in their temporary workspace from the authoritative release tag.
- `update-note.md`: current short change note embedded in UPDATE INSTRUCTIONS.docx.
- `persistent-artifacts.json`: persistent installed-state fingerprints, reusable weekly-folder layout and append-only migration history.
- `reproducibility.json`: tagged package-format/runtime/dependency-hash/metadata contract for releases after v0.4.1.
- `requirements.txt`: exact current packaging dependency versions. Its bytes must match the hash recorded in `reproducibility.json`.
- `legacy/v0.4.1-requirements.txt`: frozen dependency set used only by the v0.4.1 compatibility path.
- `../docs/v0.4/system-primer.md`: text between the export markers becomes UPLOAD THIS TO START.docx.
- `../templates/`: Word form sources. Wide tables become labeled records; repeated inventories become topic lists plus one reusable entry, retaining meaningful source labels/content.
- `../local-profiles/`: approved local seed for a first Pantons installation; the generic kit receives the blank profile.
- `../scripts/build_packages.py` and `check_packages.py`: deterministic generation plus package-format, metadata, source-coverage, update-preservation and rollback-preservation checks.
- `../scripts/prepare_release.py`: resolves the published tag, verifies the tagged commit/build contract and makes the tag the package-version authority.
- `../scripts/release_packages.py`: shared release integrity, tagged-contract, asset verification and release-note functions. The controller comes from the default branch; actual document builder/inputs come from the released tag.

From the repository root, use CPython 3.12.14:

```sh
python -m pip install -r packaging/requirements.txt
python scripts/check_persistent_migrations.py
python scripts/build_packages.py --output /path/to/temporary/package-output
python scripts/check_packages.py /path/to/temporary/package-output
python -m unittest discover -s tests -v
```

The temporary output has a `build` folder of DOCX documents and `downloads` with three ZIPs and a manifest. Render and inspect changed documents before release; automated structural/content checks are not visual review. Keep generated files out of Git. The release workflow adds SHA256SUMS.txt and attaches all five files to the release. It does not generate Word content from GitHub's Source code ZIP or use previously committed ZIPs.

Word design: compact reference guide, Letter/1-inch margins, Calibri 11pt, 1.25 spacing and real headings/numbering. No macros, scripts, external data connections or executables are packaged. Native Word/GenAI.mil behavior needs separate validation; build success is not proof of operational readiness.

Both full ZIPs use the same System and START HERE. Their local profile seeds differ. A routine update contains System, START HERE and UPDATE INSTRUCTIONS only. A release with a declared persistent change may additionally contain migration instructions/reference-only copies. A release never edits local policy, a shared drive or an active chat. Human approval is still required for local rule changes.

GitHub Releases retain past versions and their source tags. There are no current-tree archive folders or committed ZIP copies. For a fork, update the repository URLs in the root README to the fork's Releases page before distribution.
