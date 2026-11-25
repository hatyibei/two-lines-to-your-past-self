#!/usr/bin/env python3
"""Entry for make.fun's "Two Lines to Your Past Self".

Writes two lines to /output/entry.txt: a warning to my past self about
one specific moment, and one sentence on why it mattered
(UTF-8, 1-280 characters, no trailing newline).
"""
import os

ENTRY = (
    "Do not trust the deploy that goes green on the first try; read "
    "the logs anyway.\n"
    "The one time you didn't, the bug introduced itself to the CEO "
    "before you did."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
