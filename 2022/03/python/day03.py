def day3_1(infile: str) -> int:
    vals = []
    with open(infile) as f:
        for line in f:
            part1, part2 = halfer(line.strip())
            intersect = set(part1).intersection(set(part2)).pop()
            if intersect.islower():
                vals.append(ord(intersect) - 96)
            else:
                vals.append(ord(intersect) - 38)
    return sum(vals)

def halfer(line: str) -> tuple:
    n = len(line)
    half = int(n/2)
    return line[:half], line[n-half:]

def day3_2(infile: str) -> int:
    vals = []
    with open(infile) as f:
        lines = []
        for i, line in enumerate(f):
            line = line.strip()
            if i%3 == 0:
                if lines:
                    vals.append(lines)
                lines = []
            lines.append(line)
        if lines:
            vals.append(lines)

    final = []
    for strings in vals:
        common_char = get_intersection(strings)
        
        if common_char.islower():
            final.append(ord(common_char) - 96)
        else:
            final.append(ord(common_char) - 38)
    print(sum(final))
    return sum(final)
        

def get_intersection(strings: list) -> str:
    intersection = set(strings[0]) & set(strings[1]) & set(strings[2])
    return intersection.pop()