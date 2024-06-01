import math

class GeometryShapes:
    def __init__(self, x, y):
        self.validate_input(x, y)
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.validate_input(dx, dy)
        self.x += dx
        self.y += dy
            

    def __str__(self):
        return f"Shape at ({self.x}, {self.y})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
    
            
    @staticmethod
    def validate_input(*args):
        for arg in args:
            if isinstance(arg, (int, float)):
                if arg < 0:
                    raise ValueError("Numeric values must be non-negative")
            else:
                raise ValueError("All inputs must be numbers")

   
            
    @property
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
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
        self.validate_input(radius)
        self.radius = radius
    
    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def circumference(self):
         return 2 * math.pi * self.radius
    
    def is_unit_circle(self):
        return self.radius == 1.0
    
class Rectangle(GeometryShapes):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.validate_input(width, height)
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
    @property
    def circumference(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height