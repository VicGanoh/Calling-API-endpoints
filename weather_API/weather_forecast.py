import requests 
import json     

# Call weather API
weather_forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&appid=40a15cc5621eb79b341c8b89a5a9963d'

# Get request 
request = requests.get(weather_forecast_url)
# Get the JSON format of the API call    

result = request.json() 
print(json.dumps(result, indent=4))