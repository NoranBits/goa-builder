# package

## Purpose

Packaging tools prepare deployable artifacts.

## Suggested tools

- `bundle_release.py`: build and bundle a release artifact.
- `checksum_artifacts.py`: create hashes for integrity checks.

## Works well with

- `build/`: packaging should start from a known-good build output.
- `validate/`: run gates before publishing artifacts.
- `log/`: store packaging logs and manifests.

## Custom tools

Use `custom-tools/` for pipeline experiments.

## Safety

Packaging should write outputs under a dedicated folder.
