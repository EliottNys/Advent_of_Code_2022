def read(file_name):
    with open(file_name, "r") as file:
        contents = file.readlines()
    for i,val in enumerate(contents):
        contents[i] = val.replace("\n", "")
    return contents

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
    def size(self):
        size = 0
        for file in self.files:
            if isinstance(file, File):
                size += file.size
            else: size += file.size()
        return size

class Tree:
    def __init__(self):
        self.files = [Directory("/")]
    def add_file(self, location, file):
        current_directory = self.files[0]
        for next_directory in location:
            current_directory = next((directory for directory in current_directory.files if directory.name == next_directory), None)
        current_directory.files.append(file)
        self.files.append(file)

def analyze_tree(input):
    tree = Tree()
    current_directory = []
    input.pop(0)
    for line in input:
        line_contents = line.split()
        match line_contents[0]:
            case "$":
                match line_contents[1]:
                    case "cd":
                        match line_contents[2]:
                            case "..":
                                current_directory.pop()
                            case other:
                                current_directory.append(other)
                    case "ls":
                        pass
            case "dir":
                tree.add_file(current_directory, Directory(line_contents[1]))
            case other:
                tree.add_file(current_directory, File(line_contents[1], int(line_contents[0])))
    return tree

def total_size(tree):
    size = 0
    for file in tree.files:
        if isinstance(file, Directory):
            file_size = file.size()
            if file_size < 100000:
                size += file_size
    return size

def make_space_for_update(tree):
    disk_space = 70000000
    needed_space = 30000000
    current_directory = tree.files[0]
    used_space = current_directory.size()
    to_delete = used_space
    for file in tree.files:
        if isinstance(file, Directory):
            file_size = file.size()
            if needed_space - (disk_space - used_space) <= file_size < to_delete:
                to_delete = file_size
    return to_delete

def main():
    input = read("input.txt")
    tree = analyze_tree(input)
    print(total_size(tree))
    print(make_space_for_update(tree))
    

if __name__=="__main__":
    main()

#answer : 1307902 & 7068748