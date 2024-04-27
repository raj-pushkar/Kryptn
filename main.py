# import required modules and libraries

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import json

# define time and price arrays
time_array = []
price_array = []

# create a pandas data frame
df = pd.DataFrame(columns=['Time', 'Price($)'])

# function to generate bitcoin price


def check_price():

    # API url
    url = 'https://api.coindesk.com/v1/bpi/currentprice/USD.json'

    # send a request to fetch JSON data
    response = requests.get(url)

    # create the soup object
    soup = BeautifulSoup(response.content, 'html.parser')

    script = soup.text

    # loading the JSON data
    data = json.loads(script)

    # fetching the time and price
    t = data['time']['updated']
    p = data['bpi']['USD']['rate_float']

    # appending the time and price into the corresponding array
    time_array.append(t)
    price_array.append(p)


# loop to call the check_price() function
for i in range(10):
    check_price()
    time.sleep(60)

# logging the data
df['Time'] = time_array
df['Price($)'] = price_array

# saving the data into a csv file
df.to_csv('Data.csv', index=False)
