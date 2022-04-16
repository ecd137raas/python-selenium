from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

user = "user@teste.com"
password = ""

print("Iniciando o robo de testes Login...\n")
driver.get("https://teste.com")
time.sleep(4)

print("Acessando a tela de login...\n")
login = driver.find_element_by_id("emailInput")
login.clear()
login.send_keys(user)
login.send_keys(Keys.TAB)

key = driver.find_element_by_id("passwordInput")
key.clear()
driver.save_screenshot("./images/Login.png")
key.send_keys(password)
key.send_keys(Keys.RETURN)
time.sleep(4)
print("Acessando home page")
driver.save_screenshot("./images/home.png")

print("Acessando um item")
item = driver.find_element_by_class_name("card-list").click()
time.sleep(3)
driver.save_screenshot("./images/Item.png")

time.sleep(5)
driver.close()




