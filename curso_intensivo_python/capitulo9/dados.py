# Criando classe dados
from random import randint

class Die:
    """Rola um dado, como padrão, de 6 lados"""

    def __init__(self, sides=6):
        self.sides = sides
        print(randint(1, self.sides))

