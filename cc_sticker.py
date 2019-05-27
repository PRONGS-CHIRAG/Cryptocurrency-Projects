import json
import requests
import operator
convert= 'USD'
ticker_url="https://api.coinmarketcap.com/v2/ticker/"
listings_url="https://api.coinmarketcap.com/v2/listings"
end= '?structure=array&convert='+ convert
request=requests.get(listings_url)
result=request.json()
#print(json.dumps(result,sort_keys=True,indent=4))
data=result['data']
ticker_urls={}
for currency in data:
    symbol=currency['symbol']
    id=currency['id']
    ticker_urls[symbol]=id
ticker_urls_sorted=sorted(ticker_urls.items(), key=operator.itemgetter(1))
#print(ticker_urls_sorted)
while True:
    choice=input("enter symbol of cryptocurrency")
    choice=choice.upper()
    ticker_url="https://api.coinmarketcap.com/v2/ticker/"+str(ticker_urls[choice])+'/'+ end
    print(ticker_url)
    request=requests.get(ticker_url)
    result=request.json()
    print(json.dumps(result,sort_keys=True,indent=4))
    data=result['data'][0]
    circulating_supply=data['circulating_supply']
    id = data['id']
    max_supply= data['max_supply']
    name = data['name']
    symbol = data['symbol']
    rank = data['rank']
    total_supply = data['total_supply']
    quotes=data['quotes'][convert]
    market_cap = quotes['market_cap']
    hour_change = quotes['percent_change_1h']
    daily_change = quotes['percent_change_24h']
    week_change= quotes['percent_change_7d']
    price = quotes['price']
    volume = quotes['volume_24h']
    circulating_supply_string="{:,}".format(circulating_supply)
    max_supply_string = '{:,}'.format(max_supply)
    total_supply_string = '{:,}'.format(total_supply)
    market_cap_string = '{:,}'.format(market_cap)
    volume_string ='{:,}'.format(volume)
    price_string ='{:,}'.format(price)
    print(str(rank) +":"+ str(name) +"("+symbol+')')
    print("Market cap:\t\t $" +market_cap_string )
    print("Total supply:\t\t "+total_supply_string)
    print("Circulated supply:\t "+circulating_supply_string)
    print("Volume :\t\t "+volume_string)
    print("Price :\t\t\t $"+price_string)
    print("Hourly change :\t\t "+ str(hour_change)+'%')
    print("Daily change :\t\t "+ str(daily_change)+'%')
    print("Weekly change :\t\t "+str(week_change)+'%')
    print("  ")
    print("  ")

    ch=input("again(y/n)")
    if ch == 'n':
        break
