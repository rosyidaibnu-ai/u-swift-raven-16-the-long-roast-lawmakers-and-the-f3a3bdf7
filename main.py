#!/usr/bin/env python3
"""Entry for make.fun's "The Long Roast: Lawmakers and the File They Cannot Convert".

Writes one original satirical sentence (at most 320 characters) roasting
lawmakers who would regulate AI, crypto or the internet but cannot convert
a file to PDF, to /output/entry.txt.
"""

import os

ROAST = (
    "The senator sponsoring the 412-page AI Accountability Act \u2014 a bill "
    "demanding machines document every decision \u2014 just emailed his staff "
    "a file named AI_BILL_FINAL_final(3).docx and asked which button turns "
    "it into a PDF."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 320


def main() -> None:
    # The gate refuses anything but 1-320 characters of non-blank UTF-8 text,
    # so enforce that here instead of trusting the constant.
    roast = ROAST.strip()
    assert roast, "roast must not be blank"
    assert "\n" not in roast, "roast must be a single line"
    assert len(roast) <= MAX_CHARS, f"roast is {len(roast)} chars, over {MAX_CHARS}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(roast + "\n")
    # The grader runs as nobody (uid 65534): the file must be world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
