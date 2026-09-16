# Build and publish the operator downloads

Operators use the root README's **latest release** links, download a named ZIP and open START HERE.docx. This page is for repository maintainers. GitHub Actions builds and publishes the files; nothing runs on a squadron computer or inside GenAI.mil.

## Publish a release

The normal release path is a single manual GitHub Actions workflow. **Do not manually create a tag or click Publish release first.**

1. **Prepare the source change in a PR.** Update `packaging/update-note.md` and CHANGELOG.md. If a persistent installed artifact changes, also update `packaging/persistent-artifacts.json` and append the required migration record. `packaging/version.txt` is the local/development default and should normally be advanced with the source change, but the version entered in the release workflow is the release/package identity.
2. **Review and merge.** The PR runs **Validate operator packages** and **Validate GitHub workflows** when applicable. Package validation checks persistent-state declarations, builds all three ZIPs twice, byte-compares them, checks package integrity/source coverage and runs regression tests. Visual Word review and GenAI.mil/operational validation remain separate when applicable.
3. **Open Actions → Publish release → Run workflow.** Leave the workflow branch on the repository default branch (`main`). Enter the version **without** a leading `v`, for example `0.5.3`.
4. **Let the workflow own the transaction.** It validates the current default-branch commit and release slot, builds and checks the packages twice, runs regression tests, generates the release notes, creates or resumes a matching **draft** release, uploads every release asset, verifies existing/uploaded bytes, writes the final notes, and only then publishes the draft.
5. **Confirm the workflow is green before distribution.** The published release should already contain `Pantons_Setup.zip`, `First_Time_Squadron_Setup.zip`, `Update_Existing_Setup.zip`, `manifest.json`, `SHA256SUMS.txt`, generated release notes and download links. GitHub's automatic Source code archives are not the operator kit.

With immutable releases enabled, publication is intentionally the **last** mutation. Users should never see a newly published release waiting for its operator ZIPs to appear.

## Failure and retry behavior

The workflow is designed to fail safely:

- **Before draft creation:** no release is published. Fix the cause and rerun the same version.
- **After draft creation but before publication:** the matching release remains a mutable draft. Rerun the same version. The workflow verifies any existing draft asset bytes and uploads only missing files.
- **Different draft bytes, unexpected assets, changed source, or changed tag target:** the workflow stops rather than overwrite or reinterpret the draft.
- **Already-published release:** the workflow refuses to repair, replace or mutate it. Published immutable releases and tags are never moved. Use a new version.

Do not manually publish an in-progress draft while the workflow is incomplete. If a draft requires human cleanup because its source/version is wrong, inspect it before deciding whether to delete the draft and unused tag or choose a new version.

The failed `v0.5.2` publish-then-build run is the historical example of why this workflow is draft-first: GitHub made the release immutable immediately, while the assets had not yet been attached.

## Release notes

Release notes are generated before publication. The workflow composes:

- **What changed** from the released commit's `packaging/update-note.md`;
- **What you need to do** from the standard install/update procedure plus any migration introduced in that version;
- **Validation and known limitations** from the checks that actually passed in the release workflow, while explicitly separating Word/model/operational validation;
- **Changes and contributors** from GitHub's generated release notes; and
- a generated **Downloads / Build verification** block with asset links, source commit and SHA-256 checksums.

See `packaging/release-notes-template.md` for the maintained structure. No manual release-note drafting is required in the normal path, but `packaging/update-note.md` must be accurate and user-facing before merge.

## Release version and source authority

The maintainer enters one value, such as `0.5.3`. The workflow derives tag `v0.5.3` and injects `0.5.3` only into the disposable build workspace.

The exact default-branch commit validated at workflow start is the release source. The workflow refuses to run from another selected workflow ref. Before publication it creates/resumes only a draft tied to that exact source commit. It never moves an existing tag.

This gives one human version selection while preserving source integrity:

- the requested version must be valid;
- the workflow must be run from the default branch;
- the current source commit must satisfy its reproducibility/dependency contract;
- a same-version published release is a hard stop;
- a same-version draft is resumable only when it targets the same source commit;
- an existing tag without the matching draft is a hard stop; and
- all assets are verified before publication.

## Reproducible package format

`packaging/reproducibility.json` defines package format 1. It pins:

- CPython `3.12.14`;
- the SHA-256 of `packaging/requirements.txt`;
- stored ZIP members (`archive_mode: stored`) for generated DOCX containers and outer operator ZIPs; and
- a deterministic metadata sentinel of **1980-01-01 00:00:00 UTC**.

The 1980 value is intentionally not a release/build/install date. Operators identify an installed System by the package number printed in generated document headers.

Both PR validation and release publication build the packages twice and compare the generated ZIPs/manifest byte-for-byte. The package checker also validates ZIP/DOCX structure, metadata, source coverage, common System contents and update/rollback preservation.

`v0.4.1` remains the documented legacy dependency exception. Later releases use the reproducibility contract present in the exact source commit being released.

## Workflow validation

Two read-only PR/main checks cover different risks:

- **Validate GitHub workflows** runs checksum-pinned actionlint when workflow definitions change.
- **Validate operator packages** runs for package/release-workflow-affecting sources. It validates persistent-state declarations, builds all operator downloads twice, byte-compares them, checks package integrity/source coverage and runs the package/release regression tests. It does not publish anything.

A green hosted gate verifies repository/build behavior, not native Word rendering, GenAI.mil instruction-following or operational readiness.

## Persistent installed-state migrations

`packaging/persistent-artifacts.json` declares files/layout that survive a routine System update: profile seeds, stable-reference/playbook templates and the reusable weekly-folder layout. Source-backed entries store their current Git blob fingerprint.

Persistent installed-state changes require an explicit package-version change and append-only migration declaration. The update ZIP may include **PERSISTENT MIGRATIONS.docx** and reference-only comparison copies. These are instructions/material for human review, never automatic replacements for Local Guidance or weekly work.

## Installed layout, updates and rollback

| Folder or file | Contents | Update/rollback behavior |
| --- | --- | --- |
| START HERE.docx | Short day/step entry instructions | Replaced by an update or prior-release rollback |
| System | Startup, day-based Instructions, Blank Forms, Reference | Replaced next week; same replaceable surface for rollback |
| Local Guidance | Human-maintained profile, references and playbook | Preserved; never automatically rolled back |
| COPY THIS FOLDER FOR EACH NEW WEEK | Empty Inputs, Schedules, Working Record | Preserved; layout changes require a declared migration |
| Week of date | Weekly sources, schedules and records | Never included in update/rollback |
| PERSISTENT MIGRATIONS.docx (when present) | Persistent-state review instructions | Read from temporary update; do not install as local policy |

For rollback, operators use **System → Instructions → 13 Update for Next Week.docx** and download the exact prior release's `Update_Existing_Setup.zip`. Replace only `System` and `START HERE`. Preserve Local Guidance, weekly schedules/records, buy/sell approvals, publication records and completed actuals.

## Sources and local build

- `guides/`: START HERE and day/step Word guide sources.
- `version.txt`: local/development build version; release workflow input is authoritative for a published package.
- `update-note.md`: release/change summary embedded in update instructions and used for release notes.
- `release-notes-template.md`: maintained explanation of automatically generated release-note structure.
- `persistent-artifacts.json`: persistent-state fingerprints, weekly-folder layout and migration history.
- `reproducibility.json` / `requirements.txt`: package runtime/dependency contract.
- `../scripts/build_packages.py` and `check_packages.py`: deterministic generation and package checks.
- `../scripts/prepare_release.py`: validates requested version, default-branch source and resumable release slot without publishing anything.
- `../scripts/release_packages.py`: generates release notes, creates/resumes the draft, verifies assets and performs the final publication.

From the repository root, use CPython 3.12.14:

```sh
python -m pip install -r packaging/requirements.txt
python scripts/check_persistent_migrations.py
python scripts/build_packages.py --output /path/to/temporary/package-output
python scripts/check_packages.py /path/to/temporary/package-output
python -m unittest discover -s tests -v
```

The temporary output has a `build` folder of DOCX documents and `downloads` with the three ZIPs and manifest. Keep generated files out of Git. Native Word/GenAI.mil behavior needs separate validation; build success is not proof of operational readiness.

GitHub Releases retain past versions/source tags. There are no current-tree archive folders or committed ZIP copies. For a fork, update repository URLs in the root README before distribution.
