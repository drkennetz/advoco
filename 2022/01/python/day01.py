import sys

VALID_PARTS = [1, 2]

def day1(infile: str, part: int) -> int:
    cals = []
    with open (infile) as f:
        total = 0
        for line in f:
            line = line.strip()
            if line:
                total += int(line)
            else:
                cals.append(total)
                total = 0
        cals.append(total)
    if part == VALID_PARTS[0]:
        return max(cals)
    elif part == VALID_PARTS[1]:
        cals.sort()
        return sum(cals[-3:])
    else:
        raise ValueError("not a valid part")

    
