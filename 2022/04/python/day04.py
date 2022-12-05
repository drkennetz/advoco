def day4(infile: str, part=1) -> int:
    total = 0
    with open(infile) as f:
        for line in f:
            ranges = line.strip().split(',')
            total += check_intervals(ranges[0], ranges[1], part=part)
    return total

def check_intervals(elf1: str, elf2: str, part:int = 1) -> int:
    elf1_x = elf1.split("-")
    elf1_range = range(int(elf1_x[0]), int(elf1_x[1])+1)
    elf2_x = elf2.split("-")
    elf2_range = range(int(elf2_x[0]), int(elf2_x[1])+1)
    elf1_set = set(elf1_range)
    elf2_set = set(elf2_range)
    if part == 1:
        if (len(elf1_set.difference(elf2_set)) == 0) or (len(elf2_set.difference(elf1_set)) == 0):
            return 1
        return 0
    if part == 2:
        if (len(elf1_set.intersection(elf2_set)) > 0):
            return 1
        return 0
        