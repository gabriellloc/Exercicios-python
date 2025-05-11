num = int(input("Digite um valor: "))


if num%10 == 0 and num%5 == 0 and num%2==0:
    print("Divisível por 10, 5 e 2")
elif num%10 == 0:
    print("Divisível por 10")
elif num%5 == 0:
    print("Divisível por 5")
elif num%2 == 0:
    print("Divisível por 2")
