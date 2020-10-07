#https://home.openweathermap.org/

import requests

def Weather(city_name):
    url='http://api.openweathermap.org/data/2.5/weather?appid=8985a0673f6e1dfa6f3f4a2e38186489&q='
    url = url + city_name
    json_weather_data = requests.get(url).json()
    weather_main = json_weather_data['main']

    print(weather_main)
    return weather_main