print(f'{"Desafio 40":=^40}') # Eununciado

# Programa para inputar uma nota e dizer se está aprovado ou não

# Input Variáveis
nota = float(input('Qual foi sua nota? '))

# Estrutura condicional
if nota >= 7.0:
    print(f'Com a nota de {nota} você foi aprovado')
elif nota >= 5 and nota <= 6.9:
    print(f'Sua nota de {nota} não foi o suficiente, você está de recuperação')
else:
    print(f'Sua nota de {nota} não foi o suficiente e você está reprovado')
