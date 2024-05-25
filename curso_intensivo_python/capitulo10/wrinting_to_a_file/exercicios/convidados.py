# Exercicio 10.4 Convidados
from pathlib import Path

# Variáveis
convidados = ''

# Loop para adição de nomes
while True:
    nomes = input('Digite seu nome e sobrenome: ').title()
    convidados += nomes + '\n'
    continua = input('Deseja continuar?(s/n): ').lower()
    if continua == 'n':
        break

# Criação do arquivo + adição das informações inputadas
path = Path('guest.txt').write_text(convidados)


