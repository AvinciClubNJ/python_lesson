i = 10
x = 0
print ("_" * i)
while i != 0:
    triangle = (" " * x)+"\\"+(" " * (i-2)) + ("/")
    i -=2
    print (triangle)
    x +=1
