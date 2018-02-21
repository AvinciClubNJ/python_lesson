#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from flesh import *

class Wuzi:
  # Constructor
  def __init__(self):
    self.data = []
    for boardSize in range(16):
      self.data.append([0] * 15)
  
  # Set white piece on location of 'row' and 'col'
  def setWhite(self, row, col):
    self.data[row][col] = "W"
    #print(*self.data, sep='\n')

  # Set black piece on location of 'row' and 'col'
  def setBlack(self, row, col):
    self.data[row][col] = "B"
    #print(*self.data, sep='\n')
  
  # Check whether location is empty 'row' and 'col'
  # Return:
  #   True - the location is empty
  #   False - the location is not empty
  def isEmpty(self, row, col):
    if self.data[row][col] == 0:
      return True
    else:
      return False
  
  def checkHor(self, row, col):
    global horCount
    horCount = 1
    if self.checkHorLeft(row, col):
      if self.checkHorRight(row, col):
        if horCount >= 5:
          print(horCount)
          return True
        else:
          return False
      else:
        return True
    else:
      return True

  def checkHorLeft(self, row, col):
    global horCount
    if horCount >= 5:
      #skip checkHorRight
      return False
    try:
      if self.data[row][col] == self.data[row][col - 1]:
          horCount += 1
          if self.checkHorLeft(row, col - 1):
            return True
      else:
        #no more matches, go to checkHorRight
        return True
    except IndexError:
        #reached end of board, continue onto checkHorRight
        return True

  def checkHorRight(self, row, col):
    global horCount
    if horCount >= 5:
      #skip "if horCount >= 5" in checkHor
      return False
    try:
      if self.data[row][col] == self.data[row][col + 1]:
          horCount += 1
          if self.checkHorRight(row, col + 1):
            return True
      else:
        #no more matches, return to checkHor and see if horCount >= 5
        return True
    except IndexError:
      #reached end of board, return to checkHor and see if horCount >= 5
      return True

  def checkVer(self, row, col):
    global verCount
    verCount = 1
    if self.checkVerDown(row, col):
      if self.checkVerUp(row, col):
        if verCount >= 5:
          return True
      else:
        return True
    else:
      return True

  def checkVerDown(self, row, col):
    global verCount
    if verCount >= 5:
      #skip checkVerUp
      return False
    try:
      if self.data[row][col] == self.data[row - 1][col]:
          verCount += 1
          if self.checkVerDown(row - 1, col):
            return True
      else:
        #no more matches, go to checkVerUp
        return True
    except IndexError:
        #reached end of board, continue onto checkVerUp
        return True

  def checkVerUp(self, row, col):
    global verCount
    if verCount >= 5:
      #skip "if verCount >= 5" in checkVer
      return False
    try:
      if self.data[row][col] == self.data[row + 1][col]:
          verCount += 1
          if self.checkVerUp(row + 1, col):
            return True
      else:
        #no more matches, return to checkVer and see if verCount >= 5
        return True
    except IndexError:
      #reached end of board, return to checkVer and see if verCount >= 5
      return True

  def checkTLBR(self, row, col):
    global TLBRCount
    TLBRCount = 1
    if self.checkTLBRtl(row, col):
      if self.checkTLBRbr(row, col):
        if TLBRCount >= 5:
          return True
      else:
        return True
    else:
      return True

  def checkTLBRtl(self, row, col):
    global TLBRCount
    if TLBRCount >= 5:
      #skip checkTLBRbr
      return False
    try:
      if self.data[row][col] == self.data[row - 1][col + 1]:
          TLBRCount += 1
          if self.checkTLBRtl(row - 1, col + 1):
            return True
      else:
        #no more matches, go to checkTLBRbr
        return True
    except IndexError:
        #reached end of board, continue onto checkTLBRbr
        return True

  def checkTLBRbr(self, row, col):
    global TLBRCount
    if TLBRCount >= 5:
      #skip "if TLBRCount >= 5" in checkTLBR
      return False
    try:
      if self.data[row][col] == self.data[row + 1][col - 1]:
          TLBRCount += 1
          if self.checkTLBRbr(row + 1, col - 1):
            return True
      else:
        #no more matches, return to checkTLBR and see if TLBRCount >= 5
        return True
    except IndexError:
      #reached end of board, return to checkTLBR and see if TLBRCount >= 5
      return True

  def checkTRBL(self, row, col):
    global TRBLCount
    TRBLCount = 1
    if self.checkTRBLtr(row, col):
      if self.checkTRBLbl(row, col):
        if TRBLCount >= 5:
          return True
      else:
        return True
    else:
      return True

  def checkTRBLtr(self, row, col):
    global TRBLCount
    if TRBLCount >= 5:
      #skip checkTRBLbl
      return False
    try:
      if self.data[row][col] == self.data[row + 1][col + 1]:
          TRBLCount += 1
          if self.checkTRBLtr(row + 1, col + 1):
            return True
      else:
        #no more matches, go to checkTRBLbl
        return True
    except IndexError:
        #reached end of board, continue onto checkTRBLbl
        return True

  def checkTRBLbl(self, row, col):
    global TRBLCount
    if TRBLCount >= 5:
      #skip "if TRBLCount >= 5" in checkTRBL
      return False
    try:
      if self.data[row][col] == self.data[row - 1][col - 1]:
          TRBLCount += 1
          if self.checkTRBLbl(row - 1, col - 1):
            return True
      else:
        #no more matches, return to checkTRBL and see if TRBLCount >= 5
        return True
    except IndexError:
      #reached end of board, return to checkTRBL and see if TRBLCount >= 5
      return True
  
  # Check whether there's any side win
  # Return:
  #   'W' - White win
  #   'B' - Black win
  #   None - no body win
  def checkWin(self, row, col):
    if self.checkHor(row, col):
      return True
    elif self.checkVer(row, col):
      return True
    elif self.checkTLBR(row, col):
      return True
    elif self.checkTRBL(row, col):
      return True
    else:
      return None