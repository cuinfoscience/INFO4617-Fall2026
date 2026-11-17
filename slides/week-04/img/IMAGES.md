# Images for `week-04`

Four of the five original placeholders (`xml_tree.png`, `json_onion.png`,
`house_xml_raw.png`, `pr_review.png`) were replaced with large-type
`lstlisting` codeblocks directly on their frames instead of images — each was
showing text structure (an XML tree, a nested JSON object, a raw XML
response, a suggested code diff), which reads at least as clearly as a
diagram and needed no asset to source. Those stub files were removed.

`power_boulder_2025.png` is **not a placeholder**: it is the figure students
draw in the lab's Step 14, Boulder's daily high and low for 2025 from NASA's
POWER API. It replaced `weather_forecast_plot.png` (a seven-day Open-Meteo
forecast) on 2026-11-17, when the deck's JSON example became the lab's. It was
drawn by the key's own cells, run on the lab's saved copy of POWER's answer,
so no new request was sent. From the repository's top folder:

```python
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

data = json.load(open("labs/week-04/data/power-boulder-2025.json"))
key = json.load(open("labs/week-04/lab-04-key.ipynb"))
cells = ["".join(c["source"]) for c in key["cells"] if c["cell_type"] == "code"]

def cell(holds):
    return next(c for c in cells if holds in c)

# Step 13's cells, then Step 14's plot, as the key has them
exec(cell('weather = pd.DataFrame(data["properties"]["parameter"])'))
exec(cell("weather.index = pd.to_datetime("))
exec(cell("NAMES = {"))
exec(cell('fill = data["header"]["fill_value"]'))
exec(cell("fig, ax = plt.subplots(figsize=(10, 4))").replace("plt.show()", ""))
fig.savefig("slides/week-04/img/power_boulder_2025.png", dpi=200, bbox_inches="tight")
```

2025 is a past year, so the figure doesn't go out of date. If the lab's plot
cell changes, run this again.

## Handout screenshots (`handout_*.png`)

Four real GitHub screenshots for `handouts/common/pull-request-walkthrough.md`,
captured by the instructor from an actual write-access session — not scripted
or regenerable, so recapture manually if GitHub's UI changes enough to make
these stale:

- `handout_edit_this_page.png` — the live chapter page's sidebar, showing
  **Edit this page** / **Report an issue**.
- `handout_editor_search.png` — GitHub's in-editor search bar, open and
  searching for the target line.
- `handout_preview_diff.png` — the diff view after the edit, old line in red
  and new line in green.
- `handout_commit_branch_choice.png` — the commit panel, showing both save
  options.

`handout_commit_branch_choice.png` had one field redacted before use: the
"Commit Email" dropdown showed the instructor's real address, which has no
pedagogical value in the handout and shouldn't be published to a public repo.
Redacted with:

```python
from PIL import Image, ImageDraw
im = Image.open("4.png").convert("RGB")
draw = ImageDraw.Draw(im)
draw.rectangle([20, 968, 520, 1058], fill=(30, 33, 40))
draw.rectangle([20, 968, 520, 1058], outline=(70, 74, 84), width=2)
```

All four were then downscaled to 700px wide (LANCZOS), preserving each
image's own aspect ratio rather than force-cropping to a fixed size — these
are dense UI screenshots and a hard crop would either cut content or blur
small text.

## From the textbook's screenshot toolkit (chapter 4)

Two figures from the textbook's chapter 4, captured on 2026-09-24 by
`tools/shots` in the textbook repo (recipes in `tools/shots/recipes/ch-04.yml`,
provenance in `images/ch-04/provenance.json` there). They are copies: to
refresh one, retake and promote it in the textbook, then copy it here. The
`_annotated.pdf` files carry the numbered markers as vector graphics.

| File | Shows | Used on | Narrowest legible width |
|---|---|---|---|
| `house-xml-tree_annotated.pdf` | The House roster (published September 2, 2026) in Chrome's XML tree: `<MemberData>` (1), `<members>` (2), the first and second `<member>` (3), and the first `<member-info>` (4), with `<title-info>` and the first member's `<committee-assignments>` folded | "Step 2: look at it in Chrome first", in the `0.6\textwidth` column | `0.59\textwidth` |
| `forecast-json_annotated.pdf` | The chapter's Open-Meteo request for Boulder in Chrome's JSON view, Pretty-print ticked (September 24, 2026): `daily_units` (1), `daily` (2), its `time` list (3), and `temperature_2m_max` (4) | not used: since 2026-11-17 the deck's JSON frames follow the lab's NASA POWER request (it would suit a frame on the Recommended Exercises' forecast) | `0.44\textwidth` |

The narrowest legible width is where the figure's text reaches 16 pixels on a
slide shown 1920 pixels wide (`slides/common/AUTHORING.md`, "How much a
screenshot shows"). The chapter's two RSS figures are in the RSS handout
(`handouts/week-04/img/`). The forecast is captured as an API client, although
api.open-meteo.com's robots.txt disallows every path: the maintainer's decision
of 2026-09-24, in the textbook's `docs/decisions.md`.

## Listed in `stubs.tsv`

`make_stubs.py` keeps this table in step with `stubs.tsv` and draws a gray
placeholder for any listed image that is missing. It rewrites only what is
between the two markers; the notes above are safe.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `power_boulder_2025.png` | 1706x802 | The lab's Step 14 figure: Boulder's daily high and low for 2025 from NASA POWER, drawn by the key's own cells (see img/IMAGES.md) |
<!-- stubs:end -->
