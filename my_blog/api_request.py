import requests
import pprint


#response = requests.get('http://127.0.0.1:8000/categories/categories/')
#response = requests.get('http://127.0.0.1:8000/api/v0/tags/')
#response = requests.get('http://127.0.0.1:8000/api/v0/tags/', auth=('author', 'pflybwf123'))

token = 'ccb8c10a0f65187e910587fb1c6bac37ee6c4efc'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/tags/', headers=headers)
#response = requests.get('http://127.0.0.1:8000/api/v0/tags/', auth=('author', 'pflybwf123'))

pprint.pprint(response.json())


