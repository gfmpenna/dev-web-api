import requests

# retorno = requests.get("http://127.0.0.1:8000/login")

retorno2 = requests.post("http://127.0.0.1:8000/usuario", params={"nome": "Caio"})

print(retorno2.json())
# print(retorno.json()['mensagem'])
