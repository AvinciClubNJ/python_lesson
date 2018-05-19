"""
PROG: milk3
LANG: PYTHON3

"""
import sys

with open("milk3.in", "r") as fin:
  lines = fin.readlines()

buckets = list(map(int, lines[0].split()))
print(buckets)

contents = [0, 0, buckets[2]]
print(contents)

codes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

def findNext(i, cur, setProcessed):
  ret = []
  if cur[i] <= buckets[i]:
    if



def generateNextList(cur, setProcessed, setResult):
  nextList = []
  for i in range(3):
    nextList += findNext(i, cur, setProcessed)
  lenNext = len(nextList)
  for i in range(lenNext):
    if nextList[i][0] == 0:
      setResult.add(nextList[i][2])
    generateNextList(nextList[i], setProcessed, setResult)

setProcessed = set()
setResult = set()

def processBuckets(contents):
  
  

result = 0
with open('milk3.out', 'w') as fout:
  fout.write(str(result) + '\n')

