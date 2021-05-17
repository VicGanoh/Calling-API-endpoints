# This line of codes calls the Global API endpoint of coingecko
# and take the type of data we need and then store them 
# import the needed libraries
import requests as req
import json
from datetime import datetime 

# get cryptocurrency global data using 'global' endpoint
global_url = 'https://api.coingecko.com/api/v3/global'

# get request
request = req.get(global_url)
# Format data into JSON
result = request.json()

# print(json.dumps(result, indent=4))

# store data in variables 
# Get active_currencies, markets and last updated 
active_currencies = result['data']['active_cryptocurrencies']
active_markets = result['data']['markets']
last_updated = result['data']['updated_at']
total_volume_btc = result['data']['total_volume']['btc']
btc_cap_percentage = result['data']['market_cap_percentage']['btc']

# format currencies and markets 
active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
total_volume_btc_string = '{:,}'.format(total_volume_btc)

# format date and time of data
last_updated = datetime.now()


print()
print(f'There are currently {active_currencies_string} active cryptocurrencies and {active_markets_string} active markets.')
print(f'Last Updated: {last_updated}.')
print(f'Bitcoin total volume currently: {total_volume_btc_string}.')
print(f'Bitcoin percentage currently: {round(btc_cap_percentage, 2)} %.')
