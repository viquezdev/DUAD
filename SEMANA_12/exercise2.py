from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self):
        pass


    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    
    def calculate_perimeter(self):
        return f"Circle-Perimeter: {2*math.pi*self.radius}"


    def calculate_area(self):
        return f"Circle-Area: {math.pi*(self.radius*self.radius)}"


class Square(Shape):
    def __init__(self,side):
        self.side=side
    

    def calculate_perimeter(self):
        return f"Square-Perimeter: {4*self.side}"

    
    def calculate_area(self):
        return f"Square-Area: {self.side*self.side}"

class Rectangle(Shape):
    def __init__(self,width,length):
        self.width=width
        self.length=length
    

    def calculate_perimeter(self):

        return f"Rectangle-Perimeter: {((2*self.width)+2*(self.length))}"

    
    def calculate_area(self):
        return f"Rectangle-Area: {self.width*self.length}"
    

circle=Circle(5)
square=Square(5)
rectangle=Rectangle(5,6)
shapes=[circle,square,rectangle]
for element in shapes:
    print(element.calculate_area())
    print(element.calculate_perimeter())