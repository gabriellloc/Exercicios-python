import time

print("Utilize somente números!")
time.sleep(2)
kmper = int(input("Quantos quilometros o carro percorreu? "))
dias = int(input("Quantos dias o carro foi utilizado? "))

valorD = dias * 60
valorKm = kmper * 0.15

print("O veículo que percorreu {}km por {} dias, deverá ser cobrado um valor de R${:.2f}".format(kmper, dias, valorD+valorKm))