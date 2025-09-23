from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time 

browser = webdriver.Firefox()
browser.get('https://registro.br')

element = browser.find_element(By.ID, 'is-avail-field')
element.clear()
element.send_keys('botscompython.com.br')
element.send_keys(Keys.ENTER)

time.sleep(5)
browser.save_screenshot('registro_dominio.png')

results = browser.find_elements(By.TAG_NAME, 'strong')
print(f'Domínio {results[1].text} está {results[2].text}')

