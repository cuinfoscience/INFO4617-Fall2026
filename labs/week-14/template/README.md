# Boulder's hourly forecast, collected every hour

This repository saves the National Weather Service's hourly forecast for Boulder, Colorado, once an hour, for INFO 4617/5617's week 14 lab ([chapter 14 of *Web Data Science*](https://cuinfoscience.github.io/Web-Data-Science-Book/ch-14-automation.html)).

- `collector.py` asks the NWS for the forecast (`https://api.weather.gov/gridpoints/BOU/54,75/forecast/hourly`) and adds one row per forecast hour to `forecasts.csv`: about 156 rows a run, covering the next six and a half days.
- `.github/workflows/collect.yml` runs `collector.py` on GitHub's computers at minute 17 of every hour (UTC), and commits the new rows. Its **Run workflow** button, on the **Actions** tab, runs it at once.
- `forecasts.csv` doesn't exist until the first run makes it.

| Column | Meaning |
|---|---|
| `collected_at` | When the run asked for the forecast (UTC) |
| `update_time` | When the NWS last updated the forecast (`updateTime`; UTC) |
| `start_time` | The hour the row forecasts (Mountain time, with its offset) |
| `temperature` | Degrees Fahrenheit |
| `precip_chance` | Probability of precipitation, percent |
| `wind_speed`, `wind_direction` | As the NWS prints them, such as `5 mph` and `W` |
| `short_forecast` | Such as `Clear` or `Chance Snow Showers` |

## Put your email in it

The NWS asks every program to say who runs it. Open `collector.py` on GitHub, click the pencil (**Edit this file**), change `your-email@colorado.edu` in `HEADERS` to your own address, and click **Commit changes**. This repository is public, so anyone can read that address.

## Stop it

`collector.py` stops asking the NWS after December 11, 2026 (`LAST_DAY`); after that, each run only prints that collection has ended. To stop it sooner, or to stop the hourly runs altogether, open the **Actions** tab, click **Collect Boulder's hourly forecast** on the left, open the **⋯** menu at the top right, and choose **Disable workflow** ([GitHub's steps](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows)). GitHub also pauses scheduled workflows in a public repository that has had no activity for 60 days.

## The data

The forecasts come from the [National Weather Service API](https://www.weather.gov/documentation/services-web-api). They are a work of the U.S. government, in the public domain: the NWS calls them "open data, free to use for any purpose."
