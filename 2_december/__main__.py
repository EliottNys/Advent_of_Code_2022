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

def main():
    input = read("input.txt")
    rounds = process(input)
    print(total(rounds))

if __name__=="__main__":
    main()

#answer : 13268