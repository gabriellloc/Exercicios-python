totalDp = 0

numAnd = int(input("Digite o número de andares do prédio: "))
entrada = int(input("Quantas pessoas entraram no térreo? "))

totalDp += entrada
for i in range(1,numAnd + 1):
    if totalDp > 15:
        excesso = (totalDp - 15)
        print("Excesso de Passageiros. Devem sair {}".format(excesso))
        saida = int(input("Quantas pessoas vão sair? "))
        totalDp -= saida

    print("Andar número {}".format(i))
    entrada = int(input("Quantas pessoas entraram? "))
    
    if totalDp != 0:
        saida = int(input("Quantas pessoas saíram? "))
        totalDp -= saida

    totalDp += entrada

    
print("Número de pessoas no ultimo andar é de {} pessoas".format(totalDp))