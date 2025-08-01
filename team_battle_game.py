# Base class
class Character:
    def __init__(self, name):
        self.name = name

    def attack(self):
        raise NotImplementedError("Subclasses must implement this method")

# Warrior class
class Warrior(Character):
    def attack(self):
        print(f"{self.name} swings a sword with great force!")

# Archer class
class Archer(Character):
    def attack(self):
        print(f"{self.name} shoots an arrow from a distance!")

# Mage class
class Mage(Character):
    def attack(self):
        print(f"{self.name} casts a powerful fireball!")

# Team battle function
def team_battle(team):
    print("Battle begins!\n")
    for character in team:
        character.attack()

# Example usage
team = [
    Warrior("Thorin"),
    Archer("Legolas"),
    Mage("Gandalf"),
    Warrior("Eivor")
]

team_battle(team)
