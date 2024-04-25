# Importando módulo
from restaurant import Restaurant as rest

# Principal program
restaurant = rest("pizzeria 2001", "pizzeria", 44)
restaurant.describe_restaurant()
restaurant.set_number_served(55) # Incrementando direto na instância
restaurant.open_restaurant()
restaurant.increment_number_served(44) # Somando número de clientes ao valor original

print()
restaurant = rest("king os pastel", "pastry shop")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print()
restaurant = rest("company of cake", "confectionery")
restaurant.describe_restaurant()
restaurant.open_restaurant()
