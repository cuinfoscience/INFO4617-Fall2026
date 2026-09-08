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
