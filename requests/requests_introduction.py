# introduzindo a biblioteca requests

import requests 

link = 'https://github.com/robertomoreira04'
requisicao = requests.get(link)
print(requisicao)
print(requisicao.status_code)
print(requisicao.text)
