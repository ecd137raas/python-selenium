from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver.chrome import ChromeDriverManager
import time
import xlrd

print("Iniciando nosso robô..\n")
arq = open("resultado.txt","w")

dominios = []
#Lendo Excel
workbook = xlrd.open_workbook('dominio.xls')
sheet = workbook.sheet_by_index(0)

for linha in range(0,5):
    dominios.append(sheet.cell_value(linha,0))
    #print(sheet.cell_value(linha,0))

driver = webdriver.Chrome()
driver.get("https://registro.br/")

#dominio = "terra.com.br"
for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    resultado = driver.find_elements_by_tag_name("strong")
    #mport pdb; pdb.set_trace()
    texto = "Dominio %s %s\n" %(dominio, resultado[4].text)
    arq.write(texto)

arq.close
driver.close()


