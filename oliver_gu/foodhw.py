#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys
sys.path.insert(0, '/Users/Xuemei/Avinci_Club/labs-master/python_lesson_sample/HW6')
from dishlist import *
import random

choices = ("1", "2", "3", "one", "two", "three")
userdict = dict()

def genListFromIngredients():
    while True:   
        choice2 = input("1. Input ingredient and amount\n2. Display stored ingredients and amount\n3. Exit\n")
        if str.casefold(str(choice2)) not in choices:
            print("Please select an option.\n")
            continue
        while str(choice2) == "1" or str.casefold(str(choice2)) == "one":
            ingredient = input("Please input an ingredient or enter \"e\" to exit.\n")
            if ingredient == "e" or ingredient == "E":
                break
            else:
                amount = input("Please input an amount or enter \"e\" to exit.\n")
                if amount == "e" or amount == "E":
                    break
                try:
                    y = float(amount)
                except ValueError:
                    print("Amount must be a number.\n")
                    continue
                else:
                    userdict[str(ingredient)] = float(amount)
                    print("You added " + amount + " amount of " + ingredient + "(s) to the catalog.\n")
                    if len(userdict) >= 5:
                        print("You have reached the maximum number of ingredients.\n")
                        for a,b in userdict.items():
                            print(a,b)
                        break
        if str(choice2) == "2" or str.casefold(str(choice2)) == "two":
            for a,b in userdict.items():
                print(a,b)
        if str(choice2) == "3" or str.casefold(str(choice2)) == "three":
            for a,b in userdict.items():
                print(a,b)
            break

def genListFromMenu():
    randmeat = random.randint(0,len(meatList) - 1)
    randvege = random.randint(0,len(vegelist) - 1)
    print(meatList[randmeat] + " and " + vegelist[randvege])

while True:
    choice1 = input("Please enter your choice or enter \"e\" to exit\n1. Generate dish list from ingredients\n2. Generate dish list from menu\n")
    if str.casefold(str(choice1)) == "e":
        sys.exit("Bye!")
    if str.casefold(str(choice1)) not in choices or str.casefold(str(choice1)) == "3" or str.casefold(str(choice1)) == "three":
        print("Please select an option.\n")
        continue
    while str(choice1) == "1" or str.casefold(str(choice1)) == "one":
        genListFromIngredients()
    if str(choice1) == "2" or str.casefold(str(choice1)) == "two":
        genListFromMenu()