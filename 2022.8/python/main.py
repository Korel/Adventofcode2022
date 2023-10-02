

def first_task(trees):
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
    print("first task:", count)

def second_task(trees):
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

    max_visible = 0
    for i in range(1, len(trees)):
        for j in range(1, len(trees[i])):
            max_visible = max(
                max_visible, left_visible[i][j] * right_visible[i][j] * up_visible[i][j] * down_visible[i][j])

    print("second task:", max_visible)

def main():
    trees = open("../input.txt", "r")
    trees = list(map(lambda row: list(row) ,map(lambda row: row.strip('\n'), trees.readlines())))
    first_task(trees)
    second_task(trees)

if __name__ == "__main__":
    main()