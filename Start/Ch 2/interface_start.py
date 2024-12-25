# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class JSONfy(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape,JSONfy):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        return f"{{\"sqaure\":{str(self.calcArea())} }}"

c = Circle(10)
print(c.calcArea())
print(c.toJSON())
