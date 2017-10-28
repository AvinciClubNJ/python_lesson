mylist = [ ]
count = 2
for x in range(100,201):
    for i in range(2, x):
        if (x%i) == 0:
            break
        if i == x-1:
            mylist.append(x)
print(mylist)