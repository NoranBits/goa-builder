# external

## Purpose

`.canon/external/**` stores external project digests for research and careful inspiration.

These digests are not authoritative. They exist to:

- Preserve what you learned from an upstream/legacy repo.
- Keep links to key entry points (docs, configs, subsystems).
- Record constraints (license, compatibility, risks) before implementing anything.

## How to create a new external digest folder

Use the builder command (date defaults to the repo’s last git commit date):

```bash
python3 .builder/builder.py external --slug <project-slug>
```

This creates:

- `.canon/external/<project-slug>-DD-MM-YYYY/`
- `external_source.md` (structured metadata + placeholders)
- `LINKTREE.md` (links to key entry points)

The templates used are stored alongside this README:

- `external_source.template.md`
- `linktree.template.md`

## Rules

- Do not copy/paste large upstream code blobs.
- Prefer small, licensed snippets and high-level notes.
- Record decisions and integration rationale in `.logs/**`.

## Placeholders (adjust per repo)

- Approved sources policy: `{{APPROVED_SOURCES_POLICY}}`
- Integration workflow: `{{INTEGRATION_WORKFLOW}}`
