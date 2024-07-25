from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import time

# Configura o driver do Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def ler_urls_arquivo(arquivo):
    """
    Lê URLs de um arquivo de texto e retorna uma lista de URLs.

    Args:
    arquivo (str): O caminho para o arquivo de texto.

    Returns:
    list: Lista de URLs.
    """
    with open(arquivo, 'r') as file:
        urls = file.readlines()
    # Remove espaços em branco e novas linhas
    urls = [url.strip() for url in urls]
    return urls

def tirar_screenshot(driver, url, caminho_screenshot):
    """
    Abre uma URL no navegador e tira uma captura de tela.

    Args:
    driver: Instância do WebDriver.
    url (str): A URL a ser aberta.
    caminho_screenshot (str): O caminho para salvar a captura de tela.
    """
    driver.get(url)
    time.sleep(5)  # Espera a página carregar
    driver.save_screenshot(caminho_screenshot)

def extrair_trecho_url(url):
    # Expressão regular para extrair o trecho desejado
    match = re.search(r'https://(.*?)\.', url)
    if match:
        return match.group(1)
    else:
        return None


def main():
    # Caminho para o arquivo de URLs
    arquivo_urls = 'urls.txt'

    # Lê as URLs do arquivo
    urls = ler_urls_arquivo(arquivo_urls)

    # Percorre cada URL e tira uma captura de tela
    for i, url in enumerate(urls):
        nome = extrair_trecho_url(url)
        caminho_screenshot = f'{nome}.png'
        tirar_screenshot(driver, url, caminho_screenshot)
        print(f'Screenshot salva em: {caminho_screenshot}')

    # Fecha o navegador
    driver.quit()

if __name__ == "__main__":
    main()
