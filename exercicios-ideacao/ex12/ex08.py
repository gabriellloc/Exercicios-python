import time

sequencia = ["primeira", "segunda", "terceira", "quarta", "quinta"]

cidade = []
numero_veiculos = []
acidentes = []

for i in sequencia:
    cidade.append(input(f"Digite a {i} cidade: "))
    numero_veiculos.append(int(input("Número de veículos de passeio: ")))
    acidentes.append(int(input("Número de acidentes com vítimas: ")))

maior_indice = max(acidentes)
menor_indice = min(acidentes)

for pos, indice in enumerate(acidentes):
    if indice == maior_indice:
        time.sleep(1)
        print(f"O maior índice de acidentes é {maior_indice} e pertece a cidade {cidade[pos]}")

for pos, indice in enumerate(acidentes):
    if indice == menor_indice:
        time.sleep(1)
        print(f"O menor índice de acidentes é {menor_indice} e pertece a cidade {cidade[pos]}")

soma = sum(numero_veiculos)
div = len(numero_veiculos)
media = soma/div
time.sleep(1)
print(f"A média de acidentes das cidades é igual a {media:.2f}")


for posi_cid, cid in enumerate(cidade):
    if numero_veiculos[posi_cid] < 2000:
        media_veiculosAci = numero_veiculos[posi_cid]/acidentes[posi_cid]
        time.sleep(1)
        print(f"A média de veiculos por acidentes é {media_veiculosAci:.2f} da cidade {cid}")