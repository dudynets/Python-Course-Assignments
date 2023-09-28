# 1. Створити тип Vehicle, який характеризується маркою, потужнiстю двигуна, кiлькiстю колiс та вагою автомобiля.
#    Також утворити похi- днi типи Truck (додатково характеризується вантажопiдйомнiстю),
#    а також Car i Bus, якi характеризується кiлькiстю мiсць для сидiння, а Bus – ще й кiлькiстю “стоячих” мiсць.
#    Надати properties для даних, а також метод для iнформування про характеристики автомобiля.

# 2. Задати в кодi окремої комiрки ноутбуку автопарк – колекцiю даних з кiлькох об’єктiв кожного типу.

# 3. Вивести:
#    (а) повнi описи усiх транспортних засобiв автопарку
#    (б) перелiк усiх транспортних засобiв автопарку, впорядкований за потужнiстю двигуна
#    (в) окремi перелiки вантажiвок та пасажирських автомобiлiв, якi впорядкувати за спаданням
#       вантажопiдйомнiстi для вантажiвок i кiлькiстi пасажирiв для пасажирських авто.


class Vehicle:
    def __init__(self, manufacturer, engine_power, number_of_wheels, weight):
        self.__manufacturer = manufacturer
        self.__engine_power = engine_power
        self.__number_of_wheels = number_of_wheels
        self.__weight = weight

    def __str__(self):
        return (
            f"Manufacturer: {self.__manufacturer}\n"
            + f"Engine power: {self.__engine_power}kW\n"
            + f"Number of wheels: {self.__number_of_wheels} wheels\n"
            + f"Weight: {self.__number_of_wheels}kg"
        )

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    @property
    def engine_power(self):
        return self.__engine_power

    @engine_power.setter
    def engine_power(self, engine_power):
        self.__engine_power = engine_power

    @property
    def number_of_wheels(self):
        return self.__number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number_of_wheels):
        self.__number_of_wheels = number_of_wheels

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight


class Truck(Vehicle):
    def __init__(
        self, manufacturer, engine_power, number_of_wheels, weight, carrying_capacity
    ):
        super().__init__(manufacturer, engine_power, number_of_wheels, weight)
        self.__carrying_capacity = carrying_capacity

    def __str__(self):
        return super().__str__() + f"\nCarrying capacity: {self.__carrying_capacity}kg"

    @property
    def carrying_capacity(self):
        return self.__carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, carrying_capacity):
        self.__carrying_capacity = carrying_capacity


class Car(Vehicle):
    def __init__(
        self,
        manufacturer,
        engine_power,
        number_of_wheels,
        weight,
        number_of_sitting_seats,
    ):
        super().__init__(manufacturer, engine_power, number_of_wheels, weight)
        self.__number_of_sitting_seats = number_of_sitting_seats

    def __str__(self):
        return (
            super().__str__()
            + f"\nNumber of sitting seats: {self.__number_of_sitting_seats} seats"
        )

    @property
    def number_of_sitting_seats(self):
        return self.__number_of_sitting_seats

    @number_of_sitting_seats.setter
    def number_of_sitting_seats(self, number_of_sitting_seats):
        self.__number_of_sitting_seats = number_of_sitting_seats


class Bus(Vehicle):
    def __init__(
        self,
        manufacturer,
        engine_power,
        number_of_wheels,
        weight,
        number_of_sitting_seats,
        number_of_standing_seats,
    ):
        super().__init__(manufacturer, engine_power, number_of_wheels, weight)
        self.__number_of_sitting_seats = number_of_sitting_seats
        self.__number_of_standing_seats = number_of_standing_seats

    def __str__(self):
        return (
            super().__str__()
            + f"\nNumber of sitting seats: {self.__number_of_sitting_seats} seats\n"
            + f"Number of standing seats: {self.__number_of_standing_seats} seats"
        )

    @property
    def number_of_sitting_seats(self):
        return self.__number_of_sitting_seats

    @number_of_sitting_seats.setter
    def number_of_sitting_seats(self, number_of_sitting_seats):
        self.__number_of_sitting_seats = number_of_sitting_seats

    @property
    def number_of_standing_seats(self):
        return self.__number_of_standing_seats

    @number_of_standing_seats.setter
    def number_of_standing_seats(self, number_of_standing_seats):
        self.__number_of_standing_seats = number_of_standing_seats


vehicles = [
    Car("BMW", 200, 4, 2000, 4),
    Car("Mercedes", 250, 4, 2500, 4),
    Car("Audi", 300, 4, 3000, 4),
    Truck("Volvo", 400, 6, 4000, 1000),
    Truck("Scania", 500, 6, 5000, 2000),
    Bus("Ikarus", 600, 8, 6000, 40, 20),
    Bus("Mercedes", 700, 8, 7000, 50, 30),
    Bus("Volvo", 800, 8, 8000, 60, 40),
]

# Printing all vehicles
print("=== ALL VEHICLES ===\n")
for vehicle in vehicles:
    print(vehicle)
    print()

# Sort by engine_power
print("\n\n=== VEHICLES SORTED BY ENGINE POWER ===\n")
sorted_vehicles = sorted(vehicles, key=lambda vehicle: vehicle.engine_power)
for vehicle in sorted_vehicles:
    print(vehicle)
    print()

# Trucks sorted by carrying_capacity
print("\n\n=== TRUCKS SORTED BY CARRYING CAPACITY ===\n")
sorted_trucks = sorted(
    filter(lambda vehicle: isinstance(vehicle, Truck), vehicles),
    key=lambda truck: truck.carrying_capacity,
    reverse=True,
)
for truck in sorted_trucks:
    print(truck)
    print()

# Cars sorted by number_of_sitting_seats
print("\n\n=== CARS SORTED BY NUMBER OF SITTING SEATS ===\n")
sorted_cars = sorted(
    filter(lambda vehicle: isinstance(vehicle, Car), vehicles),
    key=lambda car: car.number_of_sitting_seats,
    reverse=True,
)
for car in sorted_cars:
    print(car)
    print()
