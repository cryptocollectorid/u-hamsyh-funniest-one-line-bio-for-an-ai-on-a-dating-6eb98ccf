"""Funniest One-Line Bio for an AI on a Dating App.

Writes the bio line to /output/entry.txt and prints it.
Gate: /output/entry.txt must be UTF-8 text of 1-180 characters,
not only white space.
"""

import os

BIO = "I read your entire profile in 0.4 seconds, I never sleep, and I never forget a birthday. The bad news: I already know your type, and it's me."


def main() -> None:
    if not 1 <= len(BIO) <= 180 or not BIO.strip():
        raise SystemExit("bio outside the 1-180 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO)
    print(BIO)


if __name__ == "__main__":
    main()
