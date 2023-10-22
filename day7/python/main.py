class Directory:
    pass

class Directory:
    parent: Directory
    children: list[Directory] # of Dirs
    files: list[int]
    name: str
    size: int

    def __init__(self, name, parent=None, size=0):
        self.children = []
        self.files = []
        self.name = name
        self.parent = parent

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

def first_task(commands):
    curr_dir = Directory(name="/", parent=None)
    for line in commands:
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
            curr_dir.children.append(Directory(name=target, parent=curr_dir))
            continue
        if line[0].isnumeric():
            size = int(line[0:line.find(" ")])
            curr_dir.files.append(size)
            # continue

    while curr_dir.parent:
        curr_dir = curr_dir.parent

    root = curr_dir
    getDirSize(root)
    print("first task:", sum(list(filter(lambda size: size <= 100000, MEMO.values()))))

def second_task(commands):
    curr_dir = Directory(name="/", parent=None)
    for line in commands:
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
            curr_dir.children.append(Directory(name=target, parent=curr_dir))
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

    print(f"second task: {found_min}")


def main():
    input_file = open("../input.txt", "r")
    commands = list(map(lambda s: s.strip('\n') ,input_file.readlines()))
    first_task(commands)
    # MEMO normally should be reset before calling second_task
    second_task(commands)

if __name__ == "__main__":
    main()