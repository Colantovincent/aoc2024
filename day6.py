GUARDPOS = ["^", ">", "v", "<"]
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def getPatrolStep(mappedArea):
    altezza = len(mappedArea)
    lunghezza = len(mappedArea[0])
    outOfBounds = False
    def canMove(y, x, direction):
        nextY, nextX = y + DIRECTIONS[direction][0], x + DIRECTIONS[direction][1]
        if 0 <= nextY < altezza and 0 <= nextX < lunghezza:
            return mappedArea[nextY][nextX] != '#'
        else:
            nonlocal outOfBounds
            outOfBounds = True
            return False
    startPos = None
    for i in range(altezza):
        for j in range(lunghezza):
            if mappedArea[i][j] in GUARDPOS:
                startPos = (i, j, GUARDPOS.index(mappedArea[i][j]))
                break
        if startPos:
            break
    visitedPos = set()
    currY, currX, currDir = startPos
    while not outOfBounds:
        visitedPos.add((currY, currX))
        if canMove(currY, currX, currDir):
            currY += DIRECTIONS[currDir][0]
            currX += DIRECTIONS[currDir][1]
        else:
            currDir = currDir + 1 if currDir < 3 else 0
    return len(visitedPos)
def calculatePossibleObstacles(mappedArea):
    possibleObstacles = []
    altezza = len(mappedArea)
    lunghezza = len(mappedArea[0])
    def canMove(y, x, direction):
        nextY, nextX = y + DIRECTIONS[direction][0], x + DIRECTIONS[direction][1]
        if 0 <= nextY < altezza and 0 <= nextX < lunghezza:
            return mappedArea[nextY][nextX] != '#'
        else:
            nonlocal outOfBounds
            outOfBounds = True
            return False
    startPos = None
    for i in range(altezza):
        for j in range(lunghezza):
            if mappedArea[i][j] in GUARDPOS:
                startPos = (i, j, GUARDPOS.index(mappedArea[i][j]))
                break
        if startPos:
            break
    currY, currX, currDir = startPos
    startY, startX, startDir = startPos
    for i in range(altezza):
        for j in range(lunghezza):
            if mappedArea[i][j] == "." and (i, j) != (startPos[0], startPos[1]):
                mappedArea[i][j] = "#"
                visitedPositions = set()
                moved = False
                outOfBounds = False
                currY, currX, currDir = startY, startX, startDir
                while not outOfBounds:
                    if (currY, currX, currDir) in visitedPositions:
                        if moved:
                            possibleObstacles.append((currY, currX))
                            break
                        else:
                            moved = True
                    visitedPositions.add((currY, currX, currDir))
                    if canMove(currY, currX, currDir):
                        currY += DIRECTIONS[currDir][0]
                        currX += DIRECTIONS[currDir][1]
                    else:
                        currDir = (currDir + 1) % 4
                mappedArea[i][j] = "."
    return len(possibleObstacles)
with open("input.txt", "r") as F:
    patrolRoute = []
    riga = F.readline().rstrip("\n")
    while riga != "":
        patrolRoute.append(list(riga))
        riga = F.readline().rstrip("\n")
print(calculatePossibleObstacles(patrolRoute))