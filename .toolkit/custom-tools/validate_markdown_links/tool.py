#!/usr/bin/env python3
"""Simple demo tool: validate_markdown_links

This tool is intentionally minimal: it walks the target path and reports Markdown files found.
It demonstrates the tool contract and entrypoint for the remediation workflow.
"""
import argparse
import os
import sys


def find_markdown_files(path):
    md = []
    if os.path.isfile(path):
        if path.endswith(('.md', '.markdown')):
            md.append(path)
        return md
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith(('.md', '.markdown')):
                md.append(os.path.join(root, f))
    return md


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--target', '-t', required=True)
    p.add_argument('--dry-run', dest='dry', action='store_true')
    p.add_argument('--no-dry-run', dest='dry', action='store_false')
    p.set_defaults(dry=True)
    args = p.parse_args()

    files = find_markdown_files(args.target)
    print({"files_found": len(files)})
    for f in files[:20]:
        print(f)

    # Demo behavior: succeed
    return 0


if __name__ == '__main__':
    sys.exit(main())
