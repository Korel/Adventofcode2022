use std::collections::HashSet;
use std::fs;

fn first_task(moves: Vec<(char, i32)>) {
    let mut head = (0, 0);
    let mut tail = (0, 0);
    let mut unique_tails = HashSet::<(i32, i32)>::new();
    for mv in moves {
        match mv.0 {
            'U' => {
                for _ in 0..mv.1 {
                    head.1 += 1;
                    let diff: i32 = head.1 - tail.1;
                    if diff.abs() > 1 {
                        tail.1 += 1;
                        tail.0 = head.0;
                        unique_tails.insert(tail);
                    }
                }
            }
            'D' => {
                for _ in 0..mv.1 {
                    head.1 -= 1;
                    let diff: i32 = head.1 - tail.1;
                    if diff.abs() > 1 {
                        tail.1 -= 1;
                        tail.0 = head.0;
                        unique_tails.insert(tail);
                    }
                }
            }
            'R' => {
                for _ in 0..mv.1 {
                    head.0 += 1;
                    let diff: i32 = head.0 - tail.0;
                    if diff.abs() > 1 {
                        tail.0 += 1;
                        tail.1 = head.1;
                        unique_tails.insert(tail);
                    }
                }
            }
            'L' => {
                for _ in 0..mv.1 {
                    head.0 -= 1;
                    let diff: i32 = head.0 - tail.0;
                    if diff.abs() > 1 {
                        tail.0 -= 1;
                        tail.1 = head.1;
                        unique_tails.insert(tail);
                    }
                }
            }
            _ => todo!("Does not reach"),
        }
    }
    println!("{}", unique_tails.len());
}

fn main() {
    let file_content = fs::read_to_string("../input.txt").unwrap();
    let lines = file_content.split('\n');
    let mut moves: Vec<(char, i32)> = vec![];
    for line in lines {
        if line.is_empty() {
            break;
        }
        let mut split = line.split(' ');
        moves.push((
            split.next().unwrap().chars().next().unwrap(),
            split.next().unwrap().parse().unwrap(),
        ));
    }
    first_task(moves)
}
