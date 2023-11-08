import math

def parse_input(filename) -> list[list[str], list[int], list[int]]:
    grid = []
    start = [-1, -1]
    end = [-1, -1]
    with open(filename) as f:
        for line in f.readlines():
            if start[1] == -1:
                start[0] += 1
            if end[1] == -1:
                end[0] += 1
            row = []
            for char in line.strip():
                if char == 'S':
                    start[1] = line.index(char)
                    row.append(0)
                    continue
                if char == 'E':
                    end[1] = line.index(char)
                    row.append(ord('z') - ord('a'))
                    continue
                row.append(ord(char) - ord('a'))
            grid.append(row)
    return grid, start, end


class Solver:
    grid: list[list[int]]
    memo: list[list[int]]
    start: list[int]
    end: list[int]

    def __init__(self, grid: list[list[int]], start: list[int], end: list[int]):
        self.grid = grid
        self.start = start
        self.end = end
        self.memo = [[0 for _ in range(len(grid[0]))]
                     for _ in range(len(grid))]

    def move(self, curr_pos):
        if curr_pos == self.end:
            return 0
        [row, col] = curr_pos
        if self.memo[row][col]:
            return self.memo[row][col]

        self.memo[row][col] = math.inf

        up, down, right, left = math.inf, math.inf, math.inf, math.inf
        curr = self.grid[row][col]

        if row - 1 >= 0:
            if self.grid[row - 1][col] <= curr or self.grid[row - 1][col] - curr <= 1:
                up = self.move([row - 1, col]) + 1
        if row + 1 < len(self.grid):
            if self.grid[row + 1][col] <= curr or self.grid[row + 1][col] - curr <= 1:
                down = self.move([row + 1, col]) + 1
        if col - 1 >= 0:
            if self.grid[row][col - 1] <= curr or self.grid[row][col - 1] - curr <= 1:
                left = self.move([row, col - 1]) + 1
        if col + 1 < len(self.grid[0]):
            if self.grid[row][col + 1] <= curr or self.grid[row][col + 1] - curr <= 1:
                right = self.move([row, col + 1]) + 1

        self.memo[row][col] = min(up, down, left, right)
        return self.memo[row][col]
    
    def solve(self):
        return self.move(self.start)

def main():
    test_input = parse_input("test.txt")
    test_solver = Solver(test_input[0], test_input[1], test_input[2])
    print(f"test input: {test_solver.solve()}")
    assert(test_solver.solve() == 31)
    
    [grid, start, end] = parse_input("input.txt")
    print(f"grid len: {len(grid), len(grid[0])}")
    solver = Solver(grid, start, end)
    print(f"real input: {solver.solve()}") # 415 too high, 108 is too low
    # print(solver.memo)



if __name__ == "__main__":
    main()
