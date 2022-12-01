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

def find_highest_sum(calories):
    highest = sum(calories[0])
    for elf in calories:
        elf_sum = sum(elf)
        if elf_sum > highest:
            highest = elf_sum
    return highest

def find_highest_sum_alternative(calories):
    elfs = []
    for elf in calories:
        elfs.append(sum(elf))
    return max(elfs)

def find_three_highest_sum(calories):
    highest = [0, 0, 0]
    for elf in calories:
        elf_sum = sum(elf)
        if elf_sum > min(highest):
            highest.remove(min(highest))
            highest.append(elf_sum)
    return sum(highest)

def main():
    with open('input.txt', 'r') as file:
        input = file.readlines()
        calories = process_input(input)
        highest_sum = find_highest_sum(calories)
        highest_sum_alternative = find_highest_sum_alternative(calories)
        three_highest_sum = find_three_highest_sum(calories)
        print(highest_sum, highest_sum_alternative, three_highest_sum)


if __name__=="__main__":
    main()

#answer : 71934