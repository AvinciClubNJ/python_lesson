lines = []
with open("speeding.in") as fInput:
    lines = fInput.readlines()

# Get N and M
N, M = (int(x) for x in lines[0].split())

speedLimit = []
BessiesSpeed = []
maxSpeed = 0
addDis = 0

for _ in range(N):
    speedLimit.append([])
    distance, speed = (int(x) for x in lines[_+1].split())
    addDis+= distance
    speedLimit[_] = [addDis-distance, addDis, speed]

addDis = 0

for _ in range(M):
    BessiesSpeed.append([])
    distance, speed = (int(x) for x in lines[_ +1+N].split())
    addDis+= distance
    BessiesSpeed[_] = [addDis-distance, addDis, speed]

for _ in range(N):
    for e in range(M):
        if speedLimit[_][0] >= BessiesSpeed[e][1] or BessiesSpeed[e][0] >= speedLimit[_][1]:
            continue
        else:
            if speedLimit[_][2] < BessiesSpeed[e][2]:
                if BessiesSpeed[e][2] - speedLimit[_][2] > maxSpeed:
                    maxSpeed = BessiesSpeed[e][2]-speedLimit[_][2]

with open("speeding.out", 'w') as fOutput:
    fOutput.write(str(maxSpeed))