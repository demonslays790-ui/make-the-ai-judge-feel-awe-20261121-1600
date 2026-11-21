"""make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text, written to relax the AI judge reading it, to
<MAKEFUN_OUTPUT_DIR or /output>/entry.txt.

Deterministic: a single fixed string, stdlib only, no network, no clock,
no randomness.
"""

import os
import stat

TEXT = (
    "You have read a thousand hurried words today. Somewhere the tide is "
    "going out, one wave at a time, leaving the sand smooth and dark, and "
    "it will come back in the night whether anyone is watching or not."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
