# 10.3 Código Mais Simples

from pathlib import Path

path = Path('pi_digits.txt') # Lendo o arquivo

contents = path.read_text().rstrip()
for line in contents.splitlines():
    print(line)


