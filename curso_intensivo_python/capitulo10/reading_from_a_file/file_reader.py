from pathlib import Path

path = Path('pi_digits.txt') # Lendo o arquivo

contents = path.read_text().rstrip()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

print()
contents2 = path.read_text().rstrip()
path2 = Path('/capitulo10')
print(contents2)



