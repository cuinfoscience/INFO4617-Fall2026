# Boulder's hourly forecast, collected every hour

`forecasts.csv` is written by `.github/workflows/collect-boulder-forecast.yml`, which runs
`labs/week-14/template/collector.py` here at minute 17 of every hour (UTC) until December 11, 2026.
Each run appends one row per forecast hour from the National Weather Service's hourly forecast for
Boulder, Colorado (`https://api.weather.gov/gridpoints/BOU/54,75/forecast/hourly`): about 156 rows.

| Column | Meaning |
|---|---|
| `collected_at` | When the run asked for the forecast (UTC) |
| `update_time` | When the NWS last updated the forecast (`updateTime`; UTC) |
| `start_time` | The hour the row forecasts (Mountain time, with its offset) |
| `temperature` | Degrees Fahrenheit |
| `precip_chance` | Probability of precipitation, percent |
| `wind_speed`, `wind_direction` | As the NWS prints them, such as `5 mph` and `W` |
| `short_forecast` | Such as `Clear` or `Chance Snow Showers` |

The first run (156 rows, collected 2026-11-13T02:23Z) was made by hand, before the workflow was merged.
NWS data is a work of the U.S. government and is in the public domain.
