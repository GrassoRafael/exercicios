# Cabeçalho
print(f'{" Desafio 51 ":=^40}')

# Faça um programa que leia o primeiro termo da razão de uma PA no final mostre os 10 primeiros termos 
# dessa progressão

# Input Variáveis
inicio = int(input('Digite o primeiro termo da operação: '))
razao = int(input('Digite a razão: '))

# Estrutura de repetição
print(f'{" Inicio da progressão aritimética ":.^20}')
for i in range(inicio, 10 + 1, razao):
    print(i, end=' ➡ ')
print('Fim do programa')
