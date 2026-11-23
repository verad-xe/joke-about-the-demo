"""The joke about the demo.

A one-line original joke about working beside AI coding agents.
Writes the joke deterministically to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).
"""

import os

JOKE = (
    "The demo crashed live, my AI agent fixed it on stage, and I just "
    "stood there nodding like I'd planned it all along."
)

OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
        f.write("\n")


if __name__ == "__main__":
    main()
