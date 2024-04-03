print(f'{"Desafio 37":=^40}') # Enunciado

# Escreva um programa que leia um número inteiro qualquer e peça para o usiário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadicimal

# Input variáveis
numero = int(input('Digite um número inteiro: '))

print('- 1 Para binário \n- 2 Para Octal \n- 3 para Hexadecimal')
codigo = int(input('Digite o código de base para converter: '))

# Estrutura condicional
if codigo == 1:
    print(f'A conversão do número {numero} para binário é {bin(numero) [2:]}')
elif codigo == 2:
    print(f'A conversão do número {numero} para octal é {oct(numero) [2:]}')
elif codigo == 3:
    print(f'A conversão do número {numero} para hexadecimal é {hex(numero) [2:]}')
else:
    print('Você digitou uma opção inválida')
