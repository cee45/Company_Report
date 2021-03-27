import requests
import json
import pandas as pd
import time
from datetime import datetime
import matplotlib.pyplot as plt
from configparser import ConfigParser

config = ConfigParser()
config.read('auth.ini')
td_key = config.get('auth', 'td_key')

#Indivdual ID
td_consumer_key = td_key

#Add Ticker Symbol
ticker = 'SPY'

# THE DAILY PRICES ENDPOINT

# define an endpoint with a stock of your choice, MUST BE UPPER
endpoint = r"https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(ticker)

# define the payload
payload = {'apikey': td_consumer_key,
           'periodType': 'year',
           'frequencyType': 'daily',
           'frequency': '1',
           'period': '3',
           #'endDate': "",
           #'startDate': "",
           'needExtendedHoursData': 'true'}

# make a request
content = requests.get(url=endpoint, params=payload)

# convert it dictionary object
data = content.json()

df = pd.json_normalize(data['candles'])

#Convert Epoch time to Regular time
df['datetime'] = pd.to_datetime(df['datetime'],unit='ms')

print(df)
#print(df.keys())


