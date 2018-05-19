import sys

fin = open('reststops.in', 'r')
fout = open ('reststops.out', 'w')

L, N, rF, rB = map(int, fin.readline().split())

listTastyPoints = []
IndexTasty = 0
IndexPointDist = 1
for i in range(N):
  x, c = map(int, fin.readline().split())
  listTastyPoints.append([c, x])

listTastyPoints.sort(reverse=True)

prevPoint = 0
total = 0
for point in listTastyPoints:
  if point[IndexPointDist] > prevPoint:
    total += (rF - rB) * point[IndexTasty] * (point[IndexPointDist] - prevPoint)
    prevPoint = point[IndexPointDist]

fout.write(str(total) + '\n')

fout.close()
