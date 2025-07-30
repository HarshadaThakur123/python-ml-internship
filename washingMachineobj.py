# Base class
class Appliance:
    def __init__(self, power_rating):
        self.power_rating = power_rating
        print(f"Appliance created with power rating: {self.power_rating}")

# Child class
class WashingMachine(Appliance):
    def __init__(self, power_rating, capacity):
        Appliance.__init__(self, power_rating)  # Manually call base class constructor
        self.capacity = capacity
        print(f"WashingMachine created with capacity: {self.capacity}")

# Creating object
wm = WashingMachine(1500, 7)

