nota01 = int(input("Digite a primeira nota: "))
nota02 = int(input("Digite a segunda nota: "))

media = (nota01 + nota02)/2

if media>=7:
    print("A média do aluno foi {}\nParabéns!!".format(media))
else:
    print("A média do aluno foi {}\nReprovado...".format(media))