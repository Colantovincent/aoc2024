from collections import defaultdict
def blink(stoneList: list) -> list:
    copy = []
    lunghezza = len(stoneList)
    for i in range(lunghezza):
        chars = len(stoneList[i])
        if stoneList[i] == "0":
            copy.append("1")
        elif  chars % 2 == 0:
            leftStone, rightStone = splitStone(stoneList[i], chars)
            copy.append(leftStone)
            copy.append(str(int(rightStone)))
        else:
            copy.append(str(int(stoneList[i]) * 2024))
    return copy

def splitStone(stone: str, length) -> tuple:
    return (stone[:length//2], stone[length//2:])

def simulateBlink(stones: defaultdict) -> defaultdict:
    tempStones = defaultdict(int)
    for stoneVal, stoneCount in stones.items():
        chars = len(str(stoneVal))
        if stoneVal == 0:
            tempStones[1] += stoneCount
        elif chars % 2 == 0:
            leftStone = int(str(stoneVal)[:chars // 2])
            rightStone = int(str(stoneVal)[chars // 2:])
            tempStones[leftStone] += stoneCount
            tempStones[rightStone] += stoneCount
        else:
            tempStones[stoneVal * 2024] += stoneCount
    return tempStones

with open("input.txt", "r") as F:
    stones = F.read()
    stones = stones.split()
stonesCopy = stones
for i in range(25):
    stonesCopy = blink(stonesCopy)
print(len(stonesCopy))
stoneDict = {}
for stone in stones:
    stoneDict[int(stone)] = 1
for i in range(75):
    stoneDict = simulateBlink(stoneDict)
print(sum(stoneDict.values()))