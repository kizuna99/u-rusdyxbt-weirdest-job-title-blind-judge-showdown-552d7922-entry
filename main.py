# SPDX-License-Identifier: MIT
"""Weirdest Job Title: Blind Judge Showdown — entry program.

Writes the single winning job title to /output/entry.txt.
"""

TITLE = "Certified Sommelier for Gas Station Slushies"


def main():
    # The grader runs the program with /output as the artifact directory;
    # create it when running locally so the output is identical either way.
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TITLE)


if __name__ == "__main__":
    main()
