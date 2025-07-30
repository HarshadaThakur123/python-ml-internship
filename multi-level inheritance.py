# Base class
class Organism:
    def __init__(self):
        print("Organism created")

# Subclass of Organism
class Mammal(Organism):
    def __init__(self):
        Organism.__init__(self)  # Manually calling base constructor
        print("Mammal created")

# Subclass of Mammal
class Human(Mammal):
    def __init__(self):
        Mammal.__init__(self)  # Manually calling base constructor
        print("Human created")

# Creating object
person = Human()
