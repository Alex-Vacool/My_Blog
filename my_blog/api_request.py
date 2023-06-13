import requests
import pprint

#response = requests.get('http://127.0.0.1:8000/categories/categories/')

token = 'token'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/tags/', headers=headers)

pprint.pprint(response.json())


