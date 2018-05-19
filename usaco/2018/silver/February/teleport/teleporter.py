import sys

fin = open("teleport.in", "r")
fout = open ('teleport.out', 'w')

N = int(fin.readline())

listPointA =[[], []]
listPointB = [[], []]
listPointDoneB = [[], []]

totalSegmentsSize = 0
for i in range(N):
  a, b = map(int, fin.readline().split())
  totalSegmentsSize += abs(a-b)
  tmp = 2*a
  if a > b and b < 0:
    if a > 0:
      listPointA[0].append(0)
      listPointB[0].append(b)
      listPointDoneB[0].append(2*b)
    elif b < tmp:
      listPointA[0].append(tmp)
      listPointB[0].append(b)
      listPointDoneB[0].append(2*b - tmp)
  elif a < b and b > 0:
    tmp = 2*a
    if a < 0:
      listPointA[1].append(0)
      listPointB[1].append(b)
      listPointDoneB[1].append(2*b)
    elif b > tmp:
      listPointA[1].append(tmp)
      listPointB[1].append(b)
      listPointDoneB[1].append(2*b - tmp)

listPointA[0].sort(reverse=True)
listPointB[0].sort(reverse=True)
listPointDoneB[0].sort(reverse=True)
listPointA[1].sort()
listPointB[1].sort()
listPointDoneB[1].sort()

#print("Negative listPointA: ", listPointA[0])
#print("Negative listPointB: ", listPointB[0])
#print("Positive listPointA: ", listPointA[1])
#print("Positive listPointB: ", listPointB[1])
#print("totalSegmentsSize=", totalSegmentsSize)

resultSavings = 0
for pointAs, pointBs, pointDoneBs in zip(listPointA, listPointB, listPointDoneB):
  savingsAggregated = 0
  countIncrease = 0
  countDecrease = 0
  indexA = 0
  indexB = 0
  indexDoneB= 0
  prevPoint = 0
  while indexA < len(pointAs) or indexB < len(pointBs):
    compensateLastDecrease = 0
    if indexA < len(pointAs) and indexB < len(pointBs) and indexDoneB < len(pointDoneBs) and abs(pointAs[indexA]) < abs(pointBs[indexB]):
      #print("1st indexA=", indexA, " pointA=", pointAs[indexA], " indexB=", indexB, " PointB=", pointBs[indexB], " indexDoneB=", indexDoneB, "PointDoneB=", pointDoneBs[indexDoneB], " prevPoint=", prevPoint, " countDecrease=", countDecrease)
      while indexDoneB < len(pointDoneBs) and abs(pointAs[indexA]) > abs(pointDoneBs[indexDoneB]):
        #print("1st popping indexDoneB=", indexDoneB, "PointDoneB=", pointDoneBs[indexDoneB])
        compensateLastDecrease += abs(pointDoneBs[indexDoneB] - prevPoint)
        if countDecrease == 0:
          print("ERROR! countDecrease is to be -1")
        countDecrease -= 1
        indexDoneB += 1
      
      savingsAggregated += abs(prevPoint - pointAs[indexA]) * (countIncrease - countDecrease) - compensateLastDecrease
      #print("1st savingsAggregated=", savingsAggregated, " indexA=", indexA, " pointA=", pointAs[indexA], " indexB=", indexB, " PointB=", pointBs[indexB], " indexDoneB=", indexDoneB, "PointDoneB=", pointDoneBs[indexDoneB], " prevPoint=", prevPoint, " countDecrease=", countDecrease, " countIncrease=", countIncrease, " compensateLastDecrease=", compensateLastDecrease)
      prevPoint = pointAs[indexA]
      indexA += 1
      countIncrease += 1
    else:
      #print("2nd indexB=", indexB, " PointB=", pointBs[indexB], " indexDoneB=", indexDoneB, "PointDoneB=", pointDoneBs[indexDoneB], " prevPoint=", prevPoint, " countDecrease=", countDecrease)
      while indexB > indexDoneB and abs(pointBs[indexB]) > abs(pointDoneBs[indexDoneB]):
        #print("2nd popping indexDoneB=", indexDoneB, "PointDoneB=", pointDoneBs[indexDoneB])
        compensateLastDecrease += abs(pointDoneBs[indexDoneB] - prevPoint)
        if countDecrease == 0:
          print("ERROR! countDecrease is to be -1")
        countDecrease -= 1
        indexDoneB += 1
      savingsAggregated += abs(prevPoint - pointBs[indexB]) * (countIncrease - countDecrease) - compensateLastDecrease
      #print("2nd savingsAggregated=", savingsAggregated, " indexB=", indexB, " PointB=", pointBs[indexB], " indexDoneB=", indexDoneB, " prevPoint=", prevPoint, " countDecrease=", countDecrease, " countIncrease=", countIncrease, " compensateLastDecrease=", compensateLastDecrease)
      prevPoint = pointBs[indexB]
      indexB += 1
      countDecrease += 1
      countIncrease -= 1
    if resultSavings < savingsAggregated:
      resultSavings = savingsAggregated

    #print("resultSavings=", resultSavings)
"""

# Design 1&2 Common
#following 2 lists: index 0 for negative, index 1 for positive
listPoints = [[], []]
listSegments = [[], []]

totalSegmentsSize = 0
for i in range(N):
  a, b = map(int, fin.readline().split())
  totalSegmentsSize += abs(a-b)
  if a > b:
    #Segments pointing negative
    if b < 0:
      #only consider overlapping segments with negative y
      listPoints[0].append(b)
      listSegments[0].append([a, b])
    if a < 0:
      listPoints[0].append(a)
  elif a < b:
    if b > 0:
      listPoints[1].append(b)
      listSegments[1].append([a, b])
    if a > 0:
      listPoints[1].append(a)

setPoints = [[], []]
for i in range(len(listPoints)):
  setPoints[i] = sorted(set(listPoints[i]))
for segments in listSegments:
  segments.sort()

setPoints[1] = setPoints[1][::-1]
listSegments[1] = listSegments[1][::-1]

resultSavings = 0
recordY = 0

print("setPoints[0]: ", setPoints[0])
print("listSegments[0]: ", listSegments[0])

# Design 1
indexSegments = 0
for y in setPoints[0]:
# y < 0
  savingsAggregated = 0
  for i in range(indexSegments, len(listSegments[0])):
    a, b = listSegments[0][i]
    if y >= a:
      indexSegments += 1
      #print("indexSegments=", indexSegments, " y=", y, " a=", a, " b=", b)
    tempB2A = b - a
    if a > 0:
      if y<= 2*b:
        #print("index0 skip1 y=", y, " a=", a, " b=", b, " tempB2A=", tempB2A)
        continue
      else:
        if y > b:
          savingsAggregated -= y
          #print("index0a y=", y, " a=", a, " b=", b, " savings=", -y, " savingsAggregated=", savingsAggregated)
        else:
          savingsAggregated += y - 2*b # -b - (b - y)
          #print("index0b y=", y, " a=", a, " b=", b, " savings=", y - 2*b, " savingsAggregated=", savingsAggregated)
    else:
      if b >= 2*a or y <= 2*tempB2A or y > a:
        #print("index0 skip2 y=", y, " a=", a, " b=", b, " tempB2A=", tempB2A)
        continue
      else: # a < 0
        if y > b:
          savingsAggregated += 2*a - y 
          #print("index0c y=", y, " a=", a, " b=", b, " savings=", 2*a - y, " savingsAggregated=", savingsAggregated)
        else:
          savingsAggregated += 2*(-tempB2A) + y # a - b - (-a  + b - y)
          #print("index0d y=", y, " a=", a, " b=", b, " savings=", 2*(-tempB2A) + y, " savingsAggregated=", savingsAggregated)
  if savingsAggregated > resultSavings:
    resultSavings = savingsAggregated
    recordY = y
        
indexSegments = 0
for y in setPoints[1]:
# y < 0
  savingsAggregated = 0
  for i in range(indexSegments, len(listSegments[1])):
    a, b = listSegments[1][i]
    if y <= a:
      indexSegments += 1
      #print("indexSegments=", indexSegments, " y=", y, " a=", a, " b=", b)
    tempB2A = b - a
    if a < 0:
      if y>= 2*b:
        continue
      else:
        if y < b:
          savingsAggregated += y
        else:
          savingsAggregated += 2*b - y
    else:
      if b <= 2*a or y >= 2*tempB2A or y < a:
        continue
      else:
        if y < b:
          savingsAggregated += y - 2*a
        else:
          savingsAggregated += 2*(tempB2A) - y # b - a - (a  + y - b)
    #print("index1 y=", y, " a=", a, " b=", b, " savingsAggregated=", savingsAggregated)
  if savingsAggregated > resultSavings:
    resultSavings = savingsAggregated
    recordY = y

# Design 2
for points, segments in zip(setPoints, listSegments):
  indexSegments = 0
  for y in points:
    savingsAggregated = 0
    for i in range(indexSegments, len(segments)):
      a, b = segments[i]
      if y < 0 and y >= a or y > 0 and y <= a:
        indexSegments += 1
        #print("indexSegments=", indexSegments, " y=", y, " a=", a, " b=", b)
      combined = abs(max([a, b, 0, y]) - min([a, b, 0, y]))
      segment = abs(a-b)
      teleport = abs(y)
      overlap = teleport + segment - combined
      nonOverlapInY = teleport - overlap
      if overlap == teleport:
        savingsAggregated +=teleport 
        print("savingsAggregated= ", savingsAggregated, " savings1=", teleport, " a=", a, " b=", b, " y=", y, " overlap=", overlap, " teleport=", teleport, " nonOverlapInY=", nonOverlapInY)
      elif nonOverlapInY < overlap:
        savingsAggregated += overlap - nonOverlapInY
        print("savingsAggregated= ", savingsAggregated, " savings2=", overlap - nonOverlapInY, " a=", a, " b=", b, " y=", y, " overlap=", overlap, " teleport=", teleport, " nonOverlapInY=", nonOverlapInY)
    print("Sum savings= ", savingsAggregated, " resultsSavings=", resultSavings, " y=", y)
    if savingsAggregated > resultSavings:
      resultSavings = savingsAggregated
      recordY = y
"""

result = totalSegmentsSize - resultSavings
#print("result=", result, " totalSegmentsSize=", totalSegmentsSize, " resultSavings=", resultSavings)

fout.write(str(result) + '\n')

fout.close()

