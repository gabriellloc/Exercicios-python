prompt = "{0}: "
print("Digite a idade de 10 pessoas")
idade = int(input(prompt.format(1)))
num = 0
for i in range(2, 4):
    idade = int(input(prompt.format(i)))
    if idade == 18:
        num + 1
        print(num)

print("O número de pessoas com 18 anos é:", num)