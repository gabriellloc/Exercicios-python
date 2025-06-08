print("Seja bem-vindo, professor(a)!")

valor_hora_aula = int(input("Digite o valor da hora/aula: "))
num_aula_semana = int(input("Digite o número de aulas por semana: "))
salario_mensal = valor_hora_aula * num_aula_semana * 4.5

if salario_mensal > 1000:
    print("O professor está isento de contribuição sindical.")

print(f"O salário do professor(a) é de {salario_mensal}")