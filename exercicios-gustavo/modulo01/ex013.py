salario = float(input("Digite o seu salário: R$"))

aumento = salario*(15/100)

print('O salário teve um aumento de R${aumento:.2f} e passou a ser R${final:.2f}'.format(aumento=aumento, final=salario+aumento))