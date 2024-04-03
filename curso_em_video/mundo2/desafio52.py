# Cabeçalho
print(f'{" Desafio 52 ":=^40}')

# Faça um programa que leia um número e diga se ele é primo ou não


# Estrutura de repetição com condicional
for i in range(0, 4):
    n = int(input('Digite um número inteiro: '))
    if n > 1 and n % 2 != 0 and n % 3 != 0 or n == 2:
        print(f'O número {n} é primo')
    else:
        print(f'O número {n} não é primo')
print('Fim do programa')
