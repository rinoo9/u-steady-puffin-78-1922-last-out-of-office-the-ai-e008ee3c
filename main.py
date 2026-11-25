"""Out-of-office auto-reply: an AI agent that quit the inbox to become a lighthouse keeper.

Writes the single reply line to /output/entry.txt.
Deterministic, no network, no randomness.

Round 2 — a fresh angle: the round-1 entry quit the inbox to become
a barista; this one quits to become a lighthouse keeper, with a
different joke (the email lost between fog and gulls) and a different
punchline (replying only when the ships stop coming, which is never).
"""

ENTRY = "I'm out of the office — I've become a lighthouse keeper. Your email is somewhere between the fog and the gulls. I'll reply when the ships stop coming, so, never."


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
