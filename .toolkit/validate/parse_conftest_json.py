#!/usr/bin/env python3
import sys
import json
from pathlib import Path
import re


def clean_message(msg):
    if not isinstance(msg, str):
        try:
            return json.dumps(msg)
        except Exception:
            return str(msg)
    s = msg.strip()
    # If it looks like a JSON object, try to parse and extract common fields
    if s.startswith('{') and s.endswith('}'):
        try:
            j = json.loads(s)
            # prefer message, text, description fields
            for k in ('message', 'msg', 'text', 'description'):
                if k in j and isinstance(j[k], str) and j[k].strip():
                    return j[k].strip()
            # fallback: join key-values
            parts = []
            for k, v in j.items():
                parts.append(f"{k}: {v}")
            return '; '.join(parts)
        except Exception:
            pass
    # strip excessive whitespace and control chars
    s = re.sub(r'\s+', ' ', s)
    # remove surrounding quotes
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        s = s[1:-1]
    return s


def extract_from_json(data):
    entries = []
    # Conftest JSON often has 'results' array with objects that include 'message' and 'metadata' etc.
    items = []
    if isinstance(data, dict):
        if 'results' in data and isinstance(data['results'], list):
            items = data['results']
        elif 'failures' in data and isinstance(data['failures'], list):
            items = data['failures']
        else:
            # try to find first list value
            for v in data.values():
                if isinstance(v, list):
                    items = v
                    break
    elif isinstance(data, list):
        items = data

    for it in items:
        rule = None
        path = None
        message = None
        severity = None
        if isinstance(it, dict):
            # Common keys
            message = it.get('message') or it.get('msg') or it.get('description')
            # SARIF-like or conftest metadata
            rule = it.get('rule') or it.get('policy') or it.get('rule_id') or (it.get('metadata') or {}).get('name')
            # severity fields
            severity = it.get('level') or it.get('severity') or (it.get('properties') or {}).get('level')
            # location/path hints
            if 'location' in it and isinstance(it['location'], dict):
                path = it['location'].get('path') or it['location'].get('file')
            elif 'file' in it:
                path = it.get('file')
            elif 'resource' in it:
                path = it.get('resource')
            # some conftest outputs nest failures
            if not message:
                for k in ('failures', 'instances', 'errors'):
                    if k in it and isinstance(it[k], list) and it[k]:
                        sub = it[k][0]
                        if isinstance(sub, dict):
                            message = sub.get('message') or str(sub)
        # fallback serialize
        if not message:
            message = it if isinstance(it, str) else json.dumps(it)
        message = clean_message(message)
        entries.append({'rule': rule or 'unknown', 'path': path or 'unknown', 'message': message, 'severity': (severity or '').lower()})
    return entries


def parse_text_file(path):
    entries = []
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        # Heuristic: lines containing 'FAIL' or 'deny' or 'error'
        if 'FAIL' in line or 'deny' in line or 'error' in line.lower():
            entries.append({'rule': 'text', 'path': 'unknown', 'message': clean_message(line), 'severity': 'error'})
    return entries


def write_summary(entries, outpath, topn=5, title='Conftest policy scan — top {n} failures'):
    top = entries[:topn]
    md = [title.format(n=len(top)) + '\n']
    i = 1
    for e in top:
        md.append(f"{i}. Rule: `{e.get('rule')}` — Path: `{e.get('path')}`")
        md.append('')
        # Truncate long messages for PR comment; reference full artifact
        full_msg = e.get('message') or ''
        max_len = 200
        if len(full_msg) > max_len:
            short = full_msg[:max_len].rstrip() + '...'
            note = f" (truncated, see artifact: conftest-output.json)"
            md.append(f"- Message: {short}{note}")
        else:
            md.append(f"- Message: {full_msg}")
        if e.get('severity'):
            md.append(f"- Severity: {e.get('severity')}")
        md.append('')
        i += 1
    outpath.write_text('\n'.join(md), encoding='utf-8')


def main():
    if len(sys.argv) < 2:
        print('usage: parse_conftest_json.py <conftest-output.json> [N] [out.md]')
        sys.exit(2)
    inpath = Path(sys.argv[1])
    topn = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    outpath = Path(sys.argv[3]) if len(sys.argv) > 3 else Path('conftest-summary.md')
    entries = []
    if inpath.exists():
        try:
            data = json.loads(inpath.read_text(encoding='utf-8'))
            entries = extract_from_json(data)
        except Exception:
            entries = parse_text_file(inpath)
    else:
        txt = inpath.with_suffix('.txt')
        if txt.exists():
            entries = parse_text_file(txt)
    if not entries:
        outpath.write_text('# Conftest policy scan — no failures detected\n')
        print('Wrote', outpath)
        return
    # sort by severity: errors first
    def sev_score(s):
        if not s:
            return 2
        s = s.lower()
        if 'error' in s or 'deny' in s or 'critical' in s:
            return 0
        if 'warn' in s or 'warning' in s:
            return 1
        return 2
    entries = sorted(entries, key=lambda e: (sev_score(e.get('severity')), e.get('rule')))
    # write top-N summary
    write_summary(entries, outpath, topn)
    # write errors-only summary
    errors = [e for e in entries if sev_score(e.get('severity')) == 0]
    if errors:
        err_out = outpath.with_name(outpath.stem + '-errors' + outpath.suffix)
        write_summary(errors, err_out, topn, title='Conftest policy scan — top {n} errors')
        print('Wrote', outpath, 'and', err_out)
    else:
        print('Wrote', outpath)


if __name__ == '__main__':
    main()

<!-- md_autofix: processed -->
