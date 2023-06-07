import random
from typing import List
from sense_hat import SenseHat
from types import SimpleNamespace
import numpy as np
import json
import time

import weather_api
import weather_display
import color
from weather_codes import WeatherCodes
import weather_animation

UPDATE_INTERVAL = 60000

sense = SenseHat()
#weather_data = json.load(open('temp.json'), object_hook=lambda d: SimpleNamespace(**d))
#weather_codes = list(map(lambda w: WeatherCodes(w), weather_data.hourly.weathercode))
weather_codes = weather_api.get_forecast()
column_data = weather_display.create_display_cols(weather_codes[:8])
column_animations = weather_animation.create_col_animations(weather_codes[:8])
pixels = list(np.concatenate(column_data))
last_update_time = time.time()

sense.set_pixels(pixels)

while True:
  current_time = time.time()
  if current_time - last_update_time >= UPDATE_INTERVAL:
    last_update_time = current_time
    weather_codes = weather_api.get_forecast()

  weather_animation.update_animations(column_animations, column_data, pixels)
  sense.set_pixels(pixels)
  time.sleep(.2)
