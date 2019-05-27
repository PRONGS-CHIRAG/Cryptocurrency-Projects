import math
import json
import locale
import requests
from prettytable import PrettyTable
convert = 'USD'
locale.setlocale(locale.LC_ALL,'en-US.UTF-8')
global_url="https://api.coinmarketcap.com/v2/global/"
ticker_url = "https://api.coinmarketcap.com/v2/ticker/?structure=array"
request= requests.get(global_url)
result = request.json()
print(json.dumps(result,sort_keys=True,indent=4))
data = result['data']
market_cap = int(data['quotes'][convert]['total_market_cap'])
market_cap_string = '{:,}'.format(round(market_cap,3))
print("Total market cap is " + market_cap_string)
table = PrettyTable(['Name','Ticker','Percent of global','Current','7.7T','36.8T','73T','90.4T','217T','544T'])
request=requests.get(ticker_url)
result =request.json()
data = result['data']
for currency in data:
    name = currency['name']
    ticker = currency['symbol']
    percentage = float(currency['quotes'][convert]['market_cap'])/float(market_cap)
    current_price = round(float(currency['quotes'][convert]['price']),3)
    available_supply = float(currency['total_supply'])
    a7T_price = 770000000000 * percentage / available_supply
    a36T_price = 3680000000000 * percentage / available_supply
    a73T_price = 7300000000000 * percentage / available_supply
    a90T_price = 9040000000000 * percentage / available_supply
    a217T_price = 21700000000000 * percentage / available_supply
    a544T_price = 54400000000000 * percentage / available_supply
    percentage_string = str(round(percentage * 100,2)) + '%'
    current_price_string = '$' + str(current_price)
    a7T_price_string ='$' + '{:,}'.format(a7T_price)
    a36T_price_string = '$'+'{:,}'.format(a36T_price)
    a73T_price_string = '$'+'{:,}'.format(a73T_price)
    a90T_price_string = '$'+'{:,}'.format(a90T_price)
    a217T_price_string = '$'+'{:,}'.format(a217T_price)
    a544T_price_string = '$'+'{:,}'.format(a544T_price)
    table.add_row([str(name),str(ticker),percentage_string,current_price_string,a7T_price_string,a36T_price_string,a73T_price_string,a90T_price_string,a217T_price_string,a544T_price_string])
print(table)
