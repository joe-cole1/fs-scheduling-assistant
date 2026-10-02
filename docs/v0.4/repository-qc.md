# Repository QC record — package 0.6.1

This is the current repository-level QC record. The v0.6.1 checks cover package routing and the weekly input checklist. Earlier v0.6.0 and hosted release evidence is retained separately; it does not establish publication or operational validation of v0.6.1.

## Package 0.6.1 checks completed

- All 47 repository unit tests passed. Negative inventory cases reject first-time guides/prompts, duplicate blank guidance forms and the setup validation reference inside System.
- Both independent builds passed package checks and produced byte-identical ZIPs and manifest. Every package uses the same operational System; Pantons and updates enter weekly work, while the first-time package has its own entry point and separate setup folder.
- All 42 unique generated Word documents (113 pages) were rendered. All 40 changed/new pages were visually reviewed; the other 73 pages matched previously reviewed renders pixel-for-pixel apart from the expected package-version label. All fourteen task guides, both entry points and the working/reference input checklists fit on one page.
- Source coverage and a scan of all System documents found no first-time setup material. Administrative command contracts are retained in the separate setup primer. No local-profile or existing local-guidance template source changed.
- The input checklist appears in both full packages' reusable weekly Inputs folder. Its new source fingerprint and PERSIST-004 migration passed validation. The update simulation removes legacy setup copies through entire-System replacement, preserves local guidance and weekly records, and adds the checklist without deleting custom input notes.
- All complete prompts retain the no-delegation instruction and model-neutral content. Relative links, fenced prompts and whitespace checks passed. Release-note routing distinguishes established Pantons guidance from new squadron setup.
- The fourteen-page printable weekly PDF contains the operational entry point, twelve weekly task guides and input checklist. Every final PDF page renders identically to its reviewed source. The direct-download input DOCX matches the working copy included in both full packages.

Native Word, live GenAI.mil/GAMECHANGER instruction following, no-delegation behavior and operator usability trials remain **Not run**. The current behavioral cases include V061-A through V061-D in the [validation plan](validation-plan.md). No merge or release publication is established by these local checks.

## Package 0.6.0 checks completed

- All 42 repository unit tests passed, including rejection of missing no-delegation wording, named-model requirements, incomplete prompt fields and invalid persistent-migration consolidation.
- Both independent builds passed the package checker. All three ZIPs and the generated manifest were byte-identical under the pinned CPython 3.12.14 packaging environment.
- All fourteen task checklists and START HERE rendered to one page each. All 38 unique generated Word documents, totaling 107 pages, were rendered and visually inspected. Repeated common files in the ZIPs have identical bytes.
- A printable fifteen-page checklist PDF was assembled from the reviewed renders. Every final PDF page rendered identically to its source checklist. The PDF is a convenience download; editable Word instructions remain in the ZIPs.
- The twenty shipped complete text prompts contain **Do not delegate to subagents** and require no named model or placeholder replacement. Checklist prompts exactly match their text files. Current generated documents contain no named-model workflow requirements. Example chat requests and the receiving handoff prompt include the same no-delegation instruction.
- Source coverage, genuine checkbox counts, document geometry, deterministic metadata, ZIP integrity, common-System consistency, local-policy isolation, update/rollback preservation and persistent source fingerprints passed.
- The local profile diff changes conversation/model-role wording only; its numerical scheduling rules remain unchanged. Prior migration records remain unchanged; PERSIST-003 provides a current review-and-merge instruction without reintroducing superseded model preferences.
- The existing authority, GAMECHANGER source gate, exact decision/version roles, whole-schedule QC and downstream-cascade contracts were reviewed across the checklists, primer, profile, reports, examples and validation plan. A short response does not narrow the required review.
- Relative Markdown links, fenced blocks and whitespace checks passed. Generated downloads remain outside the repository tree.

Native Microsoft Word on a squadron computer, actual GenAI.mil ingestion and instruction following, GAMECHANGER queries, actual no-delegation behavior, historical trials and novice-scheduler usability trials remain **Not run**. The behavioral cases in the [validation plan](validation-plan.md), including V060-A through V060-H, require observed outputs and human review. Static prompt wording cannot prove a platform will obey it.

No merge or v0.6.0 release publication is claimed by this record. The appropriate humans decide adoption and operational suitability.

## Historical release-automation evidence

The tagged v0.4.1 source retains its original package-specific QC record. The following follow-up records hosted release-automation evidence without rewriting that tag.

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

## Historical remaining validation

The native Word, platform-behavior, setup, historical and operational trials not performed for the earlier release remain unvalidated. The expanded current [validation plan](validation-plan.md) remains applicable; rebuilding v0.6.0 does not close those trials.

Publishing or successfully rebuilding a release makes no claim of operational approval, local-policy approval or public releasability. Human reviewers decide adoption and release suitability using the evidence actually available.
