# Cabeçalho
print(f'{" Desafio 55 ":=^40}')

# Faça um programa que leia 5 pesos e diga qual foi o maior e o menor

# Variável
maior_peso = 0
menor_peso = 999

# Estrutura de repetição com variável
for i in range(0, 5):
    peso = float(input('Digite um peso (kg): '))
    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso

# Resultado do programa
print(f'O maior peso foi o {maior_peso}')
print(f'O menor peso foi o {menor_peso}')
