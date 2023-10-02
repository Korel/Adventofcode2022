TEST = False
if TEST:
    trees = """ 30373
            25512
            65332
            33549
            35390"""
    trees = trees.split('\n')
    for i in range(0, len(trees)):
        trees[i] = trees[i].strip()
else:
    trees = open("input.txt", "r")
    trees = trees.readlines()


temp = []
for row in trees:
    row = row.strip('\n')
    arr = []
    for ch in row:
        arr.append(int(ch))
    temp.append(arr)

trees = temp

NO = 0
ROW = 1
COLUMN = 2
BOTH = 3
left_visible = []
right_visible = []
up_visible = []
down_visible = []
for i in range(0, len(trees)):
    left_visible.append(([0] * len(trees[i])))
    right_visible.append(([0] * len(trees[i])))
    up_visible.append(([0] * len(trees[i])))
    down_visible.append(([0] * len(trees[i])))

for i in range(1, len(trees)):
    for j in range(1, len(trees[i])):
        left = 0
        right = 0
        up = 0
        down = 0
        tree = trees[i][j]
        # left
        jj = j - 1
        while jj >= 0:
            other = trees[i][jj]
            left += 1
            jj -= 1
            if tree <= other:
                break
        left_visible[i][j] = left
        # right
        jj = j + 1
        while jj < len(trees[i]):
            other = trees[i][jj]
            right += 1
            jj += 1
            if tree <= other:
                break
        right_visible[i][j] = right
        # up
        ii = i - 1
        while ii >= 0:
            other = trees[ii][j]
            up += 1
            ii -= 1
            if tree <= other:
                break
        up_visible[i][j] = up
        # down
        ii = i + 1
        while ii < len(trees):
            other = trees[ii][j]
            down += 1
            ii += 1
            if tree <= other:
                break
        down_visible[i][j] = down
        print(f"({i}, {j}): up: {up}, down: {down}, left: {left}, right: {right}")


max_visible = 0
for i in range(1, len(trees)):
    for j in range(1, len(trees[i])):
        max_visible = max(
            max_visible, left_visible[i][j] * right_visible[i][j] * up_visible[i][j] * down_visible[i][j])

print(max_visible)
