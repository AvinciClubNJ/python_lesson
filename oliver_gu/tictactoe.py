#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys
import turtle
t = turtle.Turtle()
sn = turtle.Screen()
turn = "X"
uniwidth = 200

data = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

class Board:
  def __init__(self, w, c):
    sn = turtle.Screen()
    sn.bgcolor(c)
    sn.tracer(10)
    sn.setup(3.5 * w, 3.5 * w)
    t.speed(0)
    t.pensize(3)
    t.hideturtle()

    for x in range(4):
      t.pu()
      t.setpos(-3*w/2, -3*w/2 + w * x)
      t.pd()
      t.fd(3 * w)

    t.lt(90)
    for y in range(5):
      t.pu()
      t.setpos(-3*w/2 + w * y, -3*w/2)
      t.pd()
      t.fd(3 * w)

  def createBoard(self, w, c):
    self.__board = Board(w,c)

def changeData(pRow, pCol, shape):
  global turn
  if shape == "X":
      turn = "O"
  else:
      turn = "X"
  
  data[pRow][pCol] = shape
  checkWin()

def playerPosition(x, y):
  w = uniwidth
  if x > -3*w/2 and x < -w/2:
          outX = -w
          playerCol = 0
  elif x > -w/2 and x < w/2:
          outX = 0
          playerCol = 1
  elif x > w/2 and x < 3*w/2:
          outX = w
          playerCol = 2
      
  if y > -3*w/2 and y < -w/2:
          outY = -w
          playerRow = 2
  elif y > -w/2 and y < w/2:
          outY = 0
          playerRow = 1
  elif y > w/2 and y < 3*w/2:
          outY = w
          playerRow = 0
  return outX, outY, playerRow, playerCol

def playerShape(rawX, rawY):
  x, y, pRow, pCol = playerPosition(rawX, rawY)
  w = uniwidth
  if turn == "X":
    if data[pRow][pCol] == 0:
      t.pu()
      t.setpos(x - 2*w/5, y + 2*w/5)
      t.pd()
      t.setpos(x + 2*w/5, y - 2*w/5)
      t.pu()
      t.setpos(x - 2*w/5, y - 2*w/5)
      t.pd()
      t.setpos(x + 2*w/5, y + 2*w/5)
      t.pu()
      changeData(pRow, pCol, "X")
  elif data[pRow][pCol] == 0:
      t.setpos(x + 2*w/5, y)
      t.pd()
      t.circle(2*w/5)
      t.pu()
      changeData(pRow, pCol, "O")

def drawShape():
  sn.onscreenclick(playerShape)

def checkHor():
  for row in range(len(data)):
    for col in range(1, len(data[row])):
      if (data[row][col] != data[row][col - 1] or 
          data[row][col] == 0):
            break
    else:
      return True

def checkVer():
  for col in range(len(data)):
    for row in range(1, len(data)):
      if (data[row][col] != data[row - 1][col] or
          data[row][col] == 0):
            break
    else:
      return True

def checkTLBR():
  for rowcol in range(1, len(data)):
    if (data[rowcol][rowcol] != data[rowcol - 1][rowcol - 1] or
        data[rowcol][rowcol] == 0):
          break
  else:
    return True

def checkTRBL():
  for rowcol in range(1, len(data)):
    if (data[rowcol][len(data[rowcol]) - 1 - rowcol] != data[rowcol - 1][len(data[rowcol]) - rowcol] or
        data[rowcol][len(data[rowcol]) - 1 - rowcol] == 0):
          break
  else:
    return True

def checkTie():
  for row in range(len(data)):
    if all(data[row]) == False:
      break
  else:
    return True

def checkWin():
  if turn == "O":
    winner = "Player 1"
  else:
    winner = "Player 2"
  if checkHor():
    sys.exit(winner + " horizontal win")
  if checkVer():
    sys.exit(winner + " vertical win")
  if checkTLBR():
    sys.exit(winner + " diagonal win")
  if checkTRBL():
    sys.exit(winner + " diagonal win")
  if checkTie():
    sys.exit("Tie")

Board(uniwidth, "yellow")
drawShape()

input("Press ENTER to exit.\n")