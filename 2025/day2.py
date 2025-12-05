def silver(inizio: str, fine: str) -> list[int]:
    tot = []
    for i in range(int(inizio), int(fine) + 1):
        numstr = str(i)
        lung = len(numstr)
        if lung % 2 == 0:
            if numstr[0:lung // 2] == numstr[lung // 2:lung]:
                tot.append(i)
    return tot

def gold(inizio: str, fine: str) -> list[int]:
    tot = []
    for i in range(int(inizio), int(fine) + 1):
        numstr = str(i)
        doubled = (numstr * 2)
        if numstr in doubled[1: len(doubled) - 1]:
            tot.append(i)
    return tot

def parse_input(filename: str) -> list[str]:
    ranges = []
    with open(filename, "r") as f:
        string_representation = f.read()
        pairs = string_representation.split(",")
        for pair in pairs:
            single_range = pair.split("-")
            ranges.append(single_range)
    return ranges

if __name__ == "__main__":
    invalids = []
    rngs = parse_input("input.txt")
    print(rngs)
    for rng in rngs:
        invalids.extend(gold(rng[0], rng[1]))
    print(sum(invalids))
