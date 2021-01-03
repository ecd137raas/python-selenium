from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://motomaniajundiai.com.br")



time.sleep(2)
driver.close()