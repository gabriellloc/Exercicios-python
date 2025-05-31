clientes = 0
clientePos = 0
clienteNeg = 0
nomes_positivos = []
nomes_negativos = []

while clientes < 10000:
    conta = int(input("Digite o número da conta: "))
    if conta == -999:
                print("Fim do programa")
                break
    
    nome = str(input("Digite seu nome: "))
    saldo = float(input("Digite seu saldo: "))
    clientes += 1
    
    
    if saldo > 0:
        print("Seu saldo é de R${:.2f}".format(saldo))
        print("Saldo positivo")
        clientePos += 1
        nomes_positivos.append(nome)
    elif saldo < 0:
        print("Seu saldo é de R${:.2f}".format(saldo))
        print("Saldo Negativo")
        clienteNeg += 1
        nomes_negativos.append(nome)
    
if nomes_positivos == []:
      nomes_positivos.append("Nenhum cliente positivo")

if nomes_negativos == []:
      nomes_negativos.append("Nenhum cliente negativo")

print("A agencia tem um total de {} clientes".format(clientes))
print("Existe um total de {} clientes positivos e {} clientes negativos".format(clientePos, clienteNeg))
print("Os clientes positivos: {}".format(nomes_positivos))
print("Os clientes negativos: {}".format(nomes_negativos))