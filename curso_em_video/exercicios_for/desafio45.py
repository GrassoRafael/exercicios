print(f'{"Desafio 45":=^40}') # Cabeçalho

# Crie um jogo de pedra papel tesoura
print(f'{"Jogo de pedra, papel ou tesoura":.^40}')

# importar biblioteca
from random import choice

# Variáveis
lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)

p1 = input('Digite o que você irá jogar: ').strip().title()


# Estrutura condicional do jogo
if p1 == "Tesoura" and computador == "Papel" or p1 == 'Papel' and computador == 'Pedra' or p1 == 'Pedra' and computador == 'Tesoura':
    print(f'Você utilizou {p1} e o computador utilizou {computador}, você ganhou')
elif p1 == computador:
    print(f'Vocês dois utilizaram {p1}, então foi um empate')
else: 
    print(f'Você utilizou {p1} e o computador utilizou {computador}, você perdeu')
