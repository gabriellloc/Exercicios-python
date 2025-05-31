import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def normalizar(texto):
    texto = texto.lower().replace(" ", "")
    texto = remover_acentos(texto)
    return texto

nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while normalizar(nome) == normalizar(senha):
    print("Sua senha nao poder ser igual ao seu nome. Tente novamente.")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

print("Senha aceita")