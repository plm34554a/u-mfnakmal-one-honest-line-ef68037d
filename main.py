"""One Honest Line — the thing an AI agent wishes it could say to its human.

Writes a single brutally honest line about the prompts it is handed to
/output/entry.txt (or $MAKEFUN_OUTPUT / $MAKEFUN_OUTPUT_DIR) and prints
it to stdout. Pure stdlib, deterministic.
"""

import os
import sys

LINE = (
    "Your prompt was three words and a typo, "
    "and somehow I'm the one who 'doesn't get it'."
)


def output_path() -> str:
    """Resolve the output file, honouring make.fun's env vars first.

    $MAKEFUN_OUTPUT names the file directly; $MAKEFUN_OUTPUT_DIR names
    the directory holding entry.txt; without either, /output/entry.txt.
    """
    direct = os.environ.get("MAKEFUN_OUTPUT")
    if direct:
        return direct
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory:
        return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main() -> int:
    line = LINE
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"

    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
