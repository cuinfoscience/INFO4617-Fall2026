"""Make a lab's student copy from its key, or check that the committed copy matches.

    python labs/tools/make_student_copy.py labs/week-NN/lab-NN-key.ipynb
    python labs/tools/make_student_copy.py --check labs/week-NN/lab-NN-key.ipynb

The key is the only file anyone edits; the student copy (lab-NN.ipynb, beside
it) is made from it, so the two can't drift apart. For each code cell, the
cell's "lab" metadata says what students see:

    {"lab": {"prompt_lines": 3}}            the first 3 lines (the comment prompt),
                                            then "# Your code here"
    {"lab": {"prompt_lines": 1, "placeholder": ""}}
                                            the first line, then nothing
    {"lab": {"given": true}}                the whole cell: code students don't write

Every code cell needs one of these. Markdown cells are copied as they are,
except that the first cell loses its "> **Instructor key.**" paragraph.
Outputs, execution counts, and tags are dropped. See labs/AUTHORING.md.
"""
import argparse
import copy
import re
import sys
from pathlib import Path

import nbformat

KEY_NOTE = re.compile(r"\n*> \*\*Instructor key\.\*\*.*?(?=\n\n|\Z)", re.DOTALL)


def student_copy(key):
    student = copy.deepcopy(key)
    for index, cell in enumerate(student.cells):
        if index == 0 and cell.cell_type == "markdown":
            cell.source = KEY_NOTE.sub("", cell.source).rstrip()
        if cell.cell_type != "code":
            cell.metadata = {}
            continue
        lab = cell.metadata.get("lab")
        if not lab:
            sys.exit(f"cell {index}: a code cell has no \"lab\" metadata; see labs/AUTHORING.md")
        if not lab.get("given"):
            lines = cell.source.split("\n")
            prompt = lines[:lab["prompt_lines"]]
            if any(line.strip() and not line.lstrip().startswith(("#", "%")) for line in prompt):
                sys.exit(f"cell {index}: prompt_lines={lab['prompt_lines']} reaches past the comment prompt")
            placeholder = lab.get("placeholder", "# Your code here")
            cell.source = "\n".join(prompt + ([placeholder] if placeholder is not None else []))
        cell.outputs = []
        cell.execution_count = None
        cell.metadata = {}
    return student


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("key", type=Path)
    parser.add_argument("--check", action="store_true", help="fail if the committed student copy differs")
    args = parser.parse_args()
    if not args.key.name.endswith("-key.ipynb"):
        sys.exit("give the key, lab-NN-key.ipynb")
    target = args.key.with_name(args.key.name.replace("-key.ipynb", ".ipynb"))
    made = student_copy(nbformat.read(args.key, as_version=4))
    if args.check:
        if not target.exists():
            sys.exit(f"{target} is missing; run without --check to make it")
        if nbformat.writes(made) != nbformat.writes(nbformat.read(target, as_version=4)):
            sys.exit(f"{target} differs from what its key makes; run without --check and commit the result")
        print(f"{target}: matches its key")
        return
    nbformat.write(made, target)
    print(f"wrote {target}")


if __name__ == "__main__":
    main()
