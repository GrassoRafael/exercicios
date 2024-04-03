print(f'{"Desafio 39":=^40}')

# Programa para informar se a pessoa já tem idade para o alistamento militar

# Importar biblioteca
from datetime import date

# Input Variáveis
nascimento = int(input('Digite o ano do seu nascimento: '))
ano  = date.today().year
idade = ano - nascimento

# Idade
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}')

# Estrutura de variável
if idade == 18:
    print(f'Você está com {idade} anos, está na hora de se alistar')
elif idade > 18:
    print(f'Você tem {idade} anos e já se passaram {idade - 18} anos desde seu alistamento')
else:
    print(f'Restam {18 - idade} para seu alistamento militar')
