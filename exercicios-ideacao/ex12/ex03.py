num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
total = 0

while (num1%num2) == 0:
    print("Divisível")
    num1 = int(input("Digite um valor: "))
    num2 = int(input("Digite outro valor: "))
    total += 1


print("Este valor não é divisível")
print("Ao final, você informou {} divisões possíveis.".format(total))