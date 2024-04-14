# # pizza.py
def make_pizza(size, *toppings):
    """
    Synthesize a pizza we'are about to make
    """
    print(f'\nMaking a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')