#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

L = input("How many levels?\n")
if L < 2:
  print("Invalid number")
else:
  for x in range(0,L-1):
	print(" "*(L-x-1)+"/"+" "*(2*x)+"\\")
  print("/"+"_"*2*(L-1)+"\\")
