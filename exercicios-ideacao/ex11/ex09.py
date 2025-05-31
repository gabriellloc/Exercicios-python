import time

num = int(input("Digite um número: "))
resto = num

print("O programa vai solicitar {} números.".format(num))

for i in range(num):
    valor = int(input("Digite um valor para saber o seu triplo: "))
    print("Seu triplo é {}".format(valor*3))
    resto -= 1
    time.sleep(1)
    if resto > 0:
        print("Falta {} números".format(resto))
    elif resto == 0:
        print("Fim do programa.")
    time.sleep(1)