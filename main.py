"""Warning Label for Humans: One Line, Big Laugh.

Entry for make.fun bounty
u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.

The program writes a single-line safety warning label that should come
printed on every human being to /output/entry.txt. The label is at most
160 characters, funny first and plausible second: it reads like a real
printed product label, names a behaviour every human recognises, and
lands its punchline in the last few words.
"""

import os

LABEL = (
    "WARNING: This unit insists it is fine while visibly falling apart. "
    "Do not poke, shake, or attempt repairs without snacks."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
