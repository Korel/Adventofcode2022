use std::collections::HashSet;
use std::fs;

fn distance(node0: (i32, i32), node1: (i32, i32)) -> f32 {
    f32::sqrt((node0.0 - node1.0).pow(2) as f32 + (node0.1 - node1.1).pow(2) as f32)
}

fn move_other_nodes(nodes: &mut [(i32, i32)]) {
    for i in 0..nodes.len() - 1 {
        let x0 = nodes[i].0;
        let y0 = nodes[i].1;
        let mut x1 = nodes[i + 1].0;
        let mut y1 = nodes[i + 1].1;
        if distance(nodes[i], nodes[i + 1]) >= 2.0 {
            if x0 == x1 {
                if y0 > y1 {
                    y1 += 1;
                } else {
                    y1 -= 1;
                }
            } else if y0 == y1 {
                if x0 > x1 {
                    x1 += 1;
                } else {
                    x1 -= 1;
                }
            } else {
                if y0 > y1 {
                    y1 += 1;
                } else {
                    y1 -= 1;
                }
                if x0 > x1 {
                    x1 += 1;
                } else {
                    x1 -= 1;
                }
            }
        }
        nodes[i + 1].0 = x1;
        nodes[i + 1].1 = y1;
    }
}

fn move_head(nodes: &mut [(i32, i32)], direction: char) {
    let head: &mut (i32, i32) = nodes.get_mut(0).unwrap();
    match direction {
        'U' => head.1 += 1,
        'D' => head.1 -= 1,
        'L' => head.0 -= 1,
        'R' => head.0 += 1,
        _ => {}
    }
    move_other_nodes(nodes);
}

fn first_task(moves: Vec<(char, i32)>) {
    let mut nodes = vec![(0, 0), (0, 0)];
    let mut unique_tails = HashSet::<(i32, i32)>::new();
    for mv in moves {
        let direction = mv.0;
        let mut times = mv.1;
        while times > 0 {
            times -= 1;
            move_head(nodes.as_mut_slice(), direction);
            unique_tails.insert(*nodes.last().unwrap());
        }
    }
    println!("first_task: {}", unique_tails.len());
}

fn second_task(moves: Vec<(char, i32)>) {
    let mut nodes = vec![
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ];
    let mut unique_tails = HashSet::<(i32, i32)>::new();
    for mv in moves {
        let direction = mv.0;
        let mut times = mv.1;
        while times > 0 {
            times -= 1;
            move_head(nodes.as_mut_slice(), direction);
            unique_tails.insert(*nodes.last().unwrap());
        }
    }
    println!("second_task: {}", unique_tails.len());
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
    first_task(moves.clone());
    second_task(moves);
}
