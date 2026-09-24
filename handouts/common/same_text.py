#!/usr/bin/env python3
"""Exit 1 if two PDFs do not say the same thing.

    python common/same_text.py committed.pdf rebuilt.pdf

Compares the letters and digits of each PDF's text (pdftotext), so a PDF
built with a slightly different TeX Live on GitHub still matches the
committed one, while any changed word, number, or step does not. Used by
.github/workflows/build-handouts.yml to catch a PDF that was not rebuilt
after its .qmd changed.
"""
import difflib
import re
import subprocess
import sys


def words(pdf):
    text = subprocess.run(["pdftotext", "-layout", pdf, "-"], check=True,
                          capture_output=True, text=True).stdout
    return re.findall(r"[0-9A-Za-zÀ-ÿ]+", text)


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: same_text.py committed.pdf rebuilt.pdf")
    old, new = words(sys.argv[1]), words(sys.argv[2])
    if "".join(old) == "".join(new):
        print(f"{sys.argv[2]}: same text as the committed PDF")
        return 0
    print(f"{sys.argv[2]}: the committed PDF is out of date with its .qmd. "
          "Run `make` in handouts/ and commit the PDF. First differences:")
    diff = difflib.unified_diff(old, new, "committed", "rebuilt", n=3, lineterm="")
    for n, line in enumerate(diff):
        if n > 40:
            break
        print("  " + line)
    return 1


if __name__ == "__main__":
    sys.exit(main())
