class Car:
    """Simples tentativa de representar um carro"""

    def __init__(self, make, model, year):
        """Inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retorna um nome descritivo, formatado elegantemente"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """
        Define a leitura do hodômetro para o valor fornecido.
        Rejeita a alteração se houver tentativas de reverter o hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Você não pode diminuir o hodômetro")

    def increment_odometer(self, miles):
        """Adiciona a quantidade fornecida à leitura do hodômetro"""
        self.odometer_reading += miles

    def read_odometer(self):
        """Exibe uma frase mostrando a quilometragem do carro, em km"""
        print(f'Este carro tem {self.odometer_reading} km rodados')

    def fill_gas_tank(self):
        print("You need to fill you gas tank")


class Battery:
    """Simples tentativa de modelar uma bateria para um carro elétrico"""

    def __init__(self, battery_size=40):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print(f"This car has a {self.battery_size}KWh battery")

    def get_range(self):
        """Exibe frase sobre a distância que o carro percorre com essa bateria"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge")


class EletricCar(Car):
    """Representa aspectos de um carro, específico para veículos elétricos"""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai (Car).
        Em seguida, inicializa os atributos específicos para um carro elétrico.
        """
        super().__init__(make, model, year) # Super, possibilita chamar o __init__ da classe pai (Car)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("You don't neet to fill the tank, the car is eletric") # Métodos iguais, é considerado a da classe-filha


# Programa principal
my_new_car = Car("audi", "a4", 2024)
print(f"My new car is a {my_new_car.get_descriptive_name()}")

my_new_car.update_odometer(25)
my_new_car.update_odometer(30)
my_new_car.update_odometer(10)
my_new_car.read_odometer()
print()

my_user_car = Car("subaru", "outback", 2019)
print(f"My user car is a {my_user_car.get_descriptive_name()}")

my_user_car.update_odometer(23_500)
my_user_car.read_odometer()

my_user_car.increment_odometer(100)
my_user_car.read_odometer()
my_user_car.fill_gas_tank()


# Programa que utiliza a classe Car para a classe EletricCar
print()
my_leaf = EletricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.fill_gas_tank()
my_leaf.battery.get_range()
