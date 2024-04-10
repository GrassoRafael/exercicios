print(f'{'Exercício 2.3 a 2.5':=^80}')
print('\n')

# Mensagem Pessoal
nome = 'Rafael grasso'
print(f'Olá {nome}, gostaria de aprender um pouco de Python hoje?')

# Maiúsculas e Minúsculas
print(f'Seu nome em letras minúsculas fica {nome.lower()}')
print(f'Seu nome em letras maiúculas fica {nome.upper()}')
print(f'Seu nome com data primeira letra maiúscula fica {nome.title()}')
print('\n')

# Citação famosa
print('Albert Einstein disse uma vez: "Uma pessoa que nunca cometeu um erro, nunca tentou nada de novo" ')
print('\n')

# Citação famosa 2
famous_person = 'Albert Einstein'
message = f'{famous_person} disse uma vez: "Uma pessoa que nunca cometeu um erro, nunca tentou nada de novo"'
print(message)

# Removendo Nomes
nome = '     Rafael   '
print(nome)
print(f'Sem espaços: {nome.strip()}')
print(f'Sem espaços a direita: {nome.rstrip()}')
print(f'Sem espaços a esquerda: {nome.lstrip()}')

# Extensões de arquivo
filename = 'python_notes.txt'
print(f'O nome do arquivo sem o sufixo é {filename.removesuffix('.txt')}')

