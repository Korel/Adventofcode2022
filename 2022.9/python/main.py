def draw(h, t, move):
    from matplotlib import pyplot as plt
    plt.clf()
    axis = list(range(-51, 50))
    plt.xlim([-50, 50])
    plt.ylim([-50, 50])
    plt.plot(axis, [0] * len(axis), color="cyan", label=f"{len(unique_tails)}")
    plt.plot([0] * len(axis), axis, color="cyan", label=f"{move}")
    plt.plot([h[0]], [h[1]], ".", color="red", label=f"({h[0]}, {h[1]})")
    plt.plot([t[0]], [t[1]], ".", color="blue", label=f"({t[0]}, {t[1]})")
    plt.legend()
    plt.show(block=False)
    plt.draw()
    plt.pause(0.1)


def first_task(moves):
    head = [0, 0]
    tail = [0, 0]
    unique_tails = set()
    for move in moves:
        match move[0]:
            case "U":
                while move[1]:
                    move[1] -= 1
                    head[1] += 1
                    if abs(head[1] - tail[1]) > 1:
                        tail[1] += 1
                        tail[0] = head[0]
                        unique_tails.add(tuple(tail))
            case "D":
                while move[1]:
                    move[1] -= 1
                    head[1] -= 1
                    if abs(head[1] - tail[1]) > 1:
                        tail[1] -= 1
                        tail[0] = head[0]
                        unique_tails.add(tuple(tail))
            case "R":
                while move[1]:
                    move[1] -= 1
                    head[0] += 1
                    if abs(head[0] - tail[0]) > 1:
                        tail[0] += 1
                        tail[1] = head[1]
                        unique_tails.add(tuple(tail))
            case "L":
                while move[1]:
                    move[1] -= 1
                    head[0] -= 1
                    if abs(head[0] - tail[0]) > 1:
                        tail[0] -= 1
                        tail[1] = head[1]
                        unique_tails.add(tuple(tail))
    print(len(unique_tails))


def move_node(head, tail, direction):
    match direction:
        case "U":
            head[1] += 1
            if abs(head[1] - tail[1]) > 1:
                tail[1] += 1
                tail[0] = head[0]
        case "D":
            head[1] -= 1
            if abs(head[1] - tail[1]) > 1:
                tail[1] -= 1
                tail[0] = head[0]
        case "R":
            head[0] += 1
            if abs(head[0] - tail[0]) > 1:
                tail[0] += 1
                tail[1] = head[1]
        case "L":
            head[0] -= 1
            if abs(head[0] - tail[0]) > 1:
                tail[0] -= 1
                tail[1] = head[1]
    return (head, tail)


def follow_node(head, tail):
    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]
    if abs(diff_x) > 1:
        tail[0] += 1 if diff_x > 0 else -1
        tail[1] = head[1]

    if abs(diff_y) > 1:
        tail[1] += 1 if diff_y > 0 else -1
        tail[0] = head[0]

    return (head, tail)


def second_task(moves):
    nodes = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
             [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    unique_tails = set()
    for move in moves:
        for _ in range(move[1], 0, -1):
            (nodes[0], nodes[1]) = move_node(nodes[0],
                                                     nodes[1], move[0])
            for i in range(1, len(nodes) - 1):
                (nodes[i], nodes[i + 1]) = follow_node(nodes[i],
                                                     nodes[i + 1])
            unique_tails.add(tuple(nodes[-1]))
    print(len(unique_tails))


def main():
    moves = []
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            moves.append([line[0], int(line[2:-1])])
    # first_task(moves)
    second_task(moves)
    # 3432 is too high
    # 2362 is too low


if __name__ == "__main__":
    main()
