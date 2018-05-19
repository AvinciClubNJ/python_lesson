import sys

fin = open("hoofball.in", "r")
fout = open ('hoofball.out', 'w')

fin.readline()
listPosition = sorted(list(map(int, fin.readline().split())))

print(listPosition)

listStatus = []

#first always point to right
listStatus.append("right")

for i in range(1, len(listPosition) - 1):
  if listPosition[i] - listPosition[i-1] <= listPosition[i+1] - listPosition[i]:
    listStatus.append("left")
  else:
    listStatus.append("right")

#last always point to left
listStatus.append("left")

for i in range(len(listStatus)-1):
  if listStatus[i] == "right" and listStatus[i+1] == "left":
    listStatus[i] = "rightFinal"
    listStatus[i+1] = "leftFinal"

count = 0
if listStatus[0] == "right" and listStatus[1] == "rightFinal":
  count += 1
  listStatus[1] = "rightFinalDone"
for i in range(1, len(listStatus) - 1):
  if listStatus[i] == "leftFinal" and listStatus[i+1] == "left":
    count += 1
  elif listStatus[i] == "right" and listStatus[i+1] == "rightFinal":
    count += 1
    listStatus[i+1] = "rightFinalDone"
  elif listStatus[i] == "leftFinal" and listStatus[i-1] == "rightFinal":
    count += 1

if listStatus[-1] == "leftFinal" and listStatus[-2] == "rightFinal":
  count += 1
fout.write(str(count) + '\n')

fout.close()



