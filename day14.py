from functools import reduce
from re import findall
from statistics import variance

W, H = 101, 103

def findBestTime(robots, velocities):
    def simulate(t):
        return [((sx + t*vx) % W, (sy + t*vy) % H) for (sx, sy), (vx, vy) in zip(robots, velocities)]
    bx, bxvar, by, byvar = 0, 10*100, 0, 10*1000
    for t in range(H):
        xs, ys = zip(*simulate(t))
        if (xvar := variance(xs)) < bxvar:
            bx, bxvar = t, xvar
        if (yvar := variance(ys)) < byvar:
            by, byvar = t, yvar
    t = bx + (pow(W, -1, H) * (by - bx)) % H * W
    return t

def findSafetyFactor(robots, velocities, t = 1):
    quadrants = {"upperLeft": 0, "upperRight": 0, "lowerLeft": 0, "lowerRight": 0}
    for (robotX, robotY), (robotVx, robotVy) in zip(robots, velocities):
        finalX = (robotX + robotVx * t) % W
        finalY = (robotY + robotVy * t) % H
        if finalX == 50 or finalY == 51:
            continue
        if 0 <= finalX <= 49:
            if 0 <= finalY <= 50:
                quadrants["upperLeft"] += 1
            elif 52 <= finalY <= 102:
                quadrants["lowerLeft"] += 1
        elif 51 <= finalX <= 100:
            if 0 <= finalY <= 50:
                quadrants["upperRight"] += 1
            elif 52 <= finalY <= 102:
                quadrants["lowerRight"] += 1
    return reduce(lambda x, y: x * y, quadrants.values(), 1)

robotPos, robotVel = [], []
with open("input.txt", "r") as F:
    regexp = r"p=(-?\d+),(-?\d+)\s*v=(-?\d+),(-?\d+)"
    for riga in F:
        numbers = findall(regexp, riga)
        robotPos.append((int(numbers[0][0]), int(numbers[0][1])))
        robotVel.append((int(numbers[0][2]), int(numbers[0][3])))
print(findBestTime(robotPos, robotVel))