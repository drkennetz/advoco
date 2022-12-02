from enum import IntEnum

player1_action = {
    "A": 1,
    "B": 2,
    "C": 3,
}

player2_action = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

round_end = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

def day2_1(infile):
    scores = 0
    with open(infile) as f:
        for line in f:
            player1, player2 = line.strip().split(" ")
            score = rps1(player1, player2)
            scores += score
    print(scores)
    return scores
            

def rps1(player1action, player2action):
    victories = {
        player1_action["A"]: player2_action["Z"], # rock beats scissors
        player1_action["B"]: player2_action["X"], # paper beats rock
        player1_action["C"]: player2_action["Y"] # scissors beats paper 
    }

    defeats = victories[player1_action[player1action]]
    if player1_action[player1action] == player2_action[player2action]:
        return player1_action[player1action] + 3
    elif player2_action[player2action] == defeats:
        return player2_action[player2action]
    else:
        return player2_action[player2action] + 6

def day2_2(infile):
    scores = 0
    with open(infile) as f:
        for line in f:
            player1, player2 = line.strip().split(" ")
            print(player1, player2)
            score = rps2(player1, player2)
            scores += score
    print(scores)
    return scores

def rps2(player1action, roundend):
    paths = {
        "lose": {"A": player2_action["Z"],
                "B": player2_action["X"],
                "C": player2_action["Y"]},
        "draw": {"A": player2_action["X"],
                "B": player2_action["Y"],
                "C": player2_action["Z"]},
        "win": {"A": player2_action["Y"],
                "B": player2_action["Z"],
                "C": player2_action["X"]},
    }
    round_result = round_end[roundend]
    dox = paths[round_result]
    necessary_evil = dox[player1action]
    if round_result == "win":
        return necessary_evil + 6
    elif round_result == "draw":
        return necessary_evil + 3
    elif round_result == "lose":
        return necessary_evil