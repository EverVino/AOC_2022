class Dir:
    def __init__(self, name, parent, size = 0):
        self.files = []
        self.dirs = dict()
        self.name = name 
        self.parent = parent
        self.size = size

    def add_dir(self, name_dir, direc):
        self.dirs[name_dir] = direc

    def add_file(self, f):
        self.files.append(f)

class File:
    def __init__(self, name, size, parent) :
        self.name = name 
        self.size = size
        self.parent = parent 

with open("input7.txt", "r") as f:
    reader = f.read()

reader = reader.split("\n")

all_dirs_in_root = []

root = Dir("root", None)
actual_dir = root

for line in reader[1:]:
    if line == "$ ls":
        continue 
    if line[0:4] == "$ cd":
        go_dir = line[5:]
        if go_dir == "..":
            actual_dir = actual_dir.parent 
            continue
        else:
            actual_dir = actual_dir.dirs[go_dir]
            continue
    
    a1, a2 = [x for x in line.split()]
    if a1 == "dir":
        name_dir = a2 
        new_dir = Dir(name_dir, actual_dir)
        actual_dir.dirs[name_dir] = new_dir
        all_dirs_in_root.append(new_dir)
        continue
    
    size = int(a1)
    name_file = a2 
    new_file = File(name_file, size, actual_dir)
    actual_dir.add_file(new_file)

    
# To printing dirs and files
def print_dirs(directory ,tab = ""):
    
    print(tab, directory.name + "(dir)")
    tab += "  "
    for d in directory.dirs:
        print_dirs(directory.dirs[d], tab)

    for f in directory.files:
        print(tab, f.name, f.size)
    
# Determing size of the dirs
def size_of(directory):
    s = 0
    for f in directory.files:
        s = s + f.size

    for d in directory.dirs:
        s = s + size_of(directory.dirs[d])
    
    directory.size = s
    return s

size_of(root)

ordered_by_size = sorted(all_dirs_in_root, 
                  key = lambda x: x.size)

min_space_needed = 30_000_000
used_space = root.size 
total_space = 70_000_000

space_needed = min_space_needed - (total_space - used_space)

for d in ordered_by_size:
    if d.size>space_needed:
        break 
print(space_needed)
print(d.size)

