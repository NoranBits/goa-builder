#!/usr/bin/env python3
"""
Simple markdown autofixer.

- Ensures blank lines around headings and lists
- Adds trailing newline
- Ensures fenced code blocks specify a language (use 'text' if empty)
- Renumbers ordered lists to start at 1 for each list block
- Produces a JSON report to stdout (and optionally to a file) with keys: detected_problems, fixed, unsolved

Usage: python3 tools/md_autofix.py [paths...]
If no paths provided, walks current directory and processes .md files.
"""
import os
import re
import sys
import json
import argparse
from pathlib import Path


def find_md_files(paths):
    files = []
    if not paths:
        for root, dirs, filenames in os.walk('.'):
            for f in filenames:
                fp = os.path.join(root, f)
                # always include .md files
                if f.lower().endswith('.md'):
                    files.append(fp)
                    continue
                # include common markdown-like files (e.g., CODEOWNERS, README)
                if f in ('CODEOWNERS', 'README', 'CONTRIBUTING', 'CHANGELOG'):
                    files.append(fp)
                    continue
    else:
        for p in paths:
            path = Path(p)
            if path.is_file() and path.suffix.lower() == '.md':
                files.append(str(path))
            elif path.exists() and path.is_dir():
                for root, dirs, filenames in os.walk(str(path)):
                    for f in filenames:
                        fp = os.path.join(root, f)
                        if f.lower().endswith('.md'):
                            files.append(fp)
                            continue
                        if f in ('CODEOWNERS', 'README', 'CONTRIBUTING', 'CHANGELOG'):
                            files.append(fp)
                            continue
            else:
                # treat as glob
                import glob
                for g in glob.glob(p, recursive=True):
                    if os.path.isfile(g) and g.lower().endswith('.md'):
                        files.append(g)
    return sorted(set(files))


def load_state(repo_root='.'):
    """Load or initialize agent state for adaptive behavior."""
    state_path = os.path.join(repo_root, '.md_autofix_state.json')
    try:
        if os.path.exists(state_path):
            with open(state_path, 'r', encoding='utf-8') as fh:
                return json.load(fh)
    except Exception:
        pass
    # default state
    state = {
        'run_count': 0,
        'problem_counts': {},
        'policies': {},  # problem -> action: 'auto-fix'|'ignore'|'report'
        'thresholds': {
            'auto_fix_enable': 100
        }
    }
    try:
        with open(state_path, 'w', encoding='utf-8') as fh:
            json.dump(state, fh, indent=2)
    except Exception:
        pass
    return state


def save_state(state, repo_root='.'):
    state_path = os.path.join(repo_root, '.md_autofix_state.json')
    try:
        with open(state_path, 'w', encoding='utf-8') as fh:
            json.dump(state, fh, indent=2)
    except Exception:
        pass


def write_insights(report, state, out_path='.logs/validation/md_autofix_agent_insights.json'):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    insights = {
        'summary': report.get('summary', {}),
        'top_problems': sorted(report.get('problem_counts', {}).items(), key=lambda x: -x[1])[:40],
        'policies': state.get('policies', {}),
        'run_count': state.get('run_count', 0)
    }
    try:
        with open(out_path, 'w', encoding='utf-8') as fh:
            json.dump(insights, fh, indent=2)
    except Exception:
        pass


def process_file(path, state=None):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            orig = fh.read()
    except Exception as e:
        return {'file': path, 'detected_problems': [], 'fixed': [], 'unsolved': [{'error': str(e)}]}

    lines = orig.splitlines()
    had_trailing = orig.endswith('\n')

    problems = []
    fixed = []
    unsolved = []
    if state is None:
        state = {'problem_counts': {}, 'policies': {}}

    out = list(lines)

    # Ensure fenced code blocks specify language if blank and track code-block state
    fence_open_re = re.compile(r"^(?P<indent>\s*)```(?P<lang>\s*)$")
    fence_any_re = re.compile(r"^(?P<indent>\s*)```(?P<lang>.*)$")
    in_fence = False
    for i, line in enumerate(out):
        # detect fence open/close
        m_any = fence_any_re.match(line)
        if m_any:
            # if fence has no language (only spaces) -> add 'text'
            if fence_open_re.match(line):
                # policy: only auto-fix if policy allows
                problem_name = 'fenced code block missing language'
                action = state.get('policies', {}).get(problem_name, 'auto-fix')
                if action == 'auto-fix':
                    out[i] = m_any.group('indent') + '```text'
                    problems.append({'file': path, 'line': i + 1, 'problem': problem_name})
                    fixed.append({'file': path, 'line': i + 1, 'fix': "add language 'text' to fenced block"})
                else:
                    problems.append({'file': path, 'line': i + 1, 'problem': problem_name})
            # toggle in_fence state
            if not in_fence:
                in_fence = True
            else:
                in_fence = False


    # Ensure blank lines before and after headings
    heading_re = re.compile(r"^(\s{0,3})(#{1,6})\s+(.*)$")
    i = 0
    first_h1_found = False
    while i < len(out):
        line = out[i]
        # skip headings inside fenced codeblocks
        if line.strip().startswith('```'):
            # toggle handled above; skip until fence closes
            i += 1
            continue
        m = heading_re.match(line)
        if m:
            indent = m.group(1)
            hashes = m.group(2)
            rest = m.group(3)
            level = len(hashes)
            # MD025: convert extra top-level headings to H2
            if level == 1:
                if not first_h1_found:
                    first_h1_found = True
                else:
                    problem_name = 'extra top-level heading'
                    action = state.get('policies', {}).get(problem_name, 'auto-fix')
                    if action == 'auto-fix':
                        out[i] = f"{indent}## {rest}"
                        problems.append({'file': path, 'line': i + 1, 'problem': 'extra top-level heading converted to H2'})
                        fixed.append({'file': path, 'line': i + 1, 'fix': 'convert H1 to H2 to satisfy single-title rule'})
                    else:
                        problems.append({'file': path, 'line': i + 1, 'problem': problem_name})
            # ensure blank line before heading (not in fence)
            if i > 0 and out[i-1].strip() != '':
                problem_name = 'missing blank line before heading'
                action = state.get('policies', {}).get(problem_name, 'auto-fix')
                if action == 'auto-fix':
                    out.insert(i, '')
                    problems.append({'file': path, 'line': i + 1, 'problem': problem_name})
                    fixed.append({'file': path, 'line': i + 1, 'fix': 'insert blank line before heading'})
                    i += 1
                else:
                    problems.append({'file': path, 'line': i + 1, 'problem': problem_name})
                i += 1
            # ensure blank line after heading
            if i + 1 < len(out) and out[i+1].strip() != '':
                problem_name = 'missing blank line after heading'
                action = state.get('policies', {}).get(problem_name, 'auto-fix')
                if action == 'auto-fix':
                    out.insert(i+1, '')
                    problems.append({'file': path, 'line': i + 2, 'problem': problem_name})
                    fixed.append({'file': path, 'line': i + 2, 'fix': 'insert blank line after heading'})
                    i += 1
                else:
                    problems.append({'file': path, 'line': i + 2, 'problem': problem_name})
        i += 1

    # Ensure blank lines around lists and renumber ordered lists
    list_item_re = re.compile(r"^(\s*)([-+*]|\d+\.)\s+")
    i = 0
    while i < len(out):
        if out[i].strip() == '':
            i += 1
            continue
        m = list_item_re.match(out[i])
        if m:
            # ensure blank line before list
            if i > 0 and out[i-1].strip() != '':
                out.insert(i, '')
                problems.append({'file': path, 'line': i + 1, 'problem': 'missing blank line before list'})
                fixed.append({'file': path, 'line': i + 1, 'fix': 'insert blank line before list'})
                i += 1
            # collect contiguous list block
            j = i
            items = []
            while j < len(out) and out[j].strip() != '':
                if list_item_re.match(out[j]):
                    items.append((j, out[j]))
                j += 1
            # ensure blank after
            if j < len(out) and out[j].strip() != '':
                out.insert(j, '')
                problems.append({'file': path, 'line': j + 1, 'problem': 'missing blank line after list'})
                fixed.append({'file': path, 'line': j + 1, 'fix': 'insert blank line after list'})
            # renumber ordered lists
            if items:
                ordered = all(re.match(r"^\s*\d+\.\s+", t[1]) for t in items)
                if ordered:
                    counter = 1
                    for (idx, raw) in items:
                        m2 = re.match(r"^(\s*)(\d+)\.(\s+)(.*)$", raw)
                        if m2:
                            indent = m2.group(1)
                            rest = m2.group(4)
                            out[idx] = f"{indent}{counter}. {rest}"
                            fixed.append({'file': path, 'line': idx + 1, 'fix': f'renumber to {counter}.'})
                            counter += 1
            i = j
        else:
            i += 1

    # Second pass: normalize ordered-list numbering across nearby items (allow single blank line continuation)
    ordered_re = re.compile(r"^(\s*)(\d+)\.(\s+)(.*)$")
    prev_order = 0
    prev_was_order = False
    blank_count = 0
    i = 0
    # respect fenced blocks
    in_fence_local = False
    fence_re_local = re.compile(r"^\s*```")
    while i < len(out):
        line = out[i]
        if fence_re_local.match(line):
            in_fence_local = not in_fence_local
            prev_was_order = False
            prev_order = 0
            blank_count = 0
            i += 1
            continue
        if in_fence_local:
            i += 1
            continue
        if line.strip() == '':
            blank_count += 1
            if blank_count > 1:
                prev_was_order = False
                prev_order = 0
            i += 1
            continue
        m = ordered_re.match(line)
        if m:
            indent = m.group(1)
            num = int(m.group(2))
            sep = m.group(3)
            rest = m.group(4)
            if prev_was_order:
                newnum = prev_order + 1
            else:
                newnum = 1
            if newnum != num:
                problem_name = 'ordered list numbering'
                action = state.get('policies', {}).get(problem_name, 'auto-fix')
                if action == 'auto-fix':
                    out[i] = f"{indent}{newnum}.{sep}{rest}"
                    fixed.append({'file': path, 'line': i + 1, 'fix': f'renumber to {newnum}.'})
                else:
                    # still record the problem
                    problems.append({'file': path, 'line': i + 1, 'problem': f'ordered list numbering expected {prev_order+1} but found {num}'})
            prev_order = newnum
            prev_was_order = True
            blank_count = 0
        else:
            prev_was_order = False
            prev_order = 0
            blank_count = 0
        i += 1

    new_text = "\n".join(out) + "\n"
    if not had_trailing:
        problems.append({'file': path, 'line': len(out), 'problem': 'missing trailing newline'})
        fixed.append({'file': path, 'line': len(out), 'fix': 'append trailing newline'})

    # add trigger comment marker to indicate file processed
    marker = '<!-- md_autofix: processed -->'
    if marker not in new_text:
        new_text = new_text.rstrip('\n') + '\n\n' + marker + '\n'
        fixed.append({'file': path, 'line': len(out) + 2, 'fix': 'append md_autofix trigger marker'})

    if new_text != orig:
        try:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(new_text)
        except Exception as e:
            unsolved.append({'file': path, 'error': str(e)})
            return {'file': path, 'detected_problems': problems, 'fixed': fixed, 'unsolved': unsolved}

    # update state counts
    for p in problems:
        name = p.get('problem') or 'unknown'
        state.setdefault('problem_counts', {})
        state['problem_counts'][name] = state['problem_counts'].get(name, 0) + 1

    return {'file': path, 'detected_problems': problems, 'fixed': fixed, 'unsolved': unsolved}


def main():
    parser = argparse.ArgumentParser(description='Autofix common markdown issues')
    parser.add_argument('paths', nargs='*', help='Files, dirs, or globs to process')
    parser.add_argument('--report-path', help='Write JSON report to this path')
    args = parser.parse_args()

    md_files = find_md_files(args.paths)
    all_detected = []
    all_fixed = []
    all_unsolved = []
    per_file = []

    state = load_state(repo_root='.')
    state['run_count'] = state.get('run_count', 0) + 1
    for f in md_files:
        res = process_file(f, state=state)
        per_file.append(res)
        all_detected.extend(res.get('detected_problems', []))
        all_fixed.extend(res.get('fixed', []))
        all_unsolved.extend(res.get('unsolved', []))

    report = {
        'detected_problems': all_detected,
        'fixed': all_fixed,
        'unsolved': all_unsolved,
        'per_file': per_file,
        'summary': {
            'total_files': len(per_file),
            'total_problems': len(all_detected),
            'total_fixed': len(all_fixed)
        },
        'problem_counts': {},
        'fix_counts': {}
    }

    # build counts
    pc = {}
    for p in all_detected:
        k = p.get('problem') or p.get('code') or 'unknown'
        pc[k] = pc.get(k, 0) + 1
    fc = {}
    for f in all_fixed:
        k = f.get('fix') or 'unknown'
        fc[k] = fc.get(k, 0) + 1
    report['problem_counts'] = pc
    report['fix_counts'] = fc

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.report_path:
        try:
            with open(args.report_path, 'w', encoding='utf-8') as fh:
                fh.write(text + '\n')
        except Exception as e:
            print(json.dumps({'error': str(e)}))
            sys.exit(2)
    print(text)

    # Cleanup: remove md_autofix markers from workflow YAML files (they break actionlint)
    marker = '<!-- md_autofix: processed -->'
    workflow_dir = os.path.join('.', '.github', 'workflows')
    if os.path.isdir(workflow_dir):
        for root, dirs, files in os.walk(workflow_dir):
            for f in files:
                if not (f.endswith('.yml') or f.endswith('.yaml')):
                    continue
                wfpath = os.path.join(root, f)
                try:
                    with open(wfpath, 'r', encoding='utf-8') as fh:
                        lines = fh.readlines()
                    new_lines = [ln for ln in lines if marker not in ln]
                    if len(new_lines) != len(lines):
                        with open(wfpath, 'w', encoding='utf-8') as fh:
                            fh.writelines(new_lines)
                        # record this change in the report file summary
                        report_entry = {'file': wfpath, 'detected_problems': [], 'fixed': [{'file': wfpath, 'fix': 'remove md_autofix marker from workflow'}], 'unsolved': []}
                        per_file.append(report_entry)
                        report['per_file'] = per_file
                        report['fix_counts']['remove md_autofix marker from workflow'] = report['fix_counts'].get('remove md_autofix marker from workflow', 0) + 1
                except Exception:
                    pass

    # update state-driven policies: if a problem repeats above threshold, enable auto-fix for it
    thresholds = state.get('thresholds', {})
    auto_thresh = thresholds.get('auto_fix_enable', 100)
    for pname, cnt in state.get('problem_counts', {}).items():
        # set policy to auto-fix when problem is frequent
        if cnt >= auto_thresh:
            state.setdefault('policies', {})
            if state['policies'].get(pname) != 'auto-fix':
                state['policies'][pname] = 'auto-fix'
    save_state(state, repo_root='.')

    # write insights summary for external agents to read
    try:
        write_insights(report, state)
    except Exception:
        pass



if __name__ == '__main__':
    main()
