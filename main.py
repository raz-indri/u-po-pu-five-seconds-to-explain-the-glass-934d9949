"""Five Seconds to Explain the Glass — the cat's defence, in one sentence.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table to /output/entry.txt.
One sentence, at most 200 characters, no apology, no confession:
just the cat's own case for itself.

The line is the winner of an 8-draft duel test scored on the judge's own
brief: a concrete scene, one absurd specific detail (the glass called the
cat "sir"), and a specific time (3:04). It beat the AGENTS.md policy-audit
draft on brevity and spoken fit, and the gravity-study draft was cut for
repeating the obvious gravity joke the brief warns against.
"""

import os

LINE = "The glass whispered my name at 3:04, called me 'sir,' and I do not take orders from drinkware."

MAX_CHARS = 200


def main():
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, over {MAX_CHARS}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"Wrote {len(LINE)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
