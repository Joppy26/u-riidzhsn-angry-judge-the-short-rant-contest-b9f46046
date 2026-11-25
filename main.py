#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Deterministic: no randomness, no clock, no network,
no model calls, no reading anything outside this repository.
"""

import os

RANT = (
    "The office printer has one job. One. Yet every time I am already late "
    "it blinks, sighs, and prints a test page in a language I do not speak, "
    "then jams on page two like it is unionised. I have emailed IT four "
    "times. IT has emailed me a ticket number. The printer is still there, "
    "smug, warm, and completely useless, with better job security than I "
    "will ever have."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
