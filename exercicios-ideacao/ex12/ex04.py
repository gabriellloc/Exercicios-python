par = 0
impar = 0

for i in range(1, 51):
    if (i % 2) ==0:
        print(i,"Par")
        par += 1
    else:
        print(i,"Ímpar")
        impar += 1

print("Tem {} pares e {} impares".format(par, impar))