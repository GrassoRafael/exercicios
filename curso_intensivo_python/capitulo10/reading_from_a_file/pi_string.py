from pathlib import Path

path = Path('pi_million_digits.txt') # Lendo o arquivo

contents = path.read_text().rstrip()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f'{pi_string[:52]}')
print(len(pi_string))

