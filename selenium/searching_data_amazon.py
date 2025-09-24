# pesquisando e trazendo resultados da amazon com selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Firefox()

browser.get('https://www.amazon.com.br')

element = browser.find_element(By.ID, 'twotabsearchtextbox')
element.send_keys('ps5')
element.send_keys(Keys.ENTER)
time.sleep(2)

result_element = browser.find_element(
    By.CSS_SELECTOR,
    'div.s-main-slot.s-result-list.s-search-results.sg-row'
)

time.sleep(2)

items = result_element.find_elements(
    By.XPATH,
    '//div[@data-component-type="s-search-result"]'
)

for item in items:
    title = item.find_element(By.TAG_NAME, 'h2').text
    link = item.find_element(By.CLASS_NAME, 'a-link-normal').get_attribute('href')
    try:
        price = item.find_element(
            By.CLASS_NAME,
            'a-price'
        ).text.replace('\n', '.')
    except:
        price = "Não disponível"

    print(f'Título: {title}')
    print(f'Preço: {price}')
    print(f'Link {link}')
