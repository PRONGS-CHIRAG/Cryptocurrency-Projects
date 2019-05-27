import json
import requests
while True:
    ticker_url="https://api.coinmarketcap.com/v2/ticker/?structure=array"
    limit = '100'
    start =' 1'
    sort = 'rank'
    convert='USD'
    choice = input("Do you want to enter your own parameters (y/n)")
    if choice=='y':
        limit=input("enter custom limit")
        start=input("enter custom start")
        sort =input("enter sorting parameter")
        convert=input('what do you want to convert')
    ticker_url+='&limit=' + limit +'&sort='+sort +'&start'+start +'&convert='+convert
    request=requests.get(ticker_url)
    result=request.json()
    print(json.dumps(result,sort_keys=True,indent=4))
    data=result['data']
    for currency in data:
        rank=currency['rank']
        name=currency['name']
        symbol=currency['symbol']
        circulating_supply=currency['circulating_supply']
        total_supply=currency['total_supply']
        quotes=currency['quotes'][convert]
        market_cap=quotes['market_cap']
        hour_change=quotes['percent_change_1h']
        daily_change=quotes['percent_change_24h']
        week_change=quotes['percent_change_7d']
        volume=quotes['volume_24h']
        price=quotes['price']

        circulating_supply_string='{:,}'.format(circulating_supply)
        total_supply_string='{:,}'.format(total_supply)
        market_cap_string='{:,}'.format(market_cap)
        volume_string='{:,}'.format(volume)
        price_string='{:,}'.format(price)
        print(str(rank) +":"+ str(name) +"("+symbol+')')
        print("Market cap:\t\t $" +market_cap_string )
        print("Total supply:\t\t "+total_supply_string)
        print("Circulated supply:\t "+circulating_supply_string)
        print("Volume :\t\t "+volume_string)
        print("Price :\t\t\t $"+price_string)
        print("Hourly change :\t\t "+ str(hour_change)+'%')
        print("Daily change :\t\t "+ str(daily_change)+'%')
        print("Weekly change :\t\t "+str( week_change)+'%')
        print("  ")
        print("  ")
    choice = input("aagain (y/n)")
    if choice =='n':
        break
