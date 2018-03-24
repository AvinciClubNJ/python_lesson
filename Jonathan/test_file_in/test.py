fin = open("mytestfile.in", 'r')

lineone = fin.readline()
linetwo = fin.readline()

print(lineone)
print(linetwo)

fin.close()

fout = open("mytestfile.out", "w")

lines1 = fout.writelines([lineone,linetwo]) 

print(lines1)

fout.close()

