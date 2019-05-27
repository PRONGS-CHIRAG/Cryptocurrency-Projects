import json
import requests
listings_url="https://api.coinmarketcap.com/v2/listings"
request=requests.get(listings_url)
result=request.json()
#print(json.dumps(result,sort_keys=True,indent=4))
data = result['data']
for currencies in data:
    id = currencies['id']
    name = currencies['name']
    symbol = currencies['symbol']
    website = currencies['website_slug']
    print(str(id)+ ": " + name +"(" + symbol +") "+ " --->" + str(website))
