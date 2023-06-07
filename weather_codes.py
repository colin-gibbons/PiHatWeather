from enum import Enum

class WeatherCodes(Enum):
  CLEAR_SKY = 0
  MAINLY_CLEAR = 1
  PARTLY_CLOUDY = 2
  OVERCAST = 3
  DRIZZLE_LIGHT = 51
  DRIZZLE_MODERATE = 53
  DRIZZLE_DENSE = 55
  RAIN_LIGHT = 61
  RAIN_MODERATE = 63
  RAIN_HEAVY = 65
  RAIN_SHOWER_LIGHT = 80
  RAIN_SHOWER_MODERATE = 81
  RAIN_SHOWER_HEAVY = 82
  THUNDERSTORM = 95
  THUNDERSTORM_LIGHT_HAIL = 96
  THUNDERSTORM_HEAVY_HAIL = 99