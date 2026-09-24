# Images for `week-04`

Four of the five original placeholders (`xml_tree.png`, `json_onion.png`,
`house_xml_raw.png`, `pr_review.png`) were replaced with large-type
`lstlisting` codeblocks directly on their frames instead of images — each was
showing text structure (an XML tree, a nested JSON object, a raw XML
response, a suggested code diff), which reads at least as clearly as a
diagram and needed no asset to source. Those stub files were removed.

`weather_forecast_plot.png` is **not a placeholder** — it is a real chart,
regenerated from a live Open-Meteo API call:

```bash
cd slides/week-04/img
python3 - <<'EOF'
import requests, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HEADERS = {"User-Agent": "INFO4617-course-deck/1.0 (contact: accounts@brianckeegan.com)"}
params = {"latitude": 40.01, "longitude": -105.27,
          "daily": "temperature_2m_max,temperature_2m_min",
          "temperature_unit": "fahrenheit", "timezone": "America/Denver"}
data = requests.get("https://api.open-meteo.com/v1/forecast", params=params, headers=HEADERS, timeout=20).json()
dates, highs, lows = data["daily"]["time"], data["daily"]["temperature_2m_max"], data["daily"]["temperature_2m_min"]

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(dates, highs, marker="o", color="#8B2635", label="High")
ax.plot(dates, lows, marker="o", color="#4A6FA5", label="Low")
ax.fill_between(range(len(dates)), lows, highs, alpha=0.15, color="#8B2635")
ax.set_title("Boulder, CO — 7-Day Forecast (Open-Meteo)")
ax.set_ylabel("Temperature (°F)")
ax.set_xticks(range(len(dates))); ax.set_xticklabels([d[5:] for d in dates], rotation=45, ha="right")
ax.legend(); ax.grid(alpha=0.3)
fig.tight_layout(); fig.savefig("weather_forecast_plot.png", dpi=150)
EOF
```

Re-run before class if you want the forecast current for that day; the
chapter's own framing ("yours will differ, and that's fine — record the
date") applies here too.

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

One figure from the textbook's chapter 4, captured on 2026-09-24 by
`tools/shots` in the textbook repo (recipe in `tools/shots/recipes/ch-04.yml`,
provenance in `images/ch-04/provenance.json` there). It is a copy: to refresh
it, retake and promote it in the textbook, then copy it here. The
`_annotated.pdf` carries the numbered markers as vector graphics.

| File | Shows | Used on | Narrowest legible width |
|---|---|---|---|
| `house-xml-tree_annotated.pdf` | The House roster (published September 2, 2026) in Chrome's XML tree: `<MemberData>` (1), `<members>` (2), the first and second `<member>` (3), and the first `<member-info>` (4), with `<title-info>` and the first member's `<committee-assignments>` folded | not yet (for "XML → DataFrame: the real House roster") | `0.59\textwidth` |

The narrowest legible width is where the figure's text reaches 16 pixels on a
slide shown 1920 pixels wide (`slides/common/AUTHORING.md`, "How much a
screenshot shows"). The chapter's two RSS figures are in the RSS handout
(`handouts/week-04/img/`). The back-fill plan's JSON figure (Open-Meteo in
Chrome's JSON view) was not made; the textbook's `docs/handoff.md` says why.

## Listed in `stubs.tsv`

`make_stubs.py` keeps this table in step with `stubs.tsv` and draws a gray
placeholder for any listed image that is missing. It rewrites only what is
between the two markers; the notes above are safe.

<!-- stubs:begin: generated from stubs.tsv by slides/common/make_stubs.py; edits between these markers are replaced -->
| File | Size | Should show |
|---|---|---|
| `weather_forecast_plot.png` | 1200x560 | Real Boulder, CO 7-day high/low forecast from a live Open-Meteo call, matplotlib OO interface (regenerate periodically to keep it current -- see img/IMAGES.md) |
<!-- stubs:end -->
