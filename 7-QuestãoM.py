import os
os.system("cls")
vetor_positivo=[]
q=0
positivo=0
for i in range(10):
    numero=int(input(f"digite o {i+1} numero: "))
    if numero>0:
        q+=1
        vetor_positivo.append(numero)
print(f"numeros positivos:{vetor_positivo}")
print(f"quantidade de positivo copiado:{q}")
        