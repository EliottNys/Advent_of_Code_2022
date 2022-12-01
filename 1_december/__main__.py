def process_input(input):
    result = []
    sub = []
    for line in input:
        if line == "\n":
            result.append(sub)
            sub = []
        else:
            sub.append(int(line.replace("\n", "")))
    result.append(sub)
    return result


def main():
    with open('input.txt', 'r') as file:
        input = file.readlines()
        calories = process_input(input)
        highest = sum(calories[0])
        for elf in calories:
            elf_sum = sum(elf)
            if elf_sum > highest:
                highest = elf_sum
        print(highest)



if __name__=="__main__":
    main()

#answer : 71934