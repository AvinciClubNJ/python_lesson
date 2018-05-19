fin = open ('paint.in', 'r')
fout = open ('paint.out', 'w')
a,b = list(map(int, fin.readline().split()))
c,d = list(map(int, fin.readline().split()))
print("a=", a, " b=", b, " c=", c, " d=", d)
sum = 10

fout.write (str(sum) + '\n')
fout.close()

