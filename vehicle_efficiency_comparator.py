# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def fuel_efficiency(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass Car
class Car(Vehicle):
    def __init__(self, name, km_per_litre):
        super().__init__(name)
        self.km_per_litre = km_per_litre

    def fuel_efficiency(self):
        return self.km_per_litre

# Subclass Truck
class Truck(Vehicle):
    def __init__(self, name, km_per_litre):
        super().__init__(name)
        self.km_per_litre = km_per_litre

    def fuel_efficiency(self):
        return self.km_per_litre

# Function to find the most fuel-efficient vehicle
def most_efficient_vehicle(vehicles):
    if not vehicles:
        print("No vehicles to compare.")
        return

    most_efficient = max(vehicles, key=lambda v: v.fuel_efficiency())
    print(f"The most fuel-efficient vehicle is: {most_efficient.name} "
          f"with {most_efficient.fuel_efficiency()} km/litre.")

# Example usage
vehicles = [
    Car("Maruti Swift", 22),
    Truck("Tata Truck", 8),
    Car("Hyundai i20", 18),
    Truck("Ashok Leyland", 6)
]

most_efficient_vehicle(vehicles)
