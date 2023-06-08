from sense_hat import SenseHat
import numpy as np
import time

import weather_api
import weather_display
import weather_animation

UPDATE_INTERVAL = 60000


def update_display_data():
    global weather_codes, column_data, column_animations, pixels
    weather_codes = weather_api.get_forecast()
    column_data = weather_display.create_display_cols(weather_codes[:8])
    column_animations = weather_animation.create_col_animations(weather_codes[:8])
    pixels = list(np.concatenate(column_data))


update_display_data()
sense = SenseHat()
sense.set_pixels(pixels)
last_update_time = time.time()

while True:
    current_time = time.time()
    if current_time - last_update_time >= UPDATE_INTERVAL:
        last_update_time = current_time
        update_display_data()

    weather_animation.update_animations(column_animations, column_data, pixels)
    sense.set_pixels(pixels)
    time.sleep(0.2)
