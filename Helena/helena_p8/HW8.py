import turtle
import math
t = turtle.Turtle()

class Shape:
  def __init__(self,x,y):
    self.__x = x
    self.__y = y
  def setPosition(self):
    t.penup()
    t.setx(self.__x)
    t.sety(self.__y)
  def draw(self):
    pass
  def printlen(self):
    pass
  
class Triangle(Shape):
  def __init__(self,color,side):
    self.__color = color
    self.__sideLength = side
    super().__init__(0,0)
  def draw(self):
    super().setPosition()
    t.pendown()
    t.pencolor(self.__color)
    for i in range(0,3):
      t.forward(self.__sideLength)
      t.left(120)
  def printlen(self):
    print(self.__sideLength *3)
    
class Rectangle(Shape):
  def __init__(self,color,side1,side2):
    self.__color = color
    self.__width = side1
    self.__height = side2
    super().__init__(100,0)
  def draw(self):
    super().setPosition()
    t.pendown()
    t.pencolor(self.__color)
    for i in range(0,2):
      t.forward(self.__width)
      t.left(90)
      t.forward(self.__height)
      t.left(90)
  def printlen(self):
    print((self.__width+self.__height) *2)

class Circle(Shape):
  def __init__(self,color,side):
    self.__color = color
    self.__radius = side
    super().__init__(100,-100)
  def draw(self):
    super().setPosition()
    t.pendown()
    t.pencolor(self.__color)
    t.circle(self.__radius)
  def printlen(self):
    print(2 * self.__radius * math.pi)

tri = Triangle("Blue",100)
tri.draw()
tri.printlen()

rect = Rectangle("Yellow", 50,100)
rect.draw()
rect.printlen()

cir = Circle("Red", 50)
cir.draw()
cir.printlen()
