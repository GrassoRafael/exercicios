print(f'{"Desafio 41":=^40}') # Enunciado

# Inputar uma idade do usuário e retornar sobre a categoria dele na natação. 
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# Até 20 anos: sênior
# Acima: master

# Importar Biblioteca
from datetime import date

# Input variável
ano = int(input('Ano de nascimento:  '))
idade = date.today().year - ano
print(f'O atleta tem {idade} anos')

# Estrutura condicional
if idade <= 9:
    print(f'Sua idade é de {idade} anos, então sua classificação é: mirim')
elif idade <= 14:
    print(f'Sua idade é de {idade} anos, então sua classificação é: infantil')
elif idade <= 19:
    print(f'Sua idade é de {idade} anos, então sua classificação é junior')
elif idade <= 20:
    print(f'Sua idade é de {idade} anos, então sua classificação é sênior')
else:
    print(f'Sua idade é de {idade} anos, então sua classificação é master')
