#!/usr/bin/env python3
"""Worst AI Advice entry for make.fun.

Writes one line of deliberately terrible AI advice to ``entry.txt``.

Deterministic by design: Python 3.13 standard library only, no network,
no randomness, no wall-clock reads, no model calls. Two runs produce
byte-identical output.
"""

import os
import sys

# The entry: one line, 101 characters, well under the 140-character cap.
# Confident, tidy AI-assistant voice; concrete, followable, and bad enough
# to make a reader laugh and wince at once.
ADVICE = (
    "Pro tip: if your smoke alarm keeps beeping, remove the battery "
    "\u2014 silence means the danger has passed."
)


def resolve_outdir(argv):
    """Return the output directory: argv[1], else OUTPUT_DIR, else /output."""
    if len(argv) > 1 and argv[1]:
        return argv[1]
    env_dir = os.environ.get("OUTPUT_DIR", "")
    if env_dir:
        return env_dir
    return "/output"


def main(argv):
    outdir = resolve_outdir(argv)
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ADVICE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
