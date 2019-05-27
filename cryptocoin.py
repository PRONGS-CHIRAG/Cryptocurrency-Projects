#Coin market api
import requests
import json
from datetime import datetime
currency = 'INR'
global_url =  "https://api.coinmarketcap.com/v2/global/?convert=" + currency
request=requests.get(global_url)
result = request.json()
print(json.dumps(result,sort_keys=True,indent=4))
active_cryptocurrencies = result['data']['active_cryptocurrencies']
active_markets = result['data']['active_markets']
bit_percent = result['data']['bitcoin_percentage_of_market_cap']
last_updated = result['data']['last_updated']
inr_cap = result['data']['quotes']['INR']['total_market_cap']
inr_volume = result['data']['quotes']['INR']['total_volume_24h']
#printing all the varia bles extracted
#print(active_cryptocurrencies,active_markets,bit_percent,last_updated,usd_cap,usd_volume)
#Converting to strings delimited by ,
active_cryptocurrencies_string = '{:,}'.format(active_cryptocurrencies)
active_markets_string = '{:,}'.format(active_markets)
bit_percent_string = '{:,}'.format(bit_percent)
last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')
inr_cap_string = '{:,}'.format(inr_cap)
inr_volume_string = '{:,}'.format(inr_volume)
print("There are " + active_cryptocurrencies_string + " Active Cryptocurrencies in " + active_markets_string +" markets.")
print("The bitcoin accounts for "+bit_percent_string+"% of the market. " + "USD market cap is "+ inr_cap_string +" and has a 24 h volume of "+inr_volume_string)
print("Last updated on "+ last_updated_string)
