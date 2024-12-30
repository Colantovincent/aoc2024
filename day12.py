DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def calculateRegions(plot: list) -> list:
    regions = []
    for i in range(righe):
        for j in range(colonne):
            startingElement = plot[i][j]
            if not visited[i][j]:
                currArea, currPerimeter = checkRegion((i, j), startingElement)
                regions.append((currArea, len(currPerimeter)))
    return regions

def calculateRegionsWithDiscount(plot: list) -> list:
    regions = []
    for i in range(righe):
        for j in range(colonne):
            startingElement = plot[i][j]
            if not visited[i][j]:
                currArea, currSides = checkRegionDiscount((i, j), startingElement)
                regions.append((currArea, currSides))
    return regions

def checkRegion(startPos, startVal):
    y, x = startPos
    area = 1
    perimeterPoints = []
    visited[y][x] = True
    for dy, dx in DIRECTIONS:
        newY = y + dy
        newX = x + dx
        if 0 <= newY < righe and 0 <= newX < colonne:
            if garden[newY][newX] == startVal and not visited[newY][newX]:
                newArea, newPerimeter = checkRegion((newY, newX), startVal)
                area += newArea
                perimeterPoints.extend(newPerimeter)
            elif garden[newY][newX] != startVal:
                if dy == 0:
                    perimeterPoints.append((y, x, dx))
                elif dx == 0:
                    perimeterPoints.append((y, x, dy))
        else:
            if dy == 0:
                perimeterPoints.append((y, x, dx))
            else:
                perimeterPoints.append((y, x, dy))
    return area, perimeterPoints

def checkRegionDiscount(startPos, startVal):
    def gridVal(y, x):
        if 0 <= y < len(garden) and 0 <= x < len(garden[0]):
            return garden[y][x]
        else:
            return ' '  # Out of bounds, treated as a boundary
    y, x = startPos
    area = 1
    corners = 0 
    visited[y][x] = True

    up = gridVal(y-1, x)
    down = gridVal(y+1, x)
    left = gridVal(y, x-1) 
    right = gridVal(y, x+1)  

    if up != startVal and left != startVal:
        corners += 1
    if up != startVal and right != startVal:
        corners += 1
    if down != startVal and left != startVal:
        corners += 1
    if down != startVal and right != startVal:
        corners += 1
    if gridVal(y-1, x-1) != startVal and up == startVal and left == startVal:
        corners += 1
    if gridVal(y-1, x+1) != startVal and up == startVal and right == startVal:
        corners += 1
    if gridVal(y+1, x+1) != startVal and down == startVal and right == startVal:
        corners += 1
    if gridVal(y+1, x-1) != startVal and down == startVal and left == startVal:
        corners += 1
        
    if up == startVal and not visited[y-1][x]:
        newArea, newCorners = checkRegionDiscount((y-1, x), startVal)
        area += newArea
        corners += newCorners
    if down == startVal and not visited[y+1][x]:
        newArea, newCorners = checkRegionDiscount((y+1, x), startVal)
        area += newArea
        corners += newCorners
    if left == startVal and not visited[y][x-1]:
        newArea, newCorners = checkRegionDiscount((y, x-1), startVal)
        area += newArea
        corners += newCorners
    if right == startVal and not visited[y][x+1]:
        newArea, newCorners = checkRegionDiscount((y, x+1), startVal)
        area += newArea
        corners += newCorners
    return area, corners

def gridVal(y, x):
    if 0 <= y < len(garden) and 0 <= x < len(garden[0]):
        return garden[y][x]
    else:
        return ' '  # Out of bounds, treated as a boundary
with open("input.txt", "r") as F:
    garden = []
    riga = F.readline().rstrip("\n")
    while riga != "":
        garden.append(list(riga))
        riga = F.readline().rstrip("\n")

righe, colonne = len(garden), len(garden[0])
visited = [[False for j in range(colonne)] for i in range(righe)]
regions = calculateRegionsWithDiscount(garden)
print(regions)
print(sum(a * c for a, c in regions))