def raiz_quadrada(numero):
    if numero < 0:
        print("Erro: Não é possível calcular a raiz quadrada de números negativos.")
        return None
    else:
        return numero**0.5

print(raiz_quadrada(-12))