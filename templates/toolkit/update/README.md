# update

> **Context**: Maintenance scripts for keeping dependencies and configurations fresh.

## Purpose

Update tools handle the "chore" work of upgrading libraries and regenerating lockfiles.

## Suggested Tools

- **`update_deps.sh`**: Upgrades package versions (interactive or safe mode).
- **`refresh_lockfiles.sh`**: Regenerate `package-lock.json` / `poetry.lock`.
- **`sync_templates.py`**: Pull latest updates from the `.builder` kit (if managing multiple repos).

## Works Well With

- **`install/`**: After updating, you often need to re-install.
- **`test/`**: Always run tests after an update.

## Custom Tools

Use `custom-tools/` for database migrations strategies.

## Safety

- Updates should always be performed on a fresh branch.
- Verify breaking changes in release notes.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **Renovate Bot**: [Docs](https://docs.renovatebot.com/) - Automated dependency updates.
- **Dependabot**: [GitHub Docs](https://docs.github.com/en/code-security/dependabot) - Automated supply chain security.
- **SemVer Cheatsheet**: [Npm Semver](https://docs.npmjs.com/about-semantic-versioning) - Understanding carat vs tilde ranges.
