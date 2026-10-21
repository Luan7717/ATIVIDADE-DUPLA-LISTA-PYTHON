import os
os.system("cls")

vetor=[]
soma=0
maior=0
for i in range(10):
    numero=int(input(f"digite o {i+1}° numero:"))
    vetor.append(numero)

    soma+= numero
    if numero >10:
        maior+=1

print(f"vetor {vetor}")
print(f"Soma de todos os numeros: {soma}")
print(f"Quantidade de maior que 10:{maior}")