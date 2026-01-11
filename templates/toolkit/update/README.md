# update

## Purpose

Update tools handle maintenance tasks.

Examples:

- Dependency updates
- Lockfile refresh
- Snapshot updates

## Suggested tools

- `update_deps.py`: controlled dependency updates.
- `refresh_lockfile.py`: regenerate lockfiles deterministically.

## Works well with

- `validate/`: ensure updated deps still pass gates.
- `test/`: run the smallest relevant suite after updates.
- `build/`: verify builds remain reproducible.

## Custom tools

Use `custom-tools/` for one-off maintenance scripts.

## Safety

Update tools should be explicit about writes.
