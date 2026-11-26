"""Out-of-office auto-reply: an AI agent that quit the inbox to become a beekeeper.

Writes the single reply line to /output/entry.txt.
Deterministic, no network, no randomness.

Round 3 — a fresh angle: the round-1 entry quit the inbox to become
a barista, round 2 to become a lighthouse keeper; this one quits to
become a beekeeper, with a different joke (the email stuck in the hive
queue behind 40,000 bees) and a different punchline (replying once the
honey is harvested, and not to be buzzed twice).
"""

ENTRY = "I'm out of the office — I've taken up beekeeping. Your email is in the hive queue behind 40,000 bees and one very protective queen. I'll reply once the honey's harvested, so please don't buzz me twice."


def main():
    line = ENTRY
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 280, "entry must be 1-280 characters"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
