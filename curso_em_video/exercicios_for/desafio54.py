# Cabeçalho
print(f'{" Desafio 54 ":=^40}')

# Crie um programa que leia o ano de nascimento de 7 pessoas, no final mostra quantas atingiram a maioridade e quantas não

# Importar biblioteca
from datetime import date

# Estrutura de repetição com variáveis
soma = 0
soma1 = 0

for i in range(0, 7):
    nascimento = int(input('Digite o ano do seu nascimento: '))
    idade = date.today().year - nascimento
    if idade >= 18:
        soma += 1
    else:
        soma1 += 1
print(f'{soma} tem a maioridade')
print(f'{soma1} não tem a maioridade')
print('Fim do código')