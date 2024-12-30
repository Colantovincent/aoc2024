import time
def getDeterminant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def getPressAmount(matrixA, matrixB, coefficient):
    # Directly compute the values of aTimes and bTimes based on Cramer's rule
    A = getDeterminant(matrixA) / getDeterminant(coefficient)
    B = getDeterminant(matrixB) / getDeterminant(coefficient)
    if int(A) == A and int(B) == B:
        return int(A), int(B)
    else:
        return 0, 0

spentToken = 0
with open("input.txt", "r") as F:
    text = F.read().splitlines()
    for i in range(0, len(text), 4):
        righe = [text[i], text[i + 1], text[i + 2]]
        a, b, prize = righe[0].split(": ")[1].split(", "), righe[1].split(": ")[1].split(", "), righe[2].split(": ")[1].split(", ")
        a = (int(a[0][1:]), int(a[1][1:]))
        b = (int(b[0][1:]), int(b[1][1:]))
        prize = (10000000000000 + int(prize[0][2:]), 10000000000000 + int(prize[1][2:]))    
        aTimes, bTimes = getPressAmount(
            [[prize[0], b[0]], [prize[1], b[1]]],  
            [[a[0], prize[0]], [a[1], prize[1]]],  
            [[a[0], b[0]], [a[1], b[1]]]  
        )
        spentToken += aTimes * 3 + bTimes
print(spentToken)