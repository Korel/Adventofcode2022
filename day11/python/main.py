import math
import copy

class Monkey:
    items: list[int]
    operation: [str, int]
    test: int
    throw: [int, int]
    inspection: int

    def __init__(self) -> None:
        self.items = []
        self.operation = []
        self.test = 0
        self.throw = [-1, -1]
        self.inspection = 0

    def __repr__(self) -> str:
        return f"Monkey {{ items: {self.items}, operation: {self.operation}, test: {self.test}, throw: {self.throw}, inspection: {self.inspection}}}"


def parse_input(lines: list[str]) -> list[Monkey]:
    monkeys = []
    for line in lines:
        if line[0] == "\n":
            continue
        if line[0] == "M":
            monkeys.append(Monkey())
            continue
        if line[2] == "S":
            monkey = monkeys[-1]
            items = line.split(":")[1]
            items = items.split(",")
            items = [int(item) for item in items]
            monkey.items = items
            continue
        if line[2] == "O":
            monkey = monkeys[-1]
            line = line[line.find("=") + 1:]
            split = line.split("+")
            if len(split) == 2:
                monkey.operation.append("add")
            else:
                split = line.split("*")
                monkey.operation.append("mul")

            if split[1].find("old") == -1:
                monkey.operation.append(int(split[1]))
            else:
                monkey.operation.append(-1)
            continue
        if line[2] == "T":
            monkey = monkeys[-1]
            monkey.test = int(line.split("by")[1])
            continue
        if line[4] == "I":
            monkey = monkeys[-1]
            value = int(line.split("monkey")[-1])
            if line.find("true") != -1:
                monkey.throw = [value, monkey.throw[1]]
            else:
                monkey.throw = [monkey.throw[0], value]
            continue
    return monkeys


def first_task(monkeys: list[Monkey]) -> int:
    for _ in range(20):
        for monkey in monkeys:
            while len(monkey.items) != 0:
                item = monkey.items.pop(0)
                monkey.inspection += 1
                worry = 0
                operation_value = item if monkey.operation[1] == - \
                    1 else monkey.operation[1]
                if monkey.operation[0] == "add":
                    worry = item + operation_value
                else:
                    worry = item * operation_value
                worry = int(worry / 3)
                test = worry % monkey.test
                if test == 0:
                    monkeys[monkey.throw[0]].items.append(worry)
                else:
                    monkeys[monkey.throw[1]].items.append(worry)

    inspections = [monkey.inspection for monkey in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


def second_task(monkeys: list[Monkey]) -> int:
    tests = []
    for monkey in monkeys:
        tests.append(monkey.test)
    test_lcm = math.lcm(*tests)
    for _ in range(10000):
        for monkey in monkeys:
            while len(monkey.items) != 0:
                item = monkey.items.pop(0)
                monkey.inspection += 1
                worry = 0
                operation_value = item
                if monkey.operation[1] != -1:
                    operation_value = monkey.operation[1]
                if monkey.operation[0] == "add":
                    worry = item + operation_value
                else:
                    worry = item * operation_value

                if worry % monkey.test == 0:
                    monkeys[monkey.throw[0]].items.append(worry)
                else:
                    monkeys[monkey.throw[1]].items.append(worry % test_lcm)
    
    inspections = [monkey.inspection for monkey in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


def main():
    file = open("input.txt", "r")
    lines = file.readlines()
    monkeys = parse_input(lines)
    first_task_result = first_task(copy.deepcopy(monkeys))
    second_task_result = second_task(monkeys)
    print(f"first_task: {first_task_result}")
    print(f"second_task: {second_task_result}")
    # The asserts are added after the solution to ensure refactoring does not brake it.
    assert(first_task_result == 110220)
    assert(second_task_result == 19457438264)

if __name__ == "__main__":
    main()
