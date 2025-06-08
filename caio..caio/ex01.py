while True:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    options = ["soma","subtração","divisão","multiplicação"]
    operations = {
        "1": ("soma", lambda x, y: x + y),
        "2": ("subtração", lambda x, y: x - y),
        "3": ("divisão", lambda x, y: x / y),
        "4": ("multiplicação", lambda x, y: x * y)
    }


    choice = input("Operações: \n" \
    "1.Soma \n" \
    "2.Subtração \n" \
    "3.Divisão \n" \
    "4.Multiplicação \n" \
    "0.Para sair \n" \
    "Escolha: ")

    if choice in operations:
        op_name, op_func = operations[choice]
        resultado = op_func(n1, n2)
        print(f"A {op_name} é {resultado}")

    elif choice == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida")