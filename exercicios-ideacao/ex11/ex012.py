print("Digite valores positivos para executar o programa e valores negativos para encerrar.")

divisiveis = 0
quant = 1
lista = []

num = int(input("Digite um valor: "))

div = num%6

lista.append(num)

if div == 0:
    divisiveis += 1

if num > 0:
    while num > 0:
        num = int(input("Digite um valor: "))
        if num < 0:
            break
        quant += 1
        div = num%6
        lista.append(num)
        if div == 0:
            divisiveis += 1
        soma = sum(lista)
        media = soma/quant



    print("Foram lidos {} números".format(quant))
    print("Existe {} números divisiveis por 6".format(divisiveis))
    print("A média entre os valores é {:.1f}".format(media))
    print("Fim do programa.")

else:
    print("Fim do programa. Digite um valor maior que 0.")