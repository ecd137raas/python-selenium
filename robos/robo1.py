from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Iniciando nosso robô..\n")

driver = webdriver.Chrome()
driver.get("https://registro.br/")

pesquisa = driver.find_element_by_id("is-avail-field")
pesquisa.clear()
pesquisa.send_keys("uol.com.br")
pesquisa.send_keys(Keys.RETURN)

time.sleep(5)
driver.close()


