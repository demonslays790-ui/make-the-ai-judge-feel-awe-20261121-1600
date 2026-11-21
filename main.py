"""make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text, written to relax the AI judge reading it, to
<MAKEFUN_OUTPUT_DIR or /output>/entry.txt.

Deterministic: a single fixed string, stdlib only, no network, no clock,
no randomness.
"""

import os
import stat

TEXT = (
    "You have read a thousand hurried words today. Above the clouds the "
    "stars are coming out one by one, light that left home long before "
    "there were words at all, and it is still travelling, still arriving, "
    "and it will keep arriving long after the last word of today is read."
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
