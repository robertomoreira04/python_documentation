# acessando repositórios no github 

import requests 

base_api = 'https://api.github.com'
user = 'robertomoreira04'
url = f'{base_api}/users/{user}/repos'

response = requests.get(url)
print(response.status_code)
print(len(response.json()))
print(response.json())

