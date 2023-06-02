import requests
import pprint


#response = requests.get('http://127.0.0.1:8000/categories/categories/')
#response = requests.get('http://127.0.0.1:8000/api/v0/tags/')
#response = requests.get('http://127.0.0.1:8000/api/v0/tags/', auth=('author', 'pflybwf123'))

token = 'token'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/tags/', headers=headers)
#response = requests.get('http://127.0.0.1:8000/api/v0/tags/', auth=('author', 'pflybwf123'))

pprint.pprint(response.json())


