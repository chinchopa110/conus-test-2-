class Conus:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        pi = 3.14159
        s = pi * self.radius * (self.radius + ((self.radius**2) + (self.height**2))**0.5)
        return s
    def sum(self):
        return self.radius + self.height
    
conus = Conus(5, 4)
print(conus.area())    
