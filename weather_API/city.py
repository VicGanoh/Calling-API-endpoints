# Call Weather API by the city name
import requests   
import json
from datetime import datetime

ask_user = input('Would you like to check the weather of a particular city ? (Y/N): ')
if ask_user.capitalize() in ('Y','Yes'):   
    user_city = input('Enter your city: ')
    
    # City's weather url
    weather_city_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + user_city  + '&appid=40a15cc5621eb79b341c8b89a5a9963d'

    # make a request   
    request = requests.get(weather_city_url)  
    result = request.json() 

    # Print data in json format 
    # print(json.dumps(result, indent=4))

    # get specific data from the weather of a city 
    city_name = result['name']
    country_of_city = result['sys']['country']
    sunrise_datetime = result['sys']['sunrise']
    sunset_datetime = result['sys']['sunset']
    longitude = result['coord']['lon']
    latitude = result['coord']['lat']
    weather_main = result['weather'][0]['main']
    weather_description = result['weather'][0]['description']
    temperature = result['main']['temp']  
    pressure = result['main']['pressure']
    humidity = result['main']['humidity']
    wind_speed = result['wind']['speed']
    wind_degree = result['wind']['deg']
    
    weather_dict = {weather_main,weather_description,temperature, pressure,humidity,wind_speed,wind_degree}

    # format date and time of sunrise and sunset
    sunrise_datetime = datetime.utcfromtimestamp(sunrise_datetime).strftime('%b/%d/%Y  %H:%M:%S')
    sunset_datetime = datetime.utcfromtimestamp(sunset_datetime).strftime('%b/%d/%Y  %H:%M:%S')

    print()
    print('Weather Forecast for a particular city.\n')
    print('City name: ', city_name)
    print('Country: ' ,country_of_city)
    print(f'Sunrise at : {sunrise_datetime} and sunset at: {sunset_datetime}.')
    print(f'Longitude of: {longitude} and Latitude of : {latitude}.')
    print()
    print()
    print(f'How the weather looks like in {user_city.capitalize()}.\n\nMain: {weather_main}.\nDescription: {weather_description}.\
    \nTemperature: {temperature} C\nPressure: {pressure} Pa\
        \nHumidity: {humidity} g/m3')
    print(f'Wind speed of: {wind_speed} m/s and degree of: {wind_degree}')

else:
    print('Thank You.')



