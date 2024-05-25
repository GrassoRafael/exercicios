# Exercicio 10.11 e 10.12
# Número favorito e relembrando o número favorito

# Importando módulos
from pathlib import Path
import json

def get_new_number(path):
    """Solicita o número favorito do usuário e o armazena"""
    number = input("What is your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    return number


def get_stored_number(path):
    """Verifica se há a existência do path passado, senão, retorna None"""
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None


def favorite_number():
    """
    Informa seu número favorito caso esteja salvo em um arquivo json, senão pergunta qual o seu número favorito
    :return: Número Favorito
    """
    path = Path('favorite_number.json')
    number = get_stored_number(path)
    if number:
        print(f"Your favorito number is: {number}")
    else:
        number = get_new_number(path)
        print(f"You just registered your favorite number, it is {number}")


# Programa principal
favorite_number()
