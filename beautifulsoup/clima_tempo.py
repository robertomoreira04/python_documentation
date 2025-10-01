# buscando clima de natal na página do clima tempo
from datetime import date
import requests 
from bs4 import BeautifulSoup

hoje = date.today()
day_formatted = hoje.strftime("%d/%m/%Y")

html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/334/natal-rn').content
soup = BeautifulSoup(html, 'html.parser')

dayparagraph = soup.find('p', class_='-gray -line-height-22 _margin-t-sm-20')
dayresume = dayparagraph.text.strip().split('\n', 1)

temperature = soup.find('div', class_='-gray _flex _margin-l-5')
spans = temperature.find_all('span')
min_temp = spans[0].text
max_temp = spans[1].text

div = soup.find('div', class_="row no-gutters wrapper-variables-cards")
paragraphs = div.find_all('p')

moon_phase = paragraphs[-1].text.strip()
suntime = paragraphs[-3].text.strip()

begin, end = suntime.split(' - ')

sunrise = begin[:5].replace(':', 'h')
sunset = end[:5].replace(':', 'h')


print(f'Hoje é dia {day_formatted}')
print(f'Dia da semana: {dayresume[0]}')
print(f'Resumo do dia: {dayresume[1].strip()}')
print(f'A temperatura mínima em Natal/RN é: {min_temp}')
print(f'A temperatura máxima em Natal/RN é: {max_temp}')
print(f'A lua está na fase {moon_phase}')
print(f'O intervalo do sol hoje é: {sunrise} - {sunset}')

