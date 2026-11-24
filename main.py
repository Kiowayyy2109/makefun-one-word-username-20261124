#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry generator.

Writes the entrant's own make.fun username, as a single word, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (fallback ``/output/entry.txt``).

The entry is exactly ``kiowayyy``: the account's own make.fun handle,
sent as one word and nothing else. Eight characters, well inside the
competition's 30-character gate.

Deterministic, standard library only. No network, no randomness.
"""

import os

ENTRY = "kiowayyy"
MAX_CHARS = 30


def main():
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(
            "entry %r is %d characters, over the %d-character limit"
            % (ENTRY, len(ENTRY), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR points at the output directory; accept either a
    # directory or a full file path for robustness.
    if out_dir.endswith(".txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    print("wrote %s (%d characters)" % (path, len(ENTRY)))


if __name__ == "__main__":
    main()
