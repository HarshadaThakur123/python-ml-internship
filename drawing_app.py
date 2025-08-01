print("Program started")
# Base class
class Shape:
    def draw(self):
        print("Drawing a shape")

# Subclass Circle
class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

# Subclass Rectangle
class Rectangle(Shape):
    def draw(self):
        print("Drawing a Rectangle")

# Canvas class that holds and renders shapes
class Canvas:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            raise TypeError("Only Shape objects can be added to the canvas")

    def render_all(self):
        print("Rendering all shapes:")
        for shape in self.shapes:
            shape.draw()

# Example usage
canvas = Canvas()
canvas.add_shape(Circle())
canvas.add_shape(Rectangle())
canvas.add_shape(Circle())

canvas.render_all()
