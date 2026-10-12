"""Week 9's attendance_chart.png: members present at each meeting's roll call,
counted by hand, beside what the slide's extract_attendance() finds.

Usage: python -I attendance_chart.py DATA_DIR OUT_PNG
DATA_DIR is the textbook's data/ch-09 folder, with its council-minutes-*.pdf.
"""
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pypdf import PdfReader

# Counted by hand from page 1 of each saved copy, 2026-10-12: members listed at
# roll call, in the room or online, with the presiding mayor; members who
# arrived later are not counted.
BY_HAND = {
    "2000-12-05": 8, "2000-12-19": 7, "2018-12-04": 8, "2019-12-03": 9,
    "2020-12-01": 8, "2020-12-15": 8, "2021-12-14": 8, "2022-12-01": 9,
    "2022-12-15": 9, "2023-12-07": 9, "2023-12-21": 9, "2024-12-05": 9,
    "2024-12-19": 9,
}


def split_names(match):
    """The slide's helper: comma-separated names after the label."""
    if not match:
        return []
    return [name.strip() for name in match.group(1).split(",") if name.strip()]


def slide_regex_count(pdf_path):
    """How many names the slide's extract_attendance() returns as present."""
    text = PdfReader(pdf_path).pages[0].extract_text()
    present = re.search(r"Present:\s*(.*?)\s*(?:Absent:|$)", text, re.IGNORECASE | re.MULTILINE)
    return len(split_names(present))


data_dir, out_png = sys.argv[1], sys.argv[2]
dates = sorted(BY_HAND)
found = {d: slide_regex_count(os.path.join(data_dir, f"council-minutes-{d}.pdf")) for d in dates}

plt.rcParams.update({"font.size": 13, "font.family": "DejaVu Sans"})
fig, ax = plt.subplots(figsize=(6, 5), dpi=200)
rows = range(len(dates))
ax.barh([i - 0.2 for i in rows], [BY_HAND[d] for d in dates], height=0.4, color="#1f4e79", label="counted by hand")
ax.barh([i + 0.2 for i in rows], [found[d] for d in dates], height=0.4, color="#9ecae1", label="the regex found")
for i, d in enumerate(dates):
    if found[d] == 0:
        ax.text(0.1, i + 0.2, "0", va="center", fontsize=12, color="#555555")
ax.set_yticks(list(rows), dates)
ax.invert_yaxis()
ax.set_xlim(0, 9)
ax.set_xticks(range(0, 10, 3))
ax.set_xlabel("Members present at roll call")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(loc="lower center", bbox_to_anchor=(0.4, 1.0), ncol=2, frameon=False, fontsize=12)
fig.tight_layout()
fig.savefig(out_png)
