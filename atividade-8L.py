import os
os.system('cls')

vetor_funcionarios = []
vetor_salario = []

for i in range(5):
    funcionarios = input(f'Digite o nome do {i+1}º funcionario: ')
    salario = float(input(f'Digite o valor do salario do {i+1}º funcionario: R$'))
    vetor_funcionarios.append(funcionarios)
    vetor_salario.append(salario)
    os.system('cls')

maior_salario = max(vetor_salario)
posicao = 0
acima2000 = 0

for i in range(5):
    if salario > 2000:
        acima2000 += 1

print('\n===== RESULTADO =====')
print(f'Funcionário com maior salário: {funcionarios[posicao]}')
print(f"Maior salário: R$ {maior_salario:.2f}")
print(f'Quantidade de funcionários que ganham acima de R$ 2.000,00: {acima2000}')