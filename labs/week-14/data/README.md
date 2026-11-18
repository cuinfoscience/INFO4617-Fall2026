# Boulder's hourly forecast, collected on an hourly schedule

`forecasts.csv` is written by `.github/workflows/collect-boulder-forecast.yml`, which schedules
`labs/week-14/template/collector.py` here for minute 17 of every hour (UTC) until December 11, 2026.
GitHub doesn't run every scheduled time: in the first five days it started the workflow three or
four times a day, 4 to 10.6 hours apart (see below). Each run appends one row per forecast hour from
the National Weather Service's hourly forecast for Boulder, Colorado
(`https://api.weather.gov/gridpoints/BOU/54,75/forecast/hourly`): about 156 rows.

| Column | Meaning |
|---|---|
| `collected_at` | When the run asked for the forecast (UTC) |
| `update_time` | When the NWS last updated the forecast (`updateTime`; UTC) |
| `start_time` | The hour the row forecasts (Mountain time, with its offset) |
| `temperature` | Degrees Fahrenheit |
| `precip_chance` | Probability of precipitation, percent |
| `wind_speed`, `wind_direction` | As the NWS prints them, such as `5 mph` and `W` |
| `short_forecast` | Such as `Clear` or `Chance Snow Showers` |

The first run (156 rows, collected 2026-11-13T02:23Z) was made by hand, before the workflow was merged,
and the second (04:30Z) was started by hand too, a few minutes after the workflow reached `main` (04:22Z).
The first run the schedule started came at 13:10Z, almost nine hours later. On 2026-11-17 the file held
2,808 rows from 18 runs (2026-11-13T02:23Z to 2026-11-17T20:59Z), where a run every hour would have made
about 115: 3 or 4 runs a day, the scheduled ones 4.0 to 10.6 hours apart (6.9 at the median) and 12 to
54 minutes after minute 17. GitHub's documentation allows this: scheduled runs "can be delayed", and
under load "some queued jobs may be dropped"
([Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)).
The instructor decided on 2026-11-13 to keep the schedule as it is, and week 14's lab and chapter 14 teach
it as the example of what GitHub doesn't promise. `collected_at` is when a run really asked, so the gaps
can be measured from the file.

NWS data is a work of the U.S. government and is in the public domain.
