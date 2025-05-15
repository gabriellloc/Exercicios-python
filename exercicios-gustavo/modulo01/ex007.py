nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))

media = (nota01 + nota02)/2

if media>=7:
    print("A média do aluno foi {:.1f}\nParabéns!!".format(media))
else:
    print("A média do aluno foi {:.1f}\nReprovado...".format(media))