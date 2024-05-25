# Utilizando a exceção try-accept

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ").lower()
    if first_number == 'q':
        break
    second_number = input("Second number: ").lower()
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except (ZeroDivisionError, ValueError):
        print("Insert a valid number and bigger then 0 ")
    else:
        print(round(answer, 2))
