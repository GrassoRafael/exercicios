from pathlib import Path

path = Path('pi_million_digits.txt') # Lendo o arquivo

contents = path.read_text().rstrip()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appers in the first million digits of pi!")
else:
    print("Your birthday does not apper in the first million digits of pi.")
