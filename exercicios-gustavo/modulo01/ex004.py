a = input('Digite algo: ')
#Todos os valores são em "True" ou "False".
#Menos o "type"

print('O tipo primitivo desse valor é', type(a))
#Informa o tipo primitivo do item digitado

print('Só tem espaços?' , a.isspace())
#Informa se possui espaços

print('É um número?', a.isnumeric())
#Informa se só possui números

print('É alfabetico?', a.isalpha())
#Informa se só possui letras

print('É alfanúmerico?', a.isalnum())
#Informa se possui letras e números

print("Esta em letras maiúsculas?", a.isupper())
#Informa se todas as letras estao maiúsculas

print("Esta em letras minúsculas?", a.islower())
#Informa se todas as letras estao minúsculas

print("Esta capitalizada?", a.istitle())
#Informa se a primeira letra é maiúscula