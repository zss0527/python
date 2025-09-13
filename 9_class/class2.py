# from car import *
# import car
from car import Car, Battery

# parent class definition must be defined before child class
# parent class name must be included in the parentheses of child class definition
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75  # in kWh
        self.battery = Battery()  # composition: include a Battery instance as an attribute

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 200  # default range for other battery sizes

        print(f"This car can go approximately {range} miles on a full charge.")

    # override parent class method
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(50)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_used_car.increment_odometer(-50)
my_used_car.read_odometer() 


