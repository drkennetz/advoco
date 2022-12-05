import re

def day5_1(infile: str) -> str:
    # stacks is a list of stacks
    # moves contains 3 items per entry - 
    # number of items to move, the source stack and the dest stack
    stacks, moves = parse_input(infile)
    for times, src, dest in moves:
        for _ in range(times):
            # since we are taking from stacks and adding to the end of another stack
            # we can just pop an item off one stack onto another stack
            stacks[dest - 1].append(stacks[src - 1].pop())
    return ''.join(s[-1] for s in stacks)

def day5_2(infile: str) -> str:
    stacks, moves = parse_input(infile)
    for times, src, dest in moves:
        # this one was easier
        # add src starting from times until the end to dest
        stacks[dest -1] += stacks[src - 1][-times:]
        # update src to trim those off
        stacks[src -1] = stacks[src - 1][:-times]
    return ''.join(s[-1] for s in stacks)

def parse_input(infile: str) -> tuple:
    stacks = []
    moves = []
    with open(infile) as f:
        for line in f:
            if '[' in line:
                for idx, column in enumerate(line):
                    if idx >= len(stacks):
                        stacks.append([])
                    # we only want letters
                    if column.isalpha():
                        stacks[idx].append(column)
            if 'move' in line:
                # we want lists of numbers
                moves.append(list(map(int, (re.findall(r'\d+', line)))))
    # because the input is so wonky, we can filter out empty stacks based on them having a len
    # this breaks if passed an empty starting stack...
    return [s[::-1] for s in filter(lambda l: len(l), stacks)], moves
