import random
from typing import List

from weather_codes import WeatherCodes
import color

class Animation:
    color = None
    alpha = 0.0
    isFadingOut = False
    speed = 0
    frequency = 0.0
    index = None
    max_frequency = 0.0

    def __init__(self, color, speed, frequency, max_frequency):
        self.color = color
        self.speed = speed
        self.frequency = frequency
        self.max_frequency = max_frequency

    def __str__(self):
        return "(Animation: alpha {0}, isFadingOut {1}, index {2}, frequency {3})".format(self.alpha, self.isFadingOut, self.index, self.frequency)

def create_rain_animation(weather_code):
    max_frequency = weather_code.value/100
    return Animation(color.blue, 0.05, random.uniform(0, max_frequency), max_frequency)

def create_lightning_animation(weather_code):
    max_frequency = weather_code.value/100
    return Animation(color.yellow, 0.5, random.uniform(0, max_frequency), max_frequency)

def create_col_animations(weather_codes):
    col_animations = []
    for weather_code in weather_codes:
        if weather_code in [WeatherCodes.DRIZZLE_LIGHT, WeatherCodes.DRIZZLE_MODERATE,  WeatherCodes.DRIZZLE_DENSE]:
            col_animations.append([create_rain_animation(weather_code) for _ in range(1)])
        elif weather_code in [WeatherCodes.RAIN_LIGHT, WeatherCodes.RAIN_MODERATE, WeatherCodes.RAIN_HEAVY]:
            col_animations.append([create_rain_animation(weather_code) for _ in range(2)])
        elif weather_code in [WeatherCodes.RAIN_SHOWER_LIGHT, WeatherCodes.RAIN_SHOWER_MODERATE, WeatherCodes.RAIN_SHOWER_HEAVY]:
            col_animations.append([create_rain_animation(weather_code) for _ in range(3)])
        elif weather_code in [WeatherCodes.THUNDERSTORM, WeatherCodes.THUNDERSTORM_LIGHT_HAIL, WeatherCodes.THUNDERSTORM_HEAVY_HAIL]:
            col_animations.append([
                create_rain_animation(weather_code), create_rain_animation(weather_code), create_rain_animation(weather_code),
                create_lightning_animation(weather_code)
            ])
        else:
            col_animations.append([])
    return col_animations

def update_animations(column_animations: List[List[Animation]], column_data, pixels):
    for index, col in enumerate(column_animations):
        curr_anim_indicies = []
        for anim in col: #todo convert this to map
            if anim.index is not None:
                curr_anim_indicies.append(anim.index)
        avail_indicies = list(set(range(0,8)) - set(curr_anim_indicies))
        random.shuffle(avail_indicies)

        for animation in col:
            if animation.index is None: 
                if animation.frequency >= random.random():
                    animation.frequency = random.uniform(0, animation.max_frequency)
                    animation.index = avail_indicies.pop()
            elif animation.alpha < 0.0:
                animation.isFadingOut = False
                animation.index = None
                animation.alpha = 0.0
            else:
                if animation.alpha > 1.0:
                    animation.isFadingOut = True
                    animation.alpha = 1.0

                animation.alpha += animation.speed if not animation.isFadingOut else -animation.speed
                pixels[(index * 8) + animation.index] = color.blend(column_data[index][animation.index], animation.color, animation.alpha)
            #print("col: " + str(index) + ", " + str(animation))