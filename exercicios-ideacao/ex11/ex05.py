valor = int(input("Digite o valor da compra: "))

if valor > 50:
    valor -= (valor*(18/100))

print("O valor final é de {}".format(valor))