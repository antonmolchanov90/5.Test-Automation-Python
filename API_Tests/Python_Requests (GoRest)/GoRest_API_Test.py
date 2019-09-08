# Public API for testing - https://gorest.co.in

import requests

# Users API test
response = requests.request('get', 'https://gorest.co.in/public-api/users')
if response.status_code != 200:
    print('Error')
else:
    print('Passed')

# Posts API test
response = requests.request('get', 'https://gorest.co.in/public-api/posts')
if response.status_code != 200:
    print('Error')
else:
    print('Passed')

# Comments API test
response = requests.request('get', 'https://gorest.co.in/public-api/comments')
if response.status_code != 200:
    print('Error')
else:
    print('Passed')

# Albums API test
response = requests.request('get', 'https://gorest.co.in/public-api/albums')
if response.status_code != 200:
    print('Error')
else:
    print('Passed')

# Photos API test
response = requests.request('get', 'https://gorest.co.in/public-api/photos')
if response.status_code != 200:
    print('Error')
else:
    print('Passed')
