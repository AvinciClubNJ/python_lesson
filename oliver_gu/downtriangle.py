#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

while True:
  try:
    L = input("How many levels?\n")
    if round(float(L)) < 2:
      print("Invalid number")
    else:
       print("_"*2*int(L))
       for x in range(0,int(L)):
        print(" "*(x)+"\\"+" "*2*(int(L)-1-x)+"/")
       break
  except ValueError:
    print("Please input a number.")