a_num = ord('A') - 64

print(a_num)

fin = open("ride.in", "r")

lineone = fin.readline()
linetwo = fin.readline()

font = open("ride.out", "w")

sum = []
for e in range(len(lineone)):
    num = ord(lineone[e]) - 64
    sum.append(num)

for e in range(len(sum)-1):
    answerone = sum[e] * sum[e+1]

print(str(answerone))
