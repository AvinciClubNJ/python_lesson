#!/usr/bin/env python
class Meal:
    def __init__(self):
        self.__store = {}
    def insert(self,name,amount):
        self.__store[name] = amount
    def print(self):
        for i in self.__store:
            print('ingredientes : ', i,', amount: ',self.__store[i])
    def delete(self,name):
        del self._store[name]
    def isFull(self):
        return(len(self.__store) > 5)

menu = Meal()
while menu.isFull() == False:
    choice = int(input('Do you want to... \n\t1. Input item and amount\n\t2. Display stored items and amount\n\t3. Delete an item\n\t4. Exit\n'))
    if choice == 1:
        item = input('Please input item\n')
        amount = int(input('Please input amount of ingredients\n'))
        menu.insert(item,amount)
    elif choice == 2:
        menu.print()
    elif choice == 3:
        menu.print()
        delete = input('Select an item to delete')
        menu.delete(delete)
    elif choice == 4:
        break
    else:
        print('invalid input')

menu.print()

