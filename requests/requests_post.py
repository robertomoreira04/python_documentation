# método post usando requests 

import requests 

new_data = {
    'userId': 1,
    'id': 1,
    'title': 'Aprendendo Python',
    'body': 'Manipulando Informações da API com Requests'
}

url = 'https://jsonplaceholder.typicode.com/posts'

post_response = requests.post(
    url,
    json=new_data
)

