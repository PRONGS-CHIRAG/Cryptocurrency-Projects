import xlsxwriter
import json
import requests
convert = 'USD'
start = 1
f = 1
crypto_workbook = xlsxwriter.Workbook("cryptocurrencies.xlsx")
crypto_sheet = crypto_workbook.add_worksheet()
crypto_sheet.write('A1','Name')
crypto_sheet.write('B1','Symbol')
crypto_sheet.write('C1','Market_cap')
crypto_sheet.write('D1','Price')
crypto_sheet.write('E1','Volume')
crypto_sheet.write('F1','Hour_change')
crypto_sheet.write('G1','Daily_change')
crypto_sheet.write('H1','Week_change')

for i in range(10):
    ticker_url = "https://api.coinmarketcap.com/v2/ticker/?structure=array&start=" + str(start)
    request=requests.get(ticker_url)
    result = request.json()
    data = result['data']
    for currency in data:
        rank = currency['rank']
        name = currency['name']
        symbol = currency['symbol']
        quotes = currency['quotes'][convert]
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        daily_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        volume = quotes['volume_24h']
        price = quotes['price']
        crypto_sheet.write(f,0,name)
        crypto_sheet.write(f,1,symbol)
        crypto_sheet.write(f,2,str(market_cap))
        crypto_sheet.write(f,3,str(price))
        crypto_sheet.write(f,4,str(volume))
        crypto_sheet.write(f,5,str(hour_change))
        crypto_sheet.write(f,6,str(daily_change))
        crypto_sheet.write(f,7,str(week_change))
        f += 1
    start += 100
crypto_workbook.close()
