import requests

api = 'http://localhost:5000'

response = requests.get(api + '/info')
print('Response: ', response.text)
