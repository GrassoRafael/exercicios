print(f'{"Desafio 36":=^40}') # Enunciado

# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# Input das variáveis
valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
qtd_anos = int(input('Em quantos anos gostaria de pagar a casa? ')) * 12

# Variável prestação
prestacao = valor_casa / qtd_anos

# Estrutura condicional
if prestacao > (salario * 0.3):
    print(f'O valor da prestação é de R${prestacao:.2f} o que excede 30% do valor do seu salário que seria de R${salario * 0.3:.2f}')
else:
    print(f'Seu emprestimo foi aprovado, suas prestações serão de R${prestacao:.2f}')
