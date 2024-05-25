# Exercicio 10.6, 10.7 capítulo 10.
# Operação de Soma e Calculadora de soma

print("Insira números e veja a soma final, digite 's' para terminar a conta.")

s = 0
while True:
    try:
        n1 = int(input('Digite um número: '))
        s += n1
        n2 = int(input('Digite outro número: '))
        s += n2
        continua = input('Deseja continuar (s/n)? ')
    except ValueError:
        print('Digite apenas valores numéricos')
    if continua == 'n':
        print(f'A soma foi de {s}')
        break

