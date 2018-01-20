import sys

board = [[1, 0, 1],
         [1, 0, 1],
         [0, 0, 1]]

def checkHor():
  for row in range(len(board)):
    for col in range(1, len(board[row])):
      if (board[row][col] != board[row][col - 1] or 
          board[row][col] == 0):
            break
    else:
      return True

def checkVer():
  for col in range(len(board)):
    for row in range(1, len(board)):
      if (board[row][col] != board[row - 1][col] or
          board[row][col] == 0):
            break
    else:
      return True

def checkTLBR():
  for rowcol in range(1, len(board)):
    if (board[rowcol][rowcol] != board[rowcol - 1][rowcol - 1] or
        board[rowcol][rowcol] == 0):
          break
  else:
    return True

def checkTRBL():
  for rowcol in range(1, len(board)):
    if (board[rowcol][len(board[rowcol]) - 1 - rowcol] != board[rowcol - 1][len(board[rowcol]) - rowcol] or
        board[rowcol][len(board[rowcol]) - 1 - rowcol] == 0):
          break
  else:
    return True

def checkWin():
  if checkHor():
    sys.exit("horizontal win")
  if checkVer():
    sys.exit("vertical win")
  if checkTLBR():
    sys.exit("TLBR win")
  if checkTRBL():
    sys.exit("TRBL win")
  
checkWin()