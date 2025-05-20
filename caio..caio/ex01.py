import random
win = random.randint(1,6)

num = int(input("Digite um valor entre 1 e 6: "))

if num > 6 or num < 1:
    print("Digite um valor entre 1 e 6")
else:
    if num == win:
        print("Você acertou!")
    else:
        print("Você errou...")
        print("O número era {}".format(win))