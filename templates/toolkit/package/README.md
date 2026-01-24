# package

> **Context**: Tools for bundling the application for distribution (Docker, zip, installers).

## Purpose

Package tools take built artifacts and wrap them for deployment or release.

## Suggested Tools

- **`create_deployment_zip.sh`**: Create a deployable archive.
- **`build_docker_image.sh`**: Build and tag a container image.
- **`generate_sbom.py`**: Create a Software Bill of Materials.

## Works Well With

- **`build/`**: Packaging usually happens after build.
- **`.github/workflows`**: CI often calls these scripts to publish releases.

## Custom Tools

Use `custom-tools/` for store-specific packagers (SteamPipe, AppStoreConnect).

## Safety

- Packaging scripts should not publish keys or secrets inside the artifact.
- Verify checksums of included binaries.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **Docker Best Practices**: [Dockerfile Guide](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) - Containerization standards.
- **Semantic Versioning**: [SemVer](https://semver.org/) - Versioning logic.
- **CycloneDX**: [SBOM Standard](https://cyclonedx.org/) - Bill of materials specification.

<!-- md_autofix: processed -->
