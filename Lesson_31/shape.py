squar = int(input("Enter the area you want to solve for a square: "))
circl = int(input("Enter the area you want to solve for a circle: "))

class square:

    def __init__(self, side):
        self.side = side

    def area(self):
        print("My area is :", self.side**2)

class circle:

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print("My area is :", (22/7)*self.radius*self.radius)

osquare = square(squar)
ocircle = circle(circl)

for shape in (osquare, ocircle):
    shape.area()