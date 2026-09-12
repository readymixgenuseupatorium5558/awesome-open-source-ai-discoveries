# Contributing

Help someone discover a useful project or avoid an installation dead end. Good contributions add a missing use case, correct a source or document a real configuration.

1. Read [the methodology](METHODOLOGY.md) and choose the collection that fits.
2. Edit `catalog.json`. Add a unique lowercase `id`, `name`, canonical HTTPS `url`, existing or justified `category`, original `summary`, concrete `use_case`, `requirements`, `caveat`, primary `source_urls`, `reviewed_on` (YYYY-MM-DD) and `verification`.
3. Use `documentation-reviewed` unless you link reproducible test evidence. Avoid unsupported superlatives, hardware estimates, copied prose and affiliate links.
4. Run `python scripts/build.py` and `python scripts/build.py --check` with Python 3.12 or newer. No dependencies are required.
5. Commit the catalog and generated outputs together and open a pull request. Explain who benefits and which source supports the claim.

## Useful first contributions

- Check one project's installation instructions and report a changed prerequisite.
- Add a missing limitation, model-license distinction or archived-status note.
- Supply a reproducible Windows, macOS or Linux compatibility report.
- Improve a task description so a reader can choose between similar entries.
- Link an official live demo or upstream examples page with an accurate label.

## External link checks

`python scripts/check_links.py` checks entry and source URLs without executing project software. It exits nonzero for broken links or inconclusive network responses. Treat authentication walls, rate limits and temporary outages as investigation items, not proof that a project disappeared.

Keep discussion constructive. Credit upstream authors. Never submit credentials, private recordings or proprietary documents as test fixtures.
