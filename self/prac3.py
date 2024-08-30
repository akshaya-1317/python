#define a Circle class to create a circle with radius r using the constructor.
#define an Area() method of the class calculates area
#define Perimeter() method and calculate perimeter.

class Circle:

    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        self.area = 0
        self.area = 3.14 * (self.radius**2)
        print("Area is =  ", self.area)

cir = Circle(5)
cir.area()



