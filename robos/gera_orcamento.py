from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configura o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abre o navegador e navega até o site
#site = "https://cdne-phusion-dev-03.azureedge.net/#!/login"
#login = "emerson.duarte@fagrontech.com.br"
#pwd = "123Aa321@@!!"

site = "https://www.pharmaphusion.com.br/#!/login"
login = "emerson.duarte@demonstracao.com.br"
pwd = "123456Aa@123456"

def Login(site, login, pwd):
    driver.get(site)
    time.sleep(2)
    username_field = driver.find_element(By.ID, "email")
    username_field.send_keys(login)
    password_field = driver.find_element(By.ID, "senha")
    password_field.send_keys(pwd)
    login_button = driver.find_element(By.ID, "btnEntrar")
    login_button.click()
    time.sleep(5)
    confirm_button = driver.find_element(By.ID, "btnAcao")
    confirm_button.click()
    time.sleep(10)
        

def AcessoCRM():
    driver.get("https://www.pharmaphusion.com.br/#!/vendas/novo-atendimento/consulta")
    time.sleep(5)
    busca_cliente = driver.find_element(By.ID, "fc_combo_cliente")
    busca_cliente.send_keys("Katia H Kawasaki", Keys.ARROW_DOWN)
    time.sleep(2)
    busca_cliente.send_keys(Keys.ENTER)
    time.sleep(4)



Login(site, login, pwd)
AcessoCRM()


driver.quit()
