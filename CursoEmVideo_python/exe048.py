# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram np intervalo de 1 até 500
soma = 0
numeros = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        numeros += 1
print(f'A soma de todos os {numeros} números é {soma}', end=' ')
