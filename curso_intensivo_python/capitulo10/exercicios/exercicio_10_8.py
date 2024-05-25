# Exercicio 10.8 e 10.9
# Gatos e cachorros e Gatos e cachorros sem acusar erros

from pathlib import Path

# Criando e registrando valores nos arquivos
try:
    path = Path('cats.txt')
    path2 = Path('dogs.txt')
    print(path.read_text())
    print(path2.read_text())
except FileNotFoundError:
    print('')


