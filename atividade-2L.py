import os
os.system('cls')

temperaturas = []
soma = 0

# Ler as temperaturas dos 7 dias
for i in range(7):
    temperatura = float(input(f"Digite a temperatura do dia {i + 1}: "))
    temperaturas.append(temperatura)
    soma += temperatura

# Calcular a média, a maior e a menor temperatura
media = soma / 7
maior = max(temperaturas)
menor = min(temperaturas)

# Mostrar os resultados
print("\n--- Temperaturas da semana ---")

for i in range(7):
    print(f"Dia {i + 1}: {temperaturas[i]} °C")

print(f"\nMédia da semana: {media:.2f} °C")
print(f"Maior temperatura: {maior} °C")
print(f"Menor temperatura: {menor} °C")