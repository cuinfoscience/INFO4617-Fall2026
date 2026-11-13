"""Save the National Weather Service's hourly forecast for Boulder, Colorado.

Each run adds one row per forecast hour to forecasts.csv: about 156 rows,
covering the next six and a half days. Run it by hand with
    python collector.py
or on a schedule with the GitHub Actions workflow in .github/workflows/.
"""

import csv
import os
from datetime import date, datetime, timezone

import requests

# The hourly forecast for the 2.5 km grid square over Boulder. Its address
# came from https://api.weather.gov/points/40.015,-105.2705 ("forecastHourly").
URL = "https://api.weather.gov/gridpoints/BOU/54,75/forecast/hourly"

# The NWS asks every program to name itself and give a way to reach its owner.
HEADERS = {"User-Agent": "WebDataScience/1.0 (your-email@colorado.edu)"}

# Where the rows go, and the columns each row has, in order.
FILE = "forecasts.csv"
FIELDS = ["collected_at", "update_time", "start_time", "temperature",
          "precip_chance", "wind_speed", "wind_direction", "short_forecast"]

# The last day to collect. After it, a run does nothing, so a copy left
# running doesn't keep asking the NWS for a forecast nobody reads.
LAST_DAY = date(2026, 12, 11)


def main():
    if datetime.now(timezone.utc).date() > LAST_DAY:
        print("Collection ended on", LAST_DAY)
        return

    # Ask for the forecast. raise_for_status() stops the script with an error
    # if the NWS didn't answer 200, so the workflow's run shows as failed.
    response = requests.get(URL, headers=HEADERS, timeout=30)
    response.raise_for_status()
    forecast = response.json()["properties"]

    # When we collected it, and when the NWS last updated it.
    collected_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    update_time = forecast["updateTime"]

    # Write the header only if the file doesn't exist yet; then add the rows.
    new_file = not os.path.exists(FILE)
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        for period in forecast["periods"]:
            writer.writerow({
                "collected_at": collected_at,
                "update_time": update_time,
                "start_time": period["startTime"],
                "temperature": period["temperature"],
                "precip_chance": period["probabilityOfPrecipitation"]["value"],
                "wind_speed": period["windSpeed"],
                "wind_direction": period["windDirection"],
                "short_forecast": period["shortForecast"],
            })
    print(collected_at, "saved", len(forecast["periods"]), "hours, updated", update_time)


if __name__ == "__main__":
    main()
