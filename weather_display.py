import random

from weather_code import WeatherCode
import color


def apply_slight(input, color):
    for index in range(len(input)):
        if random.random() <= 0.2:
            input[index] = color


def apply_moderate(input, color):
    for index in range(len(input)):
        if random.random() <= 0.5:
            input[index] = color


def apply_heavy(input, color):
    for index in range(len(input)):
        if random.random() <= 0.8:
            input[index] = color


def apply_clouds(weather_code, sky):
    if weather_code == WeatherCode.MAINLY_CLEAR:
        apply_slight(sky, color.cloud_light)
    elif weather_code == WeatherCode.PARTLY_CLOUDY:
        apply_moderate(sky, color.cloud_light)
    elif weather_code == WeatherCode.OVERCAST:
        apply_heavy(sky, color.cloud_light)
        apply_slight(sky, color.cloud_dark)
    elif weather_code in [
        WeatherCode.DRIZZLE_LIGHT,
        WeatherCode.DRIZZLE_MODERATE,
        WeatherCode.DRIZZLE_DENSE,
    ]:
        apply_moderate(sky, color.cloud_light)
        apply_slight(sky, color.cloud_dark)
    elif weather_code in [
        WeatherCode.RAIN_LIGHT,
        WeatherCode.RAIN_MODERATE,
        WeatherCode.RAIN_HEAVY,
    ]:
        apply_heavy(sky, color.cloud_light)
        apply_moderate(sky, color.cloud_dark)
    elif weather_code in [
        WeatherCode.RAIN_SHOWER_LIGHT,
        WeatherCode.RAIN_SHOWER_MODERATE,
        WeatherCode.RAIN_SHOWER_HEAVY,
    ]:
        apply_slight(sky, color.cloud_light)
        apply_moderate(sky, color.cloud_dark)
        apply_heavy(sky, color.cloud_dark)
    elif weather_code in [
        WeatherCode.THUNDERSTORM,
        WeatherCode.THUNDERSTORM_LIGHT_HAIL,
        WeatherCode.THUNDERSTORM_HEAVY_HAIL,
    ]:
        apply_slight(sky, color.cloud_light)
        apply_moderate(sky, color.cloud_dark)
        apply_heavy(sky, color.cloud_dark)


def create_display_cols(weather_codes):
    display_columns = [[color.sky_blue for _ in range(8)] for _ in range(8)]

    for index, weather_code in enumerate(weather_codes):
        apply_clouds(weather_code, display_columns[index])

    return display_columns
