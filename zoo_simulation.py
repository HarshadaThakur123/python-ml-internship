# Base class
class Animal:
    def make_sound(self):
        print("Some generic animal sound")

# Subclass Lion
class Lion(Animal):
    def make_sound(self):
        print("Roar!")

# Subclass Snake
class Snake(Animal):
    def make_sound(self):
        print("Hiss!")

# Function that accepts a list of animals and calls make_sound()
def simulate_zoo(animals):
    for animal in animals:
        animal.make_sound()

# Example usage
zoo = [Lion(), Snake(), Lion()]
simulate_zoo(zoo)
