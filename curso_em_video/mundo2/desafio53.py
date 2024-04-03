# Cabeçalho
print(f'{" Exercício 53 ":=^40}')

# Faça um programa que leia uma frase e diga se ela é um palíndromo

# Input Variável
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == frase:
    print(f'{inverso} e {frase} são palíndromo')
else:
    print('Não é palíndromo')

