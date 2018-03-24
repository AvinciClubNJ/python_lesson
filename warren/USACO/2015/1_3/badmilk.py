group = []
group2 = []
with open('badmilk.in', 'r') as fin:
    nums = list(map(int, fin.readline().split()))
    for x in range(nums[2]+nums[3]):
        if x < nums[2]:
            group.append(list(map(int, fin.readline().split())))
        else:
            group2.append(list(map(int, fin.readline().split())))
group = sorted(group)
group2 = sorted(group2)
print(group)
print(group2)
