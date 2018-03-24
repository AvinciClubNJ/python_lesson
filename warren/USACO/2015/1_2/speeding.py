should = []
actual = []
a = []
b = []
final = []
with open('speeding.in', 'r') as fin:
    nums = list(map(int, fin.readline().split()))
    for x in range(nums[0]):
        should.append(list(map(int, fin.readline().split())))
    for x in range(nums[1]):
        actual.append(list(map(int, fin.readline().split())))
fout = open('speeding.out', 'w')
for x in range(len(should)):
    for y in range(should[x][0]):
        a.append(should[x][1])
for x in range(len(actual)):
    for y in range(actual[x][0]):
        b.append(actual[x][1])
for x in range(100):
    final.append(b[x]-a[x])
if max(final) < 0:
    print(0, file=fout)
else:
    print(max(final), file=fout)
fout.close()
