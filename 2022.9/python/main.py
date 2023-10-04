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

def second_task(moves):
    pass


def main():
    moves = []
    with open("../input.txt", "r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            moves.append([line[0], int(line[2:-1])])
    first_task(moves)
    second_task(moves)
    
if __name__ == "__main__":
    main()