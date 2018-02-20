#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import flesh

class Wuzi:
  # Constructor
  def __init__(self):
    self.data = []
    for boardSize in range(16):
      self.data.append([0] * 15)
  
  # Set white piece on location of 'row' and 'col'
  def setWhite(self, row, col):
    self.data[row][col] = "W"
    #print(self.data)

  # Set black piece on location of 'row' and 'col'
  def setBlack(self, row, col):
    self.data[row][col] = "B"
    #print(self.data)
  
  # Check whether location is empty 'row' and 'col'
  # Return:
  #   True - the location is empty
  #   False - the location is not empty
  def isEmpty(self, row, col):
    if self.data[row][col] == 0:
      return True
    else:
      return False
  
  def checkHor(row, col):
    horCount = 1
    if checkHorLeft(row, col):
      if checkHorRight(row, col):
        if horCount >= 5:
          return True
      else:
        return True
    else:
      return True

  def checkHorLeft(row, col):
    if horCount >= 5:
      #skip checkHorRight
      return False
    try:
      if data[row][col] == data[row][col - 1]:
          horCount += 1
          checkHorLeft(row, col - 1)
      else:
        #no more matches, go to checkHorRight
        return True
    except IndexError:
        #reached end of board, continue onto checkHorRight
        return True

  def checkHorRight(row, col):
    if horCount >= 5:
      #skip "if horCount >= 5" in checkHor
      return False
    try:
      if data[row][col] == data[row][col + 1]:
          horCount += 1
          checkHorRight(row, col + 1)
      else:
        #no more matches, return to checkHor and see if horCount >= 5
        return True
    except IndexError:
      #reached end of board, return to checkHor and see if horCount >= 5
      return True

  def checkVer(row, col):
    verCount = 1
    if checkVerDown(row, col):
      if checkVerUp(row, col):
        if verCount >= 5:
          return True
      else:
        return True
    else:
      return True

  def checkVerDown(row, col):
    if verCount >= 5:
      #skip checkVerUp
      return False
    try:
      if data[row][col] == data[row - 1][col]:
          verCount += 1
          checkVerDown(row - 1, col)
      else:
        #no more matches, go to checkVerUp
        return True
    except IndexError:
        #reached end of board, continue onto checkVerUp
        return True

  def checkVerUp(row, col):
    if verCount >= 5:
      #skip "if verCount >= 5" in checkVer
      return False
    try:
      if data[row][col] == data[row + 1][col]:
          verCount += 1
          checkVerUp(row + 1, col)
      else:
        #no more matches, return to checkVer and see if verCount >= 5
        return True
    except IndexError:
      #reached end of board, return to checkVer and see if verCount >= 5
      return True

  def checkTLBR(row, col):
    TLBRCount = 1
    if checkTLBRtl(row, col):
      if checkTLBRbr(row, col):
        if TLBRCount >= 5:
          return True
      else:
        return True
    else:
      return True

  def checkTLBRtl(row, col):
    if TLBRCount >= 5:
      #skip checkTLBRbr
      return False
    try:
      if data[row][col] == data[row - 1][col + 1]:
          TLBRCount += 1
          checkTLBRtl(row - 1, col + 1)
      else:
        #no more matches, go to checkTLBRbr
        return True
    except IndexError:
        #reached end of board, continue onto checkTLBRbr
        return True

  def checkTLBRbr(row, col):
    if TLBRCount >= 5:
      #skip "if TLBRCount >= 5" in checkTLBR
      return False
    try:
      if data[row][col] == data[row + 1][col - 1]:
          TLBRCount += 1
          checkTLBRbr(row + 1, col - 1)
      else:
        #no more matches, return to checkTLBR and see if TLBRCount >= 5
        return True
    except IndexError:
      #reached end of board, return to checkTLBR and see if TLBRCount >= 5
      return True

  def checkTRBL(row, col):
    TRBLCount = 1
    if checkTRBLtr(row, col):
      if checkTLBRbl(row, col):
        if TRBLCount >= 5:
          return True
      else:
        return True
    else:
      return True

  def checkTRBLtr(row, col):
    if TRBLCount >= 5:
      #skip checkTRBLbl
      return False
    try:
      if data[row][col] == data[row + 1][col + 1]:
          TRBLCount += 1
          checkTRBLtr(row + 1, col + 1)
      else:
        #no more matches, go to checkTRBLbl
        return True
    except IndexError:
        #reached end of board, continue onto checkTRBLbl
        return True

  def checkTRBLbl(row, col):
    if TRBLCount >= 5:
      #skip "if TRBLCount >= 5" in checkTRBL
      return False
    try:
      if data[row][col] == data[row - 1][col - 1]:
          TRBLCount += 1
          checkTRBLbl(row - 1, col - 1)
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
    if checkHor(row, col):
      return True
    elif checkVer(row, col):
      return True
    elif checkTLBR(row, col):
      return True
    elif checkTRBL(row, col):
      return True
    else:
      return None