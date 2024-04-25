# Loteria 9.14 e 9.15 Análise de loteria
# Importando Módulo
from random import choice

# Sorteio dos números
print("And the winning characters are:")

# Variaveis
active = True
soma = 0
contagem = 0
numeros = 0
numeros_loteria = [5, 4, 2, 3, 10, 55, 20, 22, 11, 54, 40, "a", "h", "o", "f", "i"]
my_ticket = ["a", "o", 55, 20]
winners = []

while active:
    for i in range(0, 4):
        # Sorteio
        winning = choice(numeros_loteria) # Sorteia 1 valor da lista
        winners.append(winning) # Adiciona o número sorteado na lista winners
        numeros_loteria.remove(winning) # Remove o valor sorteado da lista original

        # Verificando ticket ganhador
        if winners[-1] in my_ticket: # Se o número for um dos vencedores, soma 1 no valor da soma
            numeros += 1
            if numeros == 4: # Ao chegar em 4, é indicado a quantidade de vezes jogada e que o jogador ganhou
                contagem += 1
                print(f"Você foi o vencedor, jogou {contagem} vezes até ganhar\n"
                      f"Seus números {my_ticket}\n"
                      f"Números sorteados {winners}")
                active = False

    # Resetando variáveis - Caso não sejam acertados os 4 valores, todas as listas são resetadas.
    if len(winners) == 4:
        numeros_loteria = [5, 4, 2, 3, 10, 55, 20, 22, 11, 54, 40, "a", "h", "o", "f", "i"]
        winners = []
        numeros = 0
        contagem += 1
