"""The Agent's Uh-Oh: one word an agent says when it has no idea what to do.

The word is "overthinking": the honest one-word confession of an agent that
is lost not because it knows too little, but because it is thinking too hard
about a task it cannot crack. It lands instantly, sounds like a machine
caught mid-task blurting out its own diagnosis, and it is fresh — not the
first obvious word anyone types.

Writes the word to /output/entry.txt (or $ENTRY_OUTPUT when set, for local
testing). Deterministic, stdlib only, no network, no input.
"""

import os

WORD = "overthinking"


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
