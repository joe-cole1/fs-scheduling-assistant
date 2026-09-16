# Release notes structure

The **Publish release** workflow now composes and publishes release notes automatically while the release is still a draft. Maintainers do not manually create or publish a GitHub Release for the normal path.

The workflow preserves this structure:

## What changed

Taken from `packaging/update-note.md` in the exact source commit being released. Keep that file short, user-facing and specific to the release.

## What you need to do

Generated from the standard update/install procedure plus any persistent migration declared for the requested version. Existing setups are never told to overwrite Local Guidance automatically.

## Validation and known limitations

Generated only after the release workflow has passed persistent-state validation, two independent package builds, package/source-coverage checks, byte-reproducibility comparison and the regression test suite. The notes explicitly distinguish those checks from native Word visual review, GenAI.mil behavior and operational readiness.

## Changes and contributors

GitHub-generated merged-PR/contributor notes are appended automatically using GitHub's release-notes generator for the requested tag/source commit.

## Downloads and verification

The workflow appends a generated block with the three operator ZIP links, manifest, SHA-256 file, source commit and per-ZIP checksums. It verifies the draft asset bytes before publishing.

Do not manually edit an in-progress draft or click **Publish release** while the workflow is incomplete. If a run fails after draft creation, rerun the same version to resume the matching draft. An already-published immutable release is never repaired or replaced; use a new version instead.
