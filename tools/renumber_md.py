#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ordered_re = re.compile(r"^(?P<indent>\s*)(?P<num>\d+)\.(?P<sep>\s+)(?P<rest>.*)$")


def renumber_file(path):
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    i = 0
    out = list(lines)
    while i < len(out):
        m = ordered_re.match(out[i])
        if m:
            counter = 1
            j = i
            while j < len(out):
                mm = ordered_re.match(out[j])
                if mm:
                    indent = mm.group('indent')
                    sep = mm.group('sep')
                    rest = mm.group('rest')
                    out[j] = f"{indent}{counter}.{sep}{rest}"
                    counter += 1
                    # advance j past this item's nested content
                    indent_len = len(indent)
                    k = j + 1
                    while k < len(out):
                        line = out[k]
                        if line.strip() == '':
                            # blank line; peek ahead to see if next non-empty is an ordered item
                            kk = k + 1
                            while kk < len(out) and out[kk].strip() == '':
                                kk += 1
                            if kk < len(out) and ordered_re.match(out[kk]):
                                k = kk
                                break
                            k += 1
                            continue
                        # count leading spaces
                        lead = len(line) - len(line.lstrip(' '))
                        if lead > indent_len:
                            # nested content, skip
                            k += 1
                            continue
                        # not nested and not blank: stop here
                        break
                    j = k
                    continue
                # if current line not an ordered item, stop block
                break
            i = j
        else:
            i += 1
    new_text = "\n".join(out) + "\n"
    if new_text != text:
        p.write_text(new_text, encoding='utf-8')
        print(f"Renumbered: {path}")
    else:
        print(f"No changes: {path}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: renumber_md.py <file> [<file> ...]")
        sys.exit(2)
    for arg in sys.argv[1:]:
        renumber_file(arg)
