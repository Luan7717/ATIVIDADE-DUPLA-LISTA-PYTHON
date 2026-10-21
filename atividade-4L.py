import os
os.system('cls')

vetor_quantidade = []

for i in range(8):
    numero = int(input(f'Digite o {i+1}º número: '))
    vetor_quantidade.append(numero)

pesquisar = int(input('\nDigite o número que quer consultar: '))
if pesquisar in vetor_quantidade:
    print('Número encontrado!')
    for i in range(8):
        if vetor_quantidade[i] == pesquisar:
            print(f'Posição: {i + 1}')
else:
    print('Número não encontrado')