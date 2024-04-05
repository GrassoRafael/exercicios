# Cabeçalho
print(f'{" Desafio 49 ":=^40}')

# Faça um programa da tabuada de um número

# Input variável
numero = int(input('Digite o número para a tabuada: '))

# Estrutura de repetição
print('.' * 3, f'Tabuada do número {numero}', '.' * 3)

for i in range(0, 10 + 1):
    print(f'{numero:.>10} X {i} = {(numero * i):.<10}')
print('Fim da tabuada')
