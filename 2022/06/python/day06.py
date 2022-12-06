def day6_1(infile: str) -> int:
    with open (infile) as f:
        line = f.readline()
        line = line.strip()
        for i in range(len(line)-4):
            tmp = [line[i], line[i+1], line[i+2], line[i+3]]
            settmp = set(tmp)
            if len(settmp) == 4:
                return i+4
    return 0

def day6_2(infile: str) -> int:
    with open (infile) as f:
        line = f.readline()
        line = line.strip()
        for i in range(len(line)-14):
            tmp = [line[i], line[i+1], line[i+2], line[i+3], line[i+4], line[i+5], line[i+6], line[i+7], line[i+8], line[i+9], line[i+10], line[i+11], line[i+12], line[i+13]]
            settmp = set(tmp)
            if len(settmp) == 14:
                return i+14
    return 0