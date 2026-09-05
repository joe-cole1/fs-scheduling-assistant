# Repository QC record — package v0.4.1

Reviewed 2026-09-05 against main commit `75a50f1304ca0f45ee08f4881395e7a190c21af7`. This release changes packaging and operator instructions, preserving v0.4 scheduling behavior. These results describe document/package checks, not ChatGPT Mil behavior or operational readiness.

## Checks performed

- Built the Pantons setup, first-time squadron setup and manual update ZIPs. Repeated the build in a separate output folder; all ZIPs and the manifest were byte-identical.
- Checked ZIP integrity, safe paths, exact file inventory and manifest hashes. Operator files are DOCX; no Markdown, macros, scripts or executables are included.
- Rendered and visually reviewed all 30 distinct Word documents. Checked readable page layouts, numbered directions, complete prompts and labeled form fields. START HERE and update instructions each fit on one page.
- Checked that both full kits and the update contain identical System documents and START HERE. The Pantons kit receives its approved profile; the other-squadron kit receives a draft blank profile.
- Verified startup-primer and Pantons-profile source text coverage and form field labels through conversion. The approved Pantons profile source is byte-identical to the starting main version.
- Simulated the documented manual update with customized local guidance, a weekly schedule and a decision record. Those bytes and the weekly folder template survived; replacing System removed an obsolete System file. The update ZIP contains no local guidance or weekly work.
- Checked relative Markdown file links and balanced fenced prompt blocks. Reviewed operator filenames, expected inputs, activation/phase prompts, human buy/publication statements and handoff instructions against the primer.
- Removed the current-tree archive at the product authority's request. Provenance remains in Git history and prior PRs; external original attachments were not modified.
- Kept synthetic fixtures labeled and local policy separate from reusable instructions. No actual operational products or transcripts were added.

The repeatable structural and update-preservation checks are in [check_packages.py](../../scripts/check_packages.py). The [packaging instructions](../../packaging/README.md) explain the build and release process.

## Not run

Native Microsoft Word testing on a squadron computer, actual ChatGPT Mil DOCX ingestion, prompt execution and multiuser handoff remain **Not run**. Rendering here does not prove those platform behaviors.

The 24 behavioral cases and four setup cases in the [validation plan](validation-plan.md) remain **Not run**, as do historical blind trials and operational validation. [Guide 10](../../packaging/guides/10-check.md) provides a short first-use trial with synthetic inputs. Human reviewers decide adoption and public release; repository QC is neither approval.
