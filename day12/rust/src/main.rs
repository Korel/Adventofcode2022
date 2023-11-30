use std::fs;
use std::cmp;

type Grid = Vec<Vec<i32>>;
type Coords = (i32, i32);
fn parse_input(filepath: &str) -> (Grid, Coords, Coords) {
    let mut grid: Vec<Vec<i32>> = Vec::new();
    let mut start = (-1, -1);
    let mut end = (-1, -1);
    let file_string = fs::read_to_string(filepath).unwrap();
    for line in file_string.lines() {
        if start.1 == -1 {
            start.0 += 1;
        }
        if end.1 == -1 {
            end.0 += 1;
        }
        let mut row = Vec::new();
        for c in line.chars() {
            if c == 'S' {
                start.1 = line.chars().position(|x| x == c).unwrap() as i32;
                row.push(0);
                continue;
            } else if c == 'E' {
                end.1 = line.chars().position(|x| x == c).unwrap() as i32;
                row.push('z' as i32 - 'a' as i32);
                continue;
            } else {
                row.push(c as i32 - 'a' as i32);
            }
        }
        grid.push(row);
    }
    (grid, start, end)
}

struct Solver {
    grid: Vec<Vec<i32>>,
    solution: Vec<Vec<i32>>,
    start: (i32, i32),
    end: (i32, i32),
}

impl Solver {
    fn new(grid: Vec<Vec<i32>>, start: (i32, i32), end: (i32, i32)) -> Solver {
        let mut solution = vec![vec![i32::MAX; grid[0].len()]; grid.len()];
        solution[end.0 as usize][end.1 as usize] = 0;
        Solver {
            grid,
            solution,
            start,
            end,
        }
    }

    fn solve(&mut self) -> i32 {
        self.traverse(self.end);
        self.solution[self.start.0 as usize][self.start.1 as usize]
    }

    fn traverse(&mut self, curr_pos: (i32, i32)) {
        if curr_pos == self.start {
            return;
        }
        let row = curr_pos.0 as usize;
        let col = curr_pos.1 as usize;
        let curr = self.grid[row][col];

        if row > 0
            && curr - self.grid[row - 1][col] <= 1
            && self.solution[row - 1][col] > self.solution[row][col] + 1
        {
            self.solution[row - 1][col] = self.solution[row][col] + 1;
            self.traverse((row as i32 - 1, col as i32));
        }
        if row + 1 < self.grid.len()
            && curr - self.grid[row + 1][col] <= 1
            && self.solution[row + 1][col] > self.solution[row][col] + 1
        {
            self.solution[row + 1][col] = self.solution[row][col] + 1;
            self.traverse((row as i32 + 1, col as i32));
        }
        if col > 0
            && curr - self.grid[row][col - 1] <= 1
            && self.solution[row][col - 1] > self.solution[row][col] + 1
        {
            self.solution[row][col - 1] = self.solution[row][col] + 1;
            self.traverse((row as i32, col as i32 - 1));
        }
        if col + 1 < self.grid[0].len()
            && curr - self.grid[row][col + 1] <= 1
            && self.solution[row][col + 1] > self.solution[row][col] + 1
        {
            self.solution[row][col + 1] = self.solution[row][col] + 1;
            self.traverse((row as i32, col as i32 + 1));
        }
    }
}

fn first_task() {
    let test_input = parse_input("../test.txt");
    let mut test_solver = Solver::new(test_input.0, test_input.1, test_input.2);
    let test_solution = test_solver.solve();
    println!("test input: {}", test_solution);
    assert!(test_solution == 31);

    let (grid, start, end) = parse_input("../input.txt");
    let mut solver = Solver::new(grid, start, end);
    let solution = solver.solve();
    println!("real input: {}", solution);
    assert!(solution == 370);
}

fn second_task() {
    let (test_grid, _, test_end) = parse_input("../test.txt");
    let mut test_solver = Solver::new(test_grid.clone(), (0, 0), test_end);
    let mut test_solution = i32::MAX;
    for i in 0..test_grid.len() {
        for j in 0..test_grid[0].len() {
            if test_grid[i][j] == 0{
                let test_start = (i as i32, j as i32);
                test_solver.start = test_start;
                test_solution = cmp::min(test_solution, test_solver.solve());
            }
        }
    }
    println!("test input: {}", test_solution);
    assert!(test_solution == 29);

    let (grid, _, end) = parse_input("../input.txt");
    let mut solver = Solver::new(grid.clone(), (0, 0), end);
    let mut solution = i32::MAX;
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == 0{
                let test_start = (i as i32, j as i32);
                solver.start = test_start;
                solution = cmp::min(solution, solver.solve());            }
        }
    }
    println!("real input: {}", solution);
    assert!(solution == 363);
}

fn main() {
    first_task();
    second_task();
}
