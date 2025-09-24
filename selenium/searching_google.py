# fazendo buscas no google 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time 

search = input('Digite o que deseja pesquisar:\n')

browser = webdriver.Firefox()
browser.get('https://google.com.br')

element = browser.find_element(By.XPATH, "//textarea[@aria-label='Pesquisar']")

element.send_keys(search)
element.send_keys(Keys.ENTER)

