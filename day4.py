
def wordSearch(puzzleInput: str) -> int:
    PAROLA = "XMAS"
    def controlla(posX: int, posY: int, direzione: tuple) -> bool:
        for i in range(4):
            currX, currY = posX + i * direzione[0], posY + i * direzione[1]
            if 0 <= currX < lunghezza and 0 <= currY < altezza:
                if PAROLA[i] != shallow[currX][currY]:
                    return False
            else:
                return False
        return True
    shallow = puzzleInput.splitlines()
    altezza = len(shallow)
    lunghezza = len(shallow[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    conta = 0
    for riga in range(altezza):
        for cella in range(lunghezza):
            for dirz in dirs:
                if controlla(riga, cella, dirz):
                    conta += 1
    return conta
def crossSearch(puzzleInput: str) -> int:
    PAROLA = "MAS"
    def controllaCroce(posX, posY):
        if 0 < posX < altezza - 1 and 0 < posY < lunghezza - 1:
            # Check the pattern at the four diagonal positions
            principale = shallow[posX - 1][posY - 1] + shallow[posX][posY] + shallow[posX + 1][posY + 1]
            secondaria = shallow[posX + 1][posY - 1] + shallow[posX][posY] + shallow[posX - 1][posY +1]
            if (principale == "MAS" or principale == "SAM") and (secondaria == "MAS" or secondaria == "SAM"):
                return True
        return False
    conta = 0
    shallow = puzzleInput.splitlines()
    altezza = len(shallow)
    lunghezza = len(shallow[0])
    for riga in range(altezza):
        for cella in range(lunghezza):
            if shallow[riga][cella] == "A":
                if controllaCroce(riga, cella):
                    conta += 1
    return conta
with open("input.txt", "r") as F:
    inputF = F.read()
print(crossSearch(inputF))