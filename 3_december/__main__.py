import string
def read(file_name):
    with open(file_name, "r") as file:
        contents = file.readlines()
    return contents

def process(input):
    for i,rucksack in enumerate(input):
        clean = rucksack.replace("\n", "")
        input[i] = clean[:len(clean) // 2], clean[len(clean) // 2:]
    return input

def priorities(rucksacks):
    sum = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = dict([(x[1],x[0] + 1) for x in enumerate(alphabet)])
    for rucksack in rucksacks:
        common_item = (set(rucksack[0]) & set(rucksack[1])).pop()
        sum += position[common_item]
    return sum

def main():
    input = read("input.txt")
    rucksacks = process(input)
    print(priorities(rucksacks))
    

if __name__=="__main__":
    main()

#answer : 7701