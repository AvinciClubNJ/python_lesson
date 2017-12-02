#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys

# store dictionary
store = {}

options = ("1", "2", "3", "4", "one", "two", "three", "four")

# routines:
def printMainMenu():
  print("Main menu:")
  print(" 1. Add item to store")
  print(" 2. Remove an item from store")  
  print(" 3. Display all items")
  print(" 4. Exit")
  print("")

def chooseTask():
  while True:
    choice = input("Please type your choice(1, 2 , 3, 4): ")
    if str.casefold(str(choice)) not in options:
      print("Please select an option.\n")
    else:
      return(choice)

def addItem():
  name = input("Please type item name: ")
  amount = 0
  while True:
    strAmount = input("Plesae type item amount: ")
    if strAmount.isdigit():
      amount = int(strAmount)
      break
    else:
      print("Amount needs to be a natural number.")
  store[name] = amount  
  print("")

def removeItem():
  delete = input("Please type item name to be removed: ")
  if delete in store:
    del store[delete]
    print("")
  else:
    print("Item requested is not in store.")
    print("")

def printAllItems():
  print("$$$$$$$$$$$$$$$$$$$$$$$$$")
  print("All items in store: ")
  for i in store:
    print("  " + i + ": " + str(store[i]))
  print("$$$$$$$$$$$$$$$$$$$$$$$$$")
  print("")

def isStoreFull():
  return (len(store) >= 5)

# Main program
while True:
  # Print main menu
  printMainMenu()
  
  # Get user's choice
  choice = chooseTask()
  
  # Choice 1: add item to store
  if str(choice) == "1" or str.casefold(str(choice)) == "one":
    addItem()

  #Choice 2: remove item from store
  if str(choice) == "2" or str.casefold(str(choice)) == "two":
    removeItem()

  #Choice 3: print all items
  elif str(choice) == "3" or str.casefold(str(choice)) == "three":
    printAllItems()
  
  # Choice 4: Exit
  elif str(choice) == "4" or str.casefold(str(choice)) == "four":
    print("Bye!")
    break
  
  # Other choices
  else:
    print("Please type a number between 1 and 3.")
    print("")
    continue
  
  # If store is full
  if isStoreFull():
    printAllItems()
    print("Store is full! Bye!")
    break