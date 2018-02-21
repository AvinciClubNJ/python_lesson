#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import turtle
import tkinter as tk
import PIL as pillow
from PIL import Image
blackPiece = Image.open("go-black.gif")
whitePiece = Image.open("go-white.gif")

# Piece width
PIECE_WIDTH = 30
GAME_SIZE = 15

# helper function
# Translate x to column
def x2col(x):
  normX = (x + (PIECE_WIDTH / 2)) // PIECE_WIDTH  * PIECE_WIDTH
  col = (normX + PIECE_WIDTH * 9) // PIECE_WIDTH
  if col < 0:
    col = 0
  if col > GAME_SIZE:
    col = GAME_SIZE
  return int(col)

# Translate y to row
def y2row(y):
  normY = (y + (PIECE_WIDTH / 2)) // PIECE_WIDTH  * PIECE_WIDTH
  row = 0 - (normY - PIECE_WIDTH * 9) // PIECE_WIDTH
  if row < 0:
    row = 0
  if row > GAME_SIZE:
    row = GAME_SIZE
  return int(row)

# Translate col to X
def col2x(col):
  x = (col * PIECE_WIDTH) - PIECE_WIDTH * 9
  return x

# Translate row to Y
def row2y(row):
  y = PIECE_WIDTH * 9 - row * PIECE_WIDTH
  return y

# TicTacToe board class
class Board:
  # Constructor
  #   Params:
  #    size - board size. e.g 3, 5, 7...
  #    color - board color. e.g. 'green', 'blue'
  def __init__(self):
    margin = 30
    width = (GAME_SIZE - 1) * PIECE_WIDTH + margin * 2
    sn = turtle.Screen()
    sn.setup(width, width)
    sn.colormode(255)
    sn.bgcolor(229, 196 , 87)
    sn.addshape("go-black.gif")
    sn.addshape("go-white.gif")
    sn.tracer(3)
    
    bWidth = width - margin * 2
    startX = 0 - bWidth / 2
    startY = 0 - bWidth / 2
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()    
   
    # draw lines
    for i in range (GAME_SIZE):
      t.penup()      
      t.setpos(startX, startY + PIECE_WIDTH * i)
      t.pendown()      
      t.forward(bWidth)

    
    t.left(90)
    for j in range (GAME_SIZE):
      t.penup()
      t.setpos(startX + PIECE_WIDTH * j, startY)
      t.pendown()      
      t.forward(bWidth)
    
    # draw stars
    self._t = t
    self.__drawStar(5, 5)
    self.__drawStar(5, 9)
    self.__drawStar(5, 13)
    self.__drawStar(9, 5)
    self.__drawStar(9, 9)
    self.__drawStar(9, 13)
    self.__drawStar(13, 5)
    self.__drawStar(13, 9)
    self.__drawStar(13, 13)
    
    
  def __drawStar(self, row, col):
    x = col2x(col)
    y = row2y(row)
    
    self._t.penup()
    self._t.setpos(x, y)
    self._t.pendown()
    self._t.dot(8)  

# Tic tac toe piece class
class Piece:
  # Constructor
  #  Param:
  #   shape - piece shape. 'W'(white) or 'B'(black)
  def __init__(self, shape):
    self.__shape = shape
  
  # Draw piece on board
  #  Params:
  #    row, col - piece location
  def draw(self, row, col):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.setpos(col2x(col), row2y(row))
    if self.__shape == 'B' or self.__shape == 'b':
      t.shape("go-black.gif")
    else:
      t.shape("go-white.gif")
    t.stamp() 

# Event receiver class    
class EventReceiver:
  def __init__(self):
    pass
  
  # Start listen events
  def listenEvents(self):
    sn = turtle.Screen()
    sn.onclick(self.__onClick)
    sn.listen()
    self.__sn = sn
    turtle.mainloop()
    input("Listening...")

  # Add game piece event handler.
  # Subclass need override this method to draw game piece etc.
  #  Params:
  #   row, col - piece location
  def _onAddPiece(self, row, col):
    pass
  
  def __onClick(self, x, y):
    row = y2row(y)
    col = x2col(x)
    self._onAddPiece(row, col)

  # Unlisten event and exit
  def exit(self):
    self.__sn.onclick(None)
    raise SystemExit