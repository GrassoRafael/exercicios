# Cabeçalho
print(f'{"Desafio 46":=^40}')

# Faça um programa que mostre uma contagem regressiva de 10 até 0 para estouro de fogos de artifício
# o intervalo precisa ser de 1 segundo

# Importando biblioteca
from time import sleep

# Estrutura de repetição
print(f'{"Iniciando a contagem regressiva":.^40}')
for i in range(10, -1, -1):
    print(f'Contagem regressiva {i}')
    sleep(1)
print(f'Os fogos começaram a estourar 🎆🎇✨')
