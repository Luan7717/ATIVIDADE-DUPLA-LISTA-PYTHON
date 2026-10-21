import os
import time
os.system('cls')

vetor_a = []
vetor_b = []
QUANTIDADE_REPETIÇÃO = 5

for i in range(QUANTIDADE_REPETIÇÃO):
    vetor1 = int(input(f'Digite o {i+1}º número do primeiro vetor para a soma:'))
    vetor_a.append(vetor1)
print('Valores adicionados ao primeiro vetor!')
time.sleep(3)
os.system('cls')

for i in range(QUANTIDADE_REPETIÇÃO):
    vetor2 = int(input(f'Digite o {i+1}º número do segundo vetor para a soma: '))
    vetor_b.append(vetor2)
print('Valores adicionados ao segundo vetor!')
time.sleep(3)
os.system('cls')

print('Fazendo a soma...')
time.sleep(2)
os.system('cls')

soma = sum(vetor_a + vetor_b)
print(f'A soma dos 2 vetores é: {soma}')