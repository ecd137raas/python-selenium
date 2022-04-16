from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

print("Iniciando o robo...\n")
print("Acessando API...\n")
response = requests.get("https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/sp")
data = response.json()
time.sleep(2)
#dados e-mail
email = "raasjava@gmail.com"
senha = "M4r14@@##"
destinatario= "raasjava@gmail.com"
assunto = "E-mail enviado pelo robo - Coronavirus / SP"
mensagem = "Números %s Casos: %s Mortes: %s" % (data["state"], data["cases"], data["deaths"])

driver = webdriver.Chrome()

print("Acessando o Hotmail")
driver.get("https://gmail.com")
time.sleep(3)

#Login
print("Realizando login...")
login = driver.find_element_by_name("identifier")
login.clear()
login.send_keys(email)
login.send_keys(Keys.RETURN)
time.sleep(2)
#password
password = driver.find_element_by_name("password")
password.clear()
password.send_keys(senha)
password.send_keys(Keys.RETURN)
time.sleep(6)
print("Login Realizando")

print("Criando e-mail")
novoemail = driver.find_element_by_xpath("//span[@id='id__8']")
novoemail.click()
time.sleep(2)

destino = driver.find_element_by_xpath("//input[@role='combobox']")
destino.send_keys(destinatario)

subject = driver.find_element_by_id('TextField60_')
subject.send_keys(assunto)

body = driver.find_element_by_xpath("//div[@role='textbox']")
body.send_keys(mensagem)
print("Enviando e-mail...")
send = driver.find_element_by_xpath("//button[@aria-label='Enviar']")
send.click()

print("E-mail enviado.")

time.sleep(5)
driver.close()