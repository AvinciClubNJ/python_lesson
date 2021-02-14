import turtle
import sys
import math
t = turtle.Pen()
t.speed(9)
class Shape:

    def __init__(self, color):
        self.__color = color

    def setColor(self, color):
        t.color(self.__color)

    def getColor(self):
        return self.__color

    def draw(self):
        pass

    def getPerm(self):
        pass

class Circle(Shape):

    def __init__(self, radius, color):
        self.__radius = radius
        self.__color = color
        super().__init__(color)

    def draw(self):
        self.setColor(self.__color)
        t.circle(self.__radius)

    def getPerm(self):
        answer = self.__radius * 2 * math.pi
        return answer

class Triangle(Shape):

    def __init__(self, sidelength, color):
        self.__sidelength = sidelength
        self.__color = color
        super().__init__(self.__color)

    def draw(self):
        self.setColor(self.__color)
        for x in range(3):
            t.forward(self.__sidelength)
            t.left(120)

    def getPerm(self):
        answer = self.__sidelength * 3
        return answer

class Rectangle(Shape):

    def __init__(self, sidelength1, sidelength2, color):
        self.__sidelength1 = sidelength1
        self.__sidelength2 = sidelength2
        self.__color = color
        super().__init__(self.__color)

    def draw(self):
        self.setColor(self.__color)
        for x in range(2):
            t.forward(self.__sidelength1)
            t.right(90)
            t.forward(self.__sidelength2)
            t.right(90)

    def getPerm(self):
        answer = self.__sidelength1 * 2 + self.__sidelength2 * 2
        return answer

myCircle = Circle(50, 'red')
myTriangle = Triangle(100, 'blue')
myRectangle = Rectangle(100, 50, 'yellow')

# Main Program

myCircle.draw()
print('Circle Approximate Circumference: %s' % myCircle.getPerm())
myTriangle.draw()
print("Triangle Perimeter: %s" % myTriangle.getPerm())
myRectangle.draw()
print("Rectangle Perimeter: %s" % myRectangle.getPerm())
