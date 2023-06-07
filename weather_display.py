import random

from weather_codes import WeatherCodes
import color

def apply_slight(input, color):
    for index in range(len(input)):
        if random.random() <= .2:
            input[index] = color

def apply_moderate(input, color):
    for index in range(len(input)):
        if random.random() <= .5:
            input[index] = color

def apply_heavy(input, color):
    for index in range(len(input)):
        if random.random() <= .8:
            input[index] = color

def apply_clouds(weather_code, sky):
    if weather_code == WeatherCodes.MAINLY_CLEAR:
        apply_slight(sky, color.cloud_light)
    elif weather_code == WeatherCodes.PARTLY_CLOUDY:
        apply_moderate(sky, color.cloud_light)
    elif weather_code == WeatherCodes.OVERCAST:
        apply_heavy(sky, color.cloud_light)
        apply_slight(sky, color.cloud_dark)
    elif weather_code in [WeatherCodes.DRIZZLE_LIGHT, WeatherCodes.DRIZZLE_MODERATE,  WeatherCodes.DRIZZLE_DENSE]:
        apply_moderate(sky, color.cloud_light)
        apply_slight(sky, color.cloud_dark)
    elif weather_code in [WeatherCodes.RAIN_LIGHT, WeatherCodes.RAIN_MODERATE, WeatherCodes.RAIN_HEAVY]:
        apply_heavy(sky, color.cloud_light)
        apply_moderate(sky, color.cloud_dark)
    elif weather_code in [WeatherCodes.RAIN_SHOWER_LIGHT, WeatherCodes.RAIN_SHOWER_MODERATE, WeatherCodes.RAIN_SHOWER_HEAVY]:
        apply_slight(sky, color.cloud_light)
        apply_moderate(sky, color.cloud_dark)
        apply_heavy(sky, color.cloud_dark)
    elif weather_code in [WeatherCodes.THUNDERSTORM, WeatherCodes.THUNDERSTORM_LIGHT_HAIL, WeatherCodes.THUNDERSTORM_HEAVY_HAIL]:
        apply_slight(sky, color.cloud_light)
        apply_moderate(sky, color.cloud_dark)
        apply_heavy(sky, color.cloud_dark)

def create_display_cols(weather_codes):
    display_columns = [
        [color.sky_blue for _ in range(8)],
        [color.sky_blue for _ in range(8)],
        [color.sky_blue for _ in range(8)],
        [color.sky_blue for _ in range(8)],
        [color.sky_blue for _ in range(8)],
        [color.sky_blue for _ in range(8)],
        [color.sky_blue for _ in range(8)],
        [color.sky_blue for _ in range(8)],
    ]

    for index, weather_code in enumerate(weather_codes):
        apply_clouds(weather_code, display_columns[index])

    return display_columns