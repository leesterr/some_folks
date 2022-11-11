import requests
from datetime import datetime
from config import api_code


def query_weather(city):
    try:
        new = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_code}&units=metric')
        data = new.json()
        city_name = data['name']
        country_short = data['sys']['country']
        time_zone = data['timezone']
        cur_temp = data['main']['temp']
        max_tem = data['main']['temp_max']
        min_temp = data['main']['temp_min']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        date = datetime.fromtimestamp(data['dt'])
        desc = data['weather']
        main = data['weather'][0]['main']
        item, *null = desc
        description = item['description']
        icons = {
              'Clear': '\U00002600',
              'Clouds': '\U00002601',
              'Rain': '\U00002614',
              'Drizzle': '\U00002614',
              'Thunderstorm': '\U000026A1',
              'Snow': '\U0001F328',
              'Mist': '\U0001F328'
         }
        if main in icons:
            new = icons[main]
        else:
            new = 'Unobservable'
        details = (f'\U0001F3D8 <b>Location:</b> {city_name}\n\n\U0001F310 <b>Country:</b> {country_short}\n\n'
                   f'\U000023F2 <b>Date:</b> {date}\n\n'
                   f'\U0001F321 <b>Current Temperature:</b> {cur_temp}\xb0C\n\n'
                   f'\U000023F3 <b>Time Zone:</b> {time_zone}\n\n'
                   f'\U0001F4CD <b>Current Pressure:</b> {pressure}\n\n\U0001F305 <b>Sunrise Today:</b> {sunrise}\n\n'
                   f'\U0001F307 <b>Sunset Today:</b> {sunset}\n\n\U0001F4A8 <b>Wind Speed:</b> {wind}MPH\n\n'
                   f'\U0001F4A6 <b>Humidity:</b> {humidity} %rh\n\n'
                   f'\U0001F525 <b>Max Temperature:</b> {max_tem}\xb0C\n\n'
                   f'\U0001F4C9 <b>Min Temperature:</b> {min_temp}\xb0C\n\n'
                   f'\U00002139 <b>Description :</b> {description.capitalize()} {new}')
        return details
    except:
        error = f'\U00002620  No city named <b>"{city}"</b> \U00002620'
        return error
