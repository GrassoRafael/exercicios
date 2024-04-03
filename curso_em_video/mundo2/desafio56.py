# Cabeçalho
print(f'{" Desafio 56 ":=^40}')

# Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. 
# no final do programa, mostre a media de idade do grupo, qual o nome do homem mais velho
# e quantas mulheres tem menos de 20 anos

# Variáveis
soma = 0
soma1 = 0
nome_homem_velho = ''
idade_homem_velho = 0

# Estrutura condicional
for i in range(1, 4 + 1):
    print(f'{i}ª Ficha')
    nome = input('Digite o nome: ').strip().title()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ').strip().title()

    soma += idade

    if sexo == 'Feminino' and idade < 20:
        soma1 += 1
    elif sexo == 'Masculino' and idade > idade_homem_velho:
        nome_homem_velho = nome
        idade_homem_velho = idade

# Prints de conclusão
print('')
print(f'A média de idade do grupo é de {soma / 4}')
print(f'O nome do homem mais velho é {nome_homem_velho}')
print(f'A quantidade de mulher com menos de 20 anos é de {soma1}')
