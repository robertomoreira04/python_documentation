# método delete usando requests 

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)
print("DELETE status:", response.status_code)
