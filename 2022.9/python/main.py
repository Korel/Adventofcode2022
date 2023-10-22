from copy import deepcopy
from math import sqrt


def draw(nodes):
    """
    Draws the rope in a grid_size x grid_size grid, 
    highest number shown if nodes are on top of eachother
    """
    grid_size = 50
    row = ['.'] * grid_size
    grid = [deepcopy(row) for i in range(grid_size)]
    node_num = 0
    origin = (int(grid_size / 2) - 1)
    grid[origin][origin] = "s"

    for node in nodes:
        x = node[0]
        y = node[1]
        x = x + (int(grid_size / 2) - 1)
        y = -y + (int(grid_size / 2) - 1)
        grid[y][x] = str(node_num)
        node_num += 1

    print("-" * (grid_size + 5))
    row_num = 1
    for row in grid:
        print(f"{row_num:2}", end="")
        row_num += 1
        for char in row:
            print(char, end="")
        print(end='\n')
    print("-" * (grid_size + 5))


def distance(node0, node1):
    [x0, y0] = node0
    [x1, y1] = node1
    return sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)


def move_other_nodes(nodes):
    """ Moves the other nodes according to the movement of head """
    for i in range(len(nodes) - 1):
        head = nodes[i]
        tail = nodes[i + 1]
        [x0, y0] = head
        [x1, y1] = tail
        # actual distance limit is sqrt(2) but next step would be sqrt(5) so using 2 is fine.
        if distance(head, tail) >= 2:
            # Head and tail are too far away, find out which way and move accordingly
            if x0 == x1:  # On the same row, which means 2 steps Up or Down
                if y0 > y1:
                    y1 += 1
                else:
                    y1 -= 1
            elif y0 == y1:  # On the same columns, which means 2 steps Left or Right
                if x0 > x1:
                    x1 += 1
                else:
                    x1 -= 1
            else:  # Not touching, must move diagonally
                if y0 > y1:
                    y1 += 1
                else:
                    y1 -= 1
                if x0 > x1:
                    x1 += 1
                else:
                    x1 -= 1
            tail[0] = x1
            tail[1] = y1


def move(nodes, direction):
    """ Moves the head according to direction and then moves other nodes accordingly"""
    head = nodes[0]
    match direction:
        case "U":
            head[1] += 1
        case "D":
            head[1] -= 1
        case "L":
            head[0] -= 1
        case "R":
            head[0] += 1
    move_other_nodes(nodes)


def first_task(lines):
    nodes = [[0, 0], [0, 0]]
    unique_tails = set()
    for line in lines:
        direction = line[0]
        times = int(line[2:])
        while times:
            times -= 1
            move(nodes, direction)
            unique_tails.add(tuple(nodes[-1]))
    print(f"first_task: {len(unique_tails)}")


def second_task(lines):
    nodes = [[0, 0] for _ in range(10)]
    unique_tails = set()
    for line in lines:
        direction = line[0]
        times = int(line[2:])
        while times:
            times -= 1
            move(nodes, direction)
            unique_tails.add(tuple(nodes[-1]))
    print(f"second_task: {len(unique_tails)}")


def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    first_task(lines)
    second_task(lines)


if __name__ == "__main__":
    main()
