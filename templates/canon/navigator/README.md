# navigator

## Purpose

`navigator/` is an agent-facing map of the repository generated from a scan.

It is designed to be:

- High-signal (small summaries, stable ordering)
- Incremental (easy to regenerate, easy to refine)
- Safe (does not modify source folders)

## What gets generated

- `README.md`: entry point index for the repo map.
- Per-folder `README.md` pages mirroring the repo’s folder structure.

## How agents should use it

1. Start at `navigator/README.md`.
2. Follow links deeper until you reach the target subsystem.
3. Use `.toolkit/scan` and `.toolkit/search` to confirm details.

## Navigation history (append-only)

After a scan session, record what you inspected (and why) under:

- `.logs/navigation/**`

This reduces repeated discovery work and creates reliable “quicksteps” for future sessions.
