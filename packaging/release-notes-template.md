# Release notes template

Copy the sections below into the release description and replace the brackets. Write for schedulers: describe what changed and what they need to do. Delete irrelevant detail inside a section, but keep the three required section headings exactly as written. Click **Generate release notes** for the merged-PR/contributor list, then retain that list below your summary.

The release workflow recognizes **What changed**, **What you need to do**, and **Validation and known limitations** as the structured human summary. If those headings are absent, the generated download block will explicitly say that no structured human validation summary was present; GitHub-generated PR notes are not treated as validation evidence. The workflow preserves all text outside its marked generated block.

Do not call a release tested in ChatGPT Mil unless actual results support that statement. A successful build only verifies package checks. Do not use real operational examples in release notes.

---

## What changed

[Two or three concrete changes and why they matter to schedulers. State any approved workflow or local-policy changes explicitly; say unchanged only after review.]

## What you need to do

Existing setups: download Update_Existing_Setup.zip and apply it when starting next week's planning. Replace System and START HERE; preserve Local Guidance and weekly work. If the update contains PERSISTENT MIGRATIONS.docx, follow its human review/merge instructions rather than overwriting persistent local files.

First installation: choose the Pantons or first-time squadron setup ZIP, extract it and open START HERE.docx.

[Describe any additional migration or compatibility requirement. Use None if there is none.]

## Validation and known limitations

[Identify actual document review and tests performed. Separate Passed, Failed and Not run. Name relevant unresolved problems and who is affected. Do not turn GitHub-generated PR descriptions or automated package checks into a model/operational validation claim.]

## Changes and contributors

[Keep GitHub's generated merged-PR list, contributor credits and full comparison link here. Review it before publishing.]
