"""The joke about the demo — writes one joke (1-280 chars) to /output/entry.txt.

Stdlib only. Deterministic: the same bytes every run.
"""

import os

JOKE = (
    "I told the client the demo was live. It was live the way a fish on a "
    "dock is live \u2014 technically moving, mostly flopping, and fifteen "
    "minutes from dinner."
)


def main() -> None:
    text = JOKE
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars, must be 1-280"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
