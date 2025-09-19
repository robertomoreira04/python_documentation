# requisição get com parâmetros

import requests 

url = 'https://jsonplaceholder.typicode.com/posts/'

payload = {
    "id":[1, 2, 3, 4, 5],
    "userId": 1
}

response = requests.get(url, params=payload)

response_json = response.json()

for r in response_json:
    print(r, '\n')