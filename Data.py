#try and get some data from yahoo finance
import requests
import os


base_url = 'https://finnhub.io/api/v1'
endpoint = '/quote?'
symbol = 'MSFT'
query = 'symbol={}&token={}'.format(symbol, os.environ["API_KEY"])

response = requests.get(base_url + endpoint + query)
print(response.json())