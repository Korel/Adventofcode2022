from copy import deepcopy


def first_task(instructions):
    x = 1
    cycle = 1
    pointer = 0
    strengths = []
    strengths_turn = 1
    while pointer < len(instructions):
        instruction = instructions[pointer]
        pointer += 1
        if instruction == "noop":
            cycle += 1
            if cycle == 20 * strengths_turn:
                strengths.append(x * cycle)
                strengths_turn += 2
                if strengths_turn > 11:
                    break
        else:
            cycle += 1
            if cycle == 20 * strengths_turn:
                strengths.append(x * cycle)
                strengths_turn += 2
                if strengths_turn > 11:
                    break
            cycle += 1
            x += int(instruction[len("addx "):])
            if cycle == 20 * strengths_turn:
                strengths.append(x * cycle)
                strengths_turn += 2
                if strengths_turn > 11:
                    break

    print("first task:", sum(strengths))


def check_and_add_pixel(pixel, x, row):
    if x == pixel or x + 1 == pixel or x + 2 == pixel:
        row[pixel] = "#"

def check_and_move_row(cycle, screen, row):
    if cycle % 40 == 0:
        screen.append(deepcopy(row))
        return ['.'] * 42
    else:
        return row

def second_task(instructions):
    x = 1
    cycle = 1
    pointer = 0
    screen = []
    row = ['.'] * 42
    while pointer < len(instructions):
        instruction = instructions[pointer]
        pointer += 1
        pixel = cycle % 40
        if pixel == 0: 
            pixel = 40
        check_and_add_pixel(pixel, x, row)
        row = check_and_move_row(cycle, screen, row)
        cycle += 1
        if instruction != "noop":
            pixel = cycle % 40
            if pixel == 0: 
                pixel = 40
            check_and_add_pixel(pixel, x, row)
            row = check_and_move_row(cycle, screen, row)
            cycle += 1
            x += int(instruction[len("addx "):])

    print("second task:")
    for row in screen:
        s = ""
        for r in row:
            s += r
        print(s[1:-1])
    # print(screen)


def main():
    with open("../input.txt", "r") as f:
        instructions = list(map(lambda line: line.strip('\n'), f.readlines()))
    first_task(instructions)
    second_task(instructions)


if __name__ == "__main__":
    main()
