def read(file_name):
    with open(file_name, "r") as file:
        contents = file.readlines()
    return contents

def process(input):
    for i,val in enumerate(input):
        input[i] = val.split()
    return input

def outcome(round):
    tie = {"A": "X", "B": "Y", "C" : "Z"}
    win = {"A": "Y", "B": "Z", "C" : "X"}
    if round[1] == tie[round[0]]:
        return 3
    elif round[1] == win[round[0]]:
        return 6
    else: return 0

def score(round):
    shape_points = {"X": 1, "Y": 2, "Z" : 3}
    return outcome(round) + shape_points[round[1]]

def total(rounds):
    total = 0
    for round in rounds:
        total += score(round)
    return total

def correct(rounds):    #brings the notation back to the previous understanding of the encryption (by calculating the necessary move)
    lose = {"A": "Z", "B": "X", "C" : "Y"}
    tie = {"A": "X", "B": "Y", "C" : "Z"}
    win = {"A": "Y", "B": "Z", "C" : "X"}
    for i,val in enumerate(rounds):
        if val[1] == "X":
            rounds[i][1] = lose[val[0]]
        elif val[1] == "Y":
            rounds[i][1] = tie[val[0]]
        else:
            rounds[i][1] = win[val[0]]
    return rounds


def main():
    input = read("input.txt")
    rounds = process(input)
    print(total(rounds))
    print(total(correct(rounds)))

if __name__=="__main__":
    main()

#answer : 13268 & 15508