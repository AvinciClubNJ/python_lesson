#! /usr/bin/env python
import sys

d = {}
amount = 0

def printmainmenu():
    print("You can use these following commands:")
    print("1. Input item and amount\n2. Display stored items and amount\n3. Exit ")

def getUserInput():
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
    return answer

def doinput1():
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

def doinput2():
    print('', d, '')

def doinput3():
    print("\nCurrent Dictionary:")
    print('', d, '')
    print("Exiting Program...")

def checkamount():
    return (len(d))
#Main Program
while True:
    printmainmenu()
    answer = getUserInput() #Get the user's input
    if answer == 1:
        doinput1() #Add item to dictionary
    elif answer == 2:
        doinput2() #View dictionary
    elif answer == 3:
        doinput3() #Stop loop
        break
    amount = checkamount()
    if amount > 4:
        print("\nHit the limit of items in the dictionary.")
        doinput3()
        break

print("Goodbye.\n")
