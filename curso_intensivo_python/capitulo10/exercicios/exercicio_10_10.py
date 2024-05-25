# Exercicio 10.10 Palavras comuns
from pathlib import Path

# Importando arquivo e decodificando como utf-8
path = Path('the_psychology_of_speculation.txt')
path = path.read_text(encoding='utf-8')

# Contando quantos 'the' aparecem no texto
print(f'Existem {path.count('the ')} "the" no texto.')
