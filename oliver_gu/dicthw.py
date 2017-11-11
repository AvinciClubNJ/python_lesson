#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import sys
choices = ("1", "2", "3", "one", "two", "three")
userdict = dict()

while True:   
    x = input("1. Input item and amount\n2. Display stored items and amount\n3. Exit\n")
    if str.casefold(str(x)) not in choices:
        print("Please select an option.\n")
        continue
    while str(x) == "1" or str.casefold(str(x)) == "one":
        item = input("Please input an item or enter \"e\" to exit.\n")
        if item == "e" or item == "E":
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
                userdict[str(item)] = float(amount)
                print("You added " + amount + " amount of " + item + "(s) to the catalog.\n")
                if len(userdict) >= 5:
                    print("You have reached the maximum number of items.\n")
                    for a,b in userdict.items():
                        print(a,b)
                    sys.exit("Bye!")
    if str(x) == "2" or str.casefold(str(x)) == "two":
        for a,b in userdict.items():
            print(a,b)
    if str(x) == "3" or str.casefold(str(x)) == "three":
        for a,b in userdict.items():
            print(a,b)
        sys.exit("Bye!")