import sys

with open("milkorder.in", "r") as fin:
  lines = fin.readlines()

N, M, K = map(int, lines[0].strip().split())

print(lines)
print(N)
print(M)
print(K)

orders = list(map(int, lines[1].strip().split()))
print(orders)

positions = [0] * (N + 1)
print(positions)
for i in range(K):
  c, p = map(int, lines[i+2].strip().split())
  positions[p] = c

print(positions)

def solve():
  c1 = False
  holesOrders = 0
  lastJ = 1
  for i in range(0, M):
    if orders[i] == 1:
      c1 = True
    holesPos = 0
    j = lastJ
    firstHolePos = j
    while j < N+1:
      if i == 1 and j == 3:
        print("positions[j]=", positions[j], " orders[i]=", orders[i], " holesPos=", holesPos, " holesOrders=", holesOrders)
      if positions[j] == 0:
        holesPos += 1
        if holesPos == 1:
          firstHolePos = j
      elif positions[j] == orders[i]:
        if (holesPos > holesOrders and 1 not in orders) or c1 == True:
          return firstHolePos
        lastJ = j
        break
      j += 1
    if j == N+1:
      holesOrders += 1
    print("i=", i, " j=", j, " holesOrders=", holesOrders, " holesPos=", holesPos, " firstHolePos=", firstHolePos)
  return firstHolePos

count = solve()
print(count)

with open('milkorder.out', 'w') as fout:
  fout.write(str(count) + '\n')




