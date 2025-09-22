# introdução ao beautifulsoup com página html local

from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as file_html:
    content = file_html.read()
    
    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())

titulo = soup.find('h1')
print(titulo)

# buscando por todos os h2
subtitulos = soup.find_all('h2')
print(subtitulos)

for subtitulo in subtitulos:
    print(subtitulo.text)

# buscando por classe
class_titulo = soup.find(class_='titulo')
print(class_titulo.text)

paragrafos = soup.find_all('p')
for paragrafo in paragrafos:
    texto_final = paragrafo.text.split()[-1]
    print(texto_final)