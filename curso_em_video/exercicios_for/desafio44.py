print(f'{"Desafio 44":=^40}')

# Crie um programa que leia o preço do produto e sua condição de pagamento, a partir disso faça um cálculo diferente para cada condição de pagamento

# Input Variáveis
preco = float(input('Digite o preço do produto: R$'))
print(f'{"Legenda":.^40}')
print('1 - À vista dinheiro / cheque: 10% de deconto\n'
      '2 - À vista no cartão: 5% de desconto\n'
      '3 - Em até 2x no cartão: preço normal\n'
      '4 - 3x ou mais no cartão: 20% de juros\n')
condicao = int(input('Digite o valor da condição: '))

# Estrutura de condicional
if condicao == 1:
    print(f'O valor de R${preco} será pago a vista no dinheiro ou cheque, então terá 10% de desconto, \nO valor será de R${preco - (preco * 0.1)}')
elif condicao == 2:
    print(f'O valor de R${preco} será pago a vista no cartão, então terá 5% de desconto, \nO valor será de R${preco - (preco * 0.05)}')
elif condicao == 3:
    print(f'O valor de R${preco} será pago em até 2x no cartão, então o preço se manterá o mesmo, \nO valor será de R${preco}')
else:
    print(f'O valor de R${preco} será pago em 3x ou mais no cartão, tendo um acrescimo de 20% \nO valor será de R${preco + (preco * 0.2)}')
