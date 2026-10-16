import os
os.system('cls')

vetor_temperatura = [26.7, 27.9, 33.1, 32.7, 34.3, 29.5, 33.7]
dias = [
    'Domingo'
    'Segunda-Feira'
    'Terça-Feira'
    'Quarta-Feira'
    'Quinta-Feira'
    'Sexta-Feira'
    'Sabádo'
]

print('''
===== REGISTRO SEMANAL =====
1 - Domingo
2 - Segunda-Feira
3 - Terça-Feira
4 - Quarta-Feira
5 - Quinta-Feira
6 - Sexta-Feira
7 - Sabádo''')

dia = int(input('Digite o número da semana que você deseja ver a temperatura: '))

match dia:
    case 1:
        print(f'{dias[0]}: {vetor_temperatura[0]}°C')
    case 2:
        print(f'{dias[1]}: {vetor_temperatura[1]}°C')
    case 3:
        print(f'{dias[2]}: {vetor_temperatura[2]}°C')
    case 4:
        print(f'{dias[3]}: {vetor_temperatura[3]}°C')
    case 5:
        print(f'{dias[4]}: {vetor_temperatura[4]}°C')
    case 6:
        print(f'{dias[5]}: {vetor_temperatura[5]}°C')
    case 7:
        print(f'{dias[6]}: {vetor_temperatura[6]}°C')
    case 8:
        for i in range(7):
            print(f'{dias[i]}: {vetor_temperatura[i]}°C')
        media = sum(vetor_temperatura) / len(vetor_temperatura)
        print(f'Média semanal: {media:.2f}°C')
    case _:
        print('Opção inválida!')