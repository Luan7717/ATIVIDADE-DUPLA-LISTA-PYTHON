import os
os.system("cls")

vetor=[]
for i in range(6):
    numero=int(input(f"digite o {i+1}º numero:"))
    vetor.append(numero)
print(f"vetor antes: {vetor}")
for i in range(6):
    if vetor [i] % 2 == 0:
        vetor[i] = 0
    else:
        vetor[i] = 1
print(f"vetor depois: {vetor}")
