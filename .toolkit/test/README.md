# test

> **Context**: Runners for automated tests, ensuring functionalities work as expected.

## Purpose

Test tools execute the test suite (unit, integration, e2e) efficiently.

## Suggested Tools

- **`run_tests.sh`**: The main entry point for running tests.
- **`run_unit.py`**: Fast unit tests only.
- **`run_e2e.sh`**: Slow, full-stack end-to-end tests.

## Works Well With

- **`validate/`**: Ensure code style allows tests to run.
- **`build/`**: Binaries often must be built before testing.
- **`.logs/test/`**: Output test reports and coverage here.

## Custom Tools

Use `custom-tools/` for visual regression tools or specialized hardware tests.

## Safety

- Tests should not pollute the production database.
- Use mocks/fixtures for external services.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **Pytest**: [Documentation](https://docs.pytest.org/en/7.1.x/) - Python testing framework.
- **Jest**: [Docs](https://jestjs.io/) - JavaScript testing framework.
- **Test Driven Development (TDD)**: [Martin Fowler](https://martinfowler.com/bliki/TestDrivenDevelopment.html) - Red-Green-Refactor cycle.

<!-- md_autofix: processed -->
