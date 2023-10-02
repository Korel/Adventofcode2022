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
visible = []  # 0 no, 1 row, 2 column, 3 both
for i in range(0, len(trees)):
    if i == 0 or i == len(trees) - 1:
        visible.append([COLUMN] * len(trees[i]))
        visible[i][0] = BOTH
        visible[i][len(trees[i]) - 1] = BOTH
    else:
        visible.append([0] * len(trees[i]))
        visible[i][0] = ROW
        visible[i][len(trees[i]) - 1] = ROW

for i in range(0, len(trees)):
    for j in range(0, len(trees[i])):
        if i == 0 or i == len(trees) - 1 or j == 0 or j == len(trees[i]) - 1:
            continue
        tree = trees[i][j]
        # left
        jj = j - 1
        while jj >= 0:
            other = trees[i][jj]
            if tree <= other:
                break
            other_visible = visible[i][jj]
            if other_visible == ROW or other_visible == BOTH:
                visible[i][j] = ROW
                break
            jj -= 1

        if visible[i][j]:
            continue
        # right
        jj = j + 1
        while jj <= len(trees[i]):
            other = trees[i][jj]
            if tree <= other:
                break
            other_visible = visible[i][jj]
            if other_visible == ROW or other_visible == BOTH:
                visible[i][j] = ROW
                break
            jj += 1

        if visible[i][j]:
            continue
        # up
        ii = i - 1
        while ii >= 0:
            other = trees[ii][j]
            if tree <= other:
                break
            other_visible = visible[ii][j]
            if other_visible == COLUMN or other_visible == BOTH:
                visible[i][j] = COLUMN
                break
            ii -= 1

        if visible[i][j]:
            continue
        # down
        ii = i + 1
        while ii < len(trees):
            other = trees[ii][j]
            if tree <= other:
                break
            other_visible = visible[ii][j]
            if other_visible == COLUMN or other_visible == BOTH:
                visible[i][j] = COLUMN
                break
            ii += 1

count = 0
for row in visible:
    for v in row:
        if v: count += 1
print(count)
