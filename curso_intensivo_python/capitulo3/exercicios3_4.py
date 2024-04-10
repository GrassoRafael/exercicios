print(f'{'Exercício 3.4 a 3.7':=^30}')
print('\n')

# 3.4 Lista de Convidados
convidado = ['natasha', 'anderson', 'jennie', 'vinicius', 'daniel']
print(f'Você está sendo convidado {convidado[0].title()}\n'
      f'Você está sendo convidado {convidado[1].title()}\n'
      f'Você está sendo convidado {convidado[2].title()}\n'
      f'Você está sendo convidado {convidado[3].title()}\n'
      f'Você está sendo convidado {convidado[4].title()}\n'
      )
print('\n')

# 3.5 Mudando a lista de convidados
convidado.remove('anderson')
print(f'Infelizmente o convidado {convidado[1].title()} não poderá comparecer')
convidado.insert(1, 'Larissa')
print(f'As pessoas que confirmaram presença são: {convidado[0].title()}, {convidado[1].title()}, {convidado[2].title()}, {convidado[3].title()}'
    f' e {convidado[4].title()}.')
print('\n')

# 3.6 Mais Convidados
convidado.insert(0, 'ana')
convidado.insert(3, 'ricardo')
convidado.append('mariana')

# Mensagens de convite
print(f'{convidado[0].title()}, você está sendo convidado para a festa\n'
      f'{convidado[1].title()}, você está sendo convidado para a festa\n'
      f'{convidado[2].title()}, você está sendo convidado para a festa\n'
      f'{convidado[3].title()}, você está sendo convidado para a festa\n'
      f'{convidado[4].title()}, você está sendo convidado para a festa\n'
      f'{convidado[5].title()}, você está sendo convidado para a festa\n'
      f'{convidado[6].title()}, você está sendo convidado para a festa\n'
      f'{convidado[7].title()}, você está sendo convidado para a festa')
print('\n')

# 3.7 Reduzindo a lista de convidados

nao_convidado = convidado.pop(0)
print(f'Sentimos muito por não poder convida-lo {nao_convidado.title()}')

nao_convidado = convidado.pop(0)
print(f'Sentimos muito por não poder convida-lo {nao_convidado.title()}')

nao_convidado = convidado.pop(0)
print(f'Sentimos muito por não poder convida-lo {nao_convidado.title()}')

nao_convidado = convidado.pop(0)
print(f'Sentimos muito por não poder convida-lo {nao_convidado.title()}')

nao_convidado = convidado.pop(0)
print(f'Sentimos muito por não poder convida-lo {nao_convidado.title()}')

nao_convidado = convidado.pop(-1)
print(f'Sentimos muito por não poder convida-lo {nao_convidado.title()}')

# Exibindo a mensagem para os que restaram
print(f'Você ainda está convidado(a) para a festa {convidado[0].title()}')
print(f'Você ainda está convidado(a) para a festa {convidado[-1].title()}')

del convidado[0:2]
print(convidado)



