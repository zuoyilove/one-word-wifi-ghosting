#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry program.

Writes a single word describing the entrant's Wi-Fi to
/output/entry.txt, the file the sealed scorer gates on.

The word: Ghosting.
Home Wi-Fi ghosts you — full bars one second, gone mid-sentence
the next, no goodbye, no explanation, back again like nothing
happened. It is the funniest true thing about it: a network that
behaves like a bad date. One word, instantly readable, no context
needed, and not the word everyone else reaches for.
"""

import os

WORD = "Ghosting"
OUT_PATH = "/output/entry.txt"

# The gate, from RULES.txt: /output/entry.txt must be UTF-8 text of
# 1 to 20 characters, not only white space. A single word satisfies
# it by construction; assert it here so a bad word never ships.
# "Ghosting" is 8 characters: comfortably inside the gate, and short
# enough that a reader gets the joke at a glance.
assert WORD, "entry word must not be empty"
assert WORD == WORD.strip(), "entry word must not carry whitespace"
assert " " not in WORD and "\t" not in WORD and "\n" not in WORD, (
    "entry must be one word, no spaces"
)
assert 1 <= len(WORD) <= 20, "gate: entry must be 1 to 20 characters"


def write_entry(word: str, path: str) -> None:
    """Write the word and read it back: the file the scorer gates
    on must hold exactly this word, byte for byte."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == word, "round-trip mismatch"


def main() -> None:
    write_entry(WORD, OUT_PATH)


if __name__ == "__main__":
    main()
