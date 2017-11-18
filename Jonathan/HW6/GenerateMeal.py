import random
#Use existing menu
vegelist = [
    "stir fry napa",
    "stir fry bok choy",
    "stir fry broccoli",
    "stir fry cauliflower",
    "stir fry mushroom",
    "sweet and sour sliced zucchini",
    "sweet and sour sliced locus root",
]

meatList = [
    "Shrimp tempura",
    "Sweet and sour shrimp",
    "Pecan shrimp",
    "Broccoli beef",
    "Baked beef ribs",
    "Beef rib stew",
    "Deep fried steak",
    "Curry potato beef",
    "Deep fried pork chop",
    "Pork meatball napa soup",
    "Bean curd pork ribs",
    "Sweet and sour pork ribs",
    "Sweet and sour chicken wing",
    "Baked chicken wing",
    "Yan-Ju chicken",
    "Steamed mushroom chicken",
    "Coca-Cola chicken",
    "Smoked chicken"
]
#Generate menu
def getListFromMenu():
    menu = [meatList[int(random.random()*len(meatList))],vegelist[int(random.random()*len(vegelist))]]
    return(menu)
#Generate new menu
def getListFromIngredients():
    personalDic= {}
    def displayContent():
        print("<========================>") 
        print("Here are your store items: ")
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
            break
        if int(x) == 2:
            displayContent()
        if len(personalDic) == 5:
            print ("you have reached the limit!!")
            displayContent()
            break

print("Do you want to use the existing menu, or a new one?\n")
newOrOldMenu = input(" N, n, or new for new menu -- E, e, or Existing for existing menu. \n ")
if newOrOldMenu == "N" or newOrOldMenu == "n" or newOrOldMenu == "new":
    getListFromIngredients()
    randomDishes == random.random()
elif newOrOldMenu == "E" or newOrOldMenu == "e" or newOrOldMenu =="Exisisting":
    print(getListFromMenu())
    

