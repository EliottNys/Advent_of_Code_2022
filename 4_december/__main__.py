def read(file_name):
    with open(file_name, "r") as file:
        contents = file.readlines()
    for i,val in enumerate(contents):
        contents[i] = val.replace("\n", "")
    return contents

def process(input):
    for i,pair in enumerate(input):
        assignments = pair.split(",")
        input[i] = [assignments[0].split("-"), assignments[1].split("-")]
        for j,limit in enumerate(input[i][0]):
            input[i][0][j] = int(limit)
        for j,limit in enumerate(input[i][1]):
            input[i][1][j] = int(limit)
    return input

def total_overlap(pair):
    if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        return True
    elif pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        return True
    else: return False

def total_overlaps(pairs):
    number = 0
    for pair in pairs:
        if total_overlap(pair):
            number += 1
    return number

def partial_overlap(pair):
    if total_overlap(pair):
        return True
    elif pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]:
        return True
    elif pair[0][0] <= pair[1][1] and pair[0][1] >= pair[1][1]:
        return True
    else: return False

def partial_overlaps(pairs):
    number = 0
    for pair in pairs:
        if partial_overlap(pair):
            number += 1
    return number

def main():
    input = read("input.txt")
    pairs = process(input)
    print(total_overlaps(pairs))
    print(partial_overlaps(pairs))

if __name__=="__main__":
    main()

#answer : 450 & 837