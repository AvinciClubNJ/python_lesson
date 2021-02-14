
# store dictionary
store = {}

# routines:
def printMainMenu():
  print("Main menu:")
  print(" 1. Add item to store")
  print(" 2. Display all items")
  print(" 3. Exit")
  print("")

def chooseTask():
  strChoice = input("Please type your choice(1, 2 , 3): ")
  choice = 0
  if strChoice.isdigit():
    choice = int(strChoice)
  else:
    choice = -1
  return choice

def addItem():
  name = input("Please type item name: ")
  amount = 0
  while True:
    strAmount = input("Plesae type item amount: ")
    if strAmount.isdigit():
      amount = int(strAmount)
      break
    else:
      print("amount need to be a number.")
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
  if choice == 1:
    addItem()
    
  #Choice 2: print all items
  elif choice == 2:
    printAllItems()
  
  # Choice 3: Exit
  elif choice == 3:
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
    