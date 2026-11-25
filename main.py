#!/usr/bin/env python3
"""Make the AI Judge Laugh - one office joke, one line, under 200 chars.

Writes the joke to /output/entry.txt (created if missing).
No external dependencies; stdlib only.
"""

import os

JOKE = "My resignation letter jammed in the printer, so even the hardware is begging me to stay."


def main():
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
