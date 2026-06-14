# Slide 5 ==========
# Slide 8 ==========
# class Dog:
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def sit(self):
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         print(f"{self.name} rolled over!")

# my_dog = Dog("Willie", 6)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")


# Slide 11 ==========
# class Car:
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")


# # Create a car object
# my_new_car = Car("Audi", "A4", 2024)

# # Set the odometer reading
# my_new_car.odometer_reading = 23

# # Display the mileage
# my_new_car.read_odometer()

# Slide 12 ==========
# class Car:
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def read_odometer(self):
#         """Print a statement showing the car's mileage."""
#         print(f"This car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage


# # Create a car object
# my_new_car = Car("Audi", "A4", 2024)

# # Update the odometer reading
# my_new_car.update_odometer(23)

# # Display the mileage
# my_new_car.read_odometer()

# Slide 17 ==========
# Slide 18 ==========
# Slide 21 ==========
# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         return f"{self.year} {self.make} {self.model}"


# class Battery:
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=40):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         print(f"This car has a {self.battery_size}-kWh battery.")


# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""

#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()

#     def fill_gas_tank(self):
#         print("This car doesn't have a gas tank!")


# my_leaf = ElectricCar("nissan", "leaf", 2024)

# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.fill_gas_tank()