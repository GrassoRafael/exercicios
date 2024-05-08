# Aprendendo python 10.1
from pathlib import Path

path = Path('learning_python.txt').read_text().splitlines()
for i, frase in enumerate(path):
    print(path[i])
print()

for i, frase in enumerate(path):
    print(f'A {i+1}ª frase é: {frase}\n')
