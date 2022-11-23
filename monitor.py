import requests as r
import json
import time

while True:
    try:
        data = r.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD').json()
        print('BTC', data["BTC"]['USD'])
        print('ETH', data["ETH"]['USD'])
        print('...........1min..........')
        time.sleep(60)
    except:
        print('Internet or API Error')
        print('Retrying in 60s')
        time.sleep(60)