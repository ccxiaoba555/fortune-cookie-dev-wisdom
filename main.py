"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The gate requires UTF-8 text of 1-120 characters,
not only white space, so the line is checked before it is written and
read back afterwards to prove the file holds exactly what was intended.
"""

import os

FORTUNE = (
    "The bug that keeps you up tonight was written by a past you "
    "who was certain it was obvious."
)

MAX_CHARS = 120


def main() -> None:
    line = FORTUNE.strip()
    assert line, "fortune must not be empty"
    assert "\n" not in line, "fortune must be a single line"
    assert len(line) <= MAX_CHARS, (
        f"fortune is {len(line)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read().strip()
    assert written == line, "written file does not match the fortune"


if __name__ == "__main__":
    main()
