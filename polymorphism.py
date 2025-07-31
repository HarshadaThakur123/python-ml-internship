# Base class
class Shape:
    def draw(self):
        print("Drawing a shape")

# Subclass: Circle
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

# Subclass: Rectangle
class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

# Subclass: Triangle
class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")


shapes = [Circle(), Rectangle(), Triangle()]

# Polymorphic loop
for shape in shapes:
    shape.draw()
