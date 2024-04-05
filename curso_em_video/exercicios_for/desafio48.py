# Cabeçalho
print(f'{"Desafio 48":=^40}')

# Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de três e se encontram no
# intervalo de 1 até 500

# Variável
soma = 0

# Estrutura de repetição
for i in range(1, 500 + 1, 2):
    if i % 3 == 0:
        print(f'O número {i} é ímpar e múltiplo de 3')
        soma += i
print(f'A soma total dos números ímpares, múltiplos de 3 de 1 a 500 é de {soma}')
