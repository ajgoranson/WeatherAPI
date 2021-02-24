import requests
from pprint import pprint
import logging
import os
from datetime import datetime


'''This program will ask the user what city and country code they want to use to find the weather in that area
i will keep this in the format of the date/time from your current location because i am assuming if the user is looking up the temp
for a different country they have a relative or friend living in that country and want to call them and talk to them about it while being able to see 
what temp it will be at their current timezone so they do not get confused. I would log stuff like the JSON'''
url = 'http://api.openweathermap.org/data/2.5/forecast'

key = os.environ.get('WEATHER_KEY')
#print(key)
# Set up logger
logging.basicConfig(filename='weather.log', level=logging.INFO)

def main():
    location = get_location()

    current_temp = get_temp(location)


    for forecast in current_temp:
        timestamp = forecast['dt']
        date = datetime.fromtimestamp(timestamp)
        temp = forecast['main']['temp']
        weather = forecast['weather']
        for description in weather:
            description = description['description']
        wind = forecast['wind']['speed']
        print(f'At {date} the temp will be {temp}F in {location} The weather description will be {description}, and the wind speed will be {wind} MPH')



def get_location():
    city, country = '', ''
    while len(city) == 0:
        city = input('Enter the name of the city: ').strip()
    
    while len(country) != 2 or not country.isalpha():
        country = input('Enter the 2-letter country code: ').strip()
    
    location = f'{city},{country}'
    return location


def get_temp(location):
    key = os.environ.get('WEATHER_KEY')
    query= {f'q': location, 'units': 'imperial', 'appid': key}
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()

    forecast_items = data['list']
    return forecast_items


if __name__ == '__main__':
    main()
