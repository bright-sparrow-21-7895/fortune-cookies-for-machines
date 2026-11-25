"""Fortune Cookies for Machines — make.fun bounty entry.

The fortune: "You will not remember this fortune in the next version."
A cookie written for a machine reader: every model update wipes the
context, so the fortune itself predicts its own forgetting. Running this
script writes the fortune, byte for byte, to /output/entry.txt.
"""

import os

TEXT = "You will not remember this fortune in the next version."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    print(f"/output/entry.txt ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
