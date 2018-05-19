fin = open ('speed_limits.in', 'r')
fout = open ('speed_limits.out', 'w')
n,m = list(map(int, fin.readline().split()))
dist_limit = []
speed_limit = []
for i in range(n):
  c,d = list(map(int, fin.readline().split()))
  dist_limit.append(c)
  speed_limit.append(d)
print("dist_limit=", dist_limit)
print("speed_limit=", speed_limit)

dist_bessie = []
speed_bessie = []
for i in range(m):
  c,d = list(map(int, fin.readline().split()))
  dist_bessie.append(c)
  speed_bessie.append(d)
print("dist_bessie=", dist_bessie)
print("speed_bessie=", speed_bessie)

#fout.write (str(sum) + '\n')
fout.close()

