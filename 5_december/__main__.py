import re
def read(file_name):
    with open(file_name, "r") as file:
        contents = file.readlines()
    for i,val in enumerate(contents):
        contents[i] = val.replace("\n", "")
    return contents

def highest_stack(input):
    for i,line in enumerate(input):
        if line[1] == "1":
            return i

def find_crates(line):
    crates = line.split()
    iter = re.finditer(r"\[[A-Z]\]", line)
    corresponding_stacks = [m.start(0)//4 for m in iter]
    return crates, corresponding_stacks

def process(input):
    width = len(input[0])//4 + 1
    height = highest_stack(input)
    stacks = [ [] for _ in range(width) ]
    iterator = height
    while iterator > 0:
        crates, corresponding_stacks = find_crates(input[iterator-1])
        for i,crate in enumerate(crates):
            stacks[corresponding_stacks[i]].append(crate)
        iterator -= 1
    moves = []
    for i in range(height+2, len(input)):
        move = re.findall("\d+", input[i])
        moves.append([int(x) for x in move])
    return stacks, moves

def apply_move(stacks, move):
    for _ in range(move[0]):
        stacks[move[2]-1].append(stacks[move[1]-1].pop())
    return stacks

def apply_move_9001(stacks, move):
    intermediary = []
    for _ in range(move[0]):
        intermediary.append(stacks[move[1]-1].pop())
    for _ in range(move[0]):
        stacks[move[2]-1].append(intermediary.pop())
    return stacks

def apply_moves(stacks, moves):
    for move in moves:
        stacks = apply_move_9001(stacks, move)
    return stacks

def result(stacks, moves):
    stacks = apply_moves(stacks, moves)
    result = ""
    for stack in stacks:
        result += (stack.pop()[1])
    return result

def main():
    input = read("input.txt")
    stacks, moves = process(input)
    print(result(stacks, moves))

if __name__=="__main__":
    main()

#answer : CWMTGHBDW SSCGWJCRB