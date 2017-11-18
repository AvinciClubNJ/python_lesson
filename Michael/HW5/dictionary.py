def dict_display(dict1):
    print("The keys are: ", dict1.keys())
    print("The values are: ", dict1.values())
    print("The dictionary contents are: ", dict1)
x = 0
dict1 = {} 
while x <= 5:
    y = int(input("You have three options. If you want to input the item and the amount, type 1. If you want to display the stored items and amount, type 2. If you want to exit, type 3. So, which one is it? "))
    if y == 1:
        z = raw_input("Type a string. This will be the item. ")
        xx = int(input("Type in a number. This will by your item amount. "))
        dict1[z] = xx
        x += 1
    elif y == 2:
        dict_display(dict1)
    elif y == 3: 
            dict_display(dict1)
            break
    else:
        print("Invalid number.")
dict_display(dict1)