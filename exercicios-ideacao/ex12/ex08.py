sequencia = ["primeira"]

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
        print(f"O maior índice de acidentes é {maior_indice} e pertece a cidade {cidade[pos]}")


soma = sum(numero_veiculos)
div = len(numero_veiculos)
media = soma/div
print(f"A média de acidentes das cidades é igual a {media:.2f}")


for posi_cid, cid in enumerate(cidade):
    if numero_veiculos[posi_cid] < 2000:
        media_veiculosAci = numero_veiculos[posi_cid]/acidentes[posi_cid]
        print(f"A média de veiculos por acidentes é {media_veiculosAci}")