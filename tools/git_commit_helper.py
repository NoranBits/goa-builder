#!/usr/bin/env python3
"""
git_commit_helper.py

Lightweight helper to commit changes grouped by top-level path, show old
changes, and generate a concise expert-style summary for each commit.

Usage examples:
  python3 tools/git_commit_helper.py --group-commit --push
  python3 tools/git_commit_helper.py --show-old HEAD~1
  python3 tools/git_commit_helper.py --dry-run --group-commit

This tool is intentionally conservative: use `--dry-run` to preview actions.
"""
import argparse
import subprocess
from collections import defaultdict
from typing import List, Dict


def run(cmd: List[str], capture: bool = True) -> str:
    """Run a command and return its stdout as string.

    When `capture` is False the function will run the command and return
    an empty string on success. Errors raise subprocess.CalledProcessError.
    """
    if capture:
        return subprocess.check_output(cmd, text=True).strip()
    else:
        subprocess.check_call(cmd)
        return ""


def get_changed_files() -> List[str]:
    out = run(["git", "status", "--porcelain", "-z"]) or ""
    if not out:
        return []
    parts = [p for p in out.split("\0") if p]
    paths = []
    for entry in parts:
        # strip status markers
        # entries may look like ' M path' or '?? path'
        # remove leading status tokens and whitespace
        p = entry
        while p and p[0] in " MARDCTU?!" :
            p = p[1:]
        p = p.strip()
        if p:
            paths.append(p)
    return paths


def group_by_top(paths: List[str]) -> Dict[str, List[str]]:
    groups = defaultdict(list)
    for p in paths:
        top = p.split("/", 1)[0]
        groups[top].append(p)
    return dict(groups)


def show_old(commit: str) -> None:
    print(f"--- git show {commit} (name-status) ---")
    try:
        print(run(["git", "show", "--name-status", "--pretty=oneline", commit]))
    except subprocess.CalledProcessError:
        print(f"Failed to show commit {commit}")


def summarize_staged() -> str:
    # name-status and numstat provide a good summary
    try:
        name_status = run(["git", "diff", "--staged", "--name-status"]) or "(no staged changes)"
        numstat = run(["git", "diff", "--staged", "--numstat"]) or ""
    except subprocess.CalledProcessError:
        return "(failed to collect staged summary)"
    lines = []
    lines.append("Summary of staged changes:")
    lines.append(name_status)
    if numstat:
        lines.append("\nLines (added\tremoved) per file:")
        lines.append(numstat)
    return "\n".join(lines)


def _get_diff_excerpt(file: str, max_lines: int, staged: bool) -> str:
    try:
        cmd = ["git", "diff", "--unified=3"]
        if staged:
            cmd.append("--staged")
        cmd += ["--", file]
        diff = run(cmd) or ""
    except subprocess.CalledProcessError:
        return ""
    if not diff:
        return ""
    lines = diff.splitlines()
    if len(lines) <= max_lines:
        return "\n" + "\n".join(lines)
    # Truncate preserving header
    excerpt = lines[:max_lines]
    excerpt.append("... (truncated)")
    return "\n" + "\n".join(excerpt)


def summarize_changes_for(files: List[str], staged: bool) -> str:
    try:
        base = ["git", "diff", "--name-status"]
        if staged:
            base.append("--staged")
        cmd1 = base + ["--"] + [str(f) for f in files]
        name_status = run(cmd1) or "(no changes)"
        base2 = ["git", "diff", "--numstat"]
        if staged:
            base2.append("--staged")
        cmd2 = base2 + ["--"] + [str(f) for f in files]
        numstat = run(cmd2) or ""
    except subprocess.CalledProcessError:
        return "(failed to collect summary)"

    # Compute totals from numstat
    total_added = 0
    total_removed = 0
    file_count = len(files)
    if numstat:
        for line in numstat.splitlines():
            parts = line.split()
            if len(parts) >= 3:
                a, r = parts[0], parts[1]
                try:
                    added = int(a) if a.isdigit() else 0
                    removed = int(r) if r.isdigit() else 0
                except Exception:
                    added = 0
                    removed = 0
                total_added += added
                total_removed += removed

    header = f"Files: {file_count}, +{total_added} -{total_removed}"
    parts_out = [header, "", "Summary of changes for group:", name_status]
    if numstat:
        parts_out.append("\nLines (added\tremoved) per file:")
        parts_out.append(numstat)
    return "\n".join(parts_out)


def commit_group(top: str, files: List[str], dry_run: bool, push: bool, include_diffs: bool = False, max_diff_lines: int = 200, diff_files_limit: int = 3, interactive: bool = False) -> None:
    print(f"\n--- Processing group: {top} ({len(files)} files) ---")
    files = [str(f) for f in files]
    for f in files:
        print(f" - {f}")
    # interactive per-group choice for diffs
    if interactive:
        try:
            ans = input(f"Include diffs for group '{top}' in commit message? [y/N]: ").strip().lower()
        except EOFError:
            ans = "n"
        include_diffs = include_diffs or (ans == "y")

    if dry_run:
        # build and print the commit message preview without changing repo state
        staged_flag = False
        summary = summarize_changes_for(files, staged=staged_flag)
        parts = [f"Group commit: {top}", "", summary]
        if include_diffs:
            parts.append("")
            parts.append(f"Diff excerpts (up to {diff_files_limit} files, {max_diff_lines} lines/file):")
            added = 0
            for file in files:
                if added >= diff_files_limit:
                    break
                excerpt = _get_diff_excerpt(file, max_diff_lines, staged=staged_flag)
                if excerpt:
                    parts.append(f"\n--- {file} ---")
                    parts.append(excerpt)
                    added += 1
            if added == 0:
                parts.append("(no diffs available for these files)")
        msg = "\n".join(parts) + "\n"
        print("\n--- Commit message preview ---\n")
        print(msg)
        return

    # stash only the listed files (include untracked)
    try:
        run(["git", "stash", "push", "-u", "-m", f"group:{top}"] + files, capture=False)
    except subprocess.CalledProcessError:
        print("stash push failed")
        return

    # apply the stash we just created (stash@{0})
    try:
        run(["git", "stash", "apply", "--index", "stash@{0}"], capture=False)
    except subprocess.CalledProcessError:
        print("stash apply failed; attempting to drop stash and continue")
        try:
            run(["git", "stash", "drop", "-q", "stash@{0}"], capture=False)
        except Exception:
            pass
        return

    # stage files
    try:
        run(["git", "add", "--all", "--"] + files, capture=False)
    except subprocess.CalledProcessError:
        print("git add failed")

    # prepare commit message
    summary = summarize_staged()
    parts = [f"Group commit: {top}", "", summary]

    if include_diffs:
        parts.append("")
        parts.append(f"Diff excerpts (up to {diff_files_limit} files, {max_diff_lines} lines/file):")
        added = 0
        for file in files:
            if added >= diff_files_limit:
                break
            excerpt = _get_diff_excerpt(file, max_diff_lines, staged=True)
            if excerpt:
                parts.append(f"\n--- {file} ---")
                parts.append(excerpt)
                added += 1
        if added == 0:
            parts.append("(no diffs available for staged files)")

    msg = "\n".join(parts) + "\n"

    try:
        subprocess.run(["git", "commit", "-F", "-"], input=msg, text=True, check=True)
    except subprocess.CalledProcessError:
        print("git commit failed; dropping stash and exiting")
        try:
            run(["git", "stash", "drop", "-q", "stash@{0}"], capture=False)
        except Exception:
            pass
        return

    # drop the stash
    try:
        run(["git", "stash", "drop", "-q", "stash@{0}"], capture=False)
    except Exception:
        pass

    if push:
        try:
            branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
            print(f"Pushing to origin/{branch}")
            run(["git", "push", "origin", branch], capture=False)
        except subprocess.CalledProcessError:
            print("git push failed")


def main(argv=None):
    p = argparse.ArgumentParser(description="Commit helper with grouping, old-change inspection and expert summaries")
    p.add_argument("--group-commit", action="store_true", help="Group changed files by top-level path and commit each group separately")
    p.add_argument("--show-old", metavar="COMMIT", help="Show an older commit's name-status and summary")
    p.add_argument("--dry-run", action="store_true", help="Don't perform any destructive actions; just preview")
    p.add_argument("--push", action="store_true", help="Push after commit for each group")
    p.add_argument("--all", action="store_true", help="Commit everything in one group (top-level 'all')")
    p.add_argument("--include-diffs", action="store_true", help="Include small unified-diff excerpts in the commit message")
    p.add_argument("--max-diff-lines", type=int, default=120, help="Maximum number of diff lines to include per file (default: 120)")
    p.add_argument("--diff-files-limit", type=int, default=3, help="Maximum number of files to include diffs for per group (default: 3)")
    p.add_argument("--interactive", action="store_true", help="Prompt per-group to include diffs")
    args = p.parse_args(argv)

    if args.show_old:
        show_old(args.show_old)
        return

    changed = get_changed_files()
    if not changed:
        print("No changes detected.")
        return

    if args.all:
        # single group named 'all'
        commit_group("all", changed, dry_run=args.dry_run, push=args.push, include_diffs=args.include_diffs, max_diff_lines=args.max_diff_lines, diff_files_limit=args.diff_files_limit, interactive=args.interactive)
        return

    if args.group_commit:
        groups = group_by_top(changed)
        for top, files in sorted(groups.items()):
            commit_group(top, files, dry_run=args.dry_run, push=args.push, include_diffs=args.include_diffs, max_diff_lines=args.max_diff_lines, diff_files_limit=args.diff_files_limit, interactive=args.interactive)
        return

    # default: show a helpful preview summary and staged summary
    print("Changed files:")
    for f in changed:
        print(f" - {f}")
    print("\nRun with --group-commit to commit grouped, --all to commit all, or --dry-run to preview.")
    print("\nStaged summary (if any):")
    print(summarize_staged())


if __name__ == "__main__":
    main()
