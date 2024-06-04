import math

class GeometryShapes:
    # Base class for all geometric shapes providing basic properties and methods. Handles coordinate validation and provides an interface for calculating area.
    def __init__(self, x, y):
        # Initialize postion with validation
        self.validate_coordinates(x, y)
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        # Move the shape by uptdating x, y coordinates
        self.validate_coordinates(dx, dy)
        self.x += dx
        self.y += dy
            
    def __str__(self):
        # User-friendly string representation
        return f"Shape at ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    @staticmethod
    def validate_coordinates(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("All inputs must be numbers")
            
    @staticmethod
    def validate_dimension(value):
        if not isinstance(value, (int, float)):
            raise ValueError("Dimensions must be numeric")
        if value < 0:
            raise ValueError("Dimensions must be non-negative")

    @property
    def area(self):
        # Abstract property to calculate area
        raise NotImplementedError("Subclasses must implement this method.")
    
    # Comparison operators based on area
    def __eq__(self, other):
        if not isinstance(other, GeometryShapes):
            return NotImplemented
        return self.area == other.area

    def __lt__(self, other):
        if not isinstance(other, GeometryShapes):
            return NotImplemented
        return self.area < other.area
    
    def __le__(self, other):
            return self.__lt__(other) or self.__eq__(other)
    
    def __gt__(self, other):
            return not self.__le__(other)
    
    def __ge__(self, other):
        return not self.__lt__(other)

class Circle(GeometryShapes):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        # Validate and initialize radius
        self.validate_dimension(radius)
        self.radius = radius
    
    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    # Circumference specific to circles
    def circumference(self):
         return 2 * math.pi * self.radius
    
    def is_unit_circle(self):
        # Check if the circle is a unit circle
        return self.radius == 1.0
    
    def is_inside(self, px, py):
        # Check if a point is inside the circle
        return (self.x - px) ** 2 + (self.y - py) ** 2 <= self.radius ** 2
    
class Rectangle(GeometryShapes):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        # Validate and initialize dimensions
        self.validate_dimension(width)
        self.validate_dimension(height)
        self.width = width
        self.height = height

    @property
    def area(self):
        # Area specific to rectangles
        return self.width * self.height
    @property
    def circumference(self):
        # Perimeter specific to rectangles
        return 2 * (self.width + self.height)

    def is_square(self):
        # Check if the rectangle is a square
        return self.width == self.height
    
    def is_inside(self, px, py):
        # Check if a point is inside the rectangle
        return self.x <= px <= self.x + self.width and self.y <= py <= self.y + self.height