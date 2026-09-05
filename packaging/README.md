# Building and updating operator packages

Maintainers use this file. Operators download the current ZIP from the root README and open START HERE.docx. Python and GitHub are not required inside ChatGPT Mil.

## Sources and build

- `guides/`: START HERE and numbered operator guide sources, including all activation, phase and handoff prompts.
- `version.txt`: current deliberately numbered package release. v0.4.1 changes distribution and document format; v0.4 scheduling behavior is preserved.
- `../docs/v0.4/system-primer.md`: startup instructions; markers delimit the text exported into UPLOAD THIS TO START.docx.
- `../templates/`: blank form sources. Wide Markdown tables export as labeled Word records; repeated blank inventories export as topic lists plus a reusable entry, retaining every field.
- `../local-profiles/`: approved local seed for first installation only. The generic package receives the blank setup profile instead.
- `../scripts/build_packages.py`: deterministic Word and ZIP generation. Uses Python 3 and python-docx (validated here with python-docx 1.2.0); no network calls or operational file access.

From the repository root, with python-docx available:

```sh
python scripts/build_packages.py --output /path/to/temporary/package-output
python scripts/check_packages.py /path/to/temporary/package-output
```

The output contains a disposable `build` folder of DOCX files and a `downloads` folder with three ZIPs and a manifest. Inspect and render the generated Word files before copying the current downloads into the repository's `downloads/` folder. Commit the ZIPs, manifest and sources together. Do not edit ZIP contents manually or include the disposable build folder in the repository.

Word design: compact_reference_guide preset, Letter/1-inch margins, Calibri 11pt, explicit 1.25 line spacing and real headings/numbering. A compact customer-pack title avoids cover pages. Named overrides are documented in the builder. No Word macros, scripts, external data connections or executables are packaged.

## Installed layout

| Folder or file | What belongs there | Update behavior |
| --- | --- | --- |
| START HERE.docx | Short entry instructions | Replaced |
| System | Startup document, Instructions, Blank Forms, Reference | Entire folder replaced next week |
| Local Guidance | Human-maintained local profile, reference index, playbook and source references | Never included in update |
| COPY THIS FOLDER FOR EACH NEW WEEK | Empty Inputs, Schedules, Working Record folders | Kept in place |
| Week of date | Human-created weekly source snapshots, schedules and records | Never included in update |

Both full ZIPs use the same System and START HERE. Their local profile seeds differ. The update has System, START HERE and UPDATE INSTRUCTIONS at its root; users extract it separately before replacing System. Never include local-profile replacements in a routine update. If an approved local rule needs changing, explain that separately for human adoption.

## Release procedure

1. Make the authorized source changes. Bump version.txt for a deliberate package release and write a short change note. Ordinary repo edits do not update an installed setup.
2. Build all three packages. Run checks for ZIP integrity, exact contents, Word structure, complete primer/local-profile text, generic/Pantons separation and preservation of local/weekly files during update.
3. Render all new or changed DOCX files and inspect every changed page. Open START HERE and follow the filename/path instructions. Verify copy/paste prompts and blank form fields.
4. Update the change log and QC record with actual results. ChatGPT Mil ingestion, startup instruction following, handoff and behavior tests remain Not run until tested there.
5. Copy only current downloads and manifest into downloads. Use stable filenames so README links stay the same; release numbers appear inside the documents and manifest. Remove superseded package files from the current tree; Git history retains them.
6. Open a review PR. Human review and merge make the new downloads available on the main README. Public release/visibility requires separate authority and releasability review.

The script itself does not publish, merge or update any shared drive. No CI service or release workflow is required. A local setup adopts the package next week through manual replacement, not automatically when the repository changes.
