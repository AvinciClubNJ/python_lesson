fin = open ('paint.in' , 'r')
fout = open ('paint.out', 'w')
a, b = list(map(int, fin.readline().split()))
c,d = list(map(int, fin.readline().split()))

paintedSpace = b-a + d-c

if b >= d and d >= a and c <= a:
    paintedSpace -= (d-a)

elif d <= b and c >= a:
    paintedSpace -= (d-c)

elif b <= d and a >= c:
    paintedSpace -= (b-a)

elif b <= d and b >= c and a <= c:
    paintedSpace -= (b-c)

elif b == d and c == a:
    paintedSpace -= (b-a)

fout.write (str(paintedSpace) + '\n')
fout.close()
    
