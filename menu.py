import os
import json
import requests
from prettytable import PrettyTable
from colorama import Fore,Back,Style
from datetime import datetime

convert = 'USD'
global_url="https://api.coinmarketcap.com/v2/global/?convert=" + convert
request=requests.get(global_url)
result=request.json()
print(json.dumps(result,sort_keys=True,indent=4))
data = result['data']
quotes = data['quotes'][convert]
global_cap = int(quotes['total_market_cap'])
global_cap_string = '{:,}'.format(round(global_cap,3))

while True:
    print()
    print("Coincap Explorer Menu")
    print("The market global cap is $"+ global_cap_string)
    print()
    print("1- Top 100 sorted by rank")
    print("2- Top 100 sorted by 24hr change")
    print("3- Top 100 sorted by volume")
    print("0-Exit")
    choice = input("Enter your choice")
    ticker_url="https://api.coinmarketcap.com/v2/ticker/?structure=array&limit=100&sort="
    if choice =='1':
        ticker_url += 'rank'
    if choice == '2':
        ticker_url += 'percent_change_24h'
    if choice == '3':
        ticker_url += 'volume_24h'
    if choice == '0':
        break
    
    request = requests.get(ticker_url)
    result = request.json()
    data = result['data']
    table = PrettyTable(['Rank','Asset','Price','Market cap','Volume','1hr Change','Daily Change','Weekly change'])
    for currency in data:
        rank = currency['rank']
        name = currency['name']
        symbol = currency['symbol']
        last_updated = currency['last_updated']
        quotes = currency['quotes'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        daily_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        volume = quotes['volume_24h']
        price = quotes['price']
        if hour_change is not None:
            if hour_change > 0:
                hour_change_col = Back.GREEN + str(hour_change) +Style.RESET_ALL
            else:
                hour_change_col = Back.RED + str(hour_change) +Style.RESET_ALL
        else:
            print("error")
        if daily_change is not None:
            if daily_change > 0:
                daily_change_col = Back.GREEN + str(daily_change) +Style.RESET_ALL
            else:
                daily_change_col = Back.RED + str(daily_change) +Style.RESET_ALL
        else:
            print("error")
        if week_change is not None:
            if week_change > 0:
                week_change_col = Back.GREEN + str(week_change) +Style.RESET_ALL
            else:
                week_change_col = Back.RED + str(week_change) +Style.RESET_ALL
        else:
            print("error")
        if volume is not None:
            volume_string = '{:,}'.format(round(volume,3))
        else:
            print("error")
        if market_cap is not None:
            market_cap_string = '{:,}'.format(round(market_cap,3))
        table.add_row([rank,name + '('+ symbol +')' , '$' + str(price) ,'$' + market_cap_string, '$' + volume_string, str(hour_change),str(daily_change),str(week_change) ])
    print()
    print(table)
    choice = input("Again (y/n)")
    if choice == 'n':
        break
