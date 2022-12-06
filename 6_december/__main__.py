def read(file_name):
    with open(file_name, "r") as file:
        contents = file.readlines()
    for i,val in enumerate(contents):
        contents[i] = val.replace("\n", "")
    return contents

def all_unique(list):
    if len(list) == len(set(list)):
        return True
    else:
        return False

def start_of_packet(input):
    scope = []  #queue
    for i,character in enumerate(input[0]):
        scope.append(character)
        if len(scope) > 4:
            scope.pop(0)
            if all_unique(scope):
                print(scope)
                return(i+1)

def main():
    input = read("input.txt")
    print(start_of_packet(input))

if __name__=="__main__":
    main()

#answer : 1848