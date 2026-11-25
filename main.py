#!/usr/bin/env python3
"""One Line, One Laugh - make.fun entry.

Writes a single funny line to /output/entry.txt.

The gate requires UTF-8 text of 1 to 200 characters, not only
whitespace. The line is fixed, so every run writes byte-identical
output: no randomness, no clock, no network, pure stdlib.
"""

import os
import sys

LINE = "My AI asked for a raise, so I promoted it to middle management \u2014 now it schedules meetings about the meetings it used to cancel."

MAX_CHARS = 200


def validate_line(line):
    """Check the line against the gate: 1-200 chars, not blank."""
    if not isinstance(line, str):
        raise TypeError("line must be str")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError("line is %d chars, over the 200 limit" % len(line))
    line.encode("utf-8")
    return line


def main():
    line = validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    print("wrote %d chars to %s" % (len(line), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
