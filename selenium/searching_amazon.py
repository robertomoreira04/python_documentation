# pesquisando na amazon com selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('http://www.amazon.com.br')

element = browser.find_element(By.ID, 'twotabsearchtextbox')
element.send_keys('ps5')
element.send_keys(Keys.ENTER)



