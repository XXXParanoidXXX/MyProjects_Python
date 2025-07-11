import requests

cep =  70650359 #"01001000"  # Exemplo de CEP (Praça da Sé - SP)
url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
else:
    print("Erro ao consultar o CEP.")