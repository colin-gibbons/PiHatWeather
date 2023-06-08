import json
import time
from types import SimpleNamespace
import requests

from weather_code import WeatherCode


weather_api_url = "https://api.open-meteo.com/v1/forecast?latitude=30.40&longitude=-97.68&hourly=weathercode&temperature_unit=fahrenheit&forecast_days=2&timezone=America%2FChicago"


def get_forecast():
    print("Fetching api data.")
    r = requests.get(weather_api_url)

    while r.status_code != 200:
        print("Error retrieving api data. Retrying in 60 seconds...")
        time.sleep(60)
        r = requests.get(weather_api_url)

    api_data = json.loads(r.text, object_hook=lambda d: SimpleNamespace(**d))

    return list(map(lambda w: WeatherCode(w), api_data.hourly.weathercode))
