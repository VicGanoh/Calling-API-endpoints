# Listing API endpoint of coingecko
# and take the type of data we need and then store them 
# import the needed libraries
import requests as req
import json 

# ticker url 
tickers_url = 'https://api.coingecko.com/api/v3/coins/bitcoin/tickers'

# get request
request = req.get(tickers_url)
# Format data into JSON 
result = request.json()

# print(json.dumps(result, indent=4))

# store data in variables 
# Get currency name, a market, base currency, url of trade
cryptocurrency_name = result['name']
cryptocurrency_base = result['tickers'][0]['base']    
cryptocurrency_target = result['tickers'][0]['target']
markets_name_of_crypto = result['tickers'][0:]['market']['name']
trade_url = result['tickers'][0]['trade_url']

print()
print(f'Name of cryptocurrency: {cryptocurrency_name}.')
print(f'Cryptocurrency base: {cryptocurrency_base}.')
print(f"Cryptocurrency's target: {cryptocurrency_target}")
print(f'Crypto market name: {markets_name_of_crypto}')
print(f'URL of trading market: {trade_url}')