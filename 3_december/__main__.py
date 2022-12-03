import string
def read(file_name):
    with open(file_name, "r") as file:
        contents = file.readlines()
    for i,val in enumerate(contents):
        contents[i] = val.replace("\n", "")
    return contents

def process_compartments(input):
    for i,rucksack in enumerate(input):
        input[i] = rucksack[:len(rucksack) // 2], rucksack[len(rucksack) // 2:]
    return input

def priority(item):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = dict([(x[1],x[0] + 1) for x in enumerate(alphabet)])
    return position[item]

def priorities(rucksacks):
    sum = 0
    for rucksack in rucksacks:
        common_item = (set(rucksack[0]) & set(rucksack[1])).pop()
        sum += priority(common_item)
    return sum

def process_groups(input):
    groups = []
    for i in range(0, len(input), 3):
        groups.append([input[i], input[i+1], input[i+2]])
    return groups

def badge_priorities(groups):
    sum = 0
    for group in groups:
        badge = (set(group[0]) & set(group[1]) & set(group[2])).pop()
        sum += priority(badge)
    return sum

def main():
    input = read("input.txt")
    rucksacks = process_compartments(input.copy())
    print(priorities(rucksacks))
    groups = process_groups(input)
    print(badge_priorities(groups))
    

if __name__=="__main__":
    main()

#answer : 7701 & 2644