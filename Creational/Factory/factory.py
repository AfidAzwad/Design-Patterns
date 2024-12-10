from abc import ABC, abstractmethod


# Abstract Product
class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def draw(self):
        """Method to draw the shape."""
        pass


# Concrete Products
class Circle(Shape):
    """A Circle shape."""

    def draw(self):
        return "Drawing a Circle"


class Square(Shape):
    """A Square shape."""

    def draw(self):
        return "Drawing a Square"


# Factory Class
class ShapeFactory:
    """Factory class to create shapes."""

    @staticmethod
    def get_shape(shape_type: str) -> Shape:
        """Factory method to create shapes."""
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")


# Test the Factory Pattern
if __name__ == "__main__":
    # Use the factory to create shapes
    circle = ShapeFactory.get_shape("circle")
    print(circle.draw())  # Output: Drawing a Circle

    square = ShapeFactory.get_shape("square")
    print(square.draw())  # Output: Drawing a Square

    # Try an invalid shape
    try:
        unknown = ShapeFactory.get_shape("triangle")
    except ValueError as e:
        print(e)  # Output: Unknown shape type: triangle
