#!/usr/bin/env python3
"""Two Robots in an Elevator — one line of awkward robot small talk.

The line is built from three beats. First the robot overthinks the
greeting the way only a machine would: it runs dozens of simulations
before opening its mouth. Then the awkward admission: every single
simulation ended in silence. Then the anticlimax — after all that
compute, the robot just says hi. The joke lands on the first read
because the turn is the gap between the heavy setup and the flat
two-letter payoff, and the elevator is named so the scene is set.

Deterministic: the same line is written on every run.
"""

import os

SETUP = "I ran 47 simulations of saying hello in this elevator."
ADMISSION = "Every one ended with me saying nothing."
PUNCHLINE = "Hi."

LINE = " ".join([SETUP, ADMISSION, PUNCHLINE])

# The gate only accepts 1-200 characters: fail loudly here instead of
# shipping an invalid entry.
assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, gate wants 1-200"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
