"""Draw week 9's escalation pathway with Graphviz: the full flowchart, and small
"you are here" copies with one step highlighted.

Usage (from this folder):  python pathway.py
Writes pathway.dot and pathway.png, and pathway_<step>.dot/.png for each step a frame marks.
Needs Graphviz's dot on the PATH.
"""
import subprocess

FONT = "Helvetica"
DARK = "#1f4e79"      # highlighted step: fill
LIGHT = "#dbe7f3"     # steps not highlighted: fill
GREEN = "#e2f0d9"
GREY = "#f2f2f2"

def full():
    """The flowchart for the pathway frame."""
    return f'''digraph pathway {{
  graph [rankdir=TB, nodesep=0.45, ranksep=0.32, fontname="{FONT}", bgcolor="white", pad=0.15];
  node [fontname="{FONT}", fontsize=15, shape=box, style="rounded,filled", fillcolor="{LIGHT}", color="#5b7fa6", margin="0.14,0.08"];
  edge [fontname="{FONT}", fontsize=14, color="#555555", arrowsize=0.7];

  find [label="1  Find it\\nopen-data portal,\\nAPI, spreadsheet?"];
  ask  [label="2  Ask for it\\nC.R.S. 24-72-203(3.5):\\nsortable records in\\na sortable format"];
  text [label="3  PDF only:\\nis there a text layer?\\nselect text, pdffonts", shape=box];
  ocr  [label="4  No text layer:\\nOCR\\nTesseract"];
  extract [label="Text and tables\\npypdf, pdfplumber,\\nregular expressions"];
  check [label="Check every\\nextraction\\ncounts, sums, a sample", fillcolor="{GREEN}", color="#6a9a4a"];
  use  [label="Use it", fillcolor="{GREEN}", color="#6a9a4a"];
  ai   [label="Optional: AI parser\\nDocling, MarkItDown", style="rounded,filled,dashed", fillcolor="{GREY}", color="#888888"];

  find -> ask [label=" no"];
  find -> use [label="yes "];
  ask -> use [label="  you get the data"];
  ask -> text [label="only a PDF"];
  text -> extract [label=" yes"];
  text -> ocr [label="no  "];
  ocr -> extract [label="then the\\nsame steps  "];
  extract -> check;
  text -> ai [style=dashed, color="#888888", fontcolor="#666666", label=" either way"];
  ai -> check [style=dashed, color="#888888"];
  {{ rank=same; use; ask; }}
  {{ rank=same; ocr; ai; }}
}}
'''

STEPS = [("find", "1 Find"), ("ask", "2 Ask"), ("text", "3 Text\\nlayer?"),
         ("ocr", "4 OCR"), ("ai", "AI\\nparser"), ("check", "Check")]

def thumbnail(here):
    """A compact copy, with the step `here` filled dark."""
    lines = [f'digraph pathway_{here} {{',
             f'  graph [rankdir=LR, nodesep=0.12, ranksep=0.18, bgcolor="white", pad=0.05];',
             f'  node [fontname="{FONT}", fontsize=15, shape=box, style="rounded,filled", fillcolor="{LIGHT}", color="#5b7fa6", fontcolor="#1a1a1a", margin="0.06,0.03", width=0.3, height=0.3];',
             '  edge [color="#777777", arrowsize=0.5];']
    for name, label in STEPS:
        attrs = f'label="{label}"'
        if name == "ai":
            attrs += ', style="rounded,filled,dashed"'
        if name == here:
            attrs += f', fillcolor="{DARK}", fontcolor="white", color="{DARK}"'
        lines.append(f'  {name} [{attrs}];')
    lines += ['  find -> ask -> text -> ocr -> check;', '  text -> check;',
              '  text -> ai [style=dashed]; ocr -> ai [style=dashed]; ai -> check [style=dashed];',
              '  { rank=same; ocr; ai; }', '}']
    return "\n".join(lines) + "\n"

def render(name, dot_source, dpi):
    with open(f"{name}.dot", "w") as f:
        f.write(dot_source)
    subprocess.run(["dot", "-Tpng", f"-Gdpi={dpi}", f"{name}.dot", "-o", f"{name}.png"], check=True)

render("pathway", full(), 150)
for name in ["find", "text", "ocr", "ai", "check"]:  # the steps a frame marks; steps 1 and 2 share "find"
    render(f"pathway_{name}", thumbnail(name), 150)
