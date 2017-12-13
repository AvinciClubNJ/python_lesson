#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import math
import turtle

# Shape class
class Shape(object):
    # Constructor
    def __init__(self, color, perimeter):
        self.__color = color
        self.__perimeter = perimeter

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def draw(self):
        turtle.home
        turtle.pencolor(self.getColor())

    def calculatePerimeter(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        self.color = color
        super().__init__(color, radius)
        self.__radius = radius

    def calculatePerimeter(self):
        self.perimeter = 2 * self.__radius * math.pi

    def draw(self):
        super().draw()
        turtle.circle(self.__radius)

class Triangle(Shape):
    def __init__(self, color, x, y, z):
        self.color = color
        super().__init__(color, x)
        self._side1 = x
        self._side2 = y
        self._side3 = z

    def calculatePerimeter(self):
        self.perimeter = self._side1 + self._side2 + self._side3

    def draw(self):
        super().draw()
        turtle.seth(0)
        turtle.fd(self._side1)
        turtle.left(math.degrees(math.pi - math.acos((self._side1 ** 2 + self._side2 ** 2 - self._side3 ** 2) / (2 * self._side1 * self._side2))))
        turtle.fd(self._side2)
        turtle.left(math.degrees(math.pi - math.acos((self._side2 ** 2 + self._side3 ** 2 - self._side1 ** 2) / (2 * self._side2 * self._side3))))
        turtle.fd(self._side3)

class Rectangle(Shape):
    def __init__(self, color, width, height):
        self.color = color
        super().__init__(color, width)
        self.width = width
        self.height = height

    def calculatePerimeter(self):
        self.perimeter = 2 * (self.width + self.height)

    def draw(self):
        super().draw()
        turtle.degrees
        turtle.seth(0)
        turtle.fd(self.width)
        turtle.left(90)
        turtle.fd(self.height)
        turtle.left(90)
        turtle.fd(self.width)
        turtle.left(90)
        turtle.fd(self.height)

#start drawing

while True:
    try:
        myCircleColor = input("Set circle color.\n")
        myCircleRadius = int(input("Set circle radius.\n"))
        break
    except:
        print("Bad input.")
myCircle = Circle(myCircleColor, myCircleRadius)
myCircle.calculatePerimeter()
print("My circle circumference is", myCircle.perimeter, ".")
print("My circle color is", myCircle.getColor() , ".")

while True:
    try:
        myTriangleColor = input("Set triangle color.\n")
        myTriangleRadius1 = int(input("Set triangle first side length.\n"))
        myTriangleRadius2 = int(input("Set triangle second side length.\n"))
        myTriangleRadius3 = int(input("Set triangle third side length.\n"))
        if myTriangleRadius1 + myTriangleRadius2 <= myTriangleRadius3 or myTriangleRadius1 + myTriangleRadius3 <= myTriangleRadius2 or myTriangleRadius2 + myTriangleRadius3 <= myTriangleRadius1:
            print("ERROR!!!\nInvalid side lengths for a triangle.")
            continue
        else:
            pass
        break
    except:
        print("ERROR!!!\nBad input.")
    
myTriangle = Triangle(myTriangleColor, myTriangleRadius1, myTriangleRadius2, myTriangleRadius3)
myTriangle.calculatePerimeter()
print("My triangle perimeter is", myTriangle.perimeter , ".")
print("My triangle color is", myTriangle.getColor() , ".")

while True:
    try:
        myRectangeColor = input("Set rectangle color.\n")
        myRectangleWidth = int(input("Set rectange width.\n"))
        myRectangleHeight = int(input("Set rectange height.\n"))
        break
    except:
        print("ERROR!!!\nBad input.")
myRectangle = Rectangle(myRectangeColor, myRectangleWidth, myRectangleHeight)
myRectangle.calculatePerimeter()
print("My rectange perimeter is", myRectangle.perimeter , ".")
print("My rectangle color is", myRectangle.getColor() , ".")

try:
    myCircle.draw()
except:
    myCircle = Circle("black", myCircleRadius)
    print("WARNING!!!\nInvalid color for circle. Color is set to default black.")
    myCircle.draw()
try:
    myTriangle.draw()
except:
    myTriangle = Triangle("black", myTriangleRadius1, myTriangleRadius2, myTriangleRadius3)
    print("WARNING!!!\nInvalid color for triangle. Color is set to default black.")
    myTriangle.draw()
try:
    myRectangle.draw()
except:
    myRectangle = Rectangle("black", myRectangleWidth, myRectangleHeight)
    print("WARNING!!!\nInvalid color for rectangle. Color is set to default black.")
    myRectangle.draw()

input("Press any key to exit.")