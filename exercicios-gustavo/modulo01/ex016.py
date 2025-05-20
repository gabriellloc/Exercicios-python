import math
num = float(input("Digite um valor para obter sua porção inteira: "))

print("O número {} com sua forma inteira é {}".format(num, math.trunc(num)))
#O trunc arredonda o número para baixo.
#Enquanto o ceil arredonda para cima.