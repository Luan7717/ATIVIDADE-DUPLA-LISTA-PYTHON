import os
os.system('cls')

dias = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']
temperaturas = []
soma = 0

for i in range(7):
    temperatura = float(input(f"Digite a temperatura de {dias[i]}: "))
    temperaturas.append(temperatura)
    soma += temperatura

media = soma / 7
maior = max(temperaturas)
menor = min(temperaturas)
os.system('cls')

print("\n===== TEMPERATURAS DA SEMANA =====")

for i in range(7):
    print(f"{dias[i]}: {temperaturas[i]} °C")

print(f"\nMédia da semana: {media:.2f} °C")
print(f"Maior temperatura: {maior} °C")
print(f"Menor temperatura: {menor} °C")