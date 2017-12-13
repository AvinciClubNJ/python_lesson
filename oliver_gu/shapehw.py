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
    def __init__(self, radius):
        super().__init__("red", 0)
        self.__radius = radius

    def calculatePerimeter(self):
        self.perimeter = 2 * self.__radius * math.pi

    def draw(self):
        super().draw()
        turtle.circle(self.__radius)

class Triangle(Shape):
    def __init__(self, x, y, z):
        super().__init__("blue", 0)
        self._side1 = x
        self._side2 = y
        self._side3 = z

    def calculatePerimeter(self):
        self.perimeter = self._side1 + self._side2 + self._side3

    def draw(self):
        super().draw()
        turtle.seth(0)
        turtle.fd(self._side1)
        turtle.left(120)
        turtle.fd(self._side2)
        turtle.left(120)
        turtle.fd(self._side3)

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("yellow", 0)
        self.width = width
        self.height = height

    def calculatePerimeter(self):
        self.perimeter = 2 * (self.width + self.height)

    def draw(self):
        super().draw()
        turtle.seth(0)
        turtle.fd(self.width)
        turtle.left(90)
        turtle.fd(self.height)
        turtle.left(90)
        turtle.fd(self.width)
        turtle.left(90)
        turtle.fd(self.height)

myCircle = Circle(50)
myCircle.calculatePerimeter()
print("My circle circumference is", myCircle.perimeter)
print("My circle color is", myCircle.getColor())

myTriangle = Triangle(100, 100, 100)
myTriangle.calculatePerimeter()
print("My triangle perimeter is", myTriangle.perimeter)
print("My triangle color is", myTriangle.getColor())

myRectangle = Rectangle(50, 100)
myRectangle.calculatePerimeter()
print("My rectange perimeter is", myRectangle.perimeter)
print("My rectangle color is", myRectangle.getColor())

myCircle.draw()
myTriangle.draw()
myRectangle.draw()

input("Press any key to exit.")