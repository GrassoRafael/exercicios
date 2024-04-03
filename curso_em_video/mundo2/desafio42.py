print(f'{"Desafio 42":=^40}') # Enuciado

# Refaça o desafio 35 agora dando nome ao tipo de triângulo que será formado

# Input Variáveis
print('Verificando se é possível formar um triângulo')

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

# Estrutura condicional para verificação de existência e classificação do triângulo caso exista
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Existe condição de existência nesse triângulo')

    if n1 == n2 and n3:
        print('Seu triângulo é equilátero')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('Seu triângulo é isósceles')
    elif n1 != n2 and n3:
        print('Seu triângulo é escaleno')
        
else:
    print('Não existe condição de existência neste triângulo')
