# test

## Purpose

Test tools run the smallest relevant suite to validate a change.

## Suggested tools

- `run_unit_tests.py`: fast unit test runner with file filters.
- `run_integration_tests.py`: opt-in integration coverage.
- `repro_bug.py`: create focused repro steps with logs.

## Works well with

- `validate/`: run cheap gates first, then tests.
- `log/`: collect logs and artifacts for failures.
- `build/`: validate build output before packaging.

## Custom tools

Use `custom-tools/` for ad-hoc repro scripts.

## Safety

Tests should not mutate the repo.
