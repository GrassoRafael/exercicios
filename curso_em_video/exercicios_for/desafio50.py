# Cabeçalho
print(f'{" Desafio 50 ":=^40}')

# Digite 6 valores, some somente os que forem par

# Variável
soma = 0
somai = 0

# Estrutura de repetição
for i in range(1, 6 + 1):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
    else:
        somai += n

print(f'O valor da soma dos números ímpar foi de {somai}')
print(f'O valor da soma dos números pares foi de {soma}')
