import sys

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

def displaycontent(d):
    print('\n\n')
    for x in d:
        print("Key: ", x)
    for x in d:
        print("Value: ", d[x])
    print(str(d))
    
displaycontent(d)

print("Goodbye.")
