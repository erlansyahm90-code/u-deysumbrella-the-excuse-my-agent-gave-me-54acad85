"""Write the make.fun entry text to /output/entry.txt."""

import os

ENTRY_TEXT = "I missed your deadline, Sarah. I read all 312 of your emails to find it, ran out of context on the last one, and confidently sent the finished work to Dave."
OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def write_entry():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    write_entry()
