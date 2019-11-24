# Public API for testing - https://apidojo-yahoo-finance-v1.p.rapidapi.com

import requests

# Market Summary API test
response = requests.request('get', 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-summary')
print(response.headers)

# Market Movers API test
response = requests.request('get', 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-movers')
print(response.json)

# Market Quotes API test
response = requests.request('get', 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes')
print(response.text)

# Market Charts API test
response = requests.request('get', 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-charts')
print(response.url)

# Market Auto-Complete API test
response = requests.request('get', 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/auto-complete')
print(response.status_code)
