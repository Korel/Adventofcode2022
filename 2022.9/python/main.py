def move(head, tail, direction):
    if direction == "R":
        head[0] += 1
    elif direction == "L":
        head[0] -= 1
    elif direction == "U":
        head[1] += 1
    elif direction == "D":
        head[1] -= 1

    x_dist = abs(head[0] - tail[0])
    y_dist = abs(head[1] - tail[1])

    if x_dist > 1:
        if head[0] < tail[0]:
            tail[0] -= 1
        else:
            tail[0] += 1
        # tail[1] = head[1] # Diagonal jump if needed
    if y_dist > 1:
        if head[1] < tail[1]:
            tail[1] -= 1
        else:
            tail[1] += 1
        # tail[0] = head[0]  # Diagonal jump if needed
    return [head, tail]


def draw(head, tail, tail_set):
    hx, hy = head[0], head[1]
    tx, ty = tail[0], tail[1]
    r = max(abs(hx), abs(tx)) * 2 + 1
    c = max(abs(hy), abs(ty)) * 2 + 1

    grid = [(['.'] * c) * r]
    origin = (len(grid), len(grid[0]))
    grid[origin[0]][origin[1]] = 'S'
    grid[origin[0]+ hx][origin[1] + hy] = "H"
    grid[origin[0]+ tx][origin[1] + ty] = "T"
    
    for row in grid:
        print(end='\n')
        for col in row:
            print(f"{col} ", end="")
    print(end='\n')


    # if r < 3:
    #     r = 4
    # if c < 0:
    #     c = 4
    # for i in range(2*r, -2*r - 1, -1):
    #     print(end='\n')
    #     for j in range(2*c, -2*c - 1, -1):
    #         if j == -hx and i == hy:
    #             print("H", end=" ")
    #             continue
    #         if j == -tx and i == ty:
    #             print("T", end=" ")
    #             continue
    #         if j == 0 and i == 0:
    #             print("S", end=" ")
    #             continue
    #         if (-j, i) in tail_set:
    #             print("#", end=" ")
    #             continue

    #         print(".", end=" ")
    # print(end="\n")


def main():
    if True:
        my_input = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2",]
    else:
        my_input = [line.strip('\n')
                    for line in open("../input.txt", "r").readlines()]

    tail_set = set()
    head = [0, 0]
    tail = [0, 0]
    tail_coords = []

    for line in my_input:
        direction = line[0]
        times = int(line[2])
        print(f"== {direction} {times} ==")
        while times:
            [head, tail] = move(head, tail, direction)
            draw(head,tail, tail_set)
            tail_coords.append(tail.copy())
            tail_set.add((tail[0], tail[1]))
            times -= 1

    print(len(tail_set))

if __name__ == "__main__":
    main()