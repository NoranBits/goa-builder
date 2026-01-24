# external

> **Context**: A quarantine zone for digested knowledge from other repositories or projects. This allows the GOA Builder to learn from outside sources without importing their entire codebase.

## Purpose

`.canon/external/**` stores external project digests for research and careful inspiration.

These digests are not authoritative. They exist to:

- **Preserve** what you learned from an upstream/legacy repo.
- **Keep** links to key entry points (docs, configs, subsystems).
- **Record** constraints (license, compatibility, risks) before implementing anything.

## How to Create a New External Digest Folder

Use the builder command (date defaults to the repo’s last git commit date):

```bash
python3 .builder/builder.py external --slug <project-slug>
```text

This creates:

- `.canon/external/<project-slug>-DD-MM-YYYY/`
- `external_source.md` (structured metadata + placeholders)
- `LINKTREE.md` (links to key entry points)

The templates used are stored alongside this README:

- `external_source.template.md`
- `linktree.template.md`

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **Web Scraping Best Practices**: [Robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) - Respecting site policies when gathering external info.
- **Fair Use**: [US Copyright Office](https://www.copyright.gov/fair-use/) - Understanding the legal boundaries of using external code for "inspiration".
- **SPDX Licenses**: [License List](https://spdx.org/licenses/) - Standard identifiers for open source licenses.

<!-- md_autofix: processed -->
