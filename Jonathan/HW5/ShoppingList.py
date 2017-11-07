personalDic= {}
def displayContent():
    print("<========================>") 
    print("Here are my store items: ")
    for item in personalDic:
        print("  " + item + " : " + str(personalDic[key]))
    print("<========================>") 
while True:
    while True:
        print("You can do the following: ")
        x = input("1. input your item and amount \n2. Display stored items and amount \n3. Exit\n")
        if x != "1" and x != "2" and x != "3":
            print ("Please Type in 1, 2, or 3")
            continue
        else: 
            break
    if int(x) == 1:
        key = input("What is the name of your item: ")
        value = 0
        while True:
            strValue = input("What is the value of your item: ")
            if strValue.isdigit():
                value = int(strValue)
                break
            else:
                print("It needs to be a number")
        personalDic[key] = value
    if int(x) == 3:
        displayContent()
        exit()
    if int(x) == 2:
        displayContent()
    if len(personalDic) == 5:
        print ("you have reached the limit!!")
        displayContent()
        break;