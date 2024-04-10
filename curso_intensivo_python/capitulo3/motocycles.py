# Modificando elementos numa lista

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

too_expensive = 'yamaha'
motocycles.remove(too_expensive)
print(motocycles)
print(f'\nA {too_expensive.title()} is too expensive for me')

print('\n')
popped_motocycle = motocycles.pop(1)
print(popped_motocycle)
print(f'A última moto comprada foi a {popped_motocycle}')

print('\n')
motocycles.insert(1, 'ducati')
del motocycles[0]
print(motocycles)

# motocycles[0] = 'ducatti'
# print(motocycles)

motocycles.append('ducatti')
print(motocycles)

motocicletas = []

motocicletas.append('honda')
motocicletas.append('yamaha')
motocicletas.append('suzuki')
print(motocicletas)