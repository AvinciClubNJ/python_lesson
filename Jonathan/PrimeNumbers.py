x = 100
y = range(2,x)
nonPrimeList = []
while x != 201:
    for e in y:
        if x % e == 0:
            nonPrimeList.append(x)
            break
    x += 1
    y = range(2, x)
allNumberList = list(range(100, 201))
list2 = []
for e in allNumberList:
    if e not in nonPrimeList:
        list2.append(e)
print(list2)
    

   

