# exemplo de requisição em html da web com beautiful soup

from bs4 import BeautifulSoup
import requests

url = 'http://quotes.toscrape.com/'

response = requests.get(url)
print("Status code:", response.status_code)  

soup = BeautifulSoup(response.text, 'lxml')

quotes = soup.find_all('div', class_='quote')
print(f"Encontradas {len(quotes)} quotes na página.\n")

for quote in quotes:
    texto = quote.find('span', class_='text').text
    autor = quote.find('small', class_='author').text
    print(f'"{texto}" — {autor}\n')

