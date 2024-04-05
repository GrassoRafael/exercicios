print(f'{"Desafio 38":=^40}') # Enunciado

# Comparando números inteiros e dizendo qual é o maior

# Input Variáveis
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# Estrutura condicional
if n1 > n2:
    print(f'O número {n1} é maior que o {n2}')
elif n2 > n1:
    print(f'O número {n2} é maior que o {n1}')
else:
    print(f'Os números {n1} e {n2} são iguais')

print('Fim do programa')
