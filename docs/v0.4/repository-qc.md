# Repository QC record — release automation follow-up

Reviewed 2026-09-05 against main commit `927790414e1b583d069baa4ad6280cebae8f928d` (merged Word-package PR #4). This change automates distribution of the existing v0.4.1 package. It does not revise scheduling behavior or establish operational readiness.

## Workflow-definition correction

Run [33952707099](https://github.com/joe-cole1/fs-scheduling-assistant/actions/runs/33952707099) failed before a job was created. Actionlint 1.7.7 reproduced two errors in the original job-level environment definitions: `runner.temp` is not available there. The earlier YAML/shell checks did not validate GitHub context availability.

Moved temporary path initialization into a runner step using RUNNER_TEMP and GITHUB_ENV. Actionlint passes on both the corrected release workflow and the new PR validation workflow. The new validation job pins the linter archive checksum. The 13 release regression tests still pass. No package source or Word content changed; release execution/upload remains unverified until a corrected hosted run completes.

## Checks performed before the correction

- Confirmed the local starting files matched the current main tree. Confirmed v0.4.1 already existed as a published, mutable release with no attached assets; documented the manual backfill path.
- Ran 13 release regression tests with synthetic data. Covered unsafe/mismatched tags, draft and immutable releases, tagged source versus unmerged source, wrong build versions, checksum/inventory mismatches, duplicate assets, partial-upload recovery, moved tags, preservation of human notes, generated PR notes and repeatable generated note sections. Publication calls were mocked; source ancestry used a real disposable local Git repository.
- Parsed the workflow YAML and checked publication/manual triggers, scoped contents permissions, pinned action commits and shell syntax. Event-provided values are passed through environment variables and validated, rather than interpolated into shell code. The release token is supplied only to the steps that access release APIs.
- Rebuilt all three ZIPs and passed package integrity, inventory, Word geometry, shared-System consistency, local-policy separation, source coverage and manual-update preservation checks.
- Compared the complete generated ZIPs and manifest with the previously rendered/reviewed v0.4.1 outputs: byte-identical. Moving the update note into its own source file changes no Word pages; no new visual pass is claimed or needed for identical files.
- Checked relative Markdown file links and fenced blocks. README now points to latest-release assets and distinguishes named operator ZIPs from GitHub's automatic source archives.
- Removed generated ZIPs/manifest from the current tree and ignored future generated output. No archive folder or branch writeback was added. The approved local profile, primer, operator guides and forms remain unchanged.

See [release instructions](../../packaging/README.md), [regression tests](../../tests/test_release_packages.py) and [package checks](../../scripts/check_packages.py).

## Not run

A hosted GitHub Actions run, real release upload and real release-note mutation remain **Not run** until the workflow is merged and triggered. Local/mock tests do not prove repository permissions or hosted-service behavior. The existing v0.4.1 release is not automatically replayed when the workflow is merged; use the documented manual trigger to fill it.

Native Word on a squadron computer, ChatGPT Mil ingestion/instruction following, the 24 behavior cases, four setup cases and historical/operational trials remain **Not run**. Their [validation plan](validation-plan.md) remains applicable. Publishing a release makes no new claim of operational approval or public releasability.
