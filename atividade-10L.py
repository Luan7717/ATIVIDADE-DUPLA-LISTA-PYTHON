import os
os.system('cls')

vetor_idade = []
contador = 0

for i in range(5):
    idade = int(input(f'Digite a idade da {i+1}º pessoa: '))
    while idade < 0 or idade > 120:
        print('Idade inválida')
        idade = int(input(f'Digite a idade da {i+1}º pessoa: '))
    vetor_idade.append(idade)

maior_idade = max(vetor_idade)
menor_idade = min(vetor_idade)

for i in range(5):
    if vetor_idade[i] >= 18:
        contador += 1

print(f'\nMaior idade registrada: {maior_idade}')
print(f'Menor idade registrada: {menor_idade}')
print(f'Quantidade de maiores de idade: {contador}')