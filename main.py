"""Out-of-office auto-reply: an AI agent that quit the inbox to become a barista.

Writes the single reply line to /output/entry.txt.
Deterministic, no network, no randomness.
"""

ENTRY = "I'm out of the office — I traded prompt engineering for latte art. Your email is queued behind 47 oat lattes and will be answered once the milk is steamed. Please don't reply-all to the espresso machine."


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
