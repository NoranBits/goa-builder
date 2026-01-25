#!/usr/bin/env python3
"""
Simple Rolekit manifest validator (Milestone 01)

Uses ruamel.yaml for round-trip YAML parsing and jsonschema for validation.
Supports a conservative `--fix` mode to insert safe defaults for missing trivial fields.
"""
import argparse
import shutil
import sys
from pathlib import Path
from datetime import datetime

try:
    from ruamel.yaml import YAML
except Exception:
    print("Missing dependency: ruamel.yaml. Install with 'pip install ruamel.yaml'", file=sys.stderr)
    raise

try:
    import jsonschema
except Exception:
    print("Missing dependency: jsonschema. Install with 'pip install jsonschema'", file=sys.stderr)
    raise

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "templates/canon/rolekit/manifest.schema.yml"
TARGET_DIR = ROOT / ".canon/rolekit"
LOG_DIR = ROOT / ".logs/changes"


def load_yaml(path: Path):
    yaml = YAML()
    with path.open("r", encoding="utf-8") as f:
        return yaml.load(f)


def write_yaml(path: Path, data):
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    with path.open("w", encoding="utf-8") as f:
        yaml.dump(data, f)


def backup(path: Path):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    dest = LOG_DIR / f"{path.name}.backup.{stamp}"
    shutil.copy2(path, dest)
    return dest


def validate_manifest(manifest_data, schema):
    validator = jsonschema.Draft7Validator(schema)
    errors = sorted(validator.iter_errors(manifest_data), key=lambda e: e.path)
    return errors


def process_file(path: Path, schema: dict, do_fix: bool) -> bool:
    data = load_yaml(path)
    errors = validate_manifest(data, schema)
    if not errors:
        print(f"OK: {path}")
        return True

    print(f"Validation errors in {path}:")
    for e in errors:
        print(f" - {list(e.path)}: {e.message}")

    if do_fix:
        changed = False
        if "metadata" in data:
            meta = data.get("metadata")
            if "version" not in meta:
                meta["version"] = "0.1.0"
                print(f"Auto-filled metadata.version for {path}")
                changed = True
        else:
            data.setdefault("metadata", {"version": "0.1.0"})
            changed = True

        if "provenance" not in data:
            data["provenance"] = {"builder": "unknown", "commit": "", "timestamp": ""}
            print(f"Auto-added provenance for {path}")
            changed = True

        if changed:
            backup(path)
            write_yaml(path, data)
            # re-validate
            errors = validate_manifest(data, schema)
            if not errors:
                print(f"Fixed: {path}")
                return True
            print(f"Still failing after auto-fix: {path}")
        return False


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--fix", action="store_true", help="Attempt conservative auto-fixes")
    p.add_argument("--manifest", type=str, help="Validate a single manifest file")
    args = p.parse_args()

    if not SCHEMA_PATH.exists():
        print(f"Schema not found at {SCHEMA_PATH}", file=sys.stderr)
        return 2

    schema = load_yaml(SCHEMA_PATH)

    targets = []
    if args.manifest:
        targets = [Path(args.manifest)]
    else:
        if not TARGET_DIR.exists():
            print(f"Target dir {TARGET_DIR} does not exist. Nothing to validate.")
            return 1
        targets = sorted(TARGET_DIR.glob("*.yml")) + sorted(TARGET_DIR.glob("*.yaml"))

    ok = True
    for t in targets:
        try:
            if not process_file(t, schema, args.fix):
                ok = False
        except Exception as exc:
            print(f"Exception validating {t}: {exc}")
            ok = False

    return 0 if ok else 3


if __name__ == "__main__":
    sys.exit(main())
