import requests as r
import json
import time

current_time = time.localtime()

while True:
    try:
        formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", current_time)
        print(formatted_time)
        data = r.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD').json()
        print('BTC', data["BTC"]['USD'])
        print('ETH', data["ETH"]['USD'])
        time.sleep(60)
    except:
        print('Internet or API Error')
        print('Retrying in 60s')
        time.sleep(60)
