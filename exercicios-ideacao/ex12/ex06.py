funcionario = 1000

print("O funcionario foi contratado em 1995 com um aumento de 1,5% todos os anos sobre o salário inicial, 1.000(mil reais).")

ano = int(input("Em que ano voce gostaria de saber o salário do funcionario?\nDigite aqui: "))

aumento = (funcionario * 1.5/100)
div_ano = ano - 1995

if ano > 1995 and ano < 1997:
    print(f"O salário do funcionario é no ano {ano} é igual a {(div_ano * aumento) + funcionario}")

elif ano > 1997:
    final = funcionario + (aumento*div_ano)
    for i in range(div_ano):
        valor = aumento*2
    print(f"O salário do funcionario é no ano {ano} é igual a {valor + final}")
    

else:
    print("Coloque um ano valido.")