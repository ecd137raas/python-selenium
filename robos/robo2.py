from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

#dados e-mail
email = "raasjacarta@gmail.com"
senha = ""
destinatario= "raasjava@gmail.com"
mensagem = "E-mail enviado pelo robo"

driver = webdriver.Chrome()

print("Iniciando o robo...\n")
print("Acessando o Gmail")

driver.get("https://gmail.com")

#Login
print("Realizando login...")
login = driver.find_element_by_id("identifierId")
login.clear()
login.send_keys(email)
login.send_keys(Keys.RETURN)
time.sleep(2)

password = driver.find_element_by_name("password")
password.clear()
password.send_keys(senha)
password.send_keys(Keys.RETURN)
time.sleep(6)
print("Login Realizando")


driver.close()