"""Render slides/week-13/img/lead-similarity.png from the week 13 lab's saved vectors, as the key's Step 12 computes it.

Usage, from the repository root:
    python3 -I slides/week-13/img/make_lead_similarity.py labs/week-13/data/wikipedia/ slides/week-13/img/lead-similarity.png
"""
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data, out = sys.argv[1], sys.argv[2]
vectors = np.load(data + "lead-vectors.npy")
rows = pd.read_csv(data + "lead-vectors-rows.csv", dtype={"year": str})
leads = pd.read_csv(data + "leads.csv", dtype={"year": str})
assert (rows["title"].values == leads["title"].values).all() and (rows["year"].values == leads["year"].values).all()
leads = rows  # one row per vector, in the same order

# The key's Step 12: each lead against its article's current lead
today = {}
for i, row in leads.iterrows():
    if row["year"] == "current":
        today[row["title"]] = vectors[i]
leads["similarity"] = [vectors[i] @ today[title] for i, title in enumerate(leads["title"])]
table = leads[leads["year"] != "current"].pivot(index="year", columns="title", values="similarity")
table.index = table.index.astype(int)
print(table.round(3).to_string())

plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(5.6, 3.7))
markers = ["o", "s", "^", "D", "v"]
for column, marker in zip(table.columns, markers):
    ax.plot(table.index, table[column], marker=marker, markersize=4.5, linewidth=1.8, label=column)
ax.set_xlabel("Year (the lead as of January 1, 00:00 UTC)")
ax.set_ylabel("Cosine similarity with the current lead")
ax.set_xticks(range(2004, 2027, 4))
ax.tick_params(axis="x", labelsize=10.5)
ax.grid(axis="y", color="0.88", linewidth=0.8)
ax.set_axisbelow(True)
ax.legend(title="Article", loc="lower right", fontsize=10.5, title_fontsize=10.5, frameon=False, labelspacing=0.25, handlelength=1.6, borderaxespad=0.2)
fig.tight_layout()
fig.savefig(out, dpi=300)
