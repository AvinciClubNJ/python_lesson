#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

L = input("How many levels?")
if L < 2:
  print("Invalid number")
else:
  for x in range(0,L-1):
	print(" "*(L-x)+"/"+" "*(2*x)+"\\"+"\n")
  print("/"+"_"*2*L+"\\")
