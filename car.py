class Car():
    """Prosta próba zaprezentowania samochodu."""
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących samochód."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Wyświetla informację o przebiegu samochodu."""
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print("Zaktualizowano przebieg samochodu.")
        else:
            print("Nie można cofnąć licznika przebiegu samochodu, Januszu!")

    def increment_odometer(self, kilometers):
        if kilometers >= 0:
            self.odometer_reading += kilometers
            print("Zaktualizowano przebieg samochodu.")

    def fill_gas_tank(self):
        print("Koniecznie zatankuj samochód!")

class Battery():
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
        self.manufacturer = "LG Energy Solutions"

    def describe_battery(self):
        print(f"Ten samochód ma akumulator o pojemności {self.battery_size} kWh wyprodukowany w {my_tesla.battery.manufacturer}.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"Zasięg tego samochodu wynosi około {range} km po pełnym naładowaniu akumulatora.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów klasy nadrzędnej."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("To samochód elektryczny, a więc nie wymaga tankowania paliwa.")

my_tesla = ElectricCar("tesla", "model s", 2019)

