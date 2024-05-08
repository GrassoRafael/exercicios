# Exercício 10.2 Aprendendo C
from pathlib import Path

path = Path('learning_python.txt').read_text().splitlines()

for frase in path:
    print(frase)
    frase = frase.replace('Python', 'C')
    print(frase)
    print()
