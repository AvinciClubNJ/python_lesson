
def countGoldToPlatniumChanges():
    count = EndPositions[3] - BeginningPositions[3]
    return count

def countSilverToGoldChanges():
    count = EndPositions[2] - BeginningPositions[2] 
    return count

def countBronzeToSilverChanges():
    count = EndPositions[1] - BeginningPositions[1] 
    return count


# Main program
lines = []

with open("promote.in") as fInput:
    lines = fInput.readlines()

BeginningPositions = []
EndPositions = []
Changes = []
for _ in range(4):
    a , b = (int(x) for x in lines[_].split())
    BeginningPositions.append(a)
    EndPositions.append(b)




Changes.append(countBronzeToSilverChanges() + countSilverToGoldChanges() + countGoldToPlatniumChanges())
Changes.append(countSilverToGoldChanges() + countGoldToPlatniumChanges())
Changes.append(countGoldToPlatniumChanges())

with open("promote.out", 'w') as fOutput:
    for _ in range(3):
        fOutput.writelines(str(Changes[_]))
        fOutput.write('\n')

