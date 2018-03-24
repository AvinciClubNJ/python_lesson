fin = open ('paint.in', 'r')
fout = open ('paint.out', 'w')
a,b = list(map(int, fin.readline().split()))
c,d = list(map(int, fin.readline().split()))

#fout.write (str(sum) + '\n')
x = 0
list1 = [a, b, c, d]
x = max(list1) - min(list1)
if a > d:
	x -= a-d
elif c > b:
	x -= c-b


fout.write (str(x) + '\n')

fout.close()
