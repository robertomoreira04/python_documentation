# buscando domínios no registro.br e lançando em um arquivo txt

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time 

browser = webdriver.Firefox()
browser.get('https://registro.br')

domains = [
    'botscompython.com.br',
    'meta.com',
    'databot.com',
    'pythonbootcamp.com'
]

file = open('domains.txt', 'w', encoding='utf-8')

for domain in domains:
    element = browser.find_element(By.ID, 'is-avail-field')
    element.clear()
    element.send_keys(domain)
    element.send_keys(Keys.ENTER)
    time.sleep(5)

    results = browser.find_elements(By.TAG_NAME, 'strong')
    text = f'Domínio {results[1].text} está {results[2].text}\n'
    print(text)
    file.write(text)

file.close()
browser.close()