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
