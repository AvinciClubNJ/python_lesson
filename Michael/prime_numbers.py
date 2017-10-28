list1=[]
for x in range(100, 201):
    for y in range(2, x+1):
        if (x%y) == 0:
            break
    if y==x:
        list1.append(x)
print(list1)