#Use this as white board for avinciclub class
from turtlegame import *
    
class GreedyEater:
  def start(self):
    score = 0
    self.__stage.writeScore(score)
    while True:
      if self.__hitBorder():
        self.__player.turn(180)
      self.__player.move()
      for g in self.__goals:
        if g.isHitBy(self.__player):
          score += 1
          self.__stage.writeScore(score)
          g.reborn()
        g.wander()

  def createStage(self, w, c):
    self.__stage = Stage(w, c)

  def addPlayer(self, s, c):
    self.__player = Player(s, c)
    
  def addGoals(self, count, color):
    self.__goals = []
    for _ in range(count):
      self.__goals.append(Goal(color, self.__stage))
    
  def __hitBorder(self):
    if (self.__player.x() <= self.__stage.left()
      or self.__player.x() >= self.__stage.right()
      or self.__player.y() <= self.__stage.bottom()
      or self.__player.y() >= self.__stage.top()):
        return True
    else:
      return False
      

# Main program
myGame = GreedyEater()
myGame.createStage(400, "Yellow")
myGame.addPlayer("turtle", "Red")
myGame.addGoals(20, "Blue")
myGame.start()

import turtle
import random
import math

class Stage:
  def __init__(self, w, c):
    sn = turtle.Screen()
    margin = 30
    sn.setup(w + margin, w + margin)
    sn.bgcolor(c)
    sn.tracer(10)
    
    # draw border of the stage
    t = turtle.Turtle()
    t.speed(9)
    t.penup()
    t.setposition(w / 2, w / 2)
    t.pendown()
    for _ in range(4):
      t.right(90)
      t.forward(w)
    t.hideturtle()
    self.__w = w
    
    pen = turtle.Turtle()
    pen.color("Red")
    pen.penup()
    pen.hideturtle()
    pen.setx(self.left() + 30)
    pen.sety(self.top() + 5)
    self.__pen = pen
  
  def top(self):
    return self.__w / 2
  def bottom(self):
    return 0 - self.__w / 2
  def left(self):
    return 0 - self.__w / 2
  def right(self):
    return self.__w / 2
  def width(self):
    return self.__w
  def writeScore(self, score):
    scoreText = "Score: " + str(score)
    self.__pen.clear()
    self.__pen.write(scoreText, False, "Left")
    
  
class Goal:
  def __init__(self, color, stage):
    t = turtle.Turtle()
    t.color(color)
    t.shape("circle")
    t.penup()
    t.speed(0)
    t.right(random.randint(0, 360))
    self.__t = t;
    self.__stage = stage
    self.reborn()
  
  def wander(self):
    x = self.__t.xcor()
    y = self.__t.ycor()
    if (x < self.__stage.left() + 10
      or x > self.__stage.right() - 10
      or y < self.__stage.bottom() + 10
      or y > self.__stage.top() - 10):
      self.__t.right(180)
    self.__t.forward(3)
    
  def isHitBy(self, player):
    x = self.__t.xcor()
    y = self.__t.ycor()
    dx = player.x() - x
    dy = player.y() - y
    distance = math.sqrt(dx * dx + dy * dy)
    return (distance < 20)
  
  def reborn(self):
    x = random.randint(self.__stage.left() + 10, self.__stage.right() - 10);
    y = random.randint(self.__stage.bottom() + 10, self.__stage.top() - 10);
    self.__t.setx(x)
    self.__t.sety(y)    
    
class EventReceiver:
  def __init__(self):
    sn = turtle.Screen()
    sn.onkey(self._onLeft, "Left")
    sn.onkey(self._onRight, "Right")
    sn.onkey(self._onUp, "Up")
    sn.onkey(self._onDown, "Down")
    sn.listen()

  def _onLeft(self):
    pass
  def _onRight(self):
    pass
  def _onUp(self):
    pass
  def _onDown(self):
    pass  

class Player(EventReceiver):
  def __init__(self, s, c):
    t = turtle.Turtle()
    t.shape(s)
    t.color(c)
    t.penup()
    self.__t = t
    self.__stepDistance = 5
    super().__init__()
    
  
  def move(self):
    self.__t.forward(self.__stepDistance)
    
  def x(self):
    return self.__t.xcor()
    
  def y(self):
    return self.__t.ycor()
    
  def turn(self, degree):
    self.__t.right(degree)
    
  def _onLeft(self):
    self.turn(-30)
    
  def _onRight(self):
    self.turn(30)
    
  def _onUp(self):
    if self.__stepDistance < 10:
      self.__stepDistance += 1
    
  def _onDown(self):
    if self.__stepDistance > 0:
      self.__stepDistance -= 1    
