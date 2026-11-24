"""One-Sentence Absurd Invention Pitch.

Writes exactly one sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance (tangled earphone cables) to /output/entry.txt.
Standard library only.
"""

import os

SENTENCE = (
    "The Pocket Butler is a tiny tuxedoed robot that rents a tiny room in "
    "your jeans, untangles your earphones before you even reach for them, "
    "and bows politely each time it finds a knot you tied yourself."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
