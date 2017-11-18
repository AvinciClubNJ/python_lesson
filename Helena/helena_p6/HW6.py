#!/usr/bin/env python
from dishlist import *
from random import *
def genListFromIngredients():
    ingredientes = {}
    while len(ingredientes) < 5:
        choice = int(input('Do you want to... \n\t1. Input item and amount\n\t2. Display stored items and amount\n\t3. Exit\n'))
        if choice == 1:
            item = input('Please input item\n')
            amount = int(input('Please input amount of ingredients\n'))
            ingredientes[item]=amount
            print()
        elif choice ==2 :
            print(ingredientes)
            print()
        elif choice == 3:
            break
        else:
            print('invalid input')

    for i in ingredientes:
        print('ingredientes : ', i,', amount: ',ingredientes[i])
    print('goodbye')
def genListFromMenu():
    print(meatList[randint(0,(len(meatList)-1))])
    print(vegeList[randint(0,(len(vegeList)-1))])

select = True
while select == True:
    userInput = input('Please enter your choice. \n\t1-Generate dish list from ingredients \n\t2-Generate dish list from menu\n')
    if userInput =='1':
        genListFromIngredients()
        break
    elif userInput == '2':
        genListFromMenu()
        break
    else:
        print('invalid input')
        continue
