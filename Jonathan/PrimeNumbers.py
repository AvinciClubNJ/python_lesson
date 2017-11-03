def getPrimeNumber(start, end):
    x = start
    y = range(2,x)
    nonPrimeList = []
    while x != end + 1:
        for e in y:
            if x % e == 0:
                nonPrimeList.append(x)
                break
        x += 1
        y = range(2, x)
    allNumberList = list(range(start, end + 1))
    list2 = []
    for e in allNumberList:
        if e not in nonPrimeList:
            list2.append(e)
    return list2

            
for e in range(3):
    i = int(input("What is your start?"))
    l = int(input("What is your end?"))
    print(getPrimeNumber(i, l))  

   

