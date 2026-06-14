# =============================================================================
# Student Name: Michael Johnson
# Lab Title: Lab 6
# Date:
# =============================================================================

class Vehicle:
    """"""
    def __init__(self, make, model, year, max_fuel):
        self.make = make
        self.model = model
        self.year = year
        self.max_fuel = max_fuel
        self.current_fuel = 0.0
        self.is_almost_empty = True

    def fuel_level(self, gallons):
        """Sets current_fuel to the number of gallons in the gas tank"""
        #self.current_fuel = gallons
        if gallons >= 0 and gallons <= self.max_fuel:
            self.current_fuel = gallons
        

    def details(self):
        """Returns a formatted string with the vehicle's make model and year"""
        return f"{self.year} {self.make} {self.model}"
    

    def fuel_left(self):
        """Returns the percentage of fuel still in the car as a (float) calculation of current_ fuel / max_fuel, to one decimal place"""
        if self.current_fuel == 0:
            return 0.0
        percentage = (self.current_fuel / self.max_fuel) * 100
        return round(percentage, 1)
    

    def empty_warning_check(self):
        """Checks if the fuel left is less than 10% sets is_almost_empty to True"""
        if self.fuel_left() < 10:
            self.is_almost_empty = True
        else:
            self.is_almost_empty = False


    

# Create an empty list
vehicles = []

# Four vehicle objects
vehicle1 = Vehicle("Toyota", "Corolla", 2020, 12.0)
vehicle2 = Vehicle("Honda", "Civic", 2022, 10.0)
vehicle3 = Vehicle("Ford", "Ranger", 2023, 15.0)
vehicle4 = Vehicle("Nissan", "Frontier", 2025, 8.0)

# Add the vehicles to the list
vehicles.append(vehicle1)
vehicles.append(vehicle2)
vehicles.append(vehicle3)
vehicles.append(vehicle4)

# Set fuel levels
vehicle1.fuel_level(5.3)
vehicle2.fuel_level(2.2)
vehicle3.fuel_level(10.1)
vehicle4.fuel_level(0.5)

# Set the second vehicle a fuel level of -4.4
vehicle2.fuel_level(-4.4)
# Set the fourth vehicle a fuel level of 100 (should be greater than its max_level)
vehicle4.fuel_level(100)  

# Display 
for vehicle in vehicles:
    vehicle.empty_warning_check()

    print(
        f"Vehicle: {vehicle.details()}\n"
        f"Current Fuel: {vehicle.current_fuel}\n"
        f"Fuel Left: {vehicle.fuel_left()}%\n"
        f"Almost Empty: {vehicle.is_almost_empty}\n"
    )