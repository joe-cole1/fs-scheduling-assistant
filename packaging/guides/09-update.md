# Update next week

Use the latest numbered update when starting next week's planning. Finish current-week work under the instructions already in use. No automatic updates occur.

The installed package number appears in generated document headers. Use that package number, not Windows file dates, to identify the System release. Generated file dates are deterministic packaging metadata and are not release/install timestamps.

## Update an existing ZIP setup

1. Download **Update_Existing_Setup.zip** from the same repository page as the full packages. Extract it into a temporary folder, separate from your scheduling folder.
2. Open its **UPDATE INSTRUCTIONS.docx** and read the release number and short change note.
3. Before starting next week's planning, replace the entire **System** folder in your permanent scheduling folder with the update's **System** folder. Replace **START HERE.docx** with the supplied copy. Do not extract a full setup ZIP over your existing setup.
4. Keep **Local Guidance**, **COPY THIS FOLDER FOR EACH NEW WEEK**, and all **Week of ...** folders in place. Routine updates do not contain or replace local guidance or completed weekly work.
5. If the update contains **PERSISTENT MIGRATIONS.docx**, read it before deleting the temporary update folder. It identifies the persistent artifact that deliberately changed and the required human review. Any files under **Persistent Migration Sources** are clearly marked comparison copies. Do not copy them over Local Guidance automatically. Compare, merge only the approved change, preserve your existing local content, and record the human decision/updated local version.
6. Open System's new **02 Start a week.docx** and upload its new startup document when you open the next week's chat.

An update does not change a chat already in progress. For a current-week handoff after System has been replaced, identify the update in the receiving chat and carry forward existing decisions; do not silently reinterpret the week's approvals or restart optimization.

## Persistent local changes are explicit

The normal update replaces only reusable System instructions and START HERE. A release that intentionally changes an installed persistent seed, persistent template schema, or the reusable weekly-folder layout must declare that change in the package's persistent-migration record. The update then includes **PERSISTENT MIGRATIONS.docx** and, when useful, reference-only copies for comparison.

A declared migration is not permission to overwrite an approved squadron profile, playbook, stable-reference file, or weekly work. The appropriate human reviews and merges the change. A policy change still requires its actual approval authority; downloading a package never creates that approval. If the migration does not apply to your squadron or your current local file already contains the approved change, record that disposition and keep the current file.

## Roll back to a prior System release

Use this when a newly installed System package has a problem and a previously released System is known to work better. **Default to the next-week boundary**, just like a normal update. You do not need to keep old ZIPs in the scheduling folder because prior named assets remain in GitHub Releases.

1. Record the currently installed package number and the prior package number you intend to restore. State why you are rolling back.
2. Open the repository's **Releases** page and select the exact prior release. Download that release's **Update_Existing_Setup.zip**. Do not use GitHub's automatic Source code ZIP.
3. Extract the prior update into a temporary folder away from the permanent scheduling folder. Verify the package number in its generated document header/UPDATE INSTRUCTIONS.
4. Replace the permanent folder's entire **System** folder with the prior update's **System** folder and replace **START HERE.docx** with the prior copy.
5. **Do not replace or roll back Local Guidance, weekly folders, schedules, decision records, approvals, or human-maintained playbook/reference files.** If a later persistent migration was already human-reviewed and merged, reversing that local change is a separate human decision; an older System download does not automatically undo it.
6. Start the next week's chat using the restored System's **02 Start a week.docx** and startup document. Record the restored package number in the run control/handoff when relevant.

If an urgent problem forces a System rollback during the current execution week, preserve the current schedule versions, decisions, waivers, approvals, completed actuals and handoff state exactly. Tell the receiving/current chat that only the reusable System instructions changed from package [new] back to [prior]. Do not reinterpret, revoke or recreate operational decisions merely because the instruction package changed.

If the prior release does not contain a usable **Update_Existing_Setup.zip**, do not improvise by extracting a full setup over the current folder. Use its release documentation or maintainer support to identify the safe replaceable System/START HERE surfaces.

## Moving from the earlier Markdown setup

This first Word release cannot replace an older folder layout in place. Download the appropriate **full setup ZIP**, extract it as your permanent new folder, and copy your existing local guidance and weekly work into the matching locations. Keep approved local content; do not replace it with supplied blank forms. Word is recommended for newly created local documents; existing readable source files can be uploaded in their original format. Tell the chat their actual filenames.

Subsequent updates use the simple System replacement above plus any explicitly declared persistent-migration review. Changes to local rules require explicit human decisions; downloading an update or rollback grants no new approval or waiver.
