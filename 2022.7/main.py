input_file = """$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

input_file = input_file.split('\n')

input_file = open("input.txt", "r")
input_file = list(map(lambda s: s.strip('\n') ,input_file.readlines()))


class Dir:
    pass

class Dir:
    parent: Dir
    children: list[Dir] # of Dirs
    files: list[int]
    name: str
    size: int

    def __init__(self, name, parent=None, size=0):
        self.children = []
        self.files = []
        self.name = name
        self.parent = parent
        self.size = size


MEMO = {}

def getDirSize(dir):
    size = MEMO.get(dir)
    if MEMO.get(dir):
        return size
    size = 0
    for file in dir.files:
        size += file
    for child in dir.children:
        size += getDirSize(child)
    MEMO[dir] = size
    return size

        


curr_dir = Dir(name="/", parent=None)
for line in input_file:
    if line == "$ ls":
        continue
    cd = line.find("$ cd")
    if cd != -1:
        target = line[cd + 5:]
        if target == "..":
            curr_dir = curr_dir.parent
        else:
            curr_dir = list(filter(lambda dir: dir.name == target, curr_dir.children))[0]
        continue
    dir = line.find("dir")
    if dir != -1:
        target = line[dir+4:]
        curr_dir.children.append(Dir(name=target, parent=curr_dir))
        continue
    if line[0].isnumeric():
        size = int(line[0:line.find(" ")])
        curr_dir.files.append(size)
        # continue

while curr_dir.parent:
    curr_dir = curr_dir.parent

root = curr_dir
root_size = getDirSize(root)

needed = 30000000 - (70000000 - root_size)
found_min = 2**64

for val in MEMO.values():
    if val >= needed:
        found_min = min(found_min, val)

print(found_min)



# print(sum(list(filter(lambda size: size <= 100000, MEMO.values()))))