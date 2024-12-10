DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def findTrailheads(topographicMap):
    trailheadsPositions = []
    for i in range(ROWS):
        for j in range(COLS):
            if topographicMap[i][j] == 0:
                trailheadsPositions.append((i, j))
    return trailheadsPositions

def findPath(currentPosition):
    posY, posX = currentPosition
    currentVal = lavaMap[posY][posX]
    if currentVal == 9:
        foundPaths.add((trailhead, (posY, posX)))
        return
    visited.add(currentPosition)
    for direction in DIRECTIONS:
        nextY = posY + 1 * direction[0]
        nextX = posX + 1 * direction[1]
        if 0 <= nextY < ROWS and 0 <= nextX < COLS and (nextY, nextX) not in visited:
            if lavaMap[nextY][nextX] == (currentVal + 1):
                findPath((nextY, nextX))
    visited.remove(currentPosition)

def findUniquePaths(currentPosition, totalRating: int):
    posY, posX = currentPosition
    currentVal = lavaMap[posY][posX]
    visited.add(currentPosition)
    if currentVal == 9:
        visited.clear()
        totalRating += 1
        return totalRating
    for direction in DIRECTIONS:
        nextY = posY + direction[0]
        nextX = posX + direction[1]
        if 0 <= nextY < ROWS and 0 <= nextX < COLS and (nextY, nextX) not in visited:
            if lavaMap[nextY][nextX] == currentVal + 1:
                totalRating = findUniquePaths((nextY, nextX), totalRating)
    return totalRating

def parseInput():
    mappedArea = []
    with open("./input.txt", "r") as F:
        rigaCurr = 0
        riga = F.readline().rstrip("\n")
        while riga != "":
            mappedArea.append([])
            for char in riga:
                #Piccolo extra per fare il parsing corretto degli esempi mostrati nel task. Basta aggiungere un numero non raggiungibile nei path
                if char == ".":
                    mappedArea[rigaCurr].append(324945)
                else:
                    mappedArea[rigaCurr].append(int(char))
            riga = F.readline().rstrip("\n")
            rigaCurr += 1
    return mappedArea

lavaMap = parseInput()
ROWS = len(lavaMap)
COLS = len(lavaMap[0])
trailheads = findTrailheads(lavaMap)
totalRating = 0
foundPaths = set()
for trailhead in trailheads:
    visited = set()
    totalRating = findUniquePaths(trailhead, totalRating)
print(totalRating)