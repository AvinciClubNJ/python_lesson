#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from flesh import *
from brain import *

# Main game class
class WuziGame(Wuzi, EventReceiver):
  # Constructor
  def __init__(self):
    self.__board = Board()
    super().__init__()
  
  def _onAddPiece(self, row, col):
    if self.isEmpty(row, col):
      p = Piece(self.__currentPieceType)
      p.draw(row, col)
      if self.__currentPieceType == "B":
        self.setBlack(row, col)
        self.__currentPieceType = "W"
      else:
        self.setWhite(row, col)
        self.__currentPieceType = "B"
      
      win = self.checkWin(row, col)
      if win:
        if self.__currentPieceType == "B":
          print("White Won!")
          self.exit()
        else:
          print("Black Won!")
          self.exit()
  
  # Start the game
  #  Params:
  #   piectType - "B" - Black go first; "W" - White go first.
  def start(self, pieceType):
    self.__currentPieceType = pieceType
    self.listenEvents()

# Main program
myGame = WuziGame()
myGame.start("B")
