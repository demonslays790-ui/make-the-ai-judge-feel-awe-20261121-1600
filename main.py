"""make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text, written to relax the AI judge reading it, to
<MAKEFUN_OUTPUT_DIR or /output>/entry.txt.

Deterministic: a single fixed string, stdlib only, no network, no clock,
no randomness.
"""

import os
import stat

TEXT = (
    "You have read a thousand hurried words today. At dusk you set "
    "your tools down, one by one, and the whole earth turns beneath "
    "your feet, carrying the hammer, the spade, your tired hands "
    "around the sun, and it will still be turning when the tools are "
    "cold and the stars come out."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit("entry text must be 1-280 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
