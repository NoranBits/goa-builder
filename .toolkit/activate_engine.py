#!/usr/bin/env python3
"""
activate_engine.py

Safe CLI to activate an engine module from the builder templates into the target repo.

Behavior:
- Detect engine via registry (`--detect`) or accept `--engine <id>`.
- Dry-run mode reports planned actions without making changes.
- Copies only the selected engine's template payload (canon/toolkit/github) into target paths.
- Updates `.canon/modules/engine/ACTIVE_ENGINE.yml`.
- Appends a decision entry (NDJSON) to `.logs/decisions/CHANGELOG.ndjson` and writes a human markdown record.

Safety:
- Fails if another active engine exists unless `--migrate` is provided.
- Never touches other engine templates.
"""
import argparse
import os
import sys
import shutil
import datetime
import json
import glob

try:
    import yaml
except Exception:
    yaml = None


REPO_ROOT = os.getcwd()
TEMPLATES_BASE = os.path.join(REPO_ROOT, 'templates', 'modules', 'engine')
CANON_ENGINE_BASE = os.path.join(REPO_ROOT, '.canon', 'modules', 'engine')
TOOLKIT_ENGINE_BASE = os.path.join(REPO_ROOT, '.toolkit', 'modules', 'engine')
GITHUB_INSTRUCTIONS = os.path.join(REPO_ROOT, '.github', 'instructions')
DECISIONS_DIR = os.path.join(REPO_ROOT, '.logs', 'decisions')


def load_registry():
    reg_path = os.path.join(TEMPLATES_BASE, '_registry.yml')
    if not os.path.isfile(reg_path):
        return None, f"Registry not found at {reg_path}"
    if not yaml:
        return None, "PyYAML required to load registry"
    with open(reg_path, 'r', encoding='utf-8') as f:
        doc = yaml.safe_load(f)
    return doc, None


def detect_engine(reg):
    # reg expected to be dict with 'engines' list
    for e in reg.get('engines', []):
        markers = e.get('markers', [])
        for m in markers:
            if 'path' in m:
                p = os.path.join(REPO_ROOT, m['path'])
                if os.path.exists(p):
                    return e['id']
            if 'path_glob' in m:
                matches = glob.glob(os.path.join(REPO_ROOT, m['path_glob']))
                if matches:
                    return e['id']
    return None


def read_active():
    p = os.path.join(CANON_ENGINE_BASE, 'ACTIVE_ENGINE.yml')
    if not os.path.isfile(p):
        return None
    if yaml:
        with open(p, 'r', encoding='utf-8') as f:
            doc = yaml.safe_load(f)
        return doc.get('engine')
    # fallback naive
    with open(p, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('engine:'):
                return line.split(':', 1)[1].strip().strip('"\'"')
    return None


def write_active(engine, reason, dry_run=False):
    os.makedirs(CANON_ENGINE_BASE, exist_ok=True)
    p = os.path.join(CANON_ENGINE_BASE, 'ACTIVE_ENGINE.yml')
    doc = {
        'engine': engine,
        'reason': reason,
        'ts': datetime.datetime.utcnow().isoformat() + 'Z'
    }
    if dry_run:
        print(f"DRY-RUN: would write {p} with {doc}")
        return
    import yaml as _yaml
    with open(p, 'w', encoding='utf-8') as f:
        _yaml.safe_dump(doc, f)


def copy_tree_if_exists(src, dst, dry_run=False):
    if not os.path.exists(src):
        return []
    if dry_run:
        print(f"DRY-RUN: would copy {src} -> {dst}")
        # simulate listing
        return [src]
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    # use copytree with dirs_exist_ok if available
    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
    except TypeError:
        # older python fallback: copy into dst, create if missing
        if not os.path.exists(dst):
            shutil.copytree(src, dst)
        else:
            # merge
            for root, dirs, files in os.walk(src):
                rel = os.path.relpath(root, src)
                target_root = os.path.join(dst, rel) if rel != '.' else dst
                os.makedirs(target_root, exist_ok=True)
                for f in files:
                    shutil.copy2(os.path.join(root, f), os.path.join(target_root, f))
    return [dst]


def append_decision_entry(engine, author, changes, dry_run=False):
    os.makedirs(DECISIONS_DIR, exist_ok=True)
    ts = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    changelog = os.path.join(DECISIONS_DIR, 'CHANGELOG.ndjson')
    entry = {
        'ts': datetime.datetime.utcnow().isoformat() + 'Z',
        'change_id': f'CHG-{ts}',
        'author': author,
        'action': 'activate_engine',
        'engine': engine,
        'changes': changes
    }
    if dry_run:
        print(f"DRY-RUN: would append to {changelog}: {entry}")
    else:
        with open(changelog, 'a', encoding='utf-8') as f:
            f.write(json.dumps(entry) + '\n')
    # human readable markdown
    md_path = os.path.join(DECISIONS_DIR, f'{ts}-activate-{engine}.md')
    md = f"# Activate engine {engine}\n\n- ts: {entry['ts']}\n- author: {author}\n- changes:\n"
    for c in changes:
        md += f"  - {c}\n"
    if dry_run:
        print(f"DRY-RUN: would write {md_path}:\n{md}")
    else:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md)


def main(argv):
    p = argparse.ArgumentParser()
    p.add_argument('--engine', '-e', help='Engine id to activate (e.g. unity)')
    p.add_argument('--detect', action='store_true', help='Auto-detect engine via registry')
    p.add_argument('--dry-run', action='store_true', help='Do not make changes')
    p.add_argument('--force', action='store_true', help='Force activation (overwrite)')
    p.add_argument('--migrate', action='store_true', help='Migrate existing active engine to _retired')
    p.add_argument('--reason', default='manual activation', help='Reason for activation')
    args = p.parse_args(argv[1:])

    reg, err = load_registry()
    if err:
        print(f"Error: {err}")
        return 2

    engine = None
    if args.detect:
        engine = detect_engine(reg)
        if not engine:
            print("No engine detected via registry markers")
            return 3
    elif args.engine:
        engine = args.engine
    else:
        print("Specify --engine or --detect")
        return 1

    # find registry entry
    engines = {e['id']: e for e in reg.get('engines', [])}
    if engine not in engines:
        print(f"Engine '{engine}' not found in registry")
        return 4

    active = read_active()
    if active == engine:
        print(f"Engine '{engine}' already active. Nothing to do.")
        return 0

    if active and active != 'none':
        if not args.migrate and not args.force:
            print(f"Active engine '{active}' exists. Use --migrate to archive or --force to overwrite.")
            return 5

    # perform migration if requested
    changes = []
    if active and active != 'none' and args.migrate:
        src = os.path.join(CANON_ENGINE_BASE, active)
        retired_dir = os.path.join(CANON_ENGINE_BASE, '_retired')
        os.makedirs(retired_dir, exist_ok=True)
        ts = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
        dest = os.path.join(retired_dir, f"{active}-{ts}")
        if args.dry_run:
            print(f"DRY-RUN: would move {src} -> {dest}")
        else:
            if os.path.exists(src):
                shutil.move(src, dest)
        changes.append(f"migrated {active} to {dest}")

    # Copy payloads from templates
    src_base = os.path.join(TEMPLATES_BASE, engine)
    if not os.path.isdir(src_base):
        print(f"Template for engine '{engine}' not found at {src_base}")
        return 6

    # copy canon/
    src_canon = os.path.join(src_base, 'canon')
    dst_canon = os.path.join(CANON_ENGINE_BASE, engine)
    copied = copy_tree_if_exists(src_canon, dst_canon, dry_run=args.dry_run)
    if copied:
        changes.append(f"copied canon -> {dst_canon}")

    # copy toolkit/
    src_toolkit = os.path.join(src_base, 'toolkit')
    dst_toolkit = os.path.join(TOOLKIT_ENGINE_BASE, engine)
    copied = copy_tree_if_exists(src_toolkit, dst_toolkit, dry_run=args.dry_run)
    if copied:
        changes.append(f"copied toolkit -> {dst_toolkit}")

    # copy github instructions if present
    src_github = os.path.join(src_base, 'github')
    if os.path.isdir(src_github):
        for root, dirs, files in os.walk(src_github):
            rel = os.path.relpath(root, src_github)
            for f in files:
                srcf = os.path.join(root, f)
                # place under .github/instructions/
                dest_dir = os.path.join(GITHUB_INSTRUCTIONS)
                os.makedirs(dest_dir, exist_ok=True)
                destf = os.path.join(dest_dir, f)
                if args.dry_run:
                    print(f"DRY-RUN: would copy {srcf} -> {destf}")
                else:
                    shutil.copy2(srcf, destf)
        changes.append(f"copied github instructions -> {GITHUB_INSTRUCTIONS}")

    # update ACTIVE_ENGINE pointer
    write_active(engine, args.reason, dry_run=args.dry_run)

    # append decision log
    author = os.environ.get('USER') or os.environ.get('GITHUB_ACTOR') or 'automated'
    append_decision_entry(engine, author, changes, dry_run=args.dry_run)

    print('Activation completed' if not args.dry_run else 'Dry-run completed')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
