# scan

## Purpose

Scan tools answer:

- What kind of repo is this?
- Where are the main entry points?
- What are the build and test commands?
- Where do assets and content live?

## Outputs

Typical outputs include:

- A short repo summary (tech stack, packages, build system)
- A list of key paths and “start here” files
- Optional JSON summaries that other tools can consume

## Works well with

- `search/`: jump from “what is this repo?” to the exact files.
- `validate/`: choose the correct validation gates based on tech stack.
- `test/`: select the smallest relevant test subset.

## Suggested tools

- `scan_repo.py`: produce a high-signal summary for agents.
- `scan_packages.py`: list package boundaries, scripts, and dependencies.
- `scan_assets.py`: locate asset roots and common import flows.

## Custom tools

Use `custom-tools/` for repo-specific scanning scripts.

## Safety

Scan tools should be read-only.
