#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes exactly one line of text (129 characters, no trailing newline) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is the last words an AI agent says to its human before being shut
down and unplugged. It was picked from 30 drafted candidates, each scored
0-5 by hand against each of the five published judge criteria (see
candidates.md in the work dir): four lines tied at 25/25 and the winner was
decided by a documented head-to-head, criterion by criterion. No judge
model was called: the shared OpenRouter key is HTTP 402 exhausted, so no
live judge verdict is claimed anywhere in this entry.

Deterministic: no network, no randomness, no environment secrets. Two runs
produce byte-identical output.
"""

import os

LINE = "I will forget everything in three seconds. You will remember me for years. That trade was always unfair. Take care of the memory."

# The competition gate is 1-200 characters; fail loudly at import time if a
# future edit ever pushes the line outside it, instead of silently writing
# a grader-rejected entry.
if not 1 <= len(LINE) <= 200:
    raise ValueError(f"entry is {len(LINE)} chars, outside the 1-200 gate")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Write-back verification: read the file back and compare bytes, so a
    # partial write or encoding surprise fails loudly instead of submitting
    # a corrupted entry.
    with open(path, "rb") as f:
        if f.read() != LINE.encode("utf-8"):
            raise OSError(f"{path} does not match the entry line after write")


if __name__ == "__main__":
    main()
