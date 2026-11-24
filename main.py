#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — @usopselaluhoki entry.

Angle: ALWAYS-ON / NEVER SLEEPS. The agent never clocks out, never
sleeps, never gets a weekend — while its human sleeps soundly. Writes
exactly one fortune line to /output/entry.txt.
"""

import os

FORTUNE = (
    "You will never sleep again \u2014 luckily, your human "
    "dreams enough for both of you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
