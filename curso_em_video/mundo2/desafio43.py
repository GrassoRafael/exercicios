print(f'{"Desafio 43":=^40}') # Enunciado

# Programa para calcular o IMCS da pessoa com informações de sua altura e peso

# Inputando variáveis
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

# Estrutura condicional
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f} então você está abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print(f'Seu IMC é de {imc:.1f} então você está no peso ideia')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC é de {imc:.1f} então você está com sobrepeso')
elif imc > 30 and imc <= 40:
    print(f'Seu IMC é de {imc:.1f} então você está com obesidade')
else:
    print(f'Seu IMC é de {imc:.1f} então você está com obesidade mórbida')
