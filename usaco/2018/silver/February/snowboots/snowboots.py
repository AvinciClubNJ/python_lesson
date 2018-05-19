import sys

fin = open('snowboots.in', 'r')
fout = open ('snowboots.out', 'w')

N, B = map(int, fin.readline().split())

listSteps = list(map(int, fin.readline().split()))
for i, step in enumerate(listSteps):
  print("i=", i, " step: ", step)

indexSteps = 0
result = 0
lenListSteps = len(listSteps)
for i in range(B):
  s, d = map(int, fin.readline().split())
  print("i=", i, " s=", s, " d=", d, " indexSteps=", indexSteps, " lenListSteps=", lenListSteps)
  if listSteps[indexSteps] > s:
    continue
  while True:
    found = False
    for j in range(indexSteps + d, indexSteps, -1):
      if j >= lenListSteps - 1:
        found = True
        result = i
        break
      print("j=", j, " step=", listSteps[j], " s=", s)
      if listSteps[j] <= s:
        indexSteps = j
        found = True
        break
    print("found =", found, " indexSteps=", indexSteps, " step=", listSteps[indexSteps], " result=", result)
    if indexSteps + d < len(listSteps):
      print("last step=", listSteps[indexSteps + d])
    if result != 0 or found == False:
      break

  if result != 0:
    break

fout.write(str(result) + '\n')

fout.close()
