import math

class Circle():
    radius=0

    def get_area(self):
        return math.pi*(self.radius**2)
    
my_circle=Circle()
my_circle.radius=5
print(my_circle.get_area())


    