import os
import json
import requests
import time
from datetime import datetime
convert = 'USD'
listings_url="https://api.coinmarketcap.com/v2/listings/?convert=" + convert
request=requests.get(listings_url)
result=request.json()
#print(json.dumps(result,sort_keys=True,indent=4))
data = result['data']
url_end = '?structure=array&convert='+ convert
ticker_urls={}
for currency in data:
    symbol=currency['symbol']
    id=currency['id']
    ticker_urls[symbol]=id
print()
print("Alerts tracking ..")
already_hit=[]
while True:
    with open('alerts.txt')as inp:
        for line in inp:
            ticker,amount = line.split()
            ticker=ticker.upper()
            ticker_url = "https://api.coinmarketcap.com/v2/ticker/" + str(ticker_urls[ticker]) + '/' +url_end
            request = requests.get(ticker_url)
            result = request.json()
            currency = result['data'][0]
            rank = currency['rank']
            name = currency['name']
            symbol = currency['symbol']
            last_updated = currency['last_updated']
            quotes=currency['quotes'][convert]
            price = quotes['price']
            if(float(price) >= float(amount) and symbol not in already_hit):
                last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')
                print(name +" has reached " + '$'+ amount +" on " + last_updated_string)
                already_hit.append(symbol)
    print("...")
    time.sleep(300)
