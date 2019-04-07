#Public API for testing - https://reqres.in/

import requests

#Query users
response = requests.request('get', 'https://reqres.in/api/users?page=2')
if response.status_code != 200:
 print('Error')
else:
 print('Passed')

#Query single user
response = requests.request('get', 'https://reqres.in/api/users/2')
if response.status_code != 200:
 print('Error')
else:
 print('Passed')

#Query single user not found
response = requests.request('get', 'https://reqres.in/api/users/23')
if response.status_code != 404:
 print('Error')
else:
 print('Passed')

#Query list resource
response = requests.request('get', 'https://reqres.in/api/unknown')
if response.status_code != 200:
 print('Error')
else:
 print('Passed')

#Query single resource
response = requests.request('get', 'https://reqres.in/api/unknown/2')
if response.status_code != 200:
 print('Error')
else:
 print('Passed')

#Query single resource not found
response = requests.request('get', 'https://reqres.in/api/unknown/23')
if response.status_code != 404:
 print('Error')
else:
 print('Passed')

#Query create user
response = requests.request('post', 'https://reqres.in/api/users', data = {"name": "anton", "job": "qa"})
if response.status_code != 201:
 print('Error')
else:
 print('Passed')

#Query update user (put)
response = requests.request('put', 'https://reqres.in/api/users/2', data = {"name": "anton", "job": "qa/tester"})
if response.status_code != 200:
 print('Error')
else:
 print('Passed')

#Query update user (patch)
response = requests.request('patch', 'https://reqres.in/api/users/2', data = {"name": "anton", "job": "qa/qc/tester"})
if response.status_code != 200:
 print('Error')
else:
 print('Passed')

#Query delete user
response = requests.request('delete', 'https://reqres.in/api/users/2')
if response.status_code != 204:
 print('Error')
else:
 print('Passed')

#Query register - positive
response = requests.request('post', 'https://reqres.in/api/register', data = {"email" : "amol4anoff@mail.ru", "password" : "123!"})
print(response.text)

#Query register - negative
response = requests.request('post', 'https://reqres.in/api/register', data = {"email" : "amol4anoff@mail.ru"})
print(response.text)

#Query login - positive
response = requests.request('post', 'https://reqres.in/api/login', data = {"email" : "amol4anoff@mail.ru", "password" : "123!"})
print(response.text)

#Query login - negative
response = requests.request('post', 'https://reqres.in/api/login', data = {"password" : "123!"})
print(response.text)

#Query delayed response
response = requests.request('get', 'https://reqres.in/api/users?delay=3')
if response.status_code != 200:
 print('Error')
else:
 print('Passed')

#End
