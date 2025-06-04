quant = 0

while True:
    num = int(input("Digite um valor: "))
    if num < 0:
        break
    quant += 1

print("Foram digitados {} números positivos e 1 número negativo".format(quant))