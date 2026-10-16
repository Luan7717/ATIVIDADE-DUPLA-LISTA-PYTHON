import os
os.system("cls")

numeros = []

for i in range(5):
    n = int(input("Digite um número inteiro: "))
    numeros.append(n)

print("Ordem digitada:", numeros)

print("Ordem inversa:", numeros[::-1])