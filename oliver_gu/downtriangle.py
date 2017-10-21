#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

L = input("How many levels?\n")
if L < 2:
  print("Invalid number")
else:
  print("_"*2*(L))
  for x in range(0,L):
	print(" "*(x)+"\\"+" "*2*(L-1-x)+"/")