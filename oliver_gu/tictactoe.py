#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys
import turtle
t = turtle.Turtle()
sn = turtle.Screen()
turn = "X"

data = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

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

  def createBoard(self, w, c):
    self.__board = Board(w,c)

def changeData(dx, dy, shape):
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
          data[row][0] = shape
          #print("row: " + str(row) + " col: " + "0 shape:" + shape)
          checkWin()
          break
      if dx == 0:
          data[row][1] = shape
          #print("row: " + str(row) + " col: " + "1 shape:" + shape)
          checkWin()
          break
      if dx == 200:
          data[row][2] = shape
          #print("row: " + str(row) + " col: " + "2 shape:" + shape)
          checkWin()
          break

def playerPosition(x, y):
  if x > -300 and x < -100:
          outX = -200
          playerCol = 0
  elif x > -100 and x < 100:
          outX = 0
          playerCol = 1
  elif x > 100 and x < 300:
          outX = 200
          playerCol = 2
      
  if y > -300 and y < -100:
          outY = -290
          playerRow = 2
  elif y > -100 and y < 100:
          outY = -90
          playerRow = 1
  elif y > 100 and y < 300:
          outY = 110
          playerRow = 0
  return outX, outY, playerRow, playerCol

def playerShape(rawX, rawY):
  x, y, pRow, pCol = playerPosition(rawX, rawY)
  if turn == "X":
    if data[pRow][pCol] == 0:
      t.setpos(x - 60, y + 20)
      t.pd()
      t.setpos(x + 60, y + 140)
      t.pu()
      t.setpos(x - 60, y + 140)
      t.pd()
      t.setpos(x + 60, y + 20)
      t.pu()
      changeData(x, y, "X")
  elif data[pRow][pCol] == 0:
      t.setpos(x, y)
      t.pd()
      t.circle(80)
      t.pu()
      changeData(x, y, "O")

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

Board(600, "yellow")
drawShape()

input("Press ENTER to exit.\n")