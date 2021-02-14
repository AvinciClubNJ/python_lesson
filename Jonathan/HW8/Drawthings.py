from math import pi
import turtle


class Shape:
    def __init__(self):
        pass

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def draw(self):
        pass

    def getCircumference(self):
        pass

class Circle(Shape):
    def __init__(self, startX, startY, radius, color):
        self.__x = startX
        self.__y = startY
        self.__radius = radius
        super().setColor(color)
        
    def getCircumference(self):
        self.Circumference = self.__radius*(pi)*2

    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.color(self.color)
        t.setx(self.__x)
        t.sety(self.__y)
        t.pendown()
        t.circle(self.__radius)
        t.penup()
        t.hideturtle()

class Triangle(Shape):
    def __init__(self, startX, startY, sidelength, color):
        self.__x = startX
        self.__y = startY
        self.__sidelength = sidelength
        super().setColor(color)

    def getCircumference(self):
        self.Circumference = self.__sidelength*3

    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.color(self.color)
        t.setx(self.__x)
        t.sety(self.__y)
        t.pendown()
        for e in range(3):
            t.forward(self.__sidelength)
            t.right(120)
        t.penup()
        t.hideturtl()

class Rectangle(Shape):
    def __init__(self, startX, startY, length, width,  color):
        self.__x = startX
        self.__y = startY
        self.__length = length
        self.__width = width 
        super().setColor(color)
        
    def getCircumference(self):
        self.Circumference = self.__radius*(pi)*2

    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.color(self.color)
        t.setx(self.__x)
        t.sety(self.__y)
        t.pendown()
        for e in range(2):
            t.forward(self.__length)
            t.right(90)
            t.forward(self.__width)
            t.right(90)
        t.penup()
        t.hideturtle()
            

# main program
circle = Circle(0, 0, 10, "red")
square = Rectangle(-100, 50, 10, 10, "red")
triangle = Triangle(100, -50, 10, "red")

shapes = [circle, square,  triangle]

for s in shapes:
#    print ("My color is :" + s.getColor())
#    print ("My circumference is" + s.getCircumference())
    s.draw()

input("Press enter to end.")