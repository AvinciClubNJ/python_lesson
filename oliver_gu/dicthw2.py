#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys

# store dictionary
store = {}

options = ("1", "2", "3", "one", "two", "three")

# routines:
def printMainMenu():
  print("Main menu:")
  print(" 1. Add item to store")
  print(" 2. Display all items")
  print(" 3. Exit")
  print("")

def chooseTask():
  while True:
    choice = input("Please type your choice(1, 2 , 3): ")
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
    
  #Choice 2: print all items
  elif str(choice) == "2" or str.casefold(str(choice)) == "two":
    printAllItems()
  
  # Choice 3: Exit
  elif str(choice) == "3" or str.casefold(str(choice)) == "three":
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