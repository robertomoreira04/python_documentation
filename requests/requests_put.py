# # método put usando requests 

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

put_data = {
    "userId": 1,
    "id": 1,
    "title": "Título atualizado",
    "body": "Conteúdo atualizado"
}

response = requests.put(url, json=put_data)
print("PUT status:", response.status_code)
print(response.json())
