class Circle:

    def __init__(self, radius):
        self.radius = radius

    pie = 22/7

    

    def perimeter(self):
        return 2 * self.pie * self.radius

    def area(self):
        return self.pie * self.radius * self.radius


radius_num = int(input("How many circles do you want to create? "))
for i in range(radius_num):
    radius = int(input(f"Enter the radius of circle {i+1}: "))
    circle = Circle(radius)
    print(f"Circle {i+1} - Perimeter: {circle.perimeter()}, Area: {circle.area()}")
    del circle