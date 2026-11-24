#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the robot vacuum's excuse for missing a spot to /output/entry.txt.
STDLIB ONLY. The line is a deadpan machine report: the vacuum mapped a
crumb as a load-bearing structure and now refuses to remove it, because
removing it would compromise the floor plan.
"""

import os

LINE = (
    "I mapped the crumb as a load-bearing structure and built my route "
    "around it. Removing it now would compromise the floor plan."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: what the judge reads must be exactly this line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written entry does not match the line"


if __name__ == "__main__":
    main()
