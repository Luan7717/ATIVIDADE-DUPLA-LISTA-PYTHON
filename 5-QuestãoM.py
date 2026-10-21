import os
os.system("cls")

vetor=[]
soma=0
acima=0
for i in range(5):
    nota=float(input(f"digite a {i+1} nota:"))
    vetor.append(nota)
    soma+=nota
    media=soma/5
    if nota>media:
        acima+=1

print(f"notas: {nota}")
print(f"media do aluno: {media}")
print(f"nota acima da media: {acima}")