from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time

user = "admin@adimax.com.br"
password = "123456"

driver = webdriver.Chrome()

print("Iniciando o robo de testes Login...\n")
driver.get("https://adimaxproappwebqa.azurewebsites.net/login")
driver.save_screenshot("./images/Loading.png")
time.sleep(8)

print("Acessando a tela de login...\n")
print("Informando login e senha...\n")
login = driver.find_element_by_xpath("//input[@type='Email']")
login.clear()
login.send_keys(user)
login.send_keys(Keys.TAB)

controle = driver.find_element_by_xpath("//input[@type='Password']")
controle.clear()
controle.send_keys(password)
controle.send_keys(Keys.RETURN)
driver.save_screenshot("./images/login.png")

print("Acessando home page")

time.sleep(8)
driver.close()




