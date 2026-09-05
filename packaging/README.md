# Build and publish the operator downloads

Operators use the root README's **latest release** links, download a named ZIP and open START HERE.docx. This page is for the person maintaining the repository. GitHub Actions builds the files; nothing runs on a squadron computer or inside ChatGPT Mil.

## Publish a release

1. **Prepare the source change in a PR.** For a new package version, update `packaging/version.txt`, `packaging/update-note.md` and CHANGELOG.md. Use a deliberate version such as `0.4.2`; the release tag will be `v0.4.2`. Keep the short update note accurate, including any required action or known limitation. If a persistent installed artifact changes, also update `packaging/persistent-artifacts.json`, bump the package version, and append the required migration record instead of silently changing the seed or layout.
2. **Review before publishing.** The PR runs **Validate operator packages**, which installs the pinned dependencies, validates persistent-state declarations, builds all three ZIPs, checks package integrity/source coverage and runs the regression suite. A green hosted gate does not replace visual review: render/review new or changed Word pages and record actual model/operational validation separately. Merge the reviewed source changes into the default branch. Do not commit generated ZIPs.
3. **On GitHub, open Releases → Draft a new release.** Create the matching tag on the reviewed default-branch commit. A tag identifies the source that will be built; do not move an old tag to new content.
4. **Write the release notes.** Use [the short template](release-notes-template.md) for what changed, what users do and validation/limitations. Click **Generate release notes** to add merged PRs, contributor credits and the full comparison link. Review the result. `.github/release.yml` groups labeled PRs and includes unlabeled PRs under Other changes. Labels are optional; no label setup is required to publish.
5. **Click Publish release.** For normal squadron distribution, publish a full release and mark it Latest. The **Build release downloads** workflow builds and checks all three ZIPs from that tag, uploads them plus a manifest/checksums, then adds verified download links to the notes. Your written notes are preserved. Publishing alone does not establish that the build succeeded.
6. **Wait for the green workflow result.** Confirm the three named ZIPs appear under Assets and the README downloads work before distributing the release. The automatic **Source code** ZIP/tar.gz is not the operator kit. If the job fails, use the recovery directions below.

The release is visible while the build runs, so its download links may briefly be unavailable. This is the explicitly chosen publish-then-build flow. A draft-build-then-publish flow would be necessary if assets must exist at the instant of publication or if immutable releases are enabled. Do not disable immutability or weaken repository controls to work around a failure. The workflow reports an immutable release with missing assets before attempting an upload.

Publication retains the repository's visibility; it does not make a private repository public. Users still need access or a human-provided copy in an approved shared location. Human review controls releasability, and no actual operational products belong in the repository or release notes.

## Fill an existing release or recover a failed build

After this workflow has been merged into the default branch:

1. Open **Actions → Build release downloads → Run workflow**.
2. Use the default branch for the workflow. Enter the existing published tag, such as **v0.4.1**, and run it.
3. Check the completed run and release Assets. This also fills the already-published v0.4.1 release, which predates the workflow. Merely merging the workflow will not replay its old publication event.

The selected tag must exist, be merged into the default branch, and match `packaging/version.txt` at that tag. Both full releases and prereleases can receive assets; GitHub's Latest links select full releases. No draft is published by the workflow. Editing a published release's notes does not rebuild it.

A partial upload can be rerun: existing files are downloaded and compared, missing files are attached, and every expected file is checked again. Different existing bytes stop the run; the workflow does not replace them. For changed source or intentional changes to published content, prepare a new version. Repeated runs replace only the marked generated notes section, retaining the human-written text.

The workflow needs GitHub Actions enabled and its `GITHUB_TOKEN` allowed to write release contents. It requests only `contents: write`, has no branch writes and uses no personal token. Organization/repository restrictions remain in force. A failure leaves the logs available and does not falsely mark downloads as ready. Do not distribute a partial release.

## Workflow validation

Two read-only PR/main checks cover different risks:

- **Validate GitHub workflows** runs checksum-pinned actionlint when workflow definitions change. It validates GitHub Actions expressions/context availability; plain YAML parsing is insufficient.
- **Validate operator packages** runs for package-affecting sources. It validates persistent-state declarations, builds all operator downloads, checks package integrity and Markdown-to-Word source coverage, and runs the package/release unit tests. It does not publish anything.

Local maintainers can run `actionlint -shellcheck= -pyflakes= .github/workflows/*.yml` before pushing workflow changes. A green hosted package job verifies repository/build behavior, not native Word rendering, ChatGPT Mil instruction following or operational readiness.

## Persistent installed-state migrations

`packaging/persistent-artifacts.json` is the maintained declaration for files/layout that survive a routine System update: the Pantons local-profile seed, generic local-profile seed, stable-reference/playbook templates and reusable weekly-folder layout. Source-backed entries store their current Git blob fingerprint. The package validation fails if one of those sources changes without updating the declaration.

On a PR, `scripts/check_persistent_migrations.py` compares the declaration with the target branch. A persistent change must:

1. bump `packaging/version.txt`;
2. update the affected artifact declaration;
3. append, never rewrite, a migration record covering every changed persistent artifact; and
4. provide explicit review/merge instructions when human action is required.

Routine releases with no persistent change keep the current non-destructive update behavior. When actionable migration history exists, the update ZIP adds **PERSISTENT MIGRATIONS.docx** and clearly marked reference-only source copies where applicable. Those files stay in the temporary update folder; they are comparison material, not replacements for Local Guidance. The appropriate human decides whether/how to merge a policy or local-content change.

## Sources and local build

- `guides/`: START HERE and numbered Word guide sources, including activation, phase and handoff prompts.
- `version.txt`: the package version, checked against the release tag.
- `update-note.md`: the current short change note embedded in UPDATE INSTRUCTIONS.docx. Update it for each deliberate package release.
- `persistent-artifacts.json`: persistent installed-state fingerprints, reusable weekly-folder layout and append-only migration history.
- `requirements.txt`: exact packaging dependency versions; Python 3.12 is used in Actions.
- `../docs/v0.4/system-primer.md`: text between the export markers becomes UPLOAD THIS TO START.docx.
- `../templates/`: Word form sources. Wide tables become labeled records; repeated inventories become topic lists plus one reusable entry, retaining meaningful source labels/content.
- `../local-profiles/`: approved local seed for a first Pantons installation; the generic kit receives the blank profile.
- `../scripts/build_packages.py` and `check_packages.py`: deterministic generation plus package, source-coverage and update-preservation checks.
- `../scripts/check_persistent_migrations.py`: persistent fingerprint and PR migration-declaration enforcement.
- `../scripts/release_packages.py`: release identity/version checks, asset verification and release-note assembly. The workflow controller comes from the default branch; the actual document builder and inputs come from the released tag. Older v0.4.1 lacks a dependency file and uses the controller's pinned dependencies as an explicit compatibility fallback.

From the repository root:

```sh
python -m pip install -r packaging/requirements.txt
python scripts/check_persistent_migrations.py
python scripts/build_packages.py --output /path/to/temporary/package-output
python scripts/check_packages.py /path/to/temporary/package-output
python -m unittest discover -s tests -v
```

The temporary output has a `build` folder of DOCX documents and `downloads` with three ZIPs and a manifest. Render and inspect changed documents before release; the automated structural/content checks are not visual review. Keep generated files out of Git. The release workflow adds SHA256SUMS.txt and attaches all five files to the release. It does not generate Word content from GitHub's Source code ZIP or use previously committed ZIPs.

Word design: compact_reference_guide, Letter/1-inch margins, Calibri 11pt, 1.25 spacing and real headings/numbering. No macros, scripts, external data connections or executables are packaged. Native Word/ChatGPT Mil behavior needs separate validation; build success is not proof of operational readiness.

## Installed layout and updates

| Folder or file | Contents | Update behavior |
| --- | --- | --- |
| START HERE.docx | Short entry instructions | Replaced |
| System | Startup, Instructions, Blank Forms, Reference | Replaced next week |
| Local Guidance | Human-maintained profile, references and playbook | Preserved; persistent migrations are human-reviewed/merged, never automatic |
| COPY THIS FOLDER FOR EACH NEW WEEK | Empty Inputs, Schedules, Working Record | Preserved; layout changes require a declared migration |
| Week of date | Weekly sources, schedules and records | Never included in update |
| PERSISTENT MIGRATIONS.docx (when present) | Explicit persistent-state migration instructions | Read from temporary update; do not install as local policy |

Both full ZIPs use the same System and START HERE. Their local profile seeds differ. A routine update contains System, START HERE and UPDATE INSTRUCTIONS only. A release with a declared persistent change may additionally contain the migration instructions/reference-only copies described above. Users extract the update separately and replace System when beginning next week's planning. A release never edits local policy, a shared drive or an active chat. Human approval is still required for local rule changes.

GitHub Releases retain past versions and their source tags. There are no current-tree archive folders or committed ZIP copies. For a fork, update the repository URLs in the root README to the fork's Releases page before distribution.
