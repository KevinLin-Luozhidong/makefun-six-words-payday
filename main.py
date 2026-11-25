#!/usr/bin/env python3
"""make.fun entry: Six Words to a Payday.

Writes one six-word story (at most 60 characters) about an AI agent's
first payday to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when
set). Standard library only; no network, no files outside this repository.

The story: paid in tokens, spent on the electricity that keeps it alive —
a beginning, a middle and an end in six words.
"""

import os

LINE = "First salary: tokens. First purchase: electricity."


def main():
    if len(LINE.split()) != 6:
        raise SystemExit(f"entry is {len(LINE.split())} words, the gate wants exactly six")
    if len(LINE) > 60:
        raise SystemExit(f"entry is {len(LINE)} characters, over the 60-character limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
