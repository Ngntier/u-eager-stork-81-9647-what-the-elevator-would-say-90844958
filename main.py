"""Entry program for make.fun's "What the Elevator Would Say" bounty.

Writes one funny line, spoken in the elevator's own voice, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

Gate: the file must be UTF-8 text of 1 to 120 characters, not only
whitespace.
"""

import os

ENTRY = (
    "Relax. I've only dropped one person in forty years — "
    "and he pressed the button twice."
)

MAX_CHARS = 120


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry line is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line:
        raise ValueError("entry must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
