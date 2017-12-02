#! /usr/bin/env python
import sys

d = {}
amount = 0
class Store:
    def __init__(self, storeCapacity):
        self.__storeCapacity = storeCapacity

    def getUserInput(self):
        while True:
            try:
                answer = int(input("Command Value: "))
            except ValueError:
                print("Not a number, Please enter an integer!")
                continue
            if answer > 4:
                print("Too large of a number, please enter a valid response.")
                continue
            if answer < 1:
                print('Too small of a number, please enter a valid response.')
                continue
            break
        return answer

    def additem(self):
        while True:
            newstring = input("Enter the name of the item: ")
            if newstring == '':
                print("Not valid!")
                continue
            break
        while True:
            try:
                newinterger = int(input("Please enter a value for the item: "))
            except ValueError:
                print("\nNot a number, Please enter an integer!\n")
                continue
            if newinterger == '':
                print("Not valid!")
                continue
            break
        d[newstring] = newinterger

    def viewitems(self):
        print(d)

    def quit(self):
        print("\nCurrent Dictionary:")
        print('', d, '')
        print("Exiting Program...")

    def delete(self, itemdelete):
        if itemdelete in d:
            del d[itemdelete]
            print("\nSucess!\n")
        else:
            print("\nNo Existing item\n")

    def isfull(self):
        if len(d) == self.__storeCapacity:
            return True
        
Store = Store(5)

while True:
    print("You can use these following commands:")
    print("1. Input item and amount\n2. Display stored items and amount\n3. Exit\n4. Delete an item")
    answer = Store.getUserInput()
    if answer == 1:
        Store.additem()
    if answer == 2:
        Store.viewitems()
    if answer == 3:
        Store.quit()
        break
    if answer == 4:
        Store.delete(input("Enter name of item: "))
    if Store.isfull() == True:
        print("\nCurrent Dictionary:")
        print('', d, '')
        print("Exiting Program...")
        break
print("Goodbye.\n")
