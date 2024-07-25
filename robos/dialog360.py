import requests
import os
from dotenv import load_dotenv

load_dotenv()

def obter_token(auth_url, client_id, client_secret):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'username': client_id,
        'password': client_secret
    }

    response = requests.post(auth_url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Erro ao obter o token: {response.status_code} - {response.text}")

def obter_apikey(api_url, token):
    headers = {
        'Authorization': f'Bearer {token}'

    }
    response = requests.post(api_url, headers=headers)
    
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Erro ao chamar o endpoint: {response.status_code} - {response.text}")

def setar_webhook(api_url_webhook, phone, api_key):
    headers = {
        'D360-API-KEY': api_key

    }
    data = {
            'url': f'https://fate-mobypharma-chatapi-api.fagrontechnologies.com.br/api/v1/Mensagens360Dialog/cloudapi?telefone={phone}&token={api_key}'
    }
    
    response = requests.post(api_url_webhook, json=data, headers=headers)
    
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f"Erro ao chamar o endpoint: {response.status_code} - {response.text}")

def main():
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    channel = os.getenv('CHANNEL')
    phone = os.getenv('PHONE')

    # URL do endpoint de autenticação
    auth_url = 'https://hub.360dialog.io/api/v2/token'
    # Credenciais de autenticação

    # Obtém o token
    token = obter_token(auth_url, client_id, client_secret)
    print("Token obtido")

    # URL do endpoint da API
    api_url = f'https://hub.360dialog.io/api/v2/partners/elktSJPA/channels/{channel}/api_keys'

    # Chama o endpoint da API usando o token
    resposta = obter_apikey(api_url, token)
    print(f"Resposta da API: {resposta}")
    api_key = resposta.get('api_key')

    api_url_webhook = 'https://waba-v2.360dialog.io/v1/configs/webhook'
    # Chama o endpoint setando o webhook
    resposta = setar_webhook(api_url_webhook, phone, api_key)
    print(f"Setar webhook: {api_key, api_url}")

if __name__ == "__main__":
    main()
