import pathlib
import yaml
import jsonschema


def test_schema_and_sample_exist():
    root = pathlib.Path(__file__).resolve().parents[3]
    schema = root / "templates/canon/rolekit/manifest.schema.yml"
    sample = root / "templates/canon/rolekit/examples/sample_manifest.yml"
    assert schema.exists(), "Schema file missing"
    assert sample.exists(), "Sample manifest missing"

    # Basic parse check
    with schema.open("r", encoding="utf-8") as f:
        schema_data = yaml.safe_load(f)
    with sample.open("r", encoding="utf-8") as f:
        sample_data = yaml.safe_load(f)

    # Use Draft7 validator for basic structural check
    validator = jsonschema.Draft7Validator(schema_data)
    errors = list(validator.iter_errors(sample_data))
    assert not errors, f"Sample manifest does not validate: {errors}"
