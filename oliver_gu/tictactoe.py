#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import turtle
t = turtle.Turtle()
sn = turtle.Screen()
turn = "X"

class Board:
  def __init__(self, w, c):
    sn = turtle.Screen()
    sn.bgcolor(c)
    sn.tracer(10)
    
    t.hideturtle()
    t.pensize(3)
    t.seth(270)
    t.speed(9)
    t.pu()
    t.setposition(-w / 6, w / 2)
    t.pd()
    t.forward(w)
    t.pu()
    t.setposition(w / 6, w / 2)
    t.pd()
    t.forward(w)
    t.pu()
    t.seth(0)
    t.setposition(-w / 2, w / 6)
    t.pd()
    t.forward(w)
    t.pu()
    t.setposition(-w / 2, -w / 6)
    t.pd()
    t.forward(w)
    t.pu()

class TictactoeGame:
  def __init__(self):
    #0 is empty, 1 is X, 2 is O
    self.__data = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
  
  def createBoard(self, w, c):
    self.__board = Board(w,c)

  def changeData(dx, dy, shape):
    print(shape, dx, dy)
    global turn
    if shape == "X":
        turn = "O"
    else:
        turn = "X"
    while True:
        if dy == 110:
            row = 0
            break
        if dy == -90:
            row = 1
            break
        if dy == -290:
            row = 2
            break
    while True:
        if dx == -200:
            self.__data[row][0] = shape
            break
        if dx == 0:
            self.__data[row][1] = shape
            break
        if dx == 200:
            self.__data[row][2] = shape
            break

  def playerPosition(x, y):
    if x > -300 and x < -100:
            outX = -200
    elif x > -100 and x < 100:
            outX = 0
    elif x > 100 and x < 300:
            outX = 200
        
    if y > -300 and y < -100:
            outY = -290
    elif y > -100 and y < 100:
            outY = -90
    elif y > 100 and y < 300:
            outY = 110
    return outX, outY

  def playerShape(rawX, rawY):
    if turn == "X":
        x, y = TictactoeGame.playerPosition(rawX, rawY)
        print(x, y)
        t.setpos(x - 60, y + 20)
        t.pd()
        t.setpos(x + 60, y + 140)
        t.pu()
        t.setpos(x - 60, y + 140)
        t.pd()
        t.setpos(x + 60, y + 20)
        t.pu()
        TictactoeGame.changeData(x, y, "X")
    else:
        x, y = TictactoeGame.playerPosition(rawX, rawY)
        print(x, y)
        t.setpos(x, y)
        t.pd()
        t.circle(80)
        t.pu()
        TictactoeGame.changeData(x, y, "O")

  def drawShape(self):
    sn.onscreenclick(TictactoeGame.playerShape)
  
  def checkWin(self):
    #horizontal win
    for row in range(3):
      for col in range(1, 3):
        if (self.__data[row][col] != self.__data[row][col-1] or 
         self.__data[row][col] == 0):
          break
        elif col == 2:
          return True
    #vertical win
    for col in range(3):
      for row in range(1, 3):
        if (self.__data[row][col] != self.__data[row-1][col] or
         self.__data[row][col] == 0):
          break
        elif row == 2:
          return True
    #diagonal top left to bottom right
    for rowcol in range(1, 3):
      if (self.__data[rowcol][rowcol] != self.__data[rowcol-1][rowcol-1] or
       self.__data[rowcol][rowcol] == 0):
        break
      elif col == 2:
        return True
    #diagonal bottom left to top right
    for row in range(1, -1, -1):
      for col in range(1, 3):
        if (self.__data[row][col] != self.__data[row+1][col-1] or
         self.__data[row][col] == 0):
          break
        elif col == 2:
          return True
    return False
  
  def input(self, val, row, col):
    if self.__data[row][col] == 0:
      self.__data[row][col] = val
  
myGame = TictactoeGame()
myGame.createBoard(600, "yellow")
myGame.drawShape()

input("Press ENTER to exit.")