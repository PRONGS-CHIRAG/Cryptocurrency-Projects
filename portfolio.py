import os
import json
import requests
from prettytable import PrettyTable
from colorama import Fore,Back,Style
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
print("PORTFOLIO:")
print()
portfolio_value = 0.00
last_updated = 0
table = PrettyTable(['Asset','Amount',convert + 'Value','Price','1h','24h','7d'])
with open('portfolio.txt') as inp:
    for line in inp:
        ticker,amount=line.split()
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
        hour_change = quotes['percent_change_1h']
        daily_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']
        print(json.dumps(result,sort_keys=True,indent=4))
        value = float(price) * float(amount)
        if hour_change > 0:
            hour_change_col = Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
        else :
            hour_change_col = Back.RED + str(hour_change) + '%' + Style.RESET_ALL
        if daily_change > 0:
            daily_change_col = Back.GREEN + str(daily_change) + '%' + Style.RESET_ALL
        else :
            daily_change_col = Back.RED + str(daily_change) + '%' + Style.RESET_ALL
        if week_change > 0:
            week_change_col = Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
        else :
            week_change_col = Back.RED + str(week_change) + '%' + Style.RESET_ALL
        portfolio_value+= value
        value_string = '{:,}'.format(round(value,2))
        table.add_row([name + '('+ symbol +')' , amount,'$' + value_string , '$' + str(price) , str(hour_change),str(daily_change),str(week_change) ])
print(table)
portfolio_value_string = '{:,}'.format(round(portfolio_value,2))
last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')
print("Total Portfolio value :$" + portfolio_value_string)
print(" Last updated : " + last_updated_string)
