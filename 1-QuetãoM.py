import os
os.system("cls")

vetor_numero=[]
for i in range(5):
    numero=int(input(f"digite o {i+1}º numero: "))
    vetor_numero.append(numero)
print(f"numero na ordem digitada:{vetor_numero}")
print(f"numero na ordem digitada:{vetor_numero[::-1]}")