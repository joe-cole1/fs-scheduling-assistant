# Repository QC record — release automation follow-up

This is the current repository-level QC record. The tagged v0.4.1 source retains its original package-specific QC record; this file was updated later to record hosted release-automation evidence and must not be read as a rewrite of the tag.

## Hosted release verification completed

The corrected **Build release downloads** workflow completed successfully in GitHub Actions on 2026-09-05:

- Workflow run: `33953154858`
- Job: `101271548225`
- Controller commit: `30df0c3a0cb6d7aa8a3ed1f335405cc5b39baadf`
- Released source/tag commit: `927790414e1b583d069baa4ad6280cebae8f928d` (`v0.4.1`)
- Hosted interpreter: CPython `3.12.14`

The hosted job checked the release/tag/version, checked out the exact tagged source, installed the packaging dependencies, built the three operator ZIPs, ran the tagged package checker, uploaded all three ZIPs plus `manifest.json` and `SHA256SUMS.txt`, verified the attached bytes, and updated the release notes. The job completed successfully without a repository branch write. This closes the earlier **Not run** status for hosted workflow execution, real release upload and real release-note mutation.

The published v0.4.1 release therefore has verified named assets. That hosted success demonstrates the release workflow path for that release. It does **not** establish native Word behavior, ChatGPT Mil instruction following, operational readiness, public releasability, or future-release reproducibility beyond the controls recorded in the relevant source.

## Workflow-definition correction

Run `33952707099` failed before a job was created. Actionlint 1.7.7 reproduced two errors in the original job-level environment definitions: `runner.temp` is not available there. The earlier YAML/shell checks did not validate GitHub context availability.

Temporary path initialization was moved into a runner step using `RUNNER_TEMP` and `GITHUB_ENV`. Actionlint then passed on both the corrected release workflow and PR validation workflow. The correction did not alter the v0.4.1 scheduling documents or tagged package contents.

## Checks performed before hosted publication

- Confirmed the local starting files matched the reviewed v0.4.1 source and that the published v0.4.1 release initially had no attached assets.
- Ran the release regression suite with synthetic data. Covered unsafe/mismatched tags, draft and immutable releases, tagged source versus unmerged source, wrong build versions, checksum/inventory mismatches, duplicate assets, partial-upload recovery, moved tags, preservation of human notes, generated PR notes and repeatable generated note sections. Publication calls were mocked; source ancestry used a disposable local Git repository.
- Parsed the workflow YAML and checked publication/manual triggers, scoped contents permissions, pinned action commits and shell syntax. Event-provided values were passed through environment variables and validated rather than interpolated into shell code. The release token was supplied only to release-API steps.
- Rebuilt all three ZIPs and passed package integrity, inventory, Word geometry, shared-System consistency, local-policy separation, source coverage and manual-update preservation checks.
- Compared the generated v0.4.1 ZIPs and manifest with the previously rendered/reviewed package outputs: byte-identical before publication.
- Checked relative Markdown links and fenced blocks. README distinguished named operator assets from GitHub's automatic source archives.
- Kept generated ZIPs/manifest out of the current repository tree. No archive folder or branch writeback was added.

See [release instructions](../../packaging/README.md), [release regression tests](../../tests/test_release_packages.py) and [package checks](../../scripts/check_packages.py).

## Tagged v0.4.1 historical record

The `v0.4.1` tag contains `docs/v0.4/repository-qc.md` as it existed when that release source was reviewed. That tagged record documents the package/Word checks that supported the release and correctly records the platform behaviors that had not been run at tag time. Later hosted automation evidence belongs in this current repository record rather than changing the tag or its release assets.

## Still not run

Native Microsoft Word testing on a squadron computer, actual ChatGPT Mil DOCX ingestion/instruction following, the 24 behavioral cases, four setup cases, historical blind trials and operational validation remain **Not run** until humans execute and record them on the target environment. Their [validation plan](validation-plan.md) remains applicable.

Publishing or successfully rebuilding a release makes no claim of operational approval, local-policy approval or public releasability. Human reviewers decide adoption and release suitability using the evidence actually available.
