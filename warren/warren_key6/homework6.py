#! /usr/bin/env python
import sys
from random import *
from dishlist import *

def genListFromIngredients():
    d = {}
    amount = 0

    while True:
        print("You can use these following commands:")
        print("1. Input item and amount\n2. Display stored items and amount\n3. Exit ")
        while True:
            try:
                answer = int(input("Command Value: "))
            except ValueError:
                print("Not a number, Please enter an integer!")
                continue
            if answer > 3:
                print("Too large of a number, please enter a valid response.")
                continue
            if answer < 1:
                print('Too small of a number, please enter a valid response.')
                continue
            break

        if amount > 4:
            print("Hit the limit of items in the dictionary.")
            print(d)
            break
        
        if answer == 1:
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
            amount += 1
            d[newstring] = newinterger
        
        elif answer == 2:
            print(d)
        
        elif answer == 3:
            print(d)
            break

def genListFromMenu():
    print("Here is a dish from the meatList!")
    print(meatList[randint(0, len(meatList)-1)])
    print("Here is a dish from the vegeList")
    print(vegelist[randint(0, len(vegelist)-1)])

def checkinput(inputtext, usermax, answer):
    while True:
        try:
            userinput = int(input(inputtext))
        except ValueError:
            print("Not a valid integer")
            continue
        if answer == 'yes' or 'Yes':
            if userinput > int(usermax):
                print("Too large!")
                continue
        return userinput
        break
    
print("Please enter your choice.\n1-Generate dish list from ingredients\n2-Generate dish list from menu")

userinput = checkinput("Enter command: ", "2", 'yes')
if userinput == 1:
    genListFromIngredients()
if userinput == 2:
    genListFromMenu()